"""Local regex sweep over the Dataverse variables table.

No API, no rate limit, no search terms to guess. Pass the .tab path as an argument.
Run with -I so nothing is imported from the data directory.
"""
import csv, re, sys, collections

PATH = sys.argv[1]

# Marker patterns. Word boundaries and pf- prefixes do the work that the API's
# substring search could not: \bcrt\b will not match "chemoradiotherapy".
MARKERS = {
    "pfkelch13": r"\bpf?kelch\s*-?13\b|\bpfk13\b|\bk13\b|kelch\s*-?13|kelch[- ]like protein 13|propeller domain|"
                 r"\bC580Y\b|\bR561H\b|\bR622I\b|\bP441L\b|\bA675V\b|\bY493H\b|\bI543T\b|\bN458Y\b|\bF446I\b|"
                 r"\bP553L\b|\bC469[YF]\b|\bA578S\b|artemisinin[- ](?:partial[- ])?resistan",
    "pfcrt":     r"\bpfcrt\b|chloroquine resistance transporter|\bK76T\b|\bcrt\b\s*[KT]?76|\b76T\b|"
                 r"\bCVIET\b|\bCVMNK\b|\bSVMNT\b|\bCVMET\b|\bI356T\b|\bN326S\b|chloroquine resistan",
    "pfmdr1":    r"\bpfmdr\s*-?1?\b|\bmdr\s*-?1\b|multidrug resistance (?:protein |transporter|1)|"
                 r"p-?glycoprotein homolog|\bpgh\s*-?1\b|\bN86Y\b|\bY184F\b|\bS1034C\b|\bN1042D\b|\bD1246Y\b|"
                 r"pfmdr1 copy number",
    "pfdhfr":    r"\bpf?dhfr\b|dihydrofolate reductase|\bN51I\b|\bC59R\b|\bS108N\b|\bI164L\b|\bA16V\b|"
                 r"(?:triple|quadruple) mutant|pyrimethamine resistan",
    "pfdhps":    r"\bpf?dhps\b|dihydropteroate synthase|\bS436A\b|\bA437G\b|\bK540E\b|\bA581G\b|\bA613[ST]\b|"
                 r"(?:quintuple|sextuple) mutant|sulfadoxine resistan|sulphadoxine resistan",
    "plasmepsin": r"plasmepsin\s*-?(?:2|3|II|III|2/3)|\bpm2/?3?\b|piperaquine resistan",
    "other":     r"\bpfaat1\b|\bpfcoronin\b|\bpfubp\s*-?1\b|\bpfap2mu\b|\bpfexo\b|\bE415G\b|\bpfmrp1\b|"
                 r"\bpfnhe\s*-?1\b|\bms4760\b|\bpfatp6\b|molecular marker of resistan|drug[- ]resistance marker|"
                 r"resistance[- ]associated mutation",
}
# Must look like malaria, not human ABCB1 / TB / oncology.
MALARIA = re.compile(r"malaria|plasmodi|falcipar|\bvivax\b|parasit|artemisinin|artemether|artesunate|"
                     r"chloroquin|amodiaquin|piperaquin|mefloquin|lumefantrin|sulfadoxin|sulphadoxin|"
                     r"pyrimethamin|primaquin|\bquinine\b|gametocyt|anophel|\bpf[a-z]{2,}\b|"
                     r"\bisolate|\bmutant allele|\bIC50\b", re.I)
EXCLUDE = re.compile(r"abcb1|c3435t|\b3435\b|chemoradio|resynchroni|chemotherap|doxorubicin|paclitaxel|"
                     r"vincristin|digoxin|\bstatin|tacrolimus|cyclosporin|ciclosporin|epileps|carcinoma|"
                     r"leukemi|leukaemi|tubercul|isoniazid|rifampi|rifapentin|methotrexate|\bHER2\b", re.I)

pats = {k: re.compile(v, re.I) for k, v in MARKERS.items()}
hits, counts, excluded = [], collections.Counter(), collections.Counter()

csv.field_size_limit(10**9)
with open(PATH, newline="", encoding="utf-8", errors="replace") as fh:
    reader = csv.DictReader(fh, delimiter="\t")
    total = 0
    for row in reader:
        total += 1
        name = row.get("name") or ""
        matched = [k for k, p in pats.items() if p.search(name)]
        if not matched:
            continue
        if EXCLUDE.search(name):
            for k in matched:
                excluded[k] += 1
            continue
        if not MALARIA.search(name):
            for k in matched:
                excluded[k + " (no malaria context)"] += 1
            continue
        for k in matched:
            counts[k] += 1
        hits.append({"system_id": row["system_id"], "name": name,
                     "concept_id": row.get("concept_id") or "", "markers": "|".join(matched)})

print(f"rows scanned          : {total:,}")
print(f"marker variables kept : {len(hits):,}\n")
print("by marker (a variable can match more than one):")
for k, n in counts.most_common():
    print(f"  {k:12s} {n:6,}")
print("\nrejected:")
for k, n in excluded.most_common():
    print(f"  {k:34s} {n:6,}")

out = "/Users/ppatel/system-public-challenge/cache/bulk_marker_variables.csv"
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["system_id", "name", "concept_id", "markers"])
    w.writeheader(); w.writerows(hits)
print(f"\nwrote {out}")
