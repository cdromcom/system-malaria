"""Build the `system-malaria` Obsidian vault from the harvested System Public Graph data.

Follows living-synthesis discourse-graph conventions: QUE / CLM / EVD / CVT nodes, one file per
node, YAML frontmatter with NodeFormality + nodeID, a `## Source` section, callout blocks, and
`[[short|long]]` wikilinks.

Node titles are written for a non-specialist reader, in the style of the LIVES - EVD sheet: a
full declarative sentence that leads with the number and names both things being related.
Acronyms are expanded on first use in the title and listed in a "Terms explained" block.

Source stubs are named `@<firstauthorsurname><year>` and carry citation data only.

    python3 scripts/build_vault.py
"""
import collections
import datetime as dt
import os
import json
import pathlib
import re
import unicodedata
import uuid

HERE = pathlib.Path("/Users/ppatel/system-public-challenge")
CACHE = HERE / "cache"
# Build into a staging directory when asked. ~/Documents is under iCloud sync, and writing
# hundreds of files there directly races the sync agent, which resolves conflicts by keeping
# both copies and appending " 2". Staging outside iCloud and then rsyncing in avoids that.
VAULT = pathlib.Path(os.environ.get("VAULT_DIR", "/Users/ppatel/Documents/system-malaria"))
TODAY = dt.date.today().isoformat()

A = json.loads((CACHE / "stage3_associations.json").read_text())
STUDIES = {s["study_id"]: s for s in json.loads((CACHE / "stage4_studies.json").read_text())}
PUBMED = {p["pubmed_id"]: p for p in json.loads((CACHE / "stage4_pubmed.json").read_text())}
AUTHORS = {a["pubmed_id"]: a for a in json.loads((CACHE / "stage4_authors.json").read_text())}
# The author fetch also carries pub_date, journal and title, so it backfills any PubMed ID the
# earlier stage-4 run never saw (e.g. a finding found only in the Dataverse release).
for _pid, _rec in AUTHORS.items():
    PUBMED.setdefault(_pid, {k: _rec.get(k) for k in ("pub_date", "journal", "title")})

_overlap = CACHE / "deposit_overlap_ids.json"
DEPOSIT_IDS = set(json.loads(_overlap.read_text())) if _overlap.exists() else set()

# Full single-record detail from the API: p_value, confidence interval, concept IDs. The list
# endpoint omits all of these, so this is a separate fetch (scripts/fetch_detail.py).
_detail = CACHE / "stage5_detail.json"
DETAIL = ({d["system_id"]: d for d in json.loads(_detail.read_text())}
          if _detail.exists() else {})

# The curated Harvard Dataverse release, swept for marker findings. Used two ways: as the
# verification signal, and as a statistics fallback where the API detail call came back empty.
# Retraction / erratum / expression-of-concern check against PubMed and Crossref
# (scripts/check_integrity.py). Keyed by PubMed ID where available, else DOI.
_integ = CACHE / "integrity.json"
INTEGRITY = {}
if _integ.exists():
    for _rec in json.loads(_integ.read_text()):
        if _rec.get("pubmed_id"):
            INTEGRITY[_rec["pubmed_id"]] = _rec
        if _rec.get("doi"):
            INTEGRITY[_rec["doi"]] = _rec

FLAG_LABEL = {
    "retracted": "**RETRACTED**",
    "expression-of-concern": "**expression of concern issued**",
    "retracted-and-republished": "**retracted and republished**",
    "corrected": "a published erratum exists",
    "republished": "republished",
    "updated": "an update notice exists",
    "commented-on": "formal published comments exist",
    "is-retraction-notice": "this item is itself a retraction notice",
    "is-erratum-notice": "this item is itself an erratum",
    "is-update-notice": "this item is itself an update notice",
}
SERIOUS_FLAGS = {"retracted", "expression-of-concern", "retracted-and-republished"}


def integrity_of(a, st):
    """The integrity record for the paper behind one finding."""
    return (INTEGRITY.get(a.get("pubmed_id"))
            or INTEGRITY.get((st or {}).get("doi")) or {})


# retractionrisk.com: Retraction Watch status plus Altmetric social attention
_rr = CACHE / "retractionrisk.json"
RETRACTIONRISK = {}
if _rr.exists():
    for _rec in json.loads(_rr.read_text()):
        if _rec.get("doi"):
            RETRACTIONRISK[_rec["doi"]] = _rec

# OpenAlex open-access status, plus data and code availability read out of PMC full text
_open = CACHE / "openness.json"
OPENNESS = {}
if _open.exists():
    for _rec in json.loads(_open.read_text()):
        if _rec.get("pubmed_id"):
            OPENNESS[_rec["pubmed_id"]] = _rec
        if _rec.get("doi"):
            OPENNESS[_rec["doi"]] = _rec


def rr_of(st):
    return RETRACTIONRISK.get((st or {}).get("doi")) or {}


def open_of(a, st):
    return (OPENNESS.get(a.get("pubmed_id"))
            or OPENNESS.get((st or {}).get("doi")) or {})


DATA_CLASS_LABEL = {
    "deposited": "Deposited in a public repository",
    "on request": "Available from the authors on request only",
    "statement, unclear": "A statement exists but is not explicit",
    "no statement found": "No availability statement found in the full text",
    "unknown (no full text)": "Cannot tell — PMC holds front matter only",
    "unknown (not in PMC)": "Cannot tell — not deposited in PMC",
    "unknown": "Not determined",
}


def screening_rows(a, st):
    """The rows shared by evidence notes and source notes."""
    integ = integrity_of(a, st)
    rr = rr_of(st)
    op = open_of(a, st)
    pp = pubpeer_of(a, st)
    flags = set(integ.get("flags") or [])
    n_comments = sum(1 for n in (integ.get("notes") or []) if "CommentIn" in n)
    xneg = rr.get("x_negative") or 0
    bsky = rr.get("bluesky") or 0

    rows = [
        ("Retraction status",
         ("**RETRACTED**" if "retracted" in flags else
          "**Expression of concern**" if "expression-of-concern" in flags else
          "No retraction found")
         + f" (Retraction Watch via retractionrisk.com: {rr.get('rw_status') or 'not returned'})"),
        ("Published erratum",
         "Yes — " + "; ".join(n for n in (integ.get("notes") or [])
                              if "Erratum" in n or "correction" in n) if "corrected" in flags
         else "None found"),
        ("Formal published comments",
         f"{n_comments} indexed in PubMed" if n_comments else "None"),
        ("Critical social posts",
         (f"{xneg} negative X/Twitter, {bsky} Bluesky" if (xneg or bsky)
          else "None recorded")
         + " — algorithmic sentiment; for these papers it often reflects alarm at the findings "
           "rather than doubt about the work"),
        ("PubPeer",
         ((f"{pp.get('total_comments')} comment(s)"
           + (f", flagged {', '.join(pp['update_types'])}" if pp.get("update_types") else "")
           + f" — {pp.get('pubpeer_url')}")
          if pp.get("on_pubpeer") else
          "No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation "
          "API; see [[CVT - What the post-publication screen covers and what it cannot]])")),
        ("Open access", (f"Yes ({op.get('oa_status')})" if op.get("oa")
                         else "No" if op.get("oa") is False else "Not determined")),
        ("Open data", DATA_CLASS_LABEL.get(op.get("data_class"), "Not determined")
         + (f" — {', '.join(op.get('repositories') or [])}" if op.get("repositories") else "")),
        ("Open code", ", ".join(op.get("code_repos") or []) or "None found"),
        ("Public accessions", ", ".join((op.get("accessions") or [])[:5]) or "None found"),
    ]
    return rows, integ, rr, op


# PubPeer, via the official PubPeer Foundation extension API (scripts/check_pubpeer.py).
# PubPeer returns a record only for publications with activity, so absence is a clean negative.
_pp = CACHE / "pubpeer.json"
PUBPEER = {}
if _pp.exists():
    for _rec in json.loads(_pp.read_text()):
        if _rec.get("pubmed_id"):
            PUBPEER[_rec["pubmed_id"]] = _rec
        if _rec.get("doi"):
            PUBPEER[_rec["doi"]] = _rec


def pubpeer_of(a, st):
    return (PUBPEER.get(a.get("pubmed_id"))
            or PUBPEER.get((st or {}).get("doi")) or {})


_dep = CACHE / "deposit_marker_associations.csv"
DEPOSIT_ROWS = {}
if _dep.exists():
    import csv as _csv
    with open(_dep, newline="", encoding="utf-8") as fh:
        for _r in _csv.DictReader(fh):
            DEPOSIT_ROWS[_r["system_id"]] = _r


def _num(v):
    try:
        return float(v) if str(v).strip() not in ("", "NA", "None") else None
    except (TypeError, ValueError):
        return None


def enrich(a):
    """Merge list record + API detail + deposit row. Returns a new dict and its provenance."""
    out = dict(a)
    sources = ["API list"]
    det = DETAIL.get(a["system_id"])
    if det:
        sources.append("API detail")
        for k in ("p_value", "p_value_equality", "ci_level", "ci_lower", "ci_upper",
                  "variable_1_concept_id", "variable_2_concept_id",
                  "variable_1_wikidata_id", "variable_2_wikidata_id"):
            if det.get(k) is not None:
                out[k] = det[k]
    dep = DEPOSIT_ROWS.get(a["system_id"])
    # Presence in the release is judged by the full overlap check, not only by my marker-filtered
    # sweep of it — 30 of these findings are in the release while 25 matched that sweep.
    if a["system_id"] in DEPOSIT_IDS or dep:
        sources.append("Dataverse release")
    if dep:
        for k in ("p_value", "ci_level", "ci_lower", "ci_upper"):
            if out.get(k) is None:
                out[k] = _num(dep.get(k))
        if not out.get("p_value_equality") and dep.get("p_value_equality"):
            out["p_value_equality"] = dep["p_value_equality"]
    return out, sources

# --------------------------------------------------------------------- vocabulary

MARKER_PATTERNS = {
    "Pfkelch13": r"\bpf?kelch\s*-?13\b|\bpfk13\b|\bk13\b|kelch\s*-?13|propeller|\bC580Y\b|\bR561H\b|"
                 r"\bR622I\b|\bP441L\b|\bA675V\b|\bF446I\b|\bC469[YF]\b|artemisinin[- ](?:partial[- ])?resistan",
    "PfCRT":     r"\bpfcrt\b|chloroquine resistance transporter|\bK76T\b|\b76T\b|\bCVIET\b|\bCVMNK\b|"
                 r"\bSVMNT\b|\bI356T\b|\bN326S\b|chloroquine resistan|\bcg2\b",
    "Pfmdr1":    r"\bpfmdr\s*-?1?\b|\bmdr\s*-?1\b|multidrug resistance|p-?glycoprotein homolog|"
                 r"\bpgh\s*-?1\b|\bN86Y?\b|\b86Y\b|\bY184F?\b|\b184F\b|\bD1246Y\b|copy number",
    "PfDHFR":    r"\bpf?dhfr\b|dihydrofolate reductase|\bN51I\b|\bC59R\b|\bS108N\b|\bI164L\b|"
                 r"(?:triple|quadruple) mutant|pyrimethamine resistan",
    "PfDHPS":    r"\bpf?dhps\b|dihydropteroate synthase|\bS436A\b|\bA437G\b|\bK540E\b|\bA581G\b|"
                 r"(?:quintuple|sextuple) mutant|sulfadoxine resistan|sulphadoxine resistan",
    "Plasmepsin": r"plasmepsin|piperaquine resistan",
    "Other markers": r"\bpfaat1\b|\bpfcoronin\b|\bpfubp\s*-?1\b|\bpfexo\b|\bE415G\b|\bpfmrp1\b|"
                     r"\bpfnhe\s*-?1\b|\bms4760\b|\bpfatp6\b|molecular marker of resistan|"
                     r"drug[- ]resistance marker|resistance[- ]associated mutation",
}
MARKERS = {k: re.compile(v, re.I) for k, v in MARKER_PATTERNS.items()}

MALARIA = re.compile(r"malaria|plasmodi|falcipar|\bvivax\b|parasit|artemisinin|artemether|artesunate|"
                     r"chloroquin|amodiaquin|piperaquin|mefloquin|lumefantrin|sulfadoxin|sulphadoxin|"
                     r"pyrimethamin|primaquin|\bquinine\b|pfcrt|pfmdr|pfdhfr|pfdhps|kelch|\bk13\b|"
                     r"gametocyt|anophel", re.I)
EXCLUDE = re.compile(r"abcb1|c3435t|\b3435\b|chemoradio|resynchroni|chemotherap|doxorubicin|paclitaxel|"
                     r"vincristin|digoxin|\bstatin|tacrolimus|cyclosporin|ciclosporin|epileps|carcinoma|"
                     r"leukemi|leukaemi|tubercul|isoniazid|rifampi|rifapentin|methotrexate|\bHER2\b|"
                     r"\bLSCD\b|limbal|stem cell|\bKLHL13\b|cornea|keratin|conjunctiv", re.I)

THEMES = {
    "treatment failure": r"treatment failure|recrudescen|reinfection|re-infection|cure rate|"
                         r"clinical failure|parasitological failure|\bACPR\b|adequate clinical",
    "parasite clearance": r"clearance|day[- ]3|parasitaem|parasitem|parasite density",
    "marker prevalence": r"prevalen|frequency|haplotype|mutant|polymorphism|genotype|allele",
    "drug susceptibility": r"IC50|EC50|IC90|susceptib|survival (?:rate|assay)|ex vivo|in vitro",
    "blood counts": r"an[ae]emia|h[ae]moglobin|h[ae]matocrit",
    "severe illness": r"severe malaria|cerebral|mortality|hospitali|birth weight",
}
THEME_PATTERNS = {k: re.compile(v, re.I) for k, v in THEMES.items()}

# Plain-English names for each outcome theme, used in claim titles
THEME_PLAIN = {
    "treatment failure": "whether malaria treatment failed",
    "parasite clearance": "how fast malaria parasites cleared from the blood",
    "marker prevalence": "how common the resistance mutation was",
    "drug susceptibility": "how well antimalarial drugs killed the parasite in the laboratory",
    "blood counts": "anaemia and blood counts",
    "severe illness": "severe illness, death and birth weight",
    "other": "other malaria outcomes",
}

# Glossary: pattern -> (short label, plain-English gloss). Order matters; first match wins.
GLOSSARY = [
    (r"\bpfkelch13\b|\bpfk13\b|\bkelch\s*-?13\b|\bk13\b", "Pfkelch13",
     "the malaria parasite gene whose mutations cause partial resistance to artemisinin, the "
     "backbone of modern malaria treatment"),
    (r"\bpfcrt\b", "PfCRT",
     "the malaria parasite's chloroquine-resistance transporter gene"),
    (r"\bpfmdr\s*-?1\b|\bpfmdr\b|\bmdr\s*-?1\b", "Pfmdr1",
     "the malaria parasite's multidrug-resistance gene, which affects how well several "
     "antimalarial drugs work"),
    (r"\bpf?dhfr\b|dihydrofolate reductase", "DHFR",
     "dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks"),
    (r"\bpf?dhps\b|dihydropteroate synthase", "DHPS",
     "dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks"),
    (r"\bplasmepsin\b", "plasmepsin",
     "a parasite enzyme whose extra gene copies are linked to piperaquine resistance"),
    (r"\bcg2\b", "cg2", "a parasite gene once used as a chloroquine-resistance marker"),
    (r"\bACPR\b", "ACPR",
     "adequate clinical and parasitological response, meaning the infection cleared and did not "
     "come back during follow-up"),
    (r"\bIC50\b", "IC50",
     "the drug concentration needed to halve parasite growth in the laboratory; a higher value "
     "means the parasite is less sensitive to the drug"),
    (r"\bEC50\b", "EC50", "the drug concentration producing half the maximum effect"),
    (r"\bIC90\b", "IC90", "the drug concentration needed to cut parasite growth by 90%"),
    (r"\bAL\b|artemether[- ]lumefantrine", "artemether-lumefantrine",
     "a widely used artemisinin combination treatment, sold as Coartem"),
    (r"\bSP\b|sulfadoxine[- ]pyrimethamine|sulphadoxine[- ]pyrimethamine", "sulfadoxine-pyrimethamine",
     "an older antimalarial drug pair, still used to protect pregnant women and young children"),
    (r"\bACTs?\b|artemisinin[- ]based combination", "artemisinin-based combination therapy",
     "the standard first-line malaria treatment, pairing artemisinin with a longer-acting partner drug"),
    (r"dihydroartemisinin[- ]piperaquine|\bDHA[- ]PPQ\b|\bDP\b", "dihydroartemisinin-piperaquine",
     "an artemisinin combination treatment"),
    (r"artesunate[- ]amodiaquine|\bASAQ\b", "artesunate-amodiaquine",
     "an artemisinin combination treatment"),
    (r"\bIPTp\b", "IPTp",
     "intermittent preventive treatment in pregnancy, where pregnant women are given antimalarial "
     "drugs at routine visits whether or not they are infected"),
    (r"\bIPTi\b", "IPTi", "intermittent preventive treatment in infants"),
    (r"\bSMC\b|seasonal malaria chemoprevention", "seasonal malaria chemoprevention",
     "monthly antimalarial drug courses given to young children through the rainy season"),
    (r"\bHRP2\b", "HRP2",
     "histidine-rich protein 2, the parasite protein most rapid malaria tests look for"),
    (r"\bRDTs?\b", "rapid diagnostic test",
     "a finger-prick test that detects malaria proteins without a microscope"),
    (r"\bPCR\b", "PCR", "a DNA test used to detect and genotype the parasite"),
    (r"parasitaemia|parasitemia", "parasitaemia",
     "the density of malaria parasites in the blood"),
    (r"gametocyt\w*", "gametocytes",
     "the parasite life stage that mosquitoes pick up, which spreads malaria onward"),
    (r"recrudescen\w*", "recrudescence",
     "the original infection returning after treatment, as opposed to a fresh mosquito bite"),
    (r"\bex vivo\b", "ex vivo", "tested on fresh parasites taken straight from patients"),
    (r"\bin vitro\b", "in vitro", "tested on parasites grown in the laboratory"),
    (r"\bCQ\b", "chloroquine", "a cheap older antimalarial, now largely defeated by resistance"),
]
GLOSSARY = [(re.compile(p, re.I), label, gloss) for p, label, gloss in GLOSSARY]

MUTATION = re.compile(r"\b([A-Z])(\d{2,4})([A-Z])\b")  # e.g. N86Y, K540E, C580Y

# Statistics whose null value is 1 rather than 0. Everything else pivots at 0.
RATIO_STATS = {"odds_ratio", "adjusted_odds_ratio", "relative_risk_ratio", "hazard_ratio",
               "prevalence_ratio", "incident_rate_ratio", "incidence_rate_ratio"}

# An outcome-shaped phrase on the second side means the record names an exposure and an
# outcome, so a directional sentence is safe. Two bare measurement names do not.
OUTCOME_SHAPED = re.compile(
    r"\brisk of\b|\bodds of\b|\brate of\b|\bincidence\b|\btime to\b|\bfailure\b|"
    r"\bclearance\b|\bsurviv|\brecrudescen|\bmortality\b|\bdeath\b|\bresponse\b|"
    r"\befficacy\b|\bcure\b|\bhospitali", re.I)

COMPARATOR = re.compile(r"\[vs\.?\s*(.+?)\]\s*$|\(compared with\s*(.+?)\)\s*$", re.I)


def deaccent(text):
    """Diakite, not Diakit: strip accents by decomposition rather than deleting the letter."""
    return "".join(c for c in unicodedata.normalize("NFKD", str(text))
                   if not unicodedata.combining(c))


def direction_of(a):
    """positive / negative / null / unknown, judged against the statistic's null value."""
    v = a.get("statistic_value")
    if v is None:
        return "unknown"
    null = 1.0 if (a.get("system_statistic_type") or "") in RATIO_STATS else 0.0
    if abs(v - null) < 1e-9:
        return "null"
    return "positive" if v > null else "negative"


def split_comparator(name):
    """('Dangassa', 'Nioro-du-Sahel') from 'Dangassa [vs Nioro-du-Sahel]'."""
    m = COMPARATOR.search(str(name or ""))
    if not m:
        return str(name or ""), None
    other = m.group(1) or m.group(2)
    return COMPARATOR.sub("", str(name)).strip(" ,;"), (other or "").strip(" )")

STAT_PHRASE = {
    "odds_ratio": ("Odds ratio of {v}", "An odds ratio compares how often two things occur "
                   "together; 1 means no association, and further from 1 means a stronger one."),
    "adjusted_odds_ratio": ("Adjusted odds ratio of {v}", "An odds ratio adjusted for other "
                            "factors the study measured; 1 means no association."),
    "relative_risk_ratio": ("Relative risk of {v}", "A risk ratio compares the chance of an "
                            "outcome between two groups; 1 means no difference."),
    "hazard_ratio": ("Hazard ratio of {v}", "A hazard ratio compares how quickly an event happens "
                     "between two groups; 1 means no difference."),
    "prevalence_ratio": ("Prevalence ratio of {v}", "Compares how common something is between two "
                         "groups; 1 means equally common."),
    "incident_rate_ratio": ("Incidence rate ratio of {v}", "Compares how often new cases arise "
                            "between two groups; 1 means no difference."),
    "mean_difference_unstandardized": ("Difference of {v}", "The gap between two group averages, "
                                       "in whatever units the study measured."),
    "pearson_r": ("Correlation of {v}", "A correlation runs from -1 to 1; 0 means no linear "
                  "relationship and values near 1 or -1 mean a strong one."),
    "coefficient": ("Regression coefficient of {v}", "How much the outcome changes per unit "
                    "change in the other variable; 0 means no relationship."),
}

# ------------------------------------------------------------------------ helpers

SAFE = re.compile(r'[<>:"/\\|?*\n\r\t\[\]#^]+')


def tidy(name):
    """Clean an extractor variable name into something readable."""
    s = str(name or "").strip()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("[vs ", "(compared with ").replace("[vs.", "(compared with")
    s = s.replace("]", ")") if s.count("(") > s.count(")") else s
    return s


def glossary_hits(*texts):
    """Which glossary entries and mutation codes appear in these strings."""
    blob = " ".join(str(t or "") for t in texts)
    hits = []
    for pat, label, gloss in GLOSSARY:
        if pat.search(blob) and label not in [h[0] for h in hits]:
            hits.append((label, gloss))
    muts = []
    for m in MUTATION.finditer(blob):
        code = m.group(0)
        if code not in muts:
            muts.append(code)
            hits.append((code, f"a mutation that swaps amino acid {m.group(1)} for {m.group(3)} "
                               f"at position {m.group(2)} of the protein"))
    return hits


def expand_first(text, limit=1):
    """Expand up to `limit` acronyms inline, so the title stays readable."""
    out, used = str(text), 0
    for pat, label, _ in GLOSSARY:
        if used >= limit:
            break
        m = pat.search(out)
        if not m:
            continue
        found = m.group(0)
        norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
        if norm(found) == norm(label) or norm(label) in norm(found):
            continue
        out = out[:m.start()] + f"{found} ({label})" + out[m.end():]
        used += 1
    return out


def slug(text, limit=110):
    """Clean for a filename or title, truncating on a word boundary rather than mid-word."""
    text = SAFE.sub(" ", str(text)).strip()
    text = re.sub(r"\s+", " ", text)
    if len(text) <= limit:
        return text.rstrip(" .,;:-")
    cut = text[:limit]
    if " " in cut:
        cut = cut[:cut.rfind(" ")]
    # An unclosed bracket reads as a mistake, so drop back to before it opened.
    if cut.count("(") > cut.count(")"):
        cut = cut[:cut.rfind("(")]
    return cut.rstrip(" .,;:-")


def fm(**kw):
    order = ["NodeFormality", "human_reviewed", "TruthValue", "aliases", "tags",
             "created", "updated", "nodeID", "title"]
    out = ["---"]
    for k in order:
        if k not in kw:
            continue
        v = kw[k]
        if isinstance(v, list):
            out.append(f"{k}:")
            out.extend(f"  - {json.dumps(x)}" if isinstance(x, str) else f"  - {x}" for x in v)
        elif isinstance(v, str) and (":" in v or '"' in v or v.startswith(("-", "[", "{"))):
            out.append(f"{k}: {json.dumps(v)}")
        else:
            out.append(f"{k}: {v}")
    out.append("---")
    return "\n".join(out)


def nid():
    return str(uuid.uuid4())


def write(folder, name, body):
    d = VAULT / folder if folder else VAULT
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{name}.md").write_text(body.rstrip() + "\n", encoding="utf-8")


def year_of(pmid):
    rec = PUBMED.get(pmid) or AUTHORS.get(pmid) or {}
    m = re.match(r"(\d{4})", rec.get("pub_date") or "")
    return int(m.group(1)) if m else None


def fmt_val(v):
    if v is None:
        return "an unreported value"
    if isinstance(v, float) and v == int(v):
        return str(int(v))
    return f"{v:.3g}" if isinstance(v, (int, float)) else str(v)


def context(a):
    st = STUDIES.get(a.get("study_id")) or {}
    pm = PUBMED.get(a.get("pubmed_id")) or {}
    return " ".join(str(p) for p in [a.get("variable_1_name"), a.get("variable_2_name"),
                                     st.get("population"), pm.get("title"),
                                     st.get("study_type")] if p)


# ------------------------------------------------------------------- select rows

rows = []
for a in A:
    ctx = context(a)
    if EXCLUDE.search(ctx) or not MALARIA.search(ctx):
        continue
    names = f"{a.get('variable_1_name') or ''} {a.get('variable_2_name') or ''}"
    marks = [m for m, p in MARKERS.items() if p.search(names)]
    if not marks:
        continue
    themes = [t for t, p in THEME_PATTERNS.items() if p.search(names)]
    rows.append({"a": a, "markers": marks, "themes": themes or ["other"],
                 "year": year_of(a.get("pubmed_id")), "ctx": ctx})

# The graph sometimes stores the identical finding twice, including both variable orderings.
# Collapse only exact repeats; the same pair reported with a different statistic is a real
# second finding and is kept.
_seen, _deduped, _dropped = {}, [], 0
for r in rows:
    a = r["a"]
    key = (tuple(sorted([a.get("variable_1_id") or "", a.get("variable_2_id") or ""])),
           a.get("study_id"), a.get("statistic_type"), str(a.get("statistic_value")))
    if key in _seen:
        _dropped += 1
        continue
    _seen[key] = a["system_id"]
    _deduped.append(r)
rows = _deduped

# Findings the API sweep never saw, recovered from the curated release. The deposit is far
# narrower than the API (25 marker findings against 1,184), so this adds little — but it is a
# genuine second source and the pipeline should use both.
_have = {r["a"]["system_id"] for r in rows}
_added = 0
for _sid, _dr in DEPOSIT_ROWS.items():
    if _sid in _have:
        continue
    _a = {"system_id": _sid,
          "variable_1_id": _dr.get("variable_1_id"), "variable_2_id": _dr.get("variable_2_id"),
          "variable_1_name": _dr.get("variable_1_name"), "variable_2_name": _dr.get("variable_2_name"),
          "study_id": _dr.get("study_id"),
          "pubmed_id": int(_dr["pubmed_id"]) if (_dr.get("pubmed_id") or "").strip().isdigit() else None,
          "statistic_type": _dr.get("statistic_type"),
          "system_statistic_type": _dr.get("system_statistic_type"),
          "statistic_value": _num(_dr.get("statistic_value")),
          "p_value": _num(_dr.get("p_value")), "p_value_equality": _dr.get("p_value_equality"),
          "ci_level": _num(_dr.get("ci_level")), "ci_lower": _num(_dr.get("ci_lower")),
          "ci_upper": _num(_dr.get("ci_upper")), "via_variables": []}
    _names = f"{_a['variable_1_name'] or ''} {_a['variable_2_name'] or ''}"
    _marks = [m for m, pat in MARKERS.items() if pat.search(_names)]
    if not _marks:
        continue
    _themes = [t for t, pat in THEME_PATTERNS.items() if pat.search(_names)] or ["other"]
    rows.append({"a": _a, "markers": _marks, "themes": _themes,
                 "year": year_of(_a["pubmed_id"]), "ctx": _names, "deposit_only": True})
    _added += 1

# Attach the enriched statistics and the provenance list to every row
for _r in rows:
    _r["a"], _r["provenance"] = enrich(_r["a"])
    if _r.get("deposit_only"):
        _r["provenance"] = ["Dataverse release"]

print(f"collapsed {_dropped} exact duplicate findings")
print(f"merged {_added} finding(s) present only in the curated Dataverse release")
_with_p = sum(1 for r in rows if r["a"].get("p_value") is not None)
_with_ci = sum(1 for r in rows if r["a"].get("ci_lower") is not None)
print(f"statistics available: p-value {_with_p}/{len(rows)} "
      f"({_with_p/max(len(rows),1):.0%}), interval {_with_ci}/{len(rows)} "
      f"({_with_ci/max(len(rows),1):.0%})")
print(f"{len(rows)} evidence rows across {len({r['a']['study_id'] for r in rows})} studies")

# ----------------------------------------------------------------- citekeys

# @surnameYEAR, with a/b/c suffixes when one author has several papers in a year
pmid_to_key, seen = {}, collections.defaultdict(list)
for r in sorted(rows, key=lambda x: x["a"].get("pubmed_id") or 0):
    pmid = r["a"].get("pubmed_id")
    if not pmid or pmid in pmid_to_key:
        continue
    au = AUTHORS.get(pmid) or {}
    surname = au.get("surname") or "unknown"
    yr = r["year"] or "nd"
    base = f"{surname}{yr}"
    seen[base].append(pmid)
    pmid_to_key[pmid] = base

for base, pmids in seen.items():
    if len(pmids) > 1:
        for i, pmid in enumerate(sorted(pmids)):
            pmid_to_key[pmid] = f"{base}{chr(ord('a') + i)}"


# Export the authoritative map so other scripts (build_eval.py) use the same keys, including
# the a/b/c suffixes applied when one author has several papers in a year.
(CACHE / "citekeys.json").write_text(json.dumps(
    {str(k): "@" + v for k, v in pmid_to_key.items()}, indent=1))


def citekey(a):
    pmid = a.get("pubmed_id")
    return "@" + (pmid_to_key.get(pmid) or f"study{a.get('study_id')}")


def author_tag(a):
    """'Mwai 2009' style attribution for titles."""
    pmid = a.get("pubmed_id")
    au = AUTHORS.get(pmid) or {}
    sn = deaccent(au.get("surname") or "").capitalize() or "Unknown"
    many = (au.get("author_count") or 0) > 1
    yr = year_of(pmid) or "n.d."
    return f"{sn}{' et al.' if many else ''} {yr}"


# -------------------------------------------------------------------- EVD nodes

evd_index = {}
for r in rows:
    a = r["a"]
    v1_raw, v2_raw = tidy(a.get("variable_1_name")), tidy(a.get("variable_2_name"))
    v1_base, comparator = split_comparator(v1_raw)
    stype = a.get("system_statistic_type") or a.get("statistic_type") or "statistic"
    val = fmt_val(a.get("statistic_value"))
    dirn = direction_of(a)
    is_ratio = stype in RATIO_STATS
    # Direction is only asserted when the record clearly names an exposure and an outcome.
    directional = bool(OUTCOME_SHAPED.search(v2_raw)) and not OUTCOME_SHAPED.search(v1_base)

    v1s, v2s = slug(v1_base, 68), slug(v2_raw, 68)
    comp_s = slug(comparator, 42) if comparator else None

    if directional and is_ratio:
        sentence = (f"{v1s} carried {val} times the {v2s}" if dirn == "positive"
                    else f"{v1s} carried {val} times the {v2s}, a reduction")
    elif comparator:
        sentence = f"{v2s} differed by {val} between {v1s} and {comp_s}"
    elif directional:
        mag = str(val).lstrip("-")
        word = "a decrease of" if dirn == "negative" else "an increase of"
        sentence = f"{v1s} was associated with {word} {mag} in {v2s}"
    else:
        label = stype.replace("_", " ")
        art = "an" if label[0] in "aeiou" else "a"
        sentence = f"{v1s} and {v2s} showed {art} {label} of {val}"
    # Always name the metric and show the estimate, even when the sentence reads directionally.
    metric = stype.replace("_", " ")
    if metric.lower() not in sentence.lower():
        # Don't repeat the estimate if the sentence already states it.
        sentence = (f"{sentence} ({metric})" if str(val) in sentence
                    else f"{sentence} ({metric} = {val})")
    sentence = expand_first(sentence, limit=2)

    key = citekey(a)
    title = f"{sentence} - {key}"
    fname = f"EVD - {slug(sentence, 104)} - {key}"
    if fname in {v[0] for v in evd_index.values()}:
        fname = f"EVD - {slug(sentence, 96)} {a['system_id'][:5]} - {key}"

    st = STUDIES.get(a.get("study_id")) or {}
    pm = PUBMED.get(a.get("pubmed_id")) or {}
    yr = r["year"]
    verified = a["system_id"] in DEPOSIT_IDS
    integ = integrity_of(a, st)
    terms = glossary_hits(v1_raw, v2_raw)
    have = {t[0].lower() for t in terms}
    for m in r["markers"]:
        g = next((gl for pat, lab, gl in GLOSSARY if pat.search(m)), None)
        if g and m.lower() not in have:
            terms.insert(0, (m, g))
            have.add(m.lower())

    tags = [f"marker/{m.lower().replace(' ', '-')}" for m in r["markers"]] + \
           [f"theme/{t.replace(' ', '-')}" for t in r["themes"]] + \
           [f"stat/{stype}", f"direction/{dirn}",
            "verification/in-curated-deposit" if verified else "verification/api-only"]
    if yr:
        tags.append(f"year/{yr}")

    pval = (f", p {a.get('p_value_equality') or '='} {fmt_val(a.get('p_value'))}"
            if a.get("p_value") is not None else "")
    ci = (f" The {fmt_val(a.get('ci_level')) + '% ' if a.get('ci_level') else ''}confidence "
          f"interval runs from {fmt_val(a.get('ci_lower'))} to {fmt_val(a.get('ci_upper'))}."
          if a.get("ci_lower") is not None else "")

    # --- PICOST, filled only where the record actually supports it
    setting = None
    if st.get("population"):
        m = re.search(r"\b(?:in|from|on the)\s+([A-Z][A-Za-z\-\u2013 ]{2,60}?)"
                      r"(?:[.,;]|\s+(?:with|and|aged|who))", st["population"])
        if m:
            setting = m.group(1).strip()
    picost = [
        ("Population", st.get("population") or "Not recorded in the graph."),
        ("Intervention / exposure",
         "Not separable — see the direction warning below." if not directional and not comparator
         else v1_base),
        ("Comparator", comparator or ("Implied but not named in the record." if directional
                                      else "Not recorded.")),
        ("Outcome", "Not separable — see the direction warning below."
         if not directional and not comparator else v2_raw),
        ("Setting", setting or ("Not stated separately — see Population above."
                                if st.get("population") else "Not recorded in the graph.")),
        ("Timeframe", (f"{st.get('study_type')}, published {yr}." if st.get("study_type") and yr
                       else f"Published {yr}." if yr else "Publication year unresolved.")
         + " Fieldwork dates are not recorded in the graph."),
    ]

    prov = r.get("provenance") or ["API list"]
    stats_rows = [
        ("Metric", f"`{stype}` (System's normalised type; the paper reported "
                   f"`{a.get('statistic_type')}`)"),
        ("Estimate", f"**{val}**"),
        ("p-value", (f"{a.get('p_value_equality') or '='} {fmt_val(a.get('p_value'))}"
                     if a.get("p_value") is not None else "Not recorded")),
        ("Confidence interval",
         ((f"{fmt_val(a.get('ci_level'))}% CI " if a.get("ci_level") else "CI ")
          + f"{fmt_val(a.get('ci_lower'))} to {fmt_val(a.get('ci_upper'))}"
          + ("" if a.get("ci_level") else " (confidence level not recorded)")
          if a.get("ci_lower") is not None else "Not recorded")),
        ("Direction vs null of " + ("1" if is_ratio else "0"), f"**{dirn}**"),
        ("Data source", ", ".join(prov)),
        ("In curated release", "Yes" if verified else "No"),
        ("Source paper integrity",
         (", ".join(FLAG_LABEL.get(f, f) for f in integ["flags"])
          if integ.get("flags") else
          "No retraction, erratum or expression of concern found")
         + " (checked against PubMed and Crossref)"),
    ]
    screen_rows, _, _rr_rec, _op_rec = screening_rows(a, st)

    body = [
        fm(NodeFormality="draft", human_reviewed="no", aliases=[f"EVD - {title}"], tags=tags,
           created=TODAY, updated=TODAY, nodeID=nid(), title=title),
        "", "## Source", "", f"[[{key}]]", "",
        "## In plain terms", "",
        "> [!info] What this finding says",
        f"> A study published in {yr or 'an unrecorded year'} reported a statistical link between "
        f"**{expand_first(v1_base)}** and **{expand_first(v2_raw)}**.",
        f"> {sentence[0].upper() + sentence[1:]}{pval}.{ci}",
        "",
        "## Statistic", "",
        "| | |", "|---|---|",
    ]
    body += [f"| **{k}** | {str(v).replace('|', '/')} |" for k, v in stats_rows]
    body += ["", "## Source paper screening", "",
             "> [!info] Checked on " + TODAY + " against PubMed, Crossref, "
             "retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.",
             "", "| | |", "|---|---|"]
    body += [f"| **{k}** | {str(v).replace('|', '/')} |" for k, v in screen_rows]
    body += ["", "## PICOST", "", "| | |", "|---|---|"]
    body += [f"| **{k}** | {str(v).replace('|', '/')} |" for k, v in picost]
    body += [""]

    if not directional and not comparator:
        body += [
            "> [!warning] Which is cause and which is effect cannot be determined",
            f"> The record pairs `{a.get('variable_1_name')}` with "
            f"`{a.get('variable_2_name')}` and reports a "
            f"{stype.replace('_', ' ')} of {val}. Nothing in the data says which was treated as "
            "the exposure, so this note does not claim that one caused the other. See "
            "[[CVT - The graph records no effect direction]].", ""]

    _f = set(integ.get("flags") or [])
    if _f & SERIOUS_FLAGS:
        body += [
            "> [!danger] The source paper has been retracted or carries an expression of concern",
            "> " + "; ".join(integ.get("notes") or []),
            "> Do not use this finding without reading the notice first.", ""]
    elif "corrected" in _f:
        body += [
            "> [!warning] The source paper has a published erratum",
            "> " + "; ".join(n for n in integ.get("notes") or [] if "Erratum" in n
                             or "erratum" in n or "correction" in n),
            "> System extracted this statistic from the original article, and the graph records "
            "nothing about corrections. The number above may be one the erratum changed. Check "
            "the correction notice before citing it.", ""]

    _dc = (_op_rec or {}).get("data_class")
    if _dc in ("on request", "no statement found"):
        body += [
            "> [!warning] This finding is unlikely to be independently reproducible",
            "> " + ("The source paper offers its data only on request from the authors."
                    if _dc == "on request" else
                    "No data-availability statement was found in the paper's full text.")
            + " Nobody can re-derive this statistic from public material, so it rests entirely "
              "on System's extraction being correct and on the paper's own analysis.", ""]

    if not is_ratio and stype != "pearson_r":
        body += [
            "> [!warning] Units not recorded",
            "> The graph gives no units for this value. For a prevalence or proportion it is "
            "most likely percentage points, but that is inference rather than data.", ""]

    # Does the gene named in the record also appear in the paper's title?
    pt = (pm.get("title") or "")
    named = [m for m in r["markers"] if m != "Other markers" and MARKERS[m].search(pt)]
    other_genes = [g for g in ("pfmdr1", "pfcrt", "pfdhfr", "pfdhps", "kelch")
                   if re.search(g, pt, re.I)
                   and not any(re.search(g, m, re.I) for m in r["markers"])]
    if pt and not named and other_genes:
        body += [
            "> [!warning] Possible extraction mismatch",
            f"> This record names **{', '.join(r['markers'])}**, but the source paper's title "
            f"mentions {', '.join(other_genes)} instead. The paper may well cover both, but "
            "check it against the article before citing.", ""]

    if terms:
        body += ["## Terms explained", ""]
        body += [f"- **{label}** — {gloss}" for label, gloss in terms]
        body += [""]

    body += [
        "## Description", "",
        "> [!info] The finding exactly as System extracted it",
        f"> Variable 1: `{a.get('variable_1_name')}`",
        f"> Variable 2: `{a.get('variable_2_name')}`",
        f"> {stype.replace('_', ' ')} = {val}"
        + (f", p {a.get('p_value_equality') or '='} {fmt_val(a.get('p_value'))}"
           if a.get("p_value") is not None else ""),
        ((f"> {fmt_val(a.get('ci_level'))}% CI " if a.get("ci_level") else "> CI ")
         + f"[{fmt_val(a.get('ci_lower'))}, {fmt_val(a.get('ci_upper'))}]"
         if a.get("ci_lower") is not None else
         "> Confidence interval not available from the list endpoint — see "
         "[[CVT - List endpoints omit p-values and confidence intervals]]"),
        f"> Direction against the statistic's null value of "
        f"{'1' if is_ratio else '0'}: **{dirn}**",
        "",
        "## Methods Context", "",
        "### What?", "",
        f"The study related **{expand_first(v1_base)}** to **{expand_first(v2_raw)}**, reported "
        f"as a {stype.replace('_', ' ')}.", "",
        "### How?", "",
        (f"Study design: {st.get('study_type')}." if st.get("study_type")
         else "The graph records no study design for this paper. To judge how the finding was "
              "produced you have to read the source article."), "",
        "### Who?", "",
        (f"> {st.get('population')}" if st.get("population")
         else "> The graph holds no description of who was studied."), "",
        "## Provenance", "",
        f"- Source study: [[{key}]]",
        f"- Paper: {pm.get('title') or 'title not retrieved'}",
        f"- Journal: {pm.get('journal') or 'not retrieved'}",
        f"- Published: {pm.get('pub_date') or 'not retrieved'}",
        (f"- PubMed: [{a.get('pubmed_id')}](https://pubmed.ncbi.nlm.nih.gov/{a.get('pubmed_id')}/)"
         if a.get("pubmed_id") else "- PubMed: not available"),
        f"- System association ID: `{a['system_id']}`",
        f"- Resistance gene(s): {', '.join(r['markers'])}",
        f"- Outcome theme(s): {', '.join(THEME_PLAIN.get(t, t) for t in r['themes'])}",
        "",
        "## Verification", "",
        ("> [!success] Checked against the curated dataset\n"
         "> This finding also appears in System's curated Harvard Dataverse release, from which "
         "the extractions System had flagged as inaccurate were removed. That is the best "
         "available sign that the number was read correctly from the paper."
         if verified else
         "> [!warning] Not in the curated dataset — treat as unverified\n"
         "> This finding is in the live API but not in System's curated Harvard Dataverse "
         "release. System's documentation says to discard such records, but that release is also "
         "much smaller in scope (2.0 million findings against the API's 5.9 million), so absence "
         "is a reason to check the source paper rather than proof the number is wrong. See "
         "[[CVT - The curated Dataverse deposit holds almost no resistance evidence]]."),
        "",
        "## Other Notes", "",
        "> [!info] Extraction reliability",
        "> System documents an approximate 20% error rate when its pipeline reads statistics out "
        "of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].",
    ]
    write("evidence", fname, "\n".join(body))
    evd_index[a["system_id"]] = (fname, title)

print(f"wrote {len(evd_index)} EVD nodes")

# ----------------------------------------------------------------- source nodes

by_study = collections.defaultdict(list)
for r in rows:
    by_study[r["a"]["study_id"]].append(r)

for sid, group in by_study.items():
    st = STUDIES.get(sid) or {}
    a0 = group[0]["a"]
    pmid = a0.get("pubmed_id")
    pm = PUBMED.get(pmid) or {}
    au = AUTHORS.get(pmid) or {}
    key = citekey(a0)
    yr = group[0]["year"]
    title = pm.get("title") or f"Study {sid}"
    markers = sorted({m for r in group for m in r["markers"]})
    _sinteg = integrity_of(a0, st)

    body = [
        fm(aliases=[slug(title, 170)],
           tags=[f"marker/{m.lower().replace(' ', '-')}" for m in markers]
                + ([f"year/{yr}"] if yr else [])
                + [f"integrity/{f}" for f in (_sinteg.get("flags") or ["clean"])],
           created=TODAY, updated=TODAY, nodeID=nid(), title=slug(title, 170)),
        "", "> [!info] Citation data only",
        "> This vault stores bibliographic details, not article text. Follow the DOI or PubMed "
        "link to read the paper.", "",
        "## Citation", "", f"**{title}**", "",
        f"- First author: {au.get('first_author') or 'not retrieved'}"
        + (f" (and {au['author_count'] - 1} co-author(s))"
           if (au.get("author_count") or 0) > 1 else ""),
        f"- Last author: {au.get('last_author') or 'not retrieved'}",
        f"- Journal: {pm.get('journal') or 'not retrieved'}",
        f"- Published: {pm.get('pub_date') or 'not retrieved'}"
        + (f" (online {pm['epub_date']})" if pm.get("epub_date") else ""),
        (f"- DOI: [{st['doi']}](https://doi.org/{st['doi']})" if st.get("doi")
         else "- DOI: none recorded"),
        (f"- PubMed: [{pmid}](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)" if pmid
         else "- PubMed: none recorded"),
        f"- System study ID: `{sid}`",
        f"- Study design: {st.get('study_type') or 'not recorded in the graph'}", "",
        "## Source paper screening", "",
        "> [!info] Checked on " + TODAY + " against PubMed, Crossref, retractionrisk.com "
        "(Retraction Watch + Altmetric), OpenAlex and PMC full text.",
        "", "| | |", "|---|---|",
    ] + [f"| **{k}** | {str(v).replace('|', '/')} |"
         for k, v in screening_rows(a0, st)[0]] + [
        "",
        "## Integrity check", "",
        (("> [!danger] " + ", ".join(FLAG_LABEL.get(f, f) for f in _sinteg["flags"]) + "\n"
          + "\n".join(f"> - {n}" for n in _sinteg.get("notes") or []))
         if set(_sinteg.get("flags") or []) & SERIOUS_FLAGS else
         ("> [!warning] " + ", ".join(FLAG_LABEL.get(f, f) for f in _sinteg["flags"]) + "\n"
          + "\n".join(f"> - {n}" for n in _sinteg.get("notes") or []))
         if _sinteg.get("flags") else
         "> [!success] No retraction, erratum or expression of concern found\n"
         "> Checked against PubMed's CommentsCorrections records and Crossref's update "
         "metadata."),
        "",
        ("> [!success] No PubPeer comments\n"
         "> Checked against the official PubPeer Foundation API by both DOI and PubMed ID. "
         "PubPeer returns a record only for publications that have activity, so this is a "
         "negative result rather than a failed lookup."
         if not pubpeer_of(a0, st).get("on_pubpeer") else
         "> [!warning] This paper has PubPeer comments\n"
         f"> {pubpeer_of(a0, st).get('total_comments')} comment(s). "
         f"{pubpeer_of(a0, st).get('pubpeer_url')}"),
        "",
        "> [!info] What this screen cannot cover",
        "> Informal critique outside PubMed, Crossref, Retraction Watch and PubPeer — journal "
        "clubs, conference discussion, private correspondence — leaves no machine-readable "
        f"trace. See [[CVT - What the post-publication screen covers and what it cannot]].",
        "",
        "## Who was studied", "",
        (f"> {st.get('population')}" if st.get("population")
         else "> The graph holds no description of who was studied."), "",
        "## Findings drawn from this paper", "",
        f"{len(group)} statistical finding(s), covering {', '.join(markers)}.", "",
    ]
    for r in sorted(group, key=lambda x: x["a"]["system_id"]):
        fn, t = evd_index[r["a"]["system_id"]]
        body.append(f"- [[{fn}|{t}]]")
    write("source", key, "\n".join(body))

print(f"wrote {len(by_study)} source nodes named @surnameYEAR")

# -------------------------------------------------------------------- CLM nodes

# A claim is an assertion someone could disagree with, following the living-evidence-synthesis
# house style. The direction comes from the majority of the underlying findings, measured
# against each statistic's null value, and the consistency is always stated rather than hidden.

CLAIM_TEMPLATES = {
    ("treatment failure", "positive"):
        "Mutations in {gene} are associated with higher rates of antimalarial treatment failure",
    ("treatment failure", "negative"):
        "Mutations in {gene} are associated with lower rates of antimalarial treatment failure",
    ("parasite clearance", "positive"):
        "Mutations in {gene} are associated with slower clearance of malaria parasites after "
        "treatment",
    ("parasite clearance", "negative"):
        "Mutations in {gene} are associated with faster clearance of malaria parasites after "
        "treatment",
    ("drug susceptibility", "positive"):
        "Mutations in {gene} are associated with reduced parasite sensitivity to antimalarial "
        "drugs in laboratory testing",
    ("drug susceptibility", "negative"):
        "Mutations in {gene} are associated with greater parasite sensitivity to antimalarial "
        "drugs in laboratory testing",
    ("marker prevalence", "positive"):
        "Resistance-mutation prevalence in {gene} rises with drug pressure and over time across "
        "the settings studied",
    ("marker prevalence", "negative"):
        "Resistance-mutation prevalence in {gene} falls once the drug that selected for it is "
        "withdrawn",
    ("severe illness", "positive"):
        "Mutations in {gene} are associated with worse clinical outcomes, including severe "
        "malaria, death and low birth weight",
    ("severe illness", "negative"):
        "Mutations in {gene} are not associated with worse clinical outcomes such as severe "
        "malaria, death or low birth weight",
    ("blood counts", "positive"):
        "Mutations in {gene} are associated with lower haemoglobin and more anaemia",
    ("blood counts", "negative"):
        "Mutations in {gene} are not associated with lower haemoglobin or more anaemia",
    ("other", "positive"):
        "Mutations in {gene} are positively associated with a range of other malaria measures",
    ("other", "negative"):
        "Mutations in {gene} are inversely associated with a range of other malaria measures",
}

groups = collections.defaultdict(list)
for r in rows:
    for m in r["markers"]:
        for t in r["themes"]:
            groups[(m, t)].append(r)

clm_index = {}
for (marker, theme), group in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    if len(group) < 2:
        continue
    years = sorted(x["year"] for x in group if x["year"])
    span = f"{years[0]} to {years[-1]}" if years else "years unrecorded"
    nstud = len({x["a"]["study_id"] for x in group})
    plain = THEME_PLAIN.get(theme, theme)
    gene_name = ("a group of less-studied resistance markers" if marker == "Other markers"
                 else marker)

    dirs = collections.Counter(direction_of(x["a"]) for x in group)
    pos, neg = dirs["positive"], dirs["negative"]
    decided = pos + neg
    majority = "positive" if pos >= neg else "negative"
    agree = (max(pos, neg) / decided) if decided else 0.0

    base = CLAIM_TEMPLATES.get((theme, majority))
    if not base:
        base = ("Mutations in {gene} are statistically related to " + plain)
    stem = base.format(gene=gene_name)

    if agree >= 0.9:
        qualifier, strength = ", consistently across studies", "consistent"
    elif agree >= 0.7:
        qualifier, strength = ", though a minority of findings disagree", "mostly consistent"
    else:
        qualifier, strength = " — but the published evidence is contested", "contested"
    title = stem + qualifier
    truth = round(agree, 2) if decided else 0.5

    fname = f"CLM - {slug(title, 112)}"
    if fname in {v[0] for v in clm_index.values()}:
        fname = f"CLM - {slug(title, 100)} ({marker})"
    stat_mix = collections.Counter(x["a"].get("system_statistic_type") for x in group)
    gloss = next((g for pat, lab, g in GLOSSARY if pat.search(marker)), None)
    n_f = f"{len(group)} finding" + ("s" if len(group) != 1 else "")
    n_s = f"{nstud} stud" + ("ies" if nstud != 1 else "y")

    _n_dep = sum(1 for x in group if x["a"]["system_id"] in DEPOSIT_IDS)
    _n_p = sum(1 for x in group if x["a"].get("p_value") is not None)
    _n_ci = sum(1 for x in group if x["a"].get("ci_lower") is not None)
    _ints = [integrity_of(x["a"], STUDIES.get(x["a"].get("study_id"))) for x in group]
    _n_serious = sum(1 for i in _ints if set(i.get("flags") or []) & SERIOUS_FLAGS)
    _n_errata = sum(1 for i in _ints if "corrected" in (i.get("flags") or []))
    _n_comment = sum(1 for i in _ints if "commented-on" in (i.get("flags") or []))
    _ops = [open_of(x["a"], STUDIES.get(x["a"].get("study_id"))) for x in group]
    _rrs = [rr_of(STUDIES.get(x["a"].get("study_id"))) for x in group]
    _n_oa = sum(1 for o in _ops if o.get("oa"))
    _n_data = sum(1 for o in _ops if o.get("data_class") == "deposited")
    _n_code = sum(1 for o in _ops if o.get("code_repos"))
    _n_xneg = sum(1 for x in _rrs if (x.get("x_negative") or 0) > 0)
    _pps = [pubpeer_of(x["a"], STUDIES.get(x["a"].get("study_id"))) for x in group]
    _n_pp = sum(1 for x in _pps if x.get("on_pubpeer"))
    _srcs = collections.Counter(s for x in group for s in (x.get("provenance") or []))
    _src_txt = ", ".join(f"{k} ({v})" for k, v in _srcs.most_common())

    supporting = [x for x in group if direction_of(x["a"]) == majority]
    against = [x for x in group if direction_of(x["a"]) not in (majority, "unknown", "null")]
    undecided = [x for x in group if direction_of(x["a"]) in ("unknown", "null")]

    body = [
        fm(NodeFormality="draft", human_reviewed="no", TruthValue=truth,
           aliases=[f"CLM - {title}"],
           tags=[f"marker/{marker.lower().replace(' ', '-')}",
                 f"theme/{theme.replace(' ', '-')}",
                 f"direction/{majority}", f"consistency/{strength.replace(' ', '-')}"],
           created=TODAY, updated=TODAY, nodeID=nid(), title=title),
        "", "## The claim", "", f"**{title}**", "",
        "## What it rests on", "",
        ("> [!info] About this gene\n"
         f"> **{marker}** covers several less-studied resistance markers in the malaria "
         "parasite, such as pfaat1, pfcoronin and pfexo."
         if marker == "Other markers" else
         "> [!info] About this gene\n"
         f"> **{marker}** is " + (gloss or "a malaria-parasite drug-resistance marker") + "."),
        "",
        f"{n_f} in the System Public Graph relate {gene_name} to {plain}, drawn from {n_s} "
        f"published {span}. Of the {decided} finding" + ("s" if decided != 1 else "") +
        f" whose direction can be determined, **{max(pos, neg)} point"
        + ("" if max(pos, neg) == 1 else "s") * 0 + ("s" if max(pos, neg) == 1 else "") +
        f" the same way** ({agree:.0%}) and {min(pos, neg)} point"
        + ("s" if min(pos, neg) == 1 else "") + " the other way.", "",
        "| | |", "|---|---|",
        f"| Findings | {len(group)} |",
        f"| Distinct studies | {nstud} |",
        f"| Publication window | {span} |",
        f"| Direction | {majority} ({strength}) |",
        f"| Supporting / contradicting / undecided | {len(supporting)} / {len(against)} / "
        f"{len(undecided)} |",
        f"| Confirmed in the curated dataset | "
        f"{_n_dep} of {len(group)} ({_n_dep/len(group):.0%}) |",
        f"| Carrying a p-value | {_n_p} of {len(group)} ({_n_p/len(group):.0%}) |",
        f"| Carrying a confidence interval | {_n_ci} of {len(group)} "
        f"({_n_ci/len(group):.0%}) |",
        f"| Data sources | {_src_txt} |",
        f"| Source papers retracted or under concern | {_n_serious} of {len(group)} "
        f"({_n_serious/len(group):.0%}) |",
        f"| Source papers with a published erratum | {_n_errata} of {len(group)} "
        f"({_n_errata/len(group):.0%}) |",
        f"| Source papers with formal published comments | {_n_comment} of {len(group)} "
        f"({_n_comment/len(group):.0%}) |",
        f"| Source papers with critical social posts | {_n_xneg} of {len(group)} "
        f"({_n_xneg/len(group):.0%}) |",
        f"| Source papers with PubPeer comments | {_n_pp} of {len(group)} "
        f"({_n_pp/len(group):.0%}) |",
        f"| Source papers open access | {_n_oa} of {len(group)} ({_n_oa/len(group):.0%}) |",
        f"| Source papers with data in a public repository | {_n_data} of {len(group)} "
        f"({_n_data/len(group):.0%}) |",
        f"| Source papers with public code | {_n_code} of {len(group)} "
        f"({_n_code/len(group):.0%}) |",
        "| Statistic types | " + ", ".join(f"{k.replace('_', ' ')} ({v})"
                                           for k, v in stat_mix.most_common()) + " |",
        "",
        "> [!warning] How far this claim can be pushed",
        "> The direction above is inferred from each statistic's sign against its null value — 1 "
        "for ratios, 0 for differences and correlations — not from any direction field, because "
        "the graph has none. The findings use different statistic types and cannot be pooled "
        "into a single effect size, so this claim asserts a **direction and its consistency**, "
        "not a magnitude. Which variable is cause and which is effect is also unrecorded. See "
        "[[CVT - The graph records no effect direction]].",
        "",
        "## Supporting Evidence", "",
        "> [!info] Findings pointing the same way as the claim, oldest first.", "",
    ]
    for r in sorted(supporting, key=lambda x: (x["year"] or 0)):
        fn, t = evd_index[r["a"]["system_id"]]
        body.append(f"- [[{fn}|{t}]]")

    if against:
        body += ["", "## Contradicting Evidence", "",
                 "> [!warning] Findings pointing the opposite way. A claim that hides these is "
                 "not worth making.", ""]
        for r in sorted(against, key=lambda x: (x["year"] or 0)):
            fn, t = evd_index[r["a"]["system_id"]]
            body.append(f"- [[{fn}|{t}]]")

    if undecided:
        body += ["", "## Findings with no determinable direction", "",
                 "> [!info] The statistic sits exactly at its null value, or no value was "
                 "recorded.", ""]
        for r in undecided:
            fn, t = evd_index[r["a"]["system_id"]]
            body.append(f"- [[{fn}|{t}]]")

    body += ["", "## Findings per year", "", "| Year | Findings |", "|---|---|"]
    for y, n in sorted(collections.Counter(x["year"] for x in group if x["year"]).items()):
        body.append(f"| {y} | {n} |")
    write("claims", fname, "\n".join(body))
    clm_index[(marker, theme)] = (fname, title)

print(f"wrote {len(clm_index)} CLM nodes")

# -------------------------------------------------------------------- QUE nodes

QUESTIONS = [
    ("How can we tell when new research changes what is known about a drug-resistance gene",
     "How can we tell when newly published research has changed what is known about a malaria "
     "drug-resistance gene?",
     "Malaria parasites evolve, and the genetic mutations that let them survive a drug keep "
     "shifting. A new mutation appearing in a new country can mean a drug that worked last year "
     "no longer does. The problem is that this news arrives scattered across hundreds of separate "
     "papers, so a researcher tracking one gene has no simple way to know when the overall picture "
     "has changed enough to act on. This is the challenge question set by Roberto Amato of PATH.",
     "An alert would need to fire on any of three things: a result that contradicts what earlier "
     "studies found, a sharp change in how common a mutation is, or the first sighting of a "
     "mutation in a new place or after a long gap.",
     ["challenge/build-3"]),
    ("Which malaria drug-resistance genes does the System Public Graph actually have evidence on",
     "Which malaria drug-resistance genes does the System Public Graph actually hold evidence "
     "on, and how much?",
     "Before building a monitoring tool you have to know whether the underlying data can support "
     "it. The System Public Graph gathers statistical findings from published research, so its "
     "coverage reflects what researchers have published and what the extraction pipeline managed "
     "to read — not what public-health programmes most need to know.",
     "Coverage is uneven and, awkwardly, thinnest where it matters most. See "
     "[[CVT - Pfkelch13 is the most important marker and the least covered]].",
     ["coverage"]),
    ("Can publication dates show how evidence on a resistance gene built up over time",
     "Can publication dates be used to replay how the evidence on a resistance gene built up "
     "over time?",
     "Detecting that evidence has changed requires knowing when each finding appeared. The System "
     "Public Graph does not record publication dates at all, so they have to be fetched "
     "separately from PubMed, the US National Library of Medicine's index of biomedical research, "
     "using the PubMed identifier attached to each finding.",
     "Yes. Every harvested finding resolved to a publication year, giving an unbroken run from "
     "1987 to 2025. One caution: the year a paper appeared is not the year the parasites were "
     "collected, and the graph records nothing about fieldwork dates.",
     ["method/time-series"]),
    ("How can we tell which way an effect runs when the data does not record direction",
     "How can we tell which way an effect runs when the data does not record a direction?",
     "Each finding in the graph is a pair of measured things and a number. Nothing says which of "
     "the two came first, which caused which, or whether the relationship is positive or "
     "negative. For an alert that is supposed to warn that resistance is worsening, that is a "
     "serious gap — 'worsening' is a direction.",
     "Partly solvable. Ratio statistics pivot around 1 and difference statistics around 0, so a "
     "rule can be written per statistic type. What cannot be recovered is which variable is the "
     "cause and which the effect, or the sign of comparisons that the extractor buried inside a "
     "variable name such as 'Laos (compared with Thailand)'.",
     ["method/direction"]),
    ("Where does malaria drug-resistance evidence live if not in this graph",
     "Where does malaria drug-resistance evidence live, if not in the published statistical "
     "literature this graph covers?",
     "The graph only holds findings that look like statistical relationships extracted from "
     "journal articles. Much of what the world knows about antimalarial resistance is not shaped "
     "that way, which explains why coverage of the newest and most urgent markers is so thin.",
     "The main sources outside the graph are MalariaGEN, a genomic surveillance programme that "
     "sequences parasites directly; WWARN, which pools drug-efficacy results across studies; the "
     "World Health Organization's annual World Malaria Report; and national therapeutic efficacy "
     "studies. None of these publish their results as the kind of extractable statistical "
     "sentence this graph is built from. This is also the subject of the hackathon's Explore "
     "Challenge 3.",
     ["coverage", "challenge/explore-3"]),
]

for short, full, why, answer, tags in QUESTIONS:
    fname = f"QUE - {slug(short, 112)}"
    body = [
        fm(NodeFormality="draft", human_reviewed="no", aliases=[f"QUE - {full}"], tags=tags,
           created=TODAY, updated=TODAY, nodeID=nid(), title=full),
        "", "## The question", "", f"**{full}**", "",
        "## Why it matters", "", why, "",
        "## Where we have got to", "", f"> [!info] Current answer", f"> {answer}", "",
        "## Supporting Claims (with their evidence)", "",
        "> [!info] Each claim below counts how many published findings link one resistance gene "
        "to one kind of outcome. Auto-linked — check relevance before citing.", "",
    ]
    ordered = sorted(clm_index.items(), key=lambda kv: (-len(groups[kv[0]]), kv[1][1]))
    for _, (fn, t) in ordered:
        body.append(f"- [[{fn}|{t}]]")
    body += ["", "## Limits on any answer", "",
             "> [!warning] Read these before relying on anything above", ""]
    for c in ["CVT - Roughly 20 percent of API associations are mis-extracted",
              "CVT - The graph records no effect direction",
              "CVT - List endpoints omit p-values and confidence intervals",
              "CVT - Variables are one-per-paper phrasings not canonical entities",
              "CVT - Pfkelch13 is the most important marker and the least covered",
              "CVT - Concept grounding is coarse and sometimes wrong",
              "CVT - The curated Dataverse deposit holds almost no resistance evidence"]:
        body.append(f"- [[{c}]]")
    write("questions", fname, "\n".join(body))

print(f"wrote {len(QUESTIONS)} QUE nodes")

# -------------------------------------------------------------------- CVT nodes

CAVEATS = [
    ("Roughly 20 percent of API associations are mis-extracted", "api/data-quality",
     "System's documentation states that roughly 20% of the findings its API returns were read "
     "inaccurately out of the source papers — it gives wrong mean differences as the example. The "
     "records System had flagged were removed from its curated Harvard Dataverse release, and the "
     "documentation advises checking API results against that release.",
     "For an alert system this is the central threat. A number misread from a paper looks exactly "
     "like a genuinely surprising new result, which is precisely what the tool is built to spot. "
     "An alert that simply ranks findings by how surprising they are would work as a "
     "misextraction detector. Every finding must therefore carry its verification state, and no "
     "unverified number should ever be shown as a bare figure."),
    ("The graph records no effect direction", "api/schema",
     "Findings carry a statistic type and a value but no field saying which way the relationship "
     "runs, and no field saying which of the two variables is the cause. The harvested set mixes "
     "odds ratios, adjusted odds ratios, risk ratios, hazard ratios, prevalence ratios, incidence "
     "rate ratios, unstandardised mean differences, regression coefficients and correlations.",
     "Direction has to be inferred from the statistic type — ratios pivot at 1, differences and "
     "correlations at 0. Two things stay unrecoverable: which variable is cause and which is "
     "effect, and the sign of a comparison the extractor folded into a variable name, as in "
     "'Laos (compared with Thailand)'. Reading such a name backwards flips the finding."),
    ("List endpoints omit p-values and confidence intervals", "api/schema",
     "A list request to the API returns 10 fields per finding. The p-value, the confidence "
     "interval and the concept identifiers exist only when a single finding is fetched on its "
     "own. The documented `fields` parameter that would widen the list response returns an HTTP "
     "500 error.",
     "Statistical precision costs one extra request per finding against a 10,000-per-day budget, "
     "so most evidence notes in this vault record no p-value or interval. The curated Dataverse "
     "release does carry all 19 columns in one file, which is its main practical advantage."),
    ("Variables are one-per-paper phrasings not canonical entities", "graph/data-model",
     "A 'variable' in this graph is one paper's exact wording — `Pfmdr1 N86`, `isolates with crt "
     "T76`, `Patients with k13 F446I mutation [vs Patients without k13 mutations]`. The graph "
     "holds 5,654,715 variables against 5,944,001 findings, roughly one new variable per finding.",
     "There is no single node for a gene, so nothing adds itself up. Assembling the evidence on "
     "one gene means matching patterns against millions of free-text strings, and every count in "
     "this vault depends on the specific patterns used, which live in `scripts/build_vault.py`. "
     "Different patterns would give different numbers. A related trap: the search is plain "
     "substring matching, so the abbreviation `crt` also matches cardiac resynchronisation "
     "therapy and chemoradiotherapy, and `IPT` matches isoniazid preventive therapy from the "
     "tuberculosis literature."),
    ("Pfkelch13 is the most important marker and the least covered", "coverage",
     "Variables found per gene in the API sweep: PfCRT 1,070 (mostly substring noise), Pfmdr1 "
     "436, other markers 364, PfDHFR 113, PfDHPS 59, Pfkelch13 30, plasmepsin 11. After "
     "filtering, the evidence notes in this vault split as Pfmdr1 90, PfCRT 77, PfDHPS 30, "
     "PfDHFR 29, Pfkelch13 21, other 6, plasmepsin 1.",
     "Pfkelch13 is the gene behind partial resistance to artemisinin, the drug family at the core "
     "of modern malaria treatment. Resistance has spread through Southeast Asia and has now "
     "reached East Africa, which is the reason this challenge exists — and it has the least "
     "evidence in the graph. Twenty-one findings is too few to replay a trajectory. A working "
     "prototype should be built on Pfmdr1 or on the DHFR/DHPS pair, with Pfkelch13 shown as the "
     "case where the method correctly fires too rarely. That contrast is itself a finding about "
     "where surveillance evidence is missing."),
    ("Concept grounding is coarse and sometimes wrong", "graph/grounding",
     "The graph can link a variable to a shared concept in Wikidata, which should let different "
     "wordings collapse together. Only 732 of 2,055 marker variables (36%) carry such a link, and "
     "they spread across 193 different concepts, including ones as broad as `mutation` and "
     "`antimicrobial resistance`, ones plainly wrong such as `postoperative complications` and "
     "`induction chemotherapy`, and one actively misleading: `5,10-methylenetetrahydrofolate "
     "reductase`, which is the human MTHFR enzyme, standing in for the parasite's DHFR.",
     "The concept layer cannot be used to group synonyms. The MTHFR case is worse than no link at "
     "all, because it would silently merge human folate-pathway research with malaria resistance "
     "research. Expanding outward through these concepts returned 18,380 sibling variables, of "
     "which exactly one was malaria-related."),
    ("Only three of 117 source papers share their analysis code", "source/reproducibility",
     "Open-access status, data availability and code availability were checked for all 117 "
     "source papers on 14 November 2026 using OpenAlex, NCBI's ID converter and PMC full text. "
     "**89 of 117 are open access** in some form (gold 44, green 21, bronze 13, hybrid 7, "
     "diamond 4) and 27 are closed. Only **58 have full text deposited in PMC**, which is what "
     "makes an availability statement readable at all. Of the 58 that could be assessed, only "
     "**6 clearly deposited their data in a public repository**, 9 offer it on request only, 18 "
     "have a statement too vague to classify and 25 have none at all. **Just 3 papers share "
     "analysis code**, all on GitHub: `Mrc-ide/mipanalyzer`, `bailey-lab/MIPTools` and "
     "`EPPIcenter/moire`. Only 4 cite an unambiguous public sequence accession, though 26 name a "
     "repository such as GenBank, the Sequence Read Archive or MalariaGEN in their text.\n\n"
     "An earlier run of this check reported 35 papers as having deposited data and 46 as citing "
     "accessions. That was wrong: the accession pattern included a generic two-letter plus "
     "six-digit form that matched ordinary words such as `Mc080501`, and any paper with a "
     "spurious match was classified as having deposited data. Tightening the pattern to named "
     "formats only (PRJNA, PRJEB, ERP, SRP, SRR, GSE, ERS) cut deposits from 35 to 6.",
     "This is the reproducibility picture for the evidence base, and it is poor in a specific "
     "way: hardly anything is shared. Six papers in 117 deposited data and three published "
     "code, so the analysis that turned raw observations into the statistic in this vault is "
     "almost never replayable, and usually neither are the observations. Worse, **for 59 papers "
     "(51%) the question cannot be answered at all** — 36 "
     "are not in PMC and 23 have only front matter there — so 'no statement found' and 'cannot "
     "tell' must not be read as the same thing. Findings whose source offers data on request or "
     "has no statement carry an explicit warning, because nobody can re-derive them from public "
     "material: they rest entirely on System's extraction being right and on the paper's own "
     "analysis being right."),
    ("What the post-publication screen covers and what it cannot", "source/integrity",
     "All 117 source papers were screened on 14 November 2026 against four sources: PubMed's "
     "CommentsCorrections records, Crossref's update metadata, Retraction Watch via "
     "retractionrisk.com, and **PubPeer via the official PubPeer Foundation extension API** "
     "(`POST https://pubpeer.com/v3/publications`, the endpoint published in their own "
     "MIT-licensed browser extension).\n\n"
     "Results: **none is retracted and none carries an expression of concern.** Four carry a "
     "published erratum (Witkowski 2017, Win 2016, Venkatesan 2014, Antia-Obong 1997). Eight "
     "attracted formal published comments, including three of the highest-profile "
     "artemisinin-resistance papers in the set (Balikagala 2021, Mihreteab 2023, Spring 2015). "
     "Five carry negatively-scored social posts. And **not one of the 117 has any PubPeer entry "
     "at all**, queried both by DOI and by PubMed ID.\n\n"
     "The PubPeer zero was verified rather than assumed: a known heavily-commented retraction "
     "placed inside a full 20-DOI batch alongside 19 of our papers came back with its 34 "
     "comments and four update types, while ours returned nothing. The batching path works, so "
     "the absence is real.",
     "**Zero PubPeer coverage is not evidence of quality.** PubPeer's attention concentrates on "
     "high-profile papers and on suspected image or statistics problems, largely in cell "
     "biology and psychology. A specialist malaria-genotyping literature having no threads most "
     "plausibly means nobody has looked, not that nothing is wrong. Read the silence as absence "
     "of scrutiny, not as endorsement.\n\n"
     "Two genuine limits remain. First, an erratum means the article was corrected after "
     "publication and System extracted its statistics from the original, so a corrected value "
     "may still sit in this vault unchanged; those four papers' findings carry a warning. "
     "Second, informal critique — journal clubs, conference corridors, correspondence — leaves "
     "no machine-readable trace anywhere, so no screen can reach it.\n\n"
     "On the Retraction Watch comparison: retractionrisk.com reported 2 corrections where "
     "PubMed's own records show 4, so the aggregator is the less sensitive of the two sources. "
     "Its Altmetric feed did add something no other source here provides — 74 negatively-scored "
     "posts for Mihreteab 2023, 52 for Balikagala 2021, 3 for Landier 2018, 1 each for two "
     "others. Treat that carefully: the sentiment is algorithmic, and for papers announcing "
     "that artemisinin resistance has reached Africa a negative score most plausibly reflects "
     "alarm at the finding rather than doubt about the work. Its own PubPeer counts are always "
     "0, because its backend is blocked by PubPeer from cloud IP addresses."),
    ("The curated Dataverse deposit holds almost no resistance evidence", "source/dataverse",
     "System's curated release on Harvard Dataverse (doi:10.7910/DVN/7V6JDO) is the cleaned "
     "version, with flagged mis-extractions removed. Its findings file holds 1,999,877 rows "
     "against the API's 5,944,001 (34%), and its variables file 1,774,551 against 5,654,715 "
     "(31%). A regex sweep of all 1,999,877 findings turned up just 25 that pair a resistance "
     "gene with malaria context, against 1,184 harvested from the API. Only 272 of those 1,184 "
     "(23%) appear in the release at all — below the ~34% a uniform random subset would give.",
     "The curated release cannot be the main data source for this topic; the API has roughly "
     "fifty times more. Its value is as a verification layer, since presence in it is the best "
     "available signal that a number was read correctly, and for the statistical columns the API "
     "withholds from list responses. Note that System's advice to discard anything absent from "
     "the release would throw away 77% of this vault, and that absence reflects the release's "
     "narrower scope as much as data quality."),
]

for short, tag, statement, implication in CAVEATS:
    write("caveats", f"CVT - {slug(short, 112)}", "\n".join([
        fm(NodeFormality="draft", human_reviewed="no", aliases=[short], tags=[f"cvt/{tag}"],
           created=TODAY, updated=TODAY, nodeID=nid(), title=short),
        "", "## Statement", "", statement, "",
        "## Why it limits the evidence", "", implication, "",
        "## Affects", "", "- Every evidence note in this vault, unless stated otherwise.", "",
        "## Provenance", "",
        f"Established by direct measurement against the live API and the curated Dataverse "
        f"release on {TODAY}. See `LOG.md` and `scripts/`.",
    ]))

print(f"wrote {len(CAVEATS)} CVT nodes")

# ------------------------------------------------------------------------ DGRAPH

lines = ["# DGRAPH — nested index", "",
         "> [!info] Auto-generated by `scripts/build_vault.py`. Questions, then the claims "
         "beneath them, then a sample of the findings behind each claim.", ""]
for short, full, *_ in QUESTIONS:
    lines.append(f"- ❓ [[QUE - {slug(short, 112)}|{full}]]")
for (marker, theme), (fn, t) in sorted(clm_index.items(),
                                       key=lambda kv: (-len(groups[kv[0]]), kv[1][1])):
    lines.append(f"    - 💡 [[{fn}|{t}]]")
    group = groups[(marker, theme)]
    for r in sorted(group, key=lambda x: (x["year"] or 0))[:10]:
        efn, et = evd_index[r["a"]["system_id"]]
        lines.append(f"        - 🔬 [[{efn}|{et}]]")
    if len(group) > 10:
        lines.append(f"        - … and {len(group) - 10} more, listed in [[{fn}]]")
lines += ["", "## Caveats", ""]
for short, *_ in CAVEATS:
    lines.append(f"- ⚠️ [[CVT - {slug(short, 112)}|{short}]]")
write("", "DGRAPH", "\n".join(lines))

stats = {
    "evidence": len(evd_index), "claims": len(clm_index), "questions": len(QUESTIONS),
    "caveats": len(CAVEATS), "sources": len(by_study),
    "verified_in_deposit": sum(1 for r in rows if r["a"]["system_id"] in DEPOSIT_IDS),
    "with_p_value": sum(1 for r in rows if r["a"].get("p_value") is not None),
    "with_interval": sum(1 for r in rows if r["a"].get("ci_lower") is not None),
    "deposit_only": sum(1 for r in rows if r.get("deposit_only")),
    "provenance": dict(collections.Counter(
        s for r in rows for s in (r.get("provenance") or []))),
    "markers": {m: sum(1 for r in rows if m in r["markers"]) for m in MARKERS},
    "years": sorted({r["year"] for r in rows if r["year"]}),
}
(VAULT / "stats.json").write_text(json.dumps(stats, indent=1))
print("\nnode counts:", {k: v for k, v in stats.items() if isinstance(v, int)})
print("by marker:", stats["markers"])
print(f"year span: {stats['years'][0]}-{stats['years'][-1]}")
print(f"\nvault at {VAULT}")
