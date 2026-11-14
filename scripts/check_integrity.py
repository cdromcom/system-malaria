"""Check every source paper for retractions, errata and expressions of concern.

Two sources, both open and keyed on identifiers we already hold:

  PubMed efetch  — PublicationType plus the CommentsCorrections list, which is where NLM
                   records RetractionIn / ErratumIn / ExpressionOfConcernIn links.
  Crossref       — `update-to` and `updated-by`, which is how Crossref carries retraction and
                   correction notices, including the Retraction Watch data it now hosts.

PubPeer is deliberately not called here: its API requires a devkey (POST returns
HTTP 422 "The devkey field is required") and its search page is a JavaScript app that serves
byte-identical HTML for every query, so it cannot be read without a key or a real browser.

Writes cache/integrity.json.

    python3 -I scripts/check_integrity.py
"""
import json
import pathlib
import time
import xml.etree.ElementTree as ET

import requests

CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")
# A generic client name. No contact address is sent: the papers and identifiers here are the
# user's research material and their address is not ours to publish to third parties.
UA = {"User-Agent": "malaria-evidence-audit/1.0 (research script; no contact configured)"}

FLAG_TYPES = {
    "Retracted Publication": "retracted",
    "Retraction of Publication": "is-retraction-notice",
    "Expression of Concern": "expression-of-concern",
    "Published Erratum": "is-erratum-notice",
}
FLAG_REFS = {
    "RetractionIn": "retracted",
    "ExpressionOfConcernIn": "expression-of-concern",
    "ErratumIn": "corrected",
    "RepublishedIn": "republished",
    "RetractedandRepublishedIn": "retracted-and-republished",
    "UpdateIn": "updated",
    "CommentIn": "commented-on",
}

ids = json.loads((CACHE / "evd_association_ids.json").read_text())
A = {a["system_id"]: a for a in json.loads((CACHE / "stage3_associations.json").read_text())}
ST = {s["study_id"]: s for s in json.loads((CACHE / "stage4_studies.json").read_text())}

papers = {}
for i in ids:
    a = A.get(i)
    if not a:
        continue
    st = ST.get(a.get("study_id")) or {}
    pmid = int(a["pubmed_id"]) if a.get("pubmed_id") else None
    key = pmid or st.get("doi")
    if key is None:
        continue
    papers.setdefault(key, {"pubmed_id": pmid, "doi": st.get("doi"),
                            "study_id": a.get("study_id"), "flags": [], "notes": []})
print(f"{len(papers)} distinct source papers to check")

# ----------------------------------------------------------------- PubMed efetch
pmids = [p["pubmed_id"] for p in papers.values() if p["pubmed_id"]]
print(f"\nPubMed efetch for {len(pmids)} PubMed IDs")
by_pmid = {p["pubmed_id"]: p for p in papers.values() if p["pubmed_id"]}

for start in range(0, len(pmids), 100):
    block = pmids[start:start + 100]
    r = requests.post("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
                      data={"db": "pubmed", "id": ",".join(map(str, block)), "retmode": "xml"},
                      headers=UA, timeout=120)
    r.raise_for_status()
    root = ET.fromstring(r.text)
    for art in root.iter("PubmedArticle"):
        pid_el = art.find(".//MedlineCitation/PMID")
        if pid_el is None:
            continue
        rec = by_pmid.get(int(pid_el.text))
        if rec is None:
            continue
        for pt in art.iter("PublicationType"):
            if pt.text in FLAG_TYPES:
                rec["flags"].append(FLAG_TYPES[pt.text])
                rec["notes"].append(f"PubMed publication type: {pt.text}")
        for cc in art.iter("CommentsCorrections"):
            rt = cc.get("RefType")
            if rt in FLAG_REFS:
                ref_pmid = cc.find("PMID")
                rec["flags"].append(FLAG_REFS[rt])
                rec["notes"].append(
                    f"PubMed CommentsCorrections {rt}"
                    + (f" -> PMID {ref_pmid.text}" if ref_pmid is not None else ""))
    print(f"  {min(start + 100, len(pmids))}/{len(pmids)}")
    time.sleep(0.4)

# --------------------------------------------------------------------- Crossref
dois = [(k, p) for k, p in papers.items() if p["doi"]]
print(f"\nCrossref for {len(dois)} DOIs")
for n, (k, rec) in enumerate(dois, 1):
    try:
        r = requests.get(f"https://api.crossref.org/works/{rec['doi']}", headers=UA, timeout=45)
    except requests.RequestException as e:
        rec["notes"].append(f"Crossref request failed: {type(e).__name__}")
        continue
    if r.status_code != 200:
        rec["notes"].append(f"Crossref HTTP {r.status_code}")
        continue
    m = r.json().get("message", {})
    for u in m.get("update-to", []) or []:
        rec["flags"].append("is-update-notice")
        rec["notes"].append(f"Crossref update-to: {u.get('type')} of {u.get('DOI')}")
    for u in m.get("updated-by", []) or []:
        t = (u.get("type") or "").lower()
        rec["flags"].append("retracted" if "retract" in t
                            else "expression-of-concern" if "concern" in t else "corrected")
        rec["notes"].append(f"Crossref updated-by: {u.get('type')} ({u.get('DOI')})")
    if (m.get("type") or "") in ("retraction", "correction"):
        rec["flags"].append("is-update-notice")
        rec["notes"].append(f"Crossref item type: {m.get('type')}")
    if n % 25 == 0:
        print(f"  {n}/{len(dois)}")
    time.sleep(0.12)

for rec in papers.values():
    rec["flags"] = sorted(set(rec["flags"]))

(CACHE / "integrity.json").write_text(json.dumps(list(papers.values()), indent=1))

import collections
counts = collections.Counter(f for p in papers.values() for f in p["flags"])
print(f"\n{len(papers)} papers checked. Flags found:")
for f, c in counts.most_common():
    print(f"  {f:28s} {c}")
serious = [p for p in papers.values()
           if {"retracted", "expression-of-concern", "retracted-and-republished"} & set(p["flags"])]
print(f"\nSERIOUS (retraction or expression of concern): {len(serious)}")
for p in serious:
    print(f"  PMID {p['pubmed_id']} doi {p['doi']}")
    for nt in p["notes"]:
        print(f"     {nt}")
clean = sum(1 for p in papers.values() if not p["flags"])
print(f"\nno flags at all: {clean} of {len(papers)}")
