"""Check each source paper for open access, open data and open code.

Three sources, all open:

  OpenAlex       — open-access status and type, batched 50 DOIs per request.
  NCBI ID conv   — PubMed ID to PMC ID, so we know which papers have deposited full text.
  PMC efetch     — the full text, searched for a data-availability statement, a code
                   repository, and public accession numbers.

The point is to predict reproducibility: a finding whose source paper deposited its data and
code is one a reader can actually re-derive. Where the signal cannot be determined — no PMC
deposit, or front matter only — the result says so rather than guessing "none".

Writes cache/openness.json.

    python3 -I scripts/check_openness.py
"""
import collections
import json
import pathlib
import re
import time

import requests

CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")
UA = {"User-Agent": "malaria-evidence-audit/1.0 (research script; no contact configured)"}
TOOL = {"tool": "malaria-evidence-audit"}

integ = json.loads((CACHE / "integrity.json").read_text())
papers = {}
for r in integ:
    key = r.get("pubmed_id") or r.get("doi")
    papers[key] = {"pubmed_id": r.get("pubmed_id"), "doi": r.get("doi"),
                   "oa": None, "oa_status": None, "pmcid": None,
                   "fulltext_in_pmc": False, "data_statement": None,
                   "data_class": "unknown", "code_repos": [], "accessions": [],
                   "repositories": [], "notes": []}
print(f"{len(papers)} papers")

# ------------------------------------------------------------------- OpenAlex
dois = [p["doi"] for p in papers.values() if p.get("doi")]
by_doi = {p["doi"]: p for p in papers.values() if p.get("doi")}
print(f"\nOpenAlex for {len(dois)} DOIs")
for start in range(0, len(dois), 40):
    block = dois[start:start + 40]
    flt = "doi:" + "|".join(d.lower() for d in block)
    try:
        r = requests.get("https://api.openalex.org/works",
                         params={"filter": flt, "per-page": 50,
                                 "select": "doi,open_access,best_oa_location,type"},
                         headers=UA, timeout=90)
        r.raise_for_status()
        for w in r.json().get("results", []):
            d = (w.get("doi") or "").replace("https://doi.org/", "")
            rec = by_doi.get(d) or next((v for k, v in by_doi.items() if k.lower() == d), None)
            if not rec:
                continue
            oa = w.get("open_access") or {}
            rec["oa"] = oa.get("is_oa")
            rec["oa_status"] = oa.get("oa_status")
    except requests.RequestException as e:
        print(f"  block {start}: {type(e).__name__}")
    print(f"  {min(start + 40, len(dois))}/{len(dois)}")
    time.sleep(0.4)

# ------------------------------------------------------ PMID -> PMCID, then PMC
pmids = [str(p["pubmed_id"]) for p in papers.values() if p.get("pubmed_id")]
by_pmid = {str(p["pubmed_id"]): p for p in papers.values() if p.get("pubmed_id")}
print(f"\nID conversion for {len(pmids)} PubMed IDs")
for start in range(0, len(pmids), 100):
    block = pmids[start:start + 100]
    r = requests.get("https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/",
                     params={"ids": ",".join(block), "format": "json", **TOOL},
                     headers=UA, timeout=90)
    if r.status_code == 200:
        for rec in r.json().get("records", []):
            tgt = by_pmid.get(str(rec.get("pmid")))
            if tgt and rec.get("pmcid"):
                tgt["pmcid"] = rec["pmcid"]
    time.sleep(0.5)
pmcs = [(p["pmcid"], p) for p in papers.values() if p.get("pmcid")]
print(f"  {len(pmcs)} of {len(pmids)} are in PMC")

DATA_SEC = re.compile(
    r"<(sec|notes)[^>]*>\s*(?:<title>([^<]{0,90})</title>)?(.{0,2500}?)</\1>", re.S)
AVAIL_TITLE = re.compile(r"availab|data sharing|data access|accession", re.I)
DEPOSITED = re.compile(
    r"github\.com/[\w\-\./]+|zenodo|figshare|dryad|osf\.io|dataverse|"
    r"PRJNA\d+|PRJEB\d+|ERP\d{6}|SRP\d{6}|SRR\d+|GSE\d+|"
    r"deposited in|publicly available|freely available|available at http", re.I)
ON_REQUEST = re.compile(r"(?:up)?on (?:reasonable )?request|from the corresponding author|"
                        r"available from the authors", re.I)
CODE_REPO = re.compile(r"github\.com/[\w\-\./]+|gitlab\.com/[\w\-\./]+|"
                       r"bitbucket\.org/[\w\-\./]+|zenodo\.org/record/\d+", re.I)
# Only accession formats specific enough to be unambiguous. A generic two-letter + six-digit
# pattern was tried and matched ordinary words, e.g. "Mc080501".
ACCESSION = re.compile(r"PRJNA\d+|PRJEB\d+|ERP\d{6}|SRP\d{6}|SRR\d{6,}|GSE\d+|ERS\d{6,}")
REPO_NAME = re.compile(r"GenBank|European Nucleotide Archive|\bENA\b|Sequence Read Archive|"
                       r"\bSRA\b|Dryad|Figshare|Zenodo|OSF|Dataverse|MalariaGEN|WWARN|"
                       r"ClinicalTrials\.gov|ISRCTN", re.I)

print(f"\nPMC full text for {len(pmcs)} papers")
for n, (pmcid, rec) in enumerate(pmcs, 1):
    try:
        r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                         params={"db": "pmc", "id": pmcid, "retmode": "xml", **TOOL},
                         headers=UA, timeout=120)
    except requests.RequestException as e:
        rec["notes"].append(f"PMC fetch failed: {type(e).__name__}")
        continue
    if r.status_code != 200:
        rec["notes"].append(f"PMC HTTP {r.status_code}")
        continue
    t = r.text
    # A real full-text deposit has a body with several sections; front matter alone does not.
    body = re.search(r"<body>(.*)</body>", t, re.S)
    n_sec = len(re.findall(r"<sec\b", body.group(1))) if body else 0
    rec["fulltext_in_pmc"] = bool(body) and n_sec >= 3
    if not rec["fulltext_in_pmc"]:
        rec["notes"].append(f"PMC holds front matter only ({n_sec} sections)")

    stmt = None
    for tag, title, inner in DATA_SEC.findall(t):
        if title and AVAIL_TITLE.search(title):
            x = re.sub(r"<[^>]+>", " ", inner)
            stmt = re.sub(r"\s+", " ", x).strip()[:700]
            break
    if stmt is None:
        m = re.search(r"((?:[^<>]{0,200})(?:data|code|script)s?[^<>]{0,80}"
                      r"(?:availab|deposit)[^<>]{0,400})", t, re.I)
        if m:
            stmt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(1))).strip()[:700]
    rec["data_statement"] = stmt

    rec["code_repos"] = sorted({m.rstrip(".,);") for m in CODE_REPO.findall(t)})[:6]
    rec["accessions"] = sorted(set(ACCESSION.findall(t)))[:8]
    # Dedupe repository names case-insensitively, keeping the best-cased form
    _seen = {}
    for m in REPO_NAME.findall(t):
        k = m.lower().replace(" ", "")
        if k not in _seen or (m[:1].isupper() and not _seen[k][:1].isupper()):
            _seen[k] = m
    rec["repositories"] = sorted(_seen.values(), key=str.lower)[:8]

    hay = stmt or t
    # Also dedupe code repositories case-insensitively
    _cr = {}
    for m in rec["code_repos"]:
        _cr.setdefault(m.lower(), m)
    rec["code_repos"] = sorted(_cr.values())

    if rec["code_repos"] or (rec["accessions"] and rec["fulltext_in_pmc"]):
        rec["data_class"] = "deposited"
    elif stmt and DEPOSITED.search(stmt):
        rec["data_class"] = "deposited"
    elif stmt and ON_REQUEST.search(stmt):
        rec["data_class"] = "on request"
    elif stmt:
        rec["data_class"] = "statement, unclear"
    elif rec["fulltext_in_pmc"]:
        rec["data_class"] = "no statement found"
    else:
        rec["data_class"] = "unknown (no full text)"

    if n % 20 == 0:
        print(f"  {n}/{len(pmcs)}")
        (CACHE / "openness.json").write_text(json.dumps(list(papers.values()), indent=1))
    time.sleep(0.4)

for p in papers.values():
    if not p.get("pmcid"):
        p["data_class"] = "unknown (not in PMC)"

(CACHE / "openness.json").write_text(json.dumps(list(papers.values()), indent=1))

n = len(papers)
print(f"\n{n} papers\n")
print("open access:")
for k, v in collections.Counter(p["oa_status"] for p in papers.values()).most_common():
    print(f"  {str(k):16s} {v}")
print(f"\nin PMC with full text : {sum(1 for p in papers.values() if p['fulltext_in_pmc'])}")
print("\ndata availability:")
for k, v in collections.Counter(p["data_class"] for p in papers.values()).most_common():
    print(f"  {k:26s} {v:4d}  ({v/n:.0%})")
print(f"\nwith a code repository    : {sum(1 for p in papers.values() if p['code_repos'])}")
print(f"with public accessions    : {sum(1 for p in papers.values() if p['accessions'])}")
print(f"naming a data repository  : {sum(1 for p in papers.values() if p['repositories'])}")
print("\npapers with code:")
for p in papers.values():
    if p["code_repos"]:
        print(f"  pmid {p['pubmed_id']}: {', '.join(p['code_repos'][:3])}")
