"""Pull verbatim evidence for each openness check, plus the fields needed for APA 7th citations.

For every source paper this collects:
  - the data-availability statement, verbatim, with the section heading it sits under
  - the sentence containing each code repository URL
  - the sentence containing each public accession
  - full citation fields from PubMed esummary: every author, volume, issue, pages

PMC XML is not paginated, so APA 7th's rule for unpaginated sources applies: cite the section
name rather than a page number. Journal page ranges come from esummary and are used in the
reference list entries.

Writes cache/open_quotes.json.

    python3 -I scripts/extract_open_quotes.py
"""
import itertools
import json
import pathlib
import re
import time

import requests

CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")
UA = {"User-Agent": "malaria-evidence-audit/1.0 (research script; no contact configured)"}
TOOL = {"tool": "malaria-evidence-audit"}

openness = json.loads((CACHE / "openness.json").read_text())
by_pmid = {o["pubmed_id"]: o for o in openness if o.get("pubmed_id")}
print(f"{len(openness)} papers, {sum(1 for o in openness if o.get('pmcid'))} in PMC")

# ------------------------------------------- full citation fields from esummary
pmids = [str(p) for p in by_pmid]
cites = {}


def chunks(seq, n):
    it = iter(seq)
    while (b := list(itertools.islice(it, n))):
        yield b


print("\nesummary for citation fields")
for block in chunks(pmids, 150):
    r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
                     params={"db": "pubmed", "id": ",".join(block), "retmode": "json", **TOOL},
                     headers=UA, timeout=90)
    r.raise_for_status()
    res = r.json().get("result", {})
    for pid in res.get("uids", []):
        rec = res[pid]
        cites[int(pid)] = {
            "authors": [a.get("name") for a in rec.get("authors", [])
                        if a.get("authtype") == "Author"],
            "year": (re.match(r"(\d{4})", rec.get("pubdate") or "") or [None])[0]
                    if re.match(r"(\d{4})", rec.get("pubdate") or "") else None,
            "title": (rec.get("title") or "").rstrip("."),
            "journal": rec.get("fulljournalname"),
            "volume": rec.get("volume") or "",
            "issue": rec.get("issue") or "",
            "pages": rec.get("pages") or "",
            "doi": next((a.get("value") for a in rec.get("articleids", [])
                         if a.get("idtype") == "doi"), None),
        }
    print(f"  {len(cites)}/{len(pmids)}")
    time.sleep(0.4)

# --------------------------------------------------- verbatim quotes from PMC
AVAIL_TITLE = re.compile(r"availab|data sharing|data access|accession", re.I)
CODE_RE = re.compile(r"(?:github|gitlab|bitbucket)\.com/[\w\-\./]+|zenodo\.org/record/\d+", re.I)
ACC_RE = re.compile(r"PRJNA\d+|PRJEB\d+|ERP\d{6}|SRP\d{6}|SRR\d{6,}|GSE\d+|ERS\d{6,}")


def clean(x):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x)).strip()


def sentences_with(text, pattern):
    """Sentences containing a match, with surrounding whitespace tidied."""
    out = []
    for m in pattern.finditer(text):
        start = max(0, text.rfind(".", 0, m.start()) + 1)
        end = text.find(".", m.end())
        end = len(text) if end == -1 else end + 1
        snip = text[start:end].strip()
        if 20 < len(snip) < 600 and snip not in out:
            out.append(snip)
    return out[:3]


pmcs = [(o["pmcid"], o) for o in openness if o.get("pmcid")]
print(f"\nPMC full text for {len(pmcs)} papers")
quotes = {}
for n, (pmcid, o) in enumerate(pmcs, 1):
    try:
        r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                         params={"db": "pmc", "id": pmcid, "retmode": "xml", **TOOL},
                         headers=UA, timeout=120)
    except requests.RequestException:
        continue
    if r.status_code != 200:
        continue
    t = r.text
    rec = {"pmcid": pmcid, "availability": None, "availability_section": None,
           "code_quotes": [], "accession_quotes": []}

    # The availability statement, with the heading it sits under
    for m in re.finditer(r"<(sec|notes)[^>]*>\s*<title>([^<]{0,120})</title>(.{0,3000}?)</\1>",
                         t, re.S):
        title = clean(m.group(2))
        if AVAIL_TITLE.search(title):
            rec["availability"] = clean(m.group(3))[:500]
            rec["availability_section"] = title
            break
    if rec["availability"] is None:
        m = re.search(r"<(notes)[^>]*data-availability[^>]*>(.{0,2000}?)</\1>", t, re.S | re.I)
        if m:
            rec["availability"] = clean(m.group(2))[:500]
            rec["availability_section"] = "Data availability"

    flat = clean(t)
    rec["code_quotes"] = sentences_with(flat, CODE_RE)
    rec["accession_quotes"] = sentences_with(flat, ACC_RE)
    quotes[o["pubmed_id"]] = rec

    if n % 20 == 0:
        print(f"  {n}/{len(pmcs)}")
    time.sleep(0.4)

out = []
for o in openness:
    pid = o.get("pubmed_id")
    out.append({**o, "citation": cites.get(pid), "quotes": quotes.get(pid)})
(CACHE / "open_quotes.json").write_text(json.dumps(out, indent=1))

got_stmt = sum(1 for r in out if (r.get("quotes") or {}).get("availability"))
got_code = sum(1 for r in out if (r.get("quotes") or {}).get("code_quotes"))
got_acc = sum(1 for r in out if (r.get("quotes") or {}).get("accession_quotes"))
got_cite = sum(1 for r in out if r.get("citation") and r["citation"].get("authors"))
print(f"\nverbatim availability statements : {got_stmt}")
print(f"papers with a code sentence      : {got_code}")
print(f"papers with an accession sentence: {got_acc}")
print(f"full citation fields             : {got_cite} of {len(out)}")
missing_pages = [r for r in out if r.get("citation") and not r["citation"].get("pages")]
print(f"citations without a page range   : {len(missing_pages)}")
