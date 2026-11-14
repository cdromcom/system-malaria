"""Sweep the Dataverse associations.csv for marker evidence and check overlap with the API harvest.

Answers two questions:
  1. How much antimalarial resistance evidence does the curated deposit hold?
  2. How many of our API-harvested findings survive in it (the integrity check System recommends)?

Run with -I; pass the csv path as argv[1].
"""
import csv, json, re, sys, collections, pathlib

CSV = sys.argv[1]
CACHE = pathlib.Path("/Users/ppatel/system-public-challenge/cache")

MARKERS = re.compile(
    r"\bpfcrt\b|chloroquine resistance transporter|\bK76T\b|\b76T\b|\bCVIET\b|\bCVMNK\b|\bSVMNT\b|"
    r"\bpfmdr\s*-?1?\b|\bmdr\s*-?1\b|p-?glycoprotein homolog|\bpgh\s*-?1\b|\bN86Y\b|\bY184F\b|\bD1246Y\b|"
    r"\bpf?dhfr\b|dihydrofolate reductase|\bN51I\b|\bC59R\b|\bS108N\b|\bI164L\b|"
    r"\bpf?dhps\b|dihydropteroate synthase|\bA437G\b|\bK540E\b|\bA581G\b|"
    r"\bpf?kelch\s*-?13\b|\bpfk13\b|\bk13\b|kelch\s*-?13|\bC580Y\b|\bR561H\b|\bR622I\b|\bF446I\b|"
    r"plasmepsin|\bpfaat1\b|\bpfcoronin\b|\bpfexo\b|"
    r"(?:triple|quadruple|quintuple|sextuple) mutant|artemisinin[- ](?:partial[- ])?resistan|"
    r"chloroquine resistan|pyrimethamine resistan|sulfadoxine resistan|piperaquine resistan", re.I)
MALARIA = re.compile(r"malaria|plasmodi|falcipar|\bvivax\b|parasit|artemisinin|artemether|artesunate|"
                     r"chloroquin|amodiaquin|piperaquin|mefloquin|lumefantrin|sulfadoxin|sulphadoxin|"
                     r"pyrimethamin|primaquin|\bquinine\b|pfcrt|pfmdr|pfdhfr|pfdhps|kelch|gametocyt", re.I)
EXCLUDE = re.compile(r"abcb1|c3435t|\b3435\b|chemoradio|resynchroni|chemotherap|doxorubicin|paclitaxel|"
                     r"vincristin|digoxin|\bstatin|tacrolimus|cyclosporin|epileps|carcinoma|leukemi|"
                     r"leukaemi|tubercul|isoniazid|rifampi|methotrexate|\bHER2\b", re.I)

harvested = {a["system_id"] for a in json.loads((CACHE/"stage3_associations.json").read_text())}
evd = json.loads((CACHE/"stage3_associations.json").read_text())
evd_ids = {a["system_id"] for a in evd}

csv.field_size_limit(10**9)
total = 0
deposit_ids = set()
marker_rows = []
overlap = set()
with open(CSV, newline="", encoding="utf-8", errors="replace") as fh:
    for row in csv.DictReader(fh):
        total += 1
        sid = row.get("system_id")
        if sid in evd_ids:
            overlap.add(sid)
        names = f"{row.get('variable_1_name') or ''} {row.get('variable_2_name') or ''}"
        if not MARKERS.search(names):
            continue
        if EXCLUDE.search(names) or not MALARIA.search(names):
            continue
        marker_rows.append(row)

print(f"deposit rows scanned                 : {total:,}")
print(f"marker + malaria associations in it   : {len(marker_rows):,}")
print(f"\nour API harvest                       : {len(evd_ids):,} associations")
print(f"of those, present in the deposit      : {len(overlap):,} ({len(overlap)/len(evd_ids):.1%})")
print(f"API-only (unverified by curation)     : {len(evd_ids)-len(overlap):,}")

with_p = sum(1 for r in marker_rows if (r.get("p_value") or "").strip() not in ("", "NA"))
with_ci = sum(1 for r in marker_rows if (r.get("ci_lower") or "").strip() not in ("", "NA"))
print(f"\nin the deposit's marker rows:")
print(f"  with a p-value                      : {with_p}")
print(f"  with a confidence interval          : {with_ci}")
print("  statistic types:", dict(collections.Counter(r.get("system_statistic_type") for r in marker_rows).most_common(8)))

out = CACHE/"deposit_marker_associations.csv"
if marker_rows:
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(marker_rows[0].keys()))
        w.writeheader(); w.writerows(marker_rows)
    print(f"\nwrote {out}")
    print("\nsample:")
    for r in marker_rows[:12]:
        print(f"  {str(r.get('variable_1_name'))[:46]:48s} | {str(r.get('variable_2_name'))[:40]:42s} "
              f"| {r.get('system_statistic_type')}={r.get('statistic_value')}")
json.dump(sorted(overlap), open(CACHE/"deposit_overlap_ids.json","w"))
