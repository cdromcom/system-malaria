"""
Harvest antimalarial drug-resistance evidence from the System Public Graph.

Runs in four stages so you can see what each one costs before paying for the next.
Everything is cached to cache/*.json, so re-running a stage you've already done is free.

  python3 harvest.py --probe        # 2 calls: confirm the API is up and field names match
  python3 harvest.py --stage 1      # find variables by name, across every search term
  python3 harvest.py --stage 2      # find grounded concepts, pull sibling variables
  python3 harvest.py --stage 3      # pull associations for the marker variables
  python3 harvest.py --stage 4      # pull study metadata, then PubMed publication dates

Vocabulary, since the graph's own terms are not obvious:
  variable    - one measured thing, as named in a paper ("pfmdr1 N86Y", "parasite clearance")
  association - one statistical result linking two variables, from one study
  concept     - a variable grounded to a Wikidata entry, so synonyms collapse together
  study       - the paper an association came from, with a DOI and PubMed ID
"""

import argparse
import itertools
import json
import os
import pathlib
import re
import sys
import time
from collections import Counter, defaultdict

import requests
from dotenv import load_dotenv

load_dotenv()

BASE = "https://public-api.system.com"  # paths below already carry the /v1 prefix
API_KEY = os.environ.get("SYSTEM_API_KEY")
if not API_KEY:
    sys.exit("SYSTEM_API_KEY not set. Put it in .env next to this script.")
NCBI_KEY = os.environ.get("NCBI_API_KEY")

ROOT = pathlib.Path(__file__).parent
CACHE = ROOT / "cache"
DATA = ROOT / "data"
CACHE.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

# ---------------------------------------------------------------- search terms

# Resistance markers. These are the anchors: stage 3 pulls associations for these
# variables only, because pulling them for every drug and outcome term too would run
# into tens of thousands of requests and the daily budget is 10,000.
MARKERS = {
    "pfkelch13": [
        "k13", "pfk13", "kelch13", "kelch 13", "pfkelch13", "kelch-13",
        "kelch propeller", "propeller domain",
        "C580Y", "R561H", "R622I", "P441L", "A675V", "Y493H", "I543T",
        "N458Y", "F446I", "P553L", "C469Y", "C469F", "A578S",
        "artemisinin resistance", "artemisinin partial resistance",
        "artemisinin-resistant", "delayed parasite clearance",
    ],
    "pfcrt": [
        "pfcrt", "crt", "chloroquine resistance transporter",
        "K76T", "76T", "CVIET", "CVMNK", "SVMNT", "CVMET",
        "I356T", "N326S", "A220S", "Q271E", "chloroquine resistance",
    ],
    "pfmdr1": [
        "pfmdr1", "pfmdr", "mdr1", "mdr-1", "multidrug resistance 1",
        "multidrug resistance protein 1", "multidrug resistance transporter",
        "P-glycoprotein homologue 1", "pgh1", "pgh-1",
        "N86Y", "86Y", "Y184F", "184F", "S1034C", "N1042D", "D1246Y", "1246Y",
        "pfmdr1 copy number", "mdr1 copy number", "gene amplification",
        "NFD haplotype", "NYD haplotype",
    ],
    "pfdhfr": [
        "dhfr", "pfdhfr", "dihydrofolate reductase",
        "N51I", "C59R", "S108N", "I164L", "A16V",
        "triple mutant", "quadruple mutant", "pyrimethamine resistance",
    ],
    "pfdhps": [
        "dhps", "pfdhps", "dihydropteroate synthase",
        "S436A", "A437G", "K540E", "A581G", "A613S", "A613T",
        "quintuple mutant", "sextuple mutant", "sulfadoxine resistance",
        "sulphadoxine resistance",
    ],
    "plasmepsin": [
        "plasmepsin 2", "plasmepsin II", "plasmepsin 2/3", "plasmepsin-2",
        "pm2", "pm2/3", "piperaquine resistance",
    ],
    "other_markers": [
        "pfaat1", "pfcoronin", "pfubp1", "pfap2mu", "pfexo", "pfexonuclease",
        "E415G", "pfmrp1", "pfnhe1", "ms4760", "pfatp6", "pfubp-1",
        "molecular marker of resistance", "drug resistance marker",
        "resistance-associated mutation", "resistance mutation",
    ],
}

# Drugs. Broad on purpose, and includes both spellings where they differ
# (sulfadoxine / sulphadoxine).
DRUGS = [
    "artemisinin", "artemether", "artesunate", "dihydroartemisinin",
    "artemisinin-based combination therapy", "ACT",
    "artemether-lumefantrine", "lumefantrine",
    "dihydroartemisinin-piperaquine", "piperaquine",
    "artesunate-amodiaquine", "amodiaquine",
    "artesunate-mefloquine", "mefloquine",
    "chloroquine", "quinine", "halofantrine",
    "sulfadoxine", "sulphadoxine", "pyrimethamine",
    "sulfadoxine-pyrimethamine", "sulphadoxine-pyrimethamine",
    "primaquine", "tafenoquine", "atovaquone", "proguanil",
    "atovaquone-proguanil", "doxycycline", "clindamycin",
    "seasonal malaria chemoprevention", "intermittent preventive treatment",
    "IPTp", "IPTi", "mass drug administration",
]

# Outcomes. Both spellings of every word that differs between American and British
# usage: parasitemia/parasitaemia, anemia/anaemia, hemoglobin/haemoglobin,
# hospitalization/hospitalisation.
OUTCOMES = [
    "parasite clearance", "parasite clearance half-life", "parasite clearance time",
    "parasite clearance rate", "fever clearance time",
    "day 3 positivity", "day-3 positivity", "day 3 parasitemia", "day 3 parasitaemia",
    "treatment failure", "early treatment failure",
    "late clinical failure", "late parasitological failure",
    "recrudescence", "reinfection", "re-infection",
    "adequate clinical and parasitological response", "ACPR", "cure rate",
    "IC50", "EC50", "IC90", "in vitro susceptibility", "ex vivo susceptibility",
    "drug susceptibility", "parasite survival rate", "ring-stage survival assay",
    "prevalence", "allele frequency", "mutant prevalence", "mutation prevalence",
    "polymorphism frequency", "genotype frequency",
    "parasitemia", "parasitaemia", "parasite density", "parasite prevalence",
    "gametocyte carriage", "gametocytemia", "gametocytaemia",
    "anemia", "anaemia", "severe anemia", "severe anaemia",
    "hemoglobin", "haemoglobin", "hematocrit", "haematocrit",
    "severe malaria", "cerebral malaria", "uncomplicated malaria",
    "malaria incidence", "malaria mortality", "all-cause mortality", "mortality",
    "hospitalization", "hospitalisation", "birth weight", "low birth weight",
]

CONCEPT_TERMS = [
    "Plasmodium falciparum", "Plasmodium vivax", "malaria", "antimalarial",
    "drug resistance", "antimalarial drug resistance", "multidrug resistance",
    "chloroquine", "artemisinin", "sulfadoxine", "pyrimethamine",
    "dihydrofolate reductase", "dihydropteroate synthase", "P-glycoprotein",
]

# ------------------------------------------------------------------ API client

SESSION = requests.Session()
SESSION.headers.update({"x-api-key": API_KEY, "Accept": "application/json"})

STATE = {"requests": 0, "budget": 9000}


def api_get(path, params=None, retries=8, retry_500=False):
    """GET one page. HTTP 500 is a dead end on some beta endpoints (concepts search,
    concept IDs starting with '-'), so by default don't burn backoff time on it."""
    if STATE["requests"] >= STATE["budget"]:
        raise SystemExit(f"\nStopping: hit the self-imposed budget of {STATE['budget']} requests.")
    url = f"{BASE}{path}"
    for attempt in range(retries):
        STATE["requests"] += 1
        try:
            r = SESSION.get(url, params=params, timeout=60)
        except requests.RequestException as exc:
            wait = 2 ** attempt
            print(f"\n  network error on {path}: {exc} — retry in {wait}s")
            time.sleep(wait)
            continue
        if r.status_code == 200:
            return r.json()
        if r.status_code == 404:
            return None
        if r.status_code == 500 and not retry_500:
            raise RuntimeError(f"HTTP 500 {url} {params}")
        if r.status_code == 500 and retry_500:
            # Flaky, not deterministic: the same ID usually succeeds on retry.
            time.sleep(0.4 * (attempt + 1))
            continue
        if r.status_code in (429, 502, 503, 504):
            wait = 2 ** attempt
            print(f"\n  HTTP {r.status_code} on {path} — retry in {wait}s")
            time.sleep(wait)
            continue
        raise RuntimeError(f"HTTP {r.status_code} {url} {params}\n{r.text[:500]}")
    raise RuntimeError(f"gave up after {retries} attempts: {url} {params}")


def paginate(path, params=None, page_size=200, cap=20000, retry_500=False):
    """Walk offset/limit pagination. The API defaults limit to 10, so always set it."""
    params = dict(params or {})
    params["limit"] = page_size
    out, offset = [], 0
    while len(out) < cap:
        params["offset"] = offset
        payload = api_get(path, params, retry_500=retry_500)
        if not payload:
            break
        batch = payload.get("data") if isinstance(payload, dict) else payload
        if not batch:
            break
        out.extend(batch)
        if len(batch) < page_size:
            break
        offset += page_size
    return out[:cap]


def save(name, obj):
    path = CACHE / f"{name}.json"
    path.write_text(json.dumps(obj, indent=1))
    print(f"  cached -> {path.relative_to(ROOT)}  ({path.stat().st_size/1024:.0f} KB)")


def load(name):
    path = CACHE / f"{name}.json"
    if not path.exists():
        sys.exit(f"Missing {path.relative_to(ROOT)} — run the earlier stage first.")
    return json.loads(path.read_text())


# ----------------------------------------------------------------------- probe

def probe():
    """Two calls to confirm the API answers and the field names are what we expect."""
    print("Probing the API...\n")
    payload = api_get("/v1/associations", {"limit": 1, "include_total": "true"})
    total = payload.get("total")
    rec = payload["data"][0]
    print(f"  associations in graph: {total:,}")
    print(f"  association fields: {sorted(rec.keys())}\n")
    print(json.dumps(rec, indent=2)[:1200])

    # Does name search behave like substring matching or exact matching?
    for term in ("pfmdr1", "mdr1", "parasitaemia"):
        hits = api_get("/v1/variables", {"search": f"name:{term}", "limit": 5, "include_total": "true"})
        n = hits.get("total")
        names = [h["name"] for h in hits.get("data", [])]
        print(f"\n  search name:{term!r} -> total={n}")
        for nm in names:
            print(f"      {nm[:90]}")
    print(f"\nrequests used: {STATE['requests']}")


# --------------------------------------------------------------------- stage 1

def stage1():
    """Search variables by name for every term, tagging each hit with its term and category."""
    groups = [(f"marker:{m}", terms) for m, terms in MARKERS.items()]
    groups += [("drug", DRUGS), ("outcome", OUTCOMES)]

    found = {}           # variable id -> record
    tags = defaultdict(set)   # variable id -> {"marker:pfcrt", "drug", ...}
    hits_by_term = {}

    total_terms = sum(len(t) for _, t in groups)
    i = 0
    for category, terms in groups:
        for term in terms:
            i += 1
            CAP = 1000  # keeps a very common word from eating the request budget
            hits = paginate("/v1/variables", {"search": f"name:{term}"}, page_size=200, cap=CAP)
            truncated = len(hits) >= CAP
            hits_by_term[f"{category}|{term}"] = {"n": len(hits), "truncated": truncated}
            for h in hits:
                found[h["system_id"]] = h
                tags[h["system_id"]].add(category)
                tags[h["system_id"]].add(f"term={term}")
            print(f"  [{i:3d}/{total_terms}] {category:22s} {term[:40]:42s} {len(hits):6d}")

    records = []
    for vid, rec in found.items():
        t = tags[vid]
        records.append({
            "system_id": vid,
            "name": rec.get("name"),
            "concept_id": rec.get("concept_id"),
            "categories": sorted(c for c in t if not c.startswith("term=")),
            "terms": sorted(c[5:] for c in t if c.startswith("term=")),
        })

    print(f"\n{len(records)} distinct variables found")
    cat_counts = Counter(c for r in records for c in r["categories"])
    for c, n in cat_counts.most_common():
        print(f"  {c:24s} {n:6d}")

    save("stage1_variables", records)
    save("stage1_hits_by_term", hits_by_term)
    print(f"requests used: {STATE['requests']}")
    return records


# --------------------------------------------------------------------- stage 2

def stage2():
    """Find grounded concepts, then pull their sibling variables to catch missed names."""
    variables = load("stage1_variables")

    concepts = {}
    broken_fields = set()
    for term in CONCEPT_TERMS:
        # wikidata_aliases is documented as searchable but returns HTTP 500 in the beta,
        # so a failure on one field must not kill the run.
        for field in ("wikidata_label", "wikidata_aliases"):
            if field in broken_fields:
                continue
            try:
                for c in paginate("/v1/concepts", {"search": f"{field}:{term}"}, page_size=100, cap=1000):
                    concepts[c["system_id"]] = c
            except RuntimeError as exc:
                broken_fields.add(field)
                print(f"  search field {field!r} is erroring server-side — skipping it\n    {exc}")
        print(f"  concept search {term[:40]:42s} running total {len(concepts)}")
    print(f"\n{len(concepts)} distinct concepts from topic search")

    # Which concepts do our marker variables actually ground to?
    marker_ids = {v["system_id"] for v in variables
                  if any(c.startswith("marker:") for c in v["categories"])}
    marker_concepts = sorted({v["concept_id"] for v in variables
                              if v["system_id"] in marker_ids and v.get("concept_id")})
    grounded = sum(1 for v in variables if v["system_id"] in marker_ids and v.get("concept_id"))
    print(f"\nmarker variables: {len(marker_ids)}")
    print(f"  grounded to a concept: {grounded} ({grounded/max(len(marker_ids),1):.0%})")
    print(f"  distinct concepts they use: {len(marker_concepts)}")

    detail, failed = [], []
    for cid in marker_concepts:
        try:
            c = api_get(f"/v1/concepts/{cid}")
        except RuntimeError:
            failed.append(cid)
            continue
        if c:
            concepts[cid] = c
            detail.append(c)
            print(f"    {cid}  {str(c.get('wikidata_id')):12s}  {c.get('wikidata_label')}")
    if failed:
        print(f"\n  {len(failed)} concept IDs returned HTTP 500 and were skipped, e.g. {failed[:5]}")

    # Sibling variables: same concept, different name. Catches spellings we didn't guess.
    known = {v["system_id"] for v in variables}
    siblings = []
    for cid in marker_concepts:
        try:
            sibs = paginate(f"/v1/concepts/{cid}/variables", page_size=200, cap=2000)
        except RuntimeError:
            continue
        for s in sibs:
            if s["system_id"] not in known:
                s = dict(s)
                s["categories"] = [f"concept:{cid}"]
                s["terms"] = []
                siblings.append(s)
                known.add(s["system_id"])
    print(f"\n{len(siblings)} extra variables found via concepts that name search missed")
    for s in siblings[:40]:
        print(f"    {s['system_id']}  {str(s.get('name'))[:90]}")

    save("stage2_concepts", list(concepts.values()))
    save("stage2_sibling_variables", siblings)
    print(f"requests used: {STATE['requests']}")


# --------------------------------------------------------------------- stage 3

def stage3(max_variables=None):
    """Pull associations for the marker variables (both sides of the edge)."""
    variables = load("stage1_variables")
    siblings = load("stage2_sibling_variables") if (CACHE / "stage2_sibling_variables.json").exists() else []

    # Two terms are substring-noise: bare "crt" matches cardiac resynchronization therapy
    # and chemoradiotherapy; "gene amplification" is mostly oncology. Drop variables that
    # ONLY those terms found, unless the name itself looks like malaria.
    NOISE_TERMS = {"crt", "gene amplification"}
    RESCUE = re.compile(
        r"pfcrt|plasmodi|falcipar|malaria|chloroquin|parasit|artemisinin|"
        r"\bk?76t?\b|t76|isolate|pfmdr|mutant allele", re.I)

    markers = [v for v in variables if any(c.startswith("marker:") for c in v["categories"])]
    anchors, dropped, rescued = [], 0, 0
    for v in markers:
        if set(v["terms"]) <= NOISE_TERMS:
            if RESCUE.search(v.get("name") or ""):
                anchors.append(v); rescued += 1
            else:
                dropped += 1
        else:
            anchors.append(v)
    # Concept-sibling expansion turned out to be a noise pump: the marker variables ground
    # to generic concepts ("mutation", "antimicrobial resistance"), and "IPT" collides with
    # isoniazid preventive therapy in tuberculosis. 18,380 siblings, 1 malaria-relevant.
    # So require malaria vocabulary in the name before a sibling becomes an anchor.
    MALARIA = re.compile(
        r"malaria|plasmodi|falcipar|parasit|artemisinin|artemether|artesunate|chloroquin|"
        r"amodiaquin|piperaquin|mefloquin|lumefantrin|sulfadoxin|sulphadoxin|pyrimethamin|"
        r"pfcrt|pfmdr|dhfr|dhps|kelch|k13|gametocyt|anophel", re.I)
    sib_keep = [s for s in siblings if MALARIA.search(s.get("name") or "")]
    print(f"  siblings from concepts: {len(siblings)} pulled, {len(sib_keep)} malaria-relevant")
    anchors += sib_keep
    if max_variables:
        anchors = anchors[:max_variables]
    print(f"{len(markers)} marker variables -> {len(anchors)} anchors "
          f"({dropped} dropped as substring noise, {rescued} rescued by name)")

    assoc = {}
    via = defaultdict(set)
    errors = []

    def flush():
        out = []
        for aid, rec in assoc.items():
            rec = dict(rec)
            rec["via_variables"] = sorted(via[aid])
            out.append(rec)
        save("stage3_associations", out)
        return out

    for i, v in enumerate(anchors, 1):
        try:
            hits = paginate(f"/v1/variables/{v['system_id']}/associations", page_size=200,
                            cap=5000, retry_500=True)
        except RuntimeError as exc:
            # Some variable IDs 500 on this sub-resource. Skip them, don't lose the run.
            errors.append({"variable_id": v["system_id"], "name": v.get("name"), "error": str(exc)})
            hits = []
        for h in hits:
            assoc[h["system_id"]] = h
            via[h["system_id"]].add(v["system_id"])
        print(f"  [{i:4d}/{len(anchors)}] {str(v['name'])[:52]:54s} {len(hits):5d} assoc  "
              f"(total {len(assoc)}, err {len(errors)}, reqs {STATE['requests']})")
        if i % 200 == 0:
            flush()  # checkpoint

    records = flush()
    if errors:
        save("stage3_errors", errors)
        print(f"\n{len(errors)} anchor variables returned HTTP 500 and were skipped")

    print(f"\n{len(records)} distinct associations")
    print(f"  distinct studies: {len({r.get('study_id') for r in records if r.get('study_id')})}")
    print(f"  with a pubmed_id: {sum(1 for r in records if r.get('pubmed_id'))}")
    save("stage3_associations", records)
    print(f"requests used: {STATE['requests']}")


# --------------------------------------------------------------------- stage 4

def stage4():
    """Study metadata from System, then publication dates from PubMed."""
    assoc = load("stage3_associations")

    study_ids = sorted({a["study_id"] for a in assoc if a.get("study_id")})
    print(f"fetching {len(study_ids)} studies")
    studies = []
    for i, sid in enumerate(study_ids, 1):
        try:
            s = api_get(f"/v1/studies/{sid}", retry_500=True)
        except RuntimeError:
            continue
        if s:
            studies.append(s)
        if i % 100 == 0:
            print(f"  {i}/{len(study_ids)}  (reqs {STATE['requests']})")
    save("stage4_studies", studies)

    # PubMed esummary: a summary record per paper, including its publication date.
    # Limit is 3 requests/second without an NCBI key, 10 with one. 200 ids per request.
    pmids = sorted({int(a["pubmed_id"]) for a in assoc if a.get("pubmed_id")})
    print(f"\nfetching publication dates for {len(pmids)} PubMed IDs")
    eutils = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    delay = 0.11 if NCBI_KEY else 0.36
    pubmed = []

    def chunks(seq, n):
        it = iter(seq)
        while (block := list(itertools.islice(it, n))):
            yield block

    for block in chunks(pmids, 200):
        params = {"db": "pubmed", "id": ",".join(map(str, block)), "retmode": "json"}
        if NCBI_KEY:
            params["api_key"] = NCBI_KEY
        for attempt in range(4):
            try:
                r = requests.get(eutils, params=params, timeout=60)
                r.raise_for_status()
                break
            except requests.RequestException as exc:
                print(f"  pubmed error: {exc} — retrying")
                time.sleep(2 ** attempt)
        else:
            continue
        result = r.json().get("result", {})
        for pid in result.get("uids", []):
            rec = result[pid]
            pubmed.append({
                "pubmed_id": int(pid),
                "pub_date": rec.get("pubdate"),
                "epub_date": rec.get("epubdate") or None,
                "journal": rec.get("fulljournalname"),
                "title": rec.get("title"),
            })
        print(f"  {len(pubmed)}/{len(pmids)}")
        time.sleep(delay)

    save("stage4_pubmed", pubmed)
    years = sorted(int(p["pub_date"][:4]) for p in pubmed
                   if p.get("pub_date") and p["pub_date"][:4].isdigit())
    if years:
        print(f"\npublication years: {years[0]}–{years[-1]}")
    print(f"requests used: {STATE['requests']}")


# ------------------------------------------------------------------------ main

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--stage", type=int, choices=[1, 2, 3, 4])
    ap.add_argument("--budget", type=int, default=9000, help="max API requests this run")
    ap.add_argument("--max-variables", type=int, default=None, help="stage 3: cap anchor variables")
    args = ap.parse_args()

    STATE["budget"] = args.budget
    start = time.time()

    if args.probe:
        probe()
    elif args.stage == 1:
        stage1()
    elif args.stage == 2:
        stage2()
    elif args.stage == 3:
        stage3(args.max_variables)
    elif args.stage == 4:
        stage4()
    else:
        ap.print_help()

    print(f"\nelapsed {time.time()-start:.0f}s, {STATE['requests']} requests")
