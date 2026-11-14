# Scripts

Copies of the pipeline that produced this vault. The working originals live in
`~/system-public-challenge/`; these are here so the vault is self-describing.

| Script                     | Does                                                                    |
| -------------------------- | ----------------------------------------------------------------------- |
| `harvest.py`               | Stages 1–4 against the System API. `--probe`, `--stage N`, `--budget N` |
| `build_vault.py`           | Generates every node in this vault from `cache/*.json`                  |
| `sweep_variables.py`       | Local regex sweep over the Dataverse variables table                    |
| `check_deposit_overlap.py` | Deposit coverage, and which API findings survive curation               |
| `fetch_detail.py`          | Per-finding detail: p-values, intervals, concept IDs                    |
| `fetch_authors.py`         | First-author surnames for `@surnameYEAR` citekeys                       |
| `check_integrity.py`       | Retractions, errata, expressions of concern (PubMed + Crossref)         |
| `check_retractionrisk.py`  | Retraction Watch status and Altmetric social attention                  |
| `check_openness.py`        | Open access, open data, open code (OpenAlex + PMC)                      |
| `extract_open_quotes.py`   | Verbatim availability statements and APA citation fields                |
| `build_eval.py`            | Generates `EVAL.md` from those quotes                                   |

Run order:

```bash
cd ~/system-public-challenge
python3 harvest.py --probe
python3 harvest.py --stage 1
python3 harvest.py --stage 2
python3 harvest.py --stage 3
python3 harvest.py --stage 4
python3 -I scripts/sweep_variables.py raw/system-public-graph-v1-variables.tab
python3 -I scripts/check_deposit_overlap.py raw/system-public-graph-v1-associations.csv
python3 scripts/build_vault.py
```

## Rebuilding safely — build outside iCloud, then sync in

This vault sits under iCloud sync. Writing hundreds of node files directly into it races the
sync agent, which resolves conflicts by keeping both copies and appending ` 2`. Deleting the
directories first is not enough — the race recurred on the very next build.

The reliable procedure is to stage the build outside iCloud and rsync it in:

```bash
STAGE=/tmp/vault-stage
rm -rf "$STAGE" && mkdir -p "$STAGE"
cd ~/system-public-challenge && VAULT_DIR="$STAGE" python3 scripts/build_vault.py

cd ~/Documents/system-malaria
for d in evidence claims questions caveats source; do
  rsync -a --delete "$STAGE/$d/" "$d/"
done
cp "$STAGE/DGRAPH.md" "$STAGE/stats.json" .
```

`build_vault.py` honours the `VAULT_DIR` environment variable for exactly this purpose.

Afterwards run the link check below. Expect **390 notes and 3 unresolved links** — `Jay Patel`
(a deliberate author link with no note) plus `short name` and `@surnameYEAR`, which sit inside
code spans in the skill and template files and so are not real links.

Do not try to delete conflict files by matching ` <digit>.md` — real variable names end in
digits too, such as "P. falciparum multidrug resistance gene 1".

```bash
python3 - <<'EOF'
import re, pathlib, collections
notes = {p.stem for p in pathlib.Path('.').rglob('*.md')}
missing = collections.defaultdict(int); n = 0
for p in pathlib.Path('.').rglob('*.md'):
    if '.obsidian' in str(p): continue
    for l in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', p.read_text(encoding='utf-8')):
        n += 1
        if l not in notes: missing[l] += 1
print(f'notes {len(notes)} | wikilinks {n}')
print('unresolved:', dict(missing))
EOF
```

Needs `SYSTEM_API_KEY` in `~/system-public-challenge/.env`. The bulk files are untrusted
downloads, so the two sweeps run under `python3 -I` with the path passed as an argument.
