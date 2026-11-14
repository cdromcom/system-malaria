# History

Chronological log of concrete changes to this vault. Newest first.

---

## 2026-11-14 — Vault created

**Pipeline runs**

- `harvest.py --probe` — 4 requests. Recorded five documentation/API discrepancies.
- `harvest.py --stage 1` — 289 requests, 38s. 23,580 variables from 202 search terms.
- `harvest.py --stage 2` — 475 requests, 89s. 36% grounding measured; concept route abandoned.
- `harvest.py --stage 3` — first run 923 requests, 62% failure, 439 associations. **Discarded.**
- `harvest.py --stage 3` — second run 1,271 requests, 804s, 4.5% failure, 1,184 associations.
- `harvest.py --stage 4` — 712 requests, 94s. 696 studies, 695 PubMed dates.
- `sweep_variables.py` — local sweep of the deposit's 1,774,551 variables. 22 marker variables.
- `check_deposit_overlap.py` — swept 1,999,877 deposit associations. 25 marker rows; 23% overlap
  with our API harvest.
- `build_vault.py` — generated all nodes.

**Code changes to `harvest.py`**

- Fixed doubled `/v1/v1/` in the base URL.
- Added truncation tracking to the stage 1 term sweep.
- Made stage 2 tolerant of permanent 500s on `wikidata_aliases` search and on concept IDs.
- Added substring-noise pruning with a malaria-vocabulary rescue rule (1,133 dropped, 1 rescued).
- Filtered concept siblings through malaria vocabulary before use (18,380 → 1).
- Split 500 handling: retry on variables and studies, fail fast on concepts. **This change
  recovered 745 associations that the previous policy had silently lost.**
- Added checkpointing to stage 3, every 200 anchors.
- Narrowed the `pfdhps` regex, which had matched the drug sulfadoxine rather than the gene and
  inflated the count from 1 to 84.

**Nodes created**

| Type | Count |
| --- | --- |
| EVD (evidence) | 225 |
| source (citation only) | 119 |
| CLM (claims) | 26 |
| CVT (caveats) | 7 |
| QUE (questions) | 5 |

**Documents created**

`Welcome.md`, `Skill.md`, `Skill-harvest.md`, `Skill-synthesis.md`, `Skill-templates.md`,
`LOG.md`, `History.md`, `DGRAPH.md`, `stats.json`, five templates in `templates/`, four scripts
plus a README in `scripts/`, Obsidian config in `.obsidian/`.

**Reversals worth recording**

1. **Recommended the Dataverse deposit as the primary data source, then reversed it.** The
   measurement showed the deposit holds 25 marker associations against the API's 1,184, and that
   only 23% of our harvest appears in it. It is a verification layer, not a source of recall.
   Recorded in [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].
2. **Disabled HTTP 500 retries globally, costing 62% of the data.** Correct for the concepts
   endpoint, wrong everywhere else. Recorded in [[Skill-harvest]] under "The expensive mistake".

---

## 2026-11-14 (later) — Rewritten for non-specialist readers

**Why:** the first pass produced machine-shaped titles (`var1 and var2: statistic = x`) that
needed the note opened to make sense, and source files were named `@pmid<id>`, which carries no
information for a reader.

**Guides used:** the `LIVES - EVD` tab of the review spreadsheet, whose column F shows the house
style — a full declarative sentence leading with the number and naming what was measured — and the
node conventions of the living-synthesis vault.

**Changes**

- **Evidence titles rewritten** as sentences: *"Odds ratio of 0.56 linking PfCRT K76T mutations
  to severe malaria (Cuu et al. 2020)"*. Each variable gets its own 72-character budget so both
  always appear; truncation lands on a word boundary and backs off before an unclosed bracket.
- **Acronyms expanded.** A 28-entry glossary covers the resistance genes, drug regimens and
  outcome measures. Up to two are expanded inline in a title; every match is listed in full in a
  new **Terms explained** section. Mutation codes are expanded mechanically (`F446I` → "swaps
  amino acid F for I at position 446"). Where a gene was matched only via a mutation code, its
  gloss is added explicitly, since otherwise nothing in the note says the finding concerns
  artemisinin resistance.
- **Suppressed self-expansions** such as `Pfmdr-1 (Pfmdr1)` by comparing strings with case,
  spaces and hyphens stripped.
- **`[vs X]` rendered as `(compared with X)`** throughout.
- **New "In plain terms" section** on every evidence node, with a paired "What this finding does
  **not** say" warning about the missing direction and causality.
- **Source files renamed** from `@pmid<id>` to `@<surname><year>` (e.g. `@bonnington2017`), with
  `a`/`b`/`c` suffixes for same-author-same-year collisions. Required fetching first-author
  surnames from PubMed, which the earlier run had not stored — 695 records, 4 requests, via
  `scripts/fetch_authors.py`. Source stubs now also list first author, co-author count and last
  author.
- **Questions rewritten** as plain-language questions with "Why it matters" and "Where we have
  got to" sections. Terms like PubMed, MalariaGEN, WWARN and IPTp are now explained rather than
  assumed.
- **Claim titles rewritten** to lead with the count and use plain descriptions of outcomes —
  "whether malaria treatment failed" rather than "theme/treatment-failure" — and each now carries
  a "This is a count, not a conclusion" warning.
- **Caveats rewritten** in plain language, with the jargon of the API replaced by description.

**Data corrections found while rewriting**

- **Excluded human KLHL13 / ophthalmology noise.** Bare `k13` had matched "number of K13+ cells"
  and "LSCD severity" — limbal stem cell deficiency, an eye condition. Three findings removed.
  That is 14% of the Pfkelch13 evidence, the marker that matters most.
- **Collapsed 7 exact duplicate findings** (same variable pair, study, statistic type and value;
  the graph sometimes stores both variable orderings). Checked first that the other 225
  same-pair repeats carry *different* statistics and are therefore genuinely separate findings —
  those were kept.

**Node counts after the rewrite**

| Type | Before | After |
| --- | --- | --- |
| EVD | 225 | 221 |
| source | 119 | 117 |
| CLM | 26 | 26 |
| QUE | 5 | 5 |
| CVT | 7 | 7 |

Pfkelch13 findings fell from 21 to 18 with the eye-research exclusion.

**Build hazard found: iCloud conflict duplicates**

`~/Documents` is under iCloud sync, and repeatedly deleting and rewriting hundreds of node files
in quick succession raced the sync agent, which resolved the conflicts by keeping both copies and
appending ` 2` to the newer one. This produced **465 stale duplicates** carrying links from
earlier builds, which is what broke 55 wikilinks.

Note that these cannot be cleaned up by pattern-matching ` <digit>.md`, because legitimate
variable names end in numbers too — "P. falciparum multidrug resistance gene 1". The safe fix is
to remove the node directories outright and let the build recreate them:

```bash
cd ~/Documents/system-malaria && rm -rf evidence claims questions caveats source
cd ~/system-public-challenge && python3 scripts/build_vault.py
```

After a clean rebuild: 390 notes, 2,089 wikilinks, all resolving except the deliberate
`[[Jay Patel]]` author link.

---

## 2026-11-14 (third pass) — PICOST evidence framing, directional claims

Approved from three inline drafts before scaling.

**Evidence nodes**

- **PICOST table added** to all 221 notes: Population, Intervention/exposure, Comparator,
  Outcome, Setting, Timeframe. Filled only where the record supports it. Comparators are split
  out of the `[vs …]` notation; Setting is regex-parsed from the population string; Timeframe
  always notes that fieldwork dates are absent from the graph.
- **Direction asserted only when safe.** A title claims a direction only when the second variable
  is outcome-shaped (`risk of`, `failure`, `clearance`, `recrudescence`, `mortality`, …) and the
  first is not. **126 of 221 findings fail that test** and carry an explicit "which is cause and
  which is effect cannot be determined" warning instead of a guess.
- **Three warnings kept** at the user's instruction: direction unknown (126 notes), units not
  recorded (99 notes), possible extraction mismatch (2 notes).
- **Filenames switched** to the living-evidence-synthesis form, ending ` - @citekey`.
- A `direction/` tag was added to every node.

**Claims rewritten as directional assertions**

The previous claims were counts — *"44 findings from 22 studies link the Pfmdr1 resistance gene
to how common the resistance mutation was"* — which is not a claim anyone can disagree with.
They now follow the living-evidence-synthesis style: *"Mutations in PfCRT are associated with
higher rates of antimalarial treatment failure, consistently across studies."*

Direction comes from the majority sign of the underlying findings against each statistic's null
value (1 for ratios, 0 otherwise). The trailing qualifier and `TruthValue` are set by the
agreement proportion: ≥90% "consistently across studies", 70–89% "though a minority of findings
disagree", below 70% "but the published evidence is contested". Each claim now carries a
**Contradicting Evidence** section and a list of findings sitting exactly at the null value.

Measured splits worth recording: treatment failure agrees at 89–100% across Pfmdr1, PfCRT,
PfDHFR and PfDHPS, and Pfkelch13 × parasite clearance agrees 7 of 7. The contested groups are
PfDHPS × marker prevalence (65%), PfDHPS × severe illness (60%) and Pfkelch13 × other (60%).

**Bugs fixed, found by writing for human readers**

- **Citekey surnames.** `Diakité` became `@diakit2019` because accents were deleted rather than
  transliterated; compound surnames collapsed to particles, so `de Kant E` became `@de2008` and
  `Di Nicolantonio F` became `@di2004`. PubMed's `sortfirstauthor` is "Surname Initials", so the
  fix is to drop the trailing initials token, keep the rest, and normalise accents by Unicode
  decomposition. 50 of 695 author records were affected.
- **"a odds ratio"** → article agreement on vowel-initial statistic names.
- **"a -13 change"** → "a decrease of 13" when the value is negative.
- **"a group of less-studied resistance markers resistance-mutation prevalence rises"** — the
  marker-prevalence claim template used the gene name as a possessive subject, which broke for
  the catch-all group. Reworded to "Resistance-mutation prevalence in {gene} rises…".
- **Doubled hedge** on negative severe-illness claims, where the template's own "most findings
  point the other way" collided with the appended ", consistently across studies".
- **Mismatch warning over-firing.** It compared the gene's display name against the paper title,
  so a title saying "K13" did not count as naming "Pfkelch13". Now matched by the gene's own
  regex: warnings fell from widespread to 2 genuine cases.
- **Setting row duplicated Population** when the regex found no country; now says "Not stated
  separately — see Population above."

**Final state:** 390 notes, 1,995 wikilinks all resolving, 386 valid frontmatter blocks.

**iCloud race recurred, and the fix that actually works**

Deleting the node directories before rebuilding was not sufficient: the second build produced
another 42 conflict duplicates (159 source files where 117 were expected), and the stale copies
carried links from the previous naming scheme, which is what showed up as 75 unresolved
wikilinks.

`build_vault.py` now honours a `VAULT_DIR` environment variable. The working procedure is to
build into a staging directory outside iCloud and `rsync -a --delete` each node directory in.
Documented in `scripts/README.md`.

After staging and syncing: **390 notes, 1,996 wikilinks, 386 valid frontmatter blocks, and 3
unresolved links — all three intentional** (`Jay Patel`, plus `short name` and `@surnameYEAR`
inside code spans).

---

## 2026-11-14 (fourth pass) — Full statistics, provenance tracking, both data sources

**Every finding now carries its metric and estimate**

A new `scripts/fetch_detail.py` fetches the single-record detail for all 222 findings, which is
the only endpoint returning p-values, confidence intervals and concept IDs. Two runs were needed:
the first hit 38 persistent HTTP 500s, and re-running against the cache cleared them all.

Each evidence note gained a **Statistic** table above PICOST, listing the metric (both System's
normalised type and the type the paper reported), the estimate, the p-value, the confidence
interval, the direction, the data sources and whether the finding appears in the curated release.
Titles now always name the metric, appending it in parentheses where the sentence doesn't already
state it, and without repeating the estimate when it is already there.

Result: **176 of 222 findings (79%) carry a p-value** and **105 (47%) a confidence interval**,
where previously almost none did.

**Both sources now used, and measured**

| Data source | Notes | Share |
|---|---|---|
| API list + API detail | 191 | 86% |
| API list + API detail + Dataverse release | 30 | 14% |
| Dataverse release only | 1 | <1% |

The curated release contributes **one** finding the API sweep never saw (DHFR mutations →
parasite clearance time, hazard ratio 0.24) and confirms 30. That settles the question of whether
to use both: yes, but as verification and statistics backfill, not for recall. The pipeline now
merges deposit-only rows and falls back to the release's columns where an API detail call came
back empty.

Claims gained provenance rows too: how many of their findings are confirmed in the release, how
many carry a p-value, how many a confidence interval, and the data-source breakdown — all with
percentages.

**Welcome.md** gained a Mermaid provenance flow chart tracing literature → extraction → API and
curated release → sweep → filter → detail fetch → vault, with paragraphs on what each source is
used for and what an API-only note means for a reader.

**Fixes**

- `ci_level` comes back as `0` when unrecorded, which rendered as "0% CI". Now shown as
  "CI x to y (confidence level not recorded)".
- The merged Dataverse-only finding produced citekey `@unknownnd`, because its PubMed ID was
  never in the author cache — only API-harvest IDs were fetched. `fetch_authors.py` now also
  reads the deposit sweep, and the builder falls back to the author cache for date, journal and
  title.
- Provenance labelling disagreed with the verification row: 30 findings are in the release but
  only 25 matched my marker-filtered sweep of it. Both now use the full overlap check.

**Final state:** 392 notes, 2,002 wikilinks, 388 valid frontmatter blocks, 3 unresolved links
(all intentional).

---

## 2026-11-14 (fifth pass) — Post-publication screening and reproducibility signals

- **retractionrisk.com** queried for all 117 papers: Retraction Watch status (115 Clean, 2
  Corrected) plus Altmetric social attention (5 papers with negative X posts, 0 Bluesky).
  Its PubPeer counts are structurally 0, since its backend is blocked by PubPeer from cloud IPs.
  Its own client works around this with PubPeer's public extension key; **I did not reuse that
  key** — the sandbox blocked it as unauthorized access, correctly.
- **Openness checked** via OpenAlex, NCBI ID converter and PMC full text: 89 of 117 open access,
  but only **6 with data deposited** and **3 publishing code**, and 51% undeterminable.
- **New tables.** Nine screening rows on every evidence and source note; four new provenance
  rows on every claim. 64 findings now warn that they are unlikely to be independently
  reproducible.
- **Two new caveats** (nine total): one on the screening gaps, one on reproducibility.
- **A measurement error caught and corrected mid-pass.** The first openness run reported 35
  papers with deposited data; a generic two-letter + six-digit accession pattern was matching
  ordinary words, and any spurious match classified the paper as having deposited data. The
  corrected figure is 6. Both the caveat and this log carry the correction rather than quietly
  replacing the number.

**Final state:** 394 notes, 2,463 wikilinks, 390 valid frontmatter blocks, 3 unresolved links
(all intentional).

---

## 2026-11-14 (sixth pass) — PubPeer corrected, FORRT recorded

**The vault was asserting something false in roughly 340 places.** After the official PubPeer
Foundation API was found, every note still carried the row *"PubPeer | Not checked — requires a
developer key"*, the source notes carried a matching callout, `EVAL.md` carried a `[!danger]`
block saying *"No PubPeer evidence appears anywhere in this vault"*, and a caveat node was
titled *"Source papers were screened for retractions but not for PubPeer comments"*. All of it
has been corrected.

**What changed**

- The per-note PubPeer row in all 222 evidence notes now reads *"No PubPeer entry (checked by
  DOI and PubMed ID via the official PubPeer Foundation API)"*, or the comment count and
  PubPeer URL where there is one.
- Source notes gained a `[!success] No PubPeer comments` block explaining why an empty response
  is a negative result rather than a failed lookup, plus a narrower note on what no screen can
  reach (journal clubs, conference discussion, correspondence).
- The caveat was rewritten and retitled **"What the post-publication screen covers and what it
  cannot"**, naming all four screening sources and carrying the warning that zero PubPeer
  coverage is absence of scrutiny, not endorsement. All links to the old title were updated.
- Claims gained a *Source papers with PubPeer comments* row with percentages.
- `EVAL.md` gained **Check 9 (PubPeer)** with the endpoint, the payload shape, the batching
  parameters, the positive-control verification table, and an explicit note recording that this
  file previously carried the opposite claim. It also gained **Check 10 (Replication
  attempts)** recording the FORRT/FLoRA zero result.
- `Welcome.md`'s provenance prose was rewritten; its Mermaid diagram was separately simplified
  for presentation (statistics moved onto edge labels, PubMed and Screening nodes removed, and
  a `118 source papers` node added so the finding-to-paper link is explicit).
- `LOG.md`'s earlier PubPeer paragraph is marked **Superseded** rather than deleted, because
  the reasoning that led to the wrong conclusion is worth keeping.

**Final state:** 395 notes, 2,521 wikilinks, 391 valid frontmatter blocks, 3 unresolved links
(all intentional). No file in the vault still claims PubPeer was unchecked.
