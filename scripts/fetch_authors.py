"""Add first-author surnames and years to the cached PubMed records, for @authorYEAR citekeys."""
import itertools, json, pathlib, re, time, requests

CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")
assoc = json.loads((CACHE / "stage3_associations.json").read_text())
pmid_set = {int(a["pubmed_id"]) for a in assoc if a.get("pubmed_id")}

# Also cover findings that exist only in the curated Dataverse release, or their citekeys
# come out as @unknownnd.
dep = CACHE / "deposit_marker_associations.csv"
if dep.exists():
    import csv
    with open(dep, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            v = (row.get("pubmed_id") or "").strip()
            if v.isdigit():
                pmid_set.add(int(v))
pmids = sorted(pmid_set)
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def chunks(seq, n):
    it = iter(seq)
    while (b := list(itertools.islice(it, n))):
        yield b

out = {}
for block in chunks(pmids, 200):
    r = requests.get(EUTILS, params={"db": "pubmed", "id": ",".join(map(str, block)),
                                     "retmode": "json"}, timeout=60)
    r.raise_for_status()
    res = r.json().get("result", {})
    for pid in res.get("uids", []):
        rec = res[pid]
        authors = [a.get("name", "") for a in rec.get("authors", []) if a.get("authtype") == "Author"]
        first = rec.get("sortfirstauthor") or (authors[0] if authors else "")
        # PubMed's sortfirstauthor is "Surname Initials", and the surname may carry particles
        # or be multi-word: "de Kant E" -> dekant, "Di Nicolantonio F" -> dinicolantonio,
        # "McKay GJ" -> mckay. A collective author has no trailing initials token.
        toks = first.split() if first else []
        if len(toks) > 1 and re.fullmatch(r"[A-Z][A-Za-z]{0,3}", toks[-1]):
            toks = toks[:-1]
        if len(toks) > 3:          # collective author, e.g. "UK Collaborative Group on ..."
            toks = toks[:2]
        surname = re.sub(r"[^A-Za-z]", "", "".join(toks))[:24]
        out[int(pid)] = {
            "pubmed_id": int(pid),
            "first_author": first,
            "surname": surname.lower(),
            "author_count": len(authors),
            "last_author": authors[-1] if authors else "",
            "pub_date": rec.get("pubdate"),
            "journal": rec.get("fulljournalname"),
            "title": rec.get("title"),
        }
    print(f"  {len(out)}/{len(pmids)}")
    time.sleep(0.36)

(CACHE / "stage4_authors.json").write_text(json.dumps(list(out.values()), indent=1))
missing = [p for p in pmids if p not in out]
print(f"\nwrote {len(out)} author records; {len(missing)} PubMed IDs returned nothing")
nosurname = [v for v in out.values() if not v["surname"]]
print(f"{len(nosurname)} records have no usable surname")
