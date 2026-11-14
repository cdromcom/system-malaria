---
name: graph-node-templates
description: Node templates and the frontmatter schema for the system-malaria vault. Companion to Skill.md.
allowed-tools: Read, Write
---

# Skill — node templates

Blank templates live in `templates/`. This file documents the schema and the naming rules.

## Frontmatter schema

Fields appear in this order, matching the living-synthesis convention:

| Field | Type | Notes |
| --- | --- | --- |
| `NodeFormality` | `draft` / `ReadyForInternal` / `ReadyForExternal` | everything generated starts `draft` |
| `human_reviewed` | `yes` / `no` | only a human sets this to `yes` |
| `TruthValue` | 0–1 | CLM only; 0.5 means unassessed |
| `aliases` | list | the long form of the title, so wikilinks can use a short name |
| `tags` | list | see namespaces below |
| `created` / `updated` | ISO date | |
| `nodeID` | UUID | stable across rebuilds only if you preserve it — see the warning below |
| `title` | string | the full statement |

> [!warning] nodeID is regenerated on every rebuild
> `scripts/build_vault.py` mints a fresh UUID each run, so IDs are not stable. If you start
> referencing nodes by ID externally, add an ID cache keyed on the association `system_id` first.

## Tag namespaces

| Namespace | Values |
| --- | --- |
| `marker/` | pfkelch13, pfcrt, pfmdr1, pfdhfr, pfdhps, plasmepsin, other-markers |
| `theme/` | treatment-failure, parasite-clearance, marker-prevalence, drug-susceptibility, haematology, severe-disease |
| `stat/` | the `system_statistic_type` value |
| `year/` | publication year |
| `verification/` | `in-curated-deposit` or `api-only` |
| `cvt/` | api/data-quality, api/schema, graph/data-model, graph/grounding, coverage, source/dataverse |
| `challenge/` | build-3, explore-3 |

## File naming

| Type | Pattern |
| --- | --- |
| Question | `questions/QUE - <short question>.md` |
| Claim | `claims/CLM - <directional assertion><qualifier>.md` |
| Evidence | `evidence/EVD - <sentence> - @<citekey>.md` |
| Caveat | `caveats/CVT - <short statement>.md` |
| Source | `source/@<firstauthorsurname><year>.md` — e.g. `@bonnington2017` |

## Writing titles for a non-specialist

Titles follow the LIVES - EVD sheet convention: **a full declarative sentence that leads with the
number and names both things being related**, then the attribution.

```
Difference of 1.6 linking F446I mutation (compared with Wildtype (no mutation))
  to Parasite Clearance Half-Life (Bonnington et al. 2017)

Odds ratio of 0.56 linking PfCRT K76T mutations to severe malaria (Cuu et al. 2020)
```

Rules the generator enforces:

- **Both variables always appear.** Each gets its own 72-character budget, so a long first
  variable cannot crowd the second out of the title.
- **Truncation lands on a word boundary** and backs off before an unclosed bracket.
- **Up to two acronyms are expanded inline**, chosen from the glossary in
  `scripts/build_vault.py`. An acronym is never expanded into itself — `Pfmdr-1 (Pfmdr1)` is
  suppressed by comparing the strings with case, spaces and hyphens removed.
- **`[vs X]` becomes `(compared with X)`**, since the extractor's bracket notation is opaque.
- **Attribution is `Surname et al. Year`**, from the PubMed first author.

Every node also carries a **Terms explained** section listing every glossary term and mutation
code found, in full. Mutation codes are expanded mechanically: `F446I` becomes "a mutation that
swaps amino acid F for I at position 446 of the protein". Where a gene was matched only through a
mutation code, the gene's own gloss is added explicitly — otherwise a reader meeting `F446I` has
no way to know the finding concerns artemisinin resistance.

Filenames are truncated to 118 characters and stripped of `<>:"/\|?*[]#^`. The full sentence
lives in `title` and `aliases`, so wikilinks use the `[[short name | full statement]]` form.

## Citekeys

`@<first author surname><year>`, lowercase, e.g. `@bonnington2017`, `@mwaiswelo2017`. Where one
author has several papers in a year, suffixes `a`, `b`, `c` are appended in PubMed ID order.
This departs from living-synthesis, which uses `@surnameTitleWordsYear`.

Extracting the surname from PubMed's `sortfirstauthor` needs care, since the format is
"Surname Initials" and the surname may carry particles or several words:

| PubMed value | Citekey surname |
|---|---|
| `Bonnington CA` | `bonnington` |
| `de Kant E` | `dekant` |
| `Di Nicolantonio F` | `dinicolantonio` |
| `Diakité SAS` | `diakite` — accents are transliterated, not deleted |
| `UK Collaborative Group on Monitoring …` | `ukcollaborative` — collective author, first two words |

Drop the trailing initials token (one capital plus up to three letters), keep everything before
it, strip accents by Unicode decomposition rather than by deleting the letter, and cap the result
at 24 characters. Deleting accents instead of transliterating produced `@diakit2019` on the first
pass, and taking only the first token produced `@de2008`.

## PICOST

Every evidence node carries a PICOST table — Population, Intervention, Comparator, Outcome,
Setting, Timeframe — filled only where the record supports it.

| Row | Source | When absent |
|---|---|---|
| Population | the study's `population` string, verbatim | "Not recorded in the graph." |
| Intervention / exposure | variable 1, with any `[vs …]` split off | "Not separable" plus the direction warning |
| Comparator | the `[vs …]` text | "Implied but not named in the record." |
| Outcome | variable 2 | "Not separable" plus the direction warning |
| Setting | country or site, regex-parsed from the population string | "Not stated separately — see Population above." |
| Timeframe | study design plus publication year | "Publication year unresolved." |

Timeframe always adds that fieldwork dates are absent from the graph, because publication year
is not the year the parasites were collected.

## When direction may be asserted

A title states a direction only when the record clearly separates an exposure from an outcome.
The test is whether the **second** variable is outcome-shaped — matching `risk of`, `odds of`,
`rate of`, `incidence`, `time to`, `failure`, `clearance`, `survival`, `recrudescence`,
`mortality`, `death`, `response`, `efficacy`, `cure`, `hospitali` — while the first is not.

| Case | Title form |
|---|---|
| Directional, ratio statistic | "X carried 9.42 times the risk of recrudescence" |
| Explicit `[vs]` comparator | "Y differed by 19.2 between A and B" |
| Directional, difference statistic | "X was associated with an increase of 13 in Y" |
| Neither | "X and Y showed an odds ratio of 2.08" + the direction warning |

126 of 221 findings fall into the last case. Those notes carry the warning rather than a guess.

## The three warnings

All three are deliberate and kept even though they add bulk:

1. **Direction unknown** — the record does not separate exposure from outcome. 126 notes.
2. **Units not recorded** — any difference or coefficient, where the graph gives no units.
   99 notes.
3. **Possible extraction mismatch** — the gene named in the record does not appear in the source
   paper's title, matched by the gene's own regex so that a title saying "K13" counts as naming
   Pfkelch13. 2 notes.

## EVD structure

```markdown
## Description
> [!info] Finding as extracted by System from the source study
> **variable 1** ↔ **variable 2**
> odds ratio = 2.4, p = 0.003
> 95% CI [1.3, 4.4]

## Methods Context
### What?   — the variables as named, and the statistic family
### How?    — study type, where recorded
### Who?    — the study's population string, verbatim

## Provenance
- source study wikilink, System IDs, PubMed link, year, markers, themes

## Verification
> [!success] or [!warning] — curated-deposit presence

## Other Notes
```

The What/How/Who schema is inherited from living-synthesis, but note the asymmetry: there, those
sections are filled from reading the paper's Methods. Here the graph supplies almost nothing, so
How and Who are usually one line each. That thinness is real and should not be padded.

## CLM structure

```markdown
> [!info] Claim scope — this is an aggregation claim, not a paper's claim

## Evidence base
- findings, distinct studies, publication window, statistic families

## Supporting Evidence
- EVD wikilinks, ordered by year

## Findings per year
| Year | Findings |
```

## CVT structure

```markdown
## Statement                  — what is true, with numbers
## Why it limits the evidence — the consequence for the build
## Affects                    — which nodes
## Provenance                 — how it was established
```

## Source structure

Citation data only. DOI, PubMed ID, journal, publication date, System study ID, study type, the
population string, and a list of the EVDs drawn from that study.

> [!danger] Never put article text in `source/`
> No abstracts, no quotes, no PDFs. The graph is the record and the DOI is the pointer. This
> keeps the vault redistributable under the graph's CC BY-NC licence without inheriting
> publisher restrictions.
