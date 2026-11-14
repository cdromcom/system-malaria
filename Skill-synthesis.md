---
name: synthesize-graph-evidence
description: How findings are grouped into claims, how outcome themes are defined, and how to design an alert rule that detects when evidence on a marker has moved. Companion to Skill.md.
allowed-tools: Read, Write, Bash
---

# Skill — synthesis and alert design

The layer above [[Skill-harvest]]: turning individual findings into something a researcher can
act on.

## Grouping: marker × outcome theme

Because [[CVT - Variables are one-per-paper phrasings not canonical entities|variables are
one-per-paper phrasings]], grouping is explicit and pattern-based. Two axes.

**Markers** — Pfkelch13, PfCRT, Pfmdr1, PfDHFR, PfDHPS, plasmepsin, other. Each matched by gene
name, protein name, codon mutations and haplotype names. Patterns live in
`scripts/build_vault.py`.

**Outcome themes** — six, matched against the partner variable's name:

| Theme | Matches |
| --- | --- |
| treatment failure | treatment failure, recrudescence, reinfection, cure rate, clinical/parasitological failure, ACPR |
| parasite clearance | clearance, day-3 positivity, parasitaemia, parasite density |
| marker prevalence | prevalence, frequency, haplotype, mutant, polymorphism, genotype, allele |
| drug susceptibility | IC50, EC50, IC90, susceptibility, survival assay, ex vivo, in vitro |
| haematology | anaemia, haemoglobin, haematocrit |
| severe disease | severe malaria, cerebral, mortality, hospitalisation, birth weight |

A CLM node is created for each pair with **≥2 findings**. 26 such pairs exist in this vault.

## Turning a group into a claim

A claim is a **directional assertion**, not a count. Construction:

1. Compute each finding's direction against its statistic's null value — 1 for ratios, 0 for
   differences, coefficients and correlations.
2. Take the majority direction among findings whose direction is determinable.
3. Pick the sentence from the template table for that (theme, direction) pair.
4. Append a qualifier set by the agreement proportion, and set `TruthValue` to that proportion.

| Agreement | Qualifier |
|---|---|
| ≥ 90% | ", consistently across studies" |
| 70–89% | ", though a minority of findings disagree" |
| < 70% | " — but the published evidence is contested" |

Every claim lists its **Contradicting Evidence** section alongside the supporting one, plus any
findings sitting exactly at the null value. Hiding the minority would make the qualifier a lie.

> [!warning] A claim commits to direction and consistency, never magnitude
> The statistic types are incompatible — an odds ratio and an unstandardised mean difference
> cannot be averaged — and which variable is cause and which is effect is unrecorded. Pooling
> them into a single effect size is the easiest available route to a confident wrong answer.

## Measured direction splits

Worth knowing before trusting any claim. The consistent groups:

| Gene | Outcome | n | Agreement |
|---|---|---|---|
| Pfkelch13 | parasite clearance | 7 | 100% |
| PfDHFR | treatment failure | 6 | 100% |
| PfCRT | treatment failure | 5 | 100% |
| PfDHPS | treatment failure | 5 | 100% |
| PfCRT | parasite clearance | 4 | 100% |
| Pfmdr1 | treatment failure | 9 | 89% |

And the contested ones, where the qualifier matters most:

| Gene | Outcome | n | Agreement |
|---|---|---|---|
| PfDHPS | marker prevalence | 23 | 65% |
| PfDHPS | severe illness | 5 | 60% |
| Pfkelch13 | other | 5 | 60% |
| Pfmdr1 | parasite clearance | 2 | 50% |

The treatment-failure rows agreeing at 89–100% across four genes is the most defensible thing in
this vault. The contested prevalence rows are the most interesting, since "prevalence rose" and
"prevalence fell" are both expected depending on whether the selecting drug was in use or
withdrawn — which means the theme is too coarse and should be split by drug-policy era.

## Direction, which the graph does not record

No direction field exists. Infer per statistic family:

| Family | Null value | Above null means |
| --- | --- | --- |
| `odds_ratio`, `adjusted_odds_ratio`, `relative_risk_ratio`, `hazard_ratio`, `prevalence_ratio`, `incident_rate_ratio` | 1 | positive association |
| `mean_difference_unstandardized`, `coefficient`, `pearson_r` | 0 | positive association |

Two things this cannot resolve. First, which variable is exposure and which is outcome — the
graph has `variable_1` and `variable_2`, not cause and effect. Second, the sign of a contrast
encoded inline in the variable name, as in `Laos [vs Thailand]` or `Patients with k13 F446I
mutation [vs Patients without k13 mutations]`; reading that correctly is a parsing problem, and
getting it backwards flips the finding.

State both limits in the pitch. A judge will ask.

## Designing the alert

The brief names three kinds of change. Each needs its own rule.

### 1. An unexpected association

Replay findings for a marker × theme pair in publication order. Maintain a running summary of
prior findings within a statistic family — median and interquartile range is more honest than a
pooled estimate here, given the extraction error rate. Fire when a new finding falls outside the
prior IQR by some multiple.

**The trap:** given a documented ~20% extraction error rate, the most statistically surprising
finding is disproportionately likely to be a bad extraction. An alert that simply ranks by
surprise is an extraction-error detector wearing a lab coat. Mitigate by weighting the
verification state, and by showing the prior distribution next to the new point so a human can
judge.

### 2. A large shift in prevalence

Restrict to the `marker prevalence` theme, where `statistic_value` is usually a percentage or
proportion. Compare new values against the trailing distribution for the same marker and, where
geography can be extracted, the same country. Watch for unit inconsistency — some findings report
percentages and some proportions, and nothing in the schema says which.

### 3. A new signal in a new place or time

The only geography source is the study's free-text `population` string. Extract country names
with a gazetteer and accept an incomplete hit rate. Fire when a marker's first finding appears for
a country, or when a gap of several years is broken.

This rule is the most useful of the three for the actual public-health problem — "resistance just
showed up somewhere new" is the thing programmes need to know — and the most limited by the data,
since geography is nowhere in the schema.

## Replay mechanics

Findings carry a publication year, not a date, so the replay is annual. The clean set spans
1987–2025 with no gap years, median around 9 findings per year. At that density, an annual step is
the right granularity; monthly would be mostly empty.

Remember that publication year is **not** the year the resistance was observed. A 2024 paper may
report 2019 isolates. The graph holds nothing about fieldwork dates, so any claim about when
resistance emerged is a claim about when it was *published*. Say that plainly.

## Honest reporting checklist

Before any number goes in the pitch:

- [ ] Does it carry its denominator?
- [ ] Is the grouping pattern that produced it stated or linked?
- [ ] Is the verification split (curated deposit vs API-only) shown?
- [ ] Does it distinguish publication year from observation year?
- [ ] Is the direction inference, and what it cannot resolve, stated?
- [ ] Are the rejected findings reported as a ratio, not silently dropped?
