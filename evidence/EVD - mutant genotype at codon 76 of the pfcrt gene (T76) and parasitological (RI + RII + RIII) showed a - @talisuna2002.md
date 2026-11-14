---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - mutant genotype at codon 76 of the pfcrt gene (T76) and parasitological (RI + RII + RIII) showed a pearson r of 0.17 - @talisuna2002"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/pearson_r"
  - "direction/positive"
  - "verification/api-only"
  - "year/2002"
created: 2026-11-14
updated: 2026-11-14
nodeID: 39988276-668e-4cd0-bc9b-8d6cafeafea2
title: mutant genotype at codon 76 of the pfcrt gene (T76) and parasitological (RI + RII + RIII) showed a pearson r of 0.17 - @talisuna2002
---

## Source

[[@talisuna2002]]

## In plain terms

> [!info] What this finding says
> A study published in 2002 reported a statistical link between **mutant genotype at codon 76 of the pfcrt gene (T76)** and **parasitological (RI + RII + RIII)**.
> Mutant genotype at codon 76 of the pfcrt gene (T76) and parasitological (RI + RII + RIII) showed a pearson r of 0.17, p = 0.73.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0.17** |
| **p-value** | = 0.73 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **positive** |
| **Data source** | API list, API detail |
| **In curated release** | No |
| **Source paper integrity** | No retraction, erratum or expression of concern found (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: Clean) |
| **Published erratum** | None found |
| **Formal published comments** | None |
| **Critical social posts** | None recorded — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 6-59-month-old children with clinical malaria in 6 Ugandan sentinel sites in 1998-99. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2002. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `mutant genotype at codon 76 of the pfcrt gene (T76)` with `parasitological (RI + RII + RIII)` and reports a pearson r of 0.17. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `mutant genotype at codon 76 of the pfcrt gene (T76)`
> Variable 2: `parasitological (RI + RII + RIII)`
> pearson r = 0.17, p = 0.73
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **mutant genotype at codon 76 of the pfcrt gene (T76)** to **parasitological (RI + RII + RIII)**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 6-59-month-old children with clinical malaria in 6 Ugandan sentinel sites in 1998-99.

## Provenance

- Source study: [[@talisuna2002]]
- Paper: Role of the pfcrt codon 76 mutation as a molecular marker for population-based surveillance of chloroquine (CQ)-resistant Plasmodium falciparum malaria in Ugandan sentinel sites with high CQ resistance.
- Journal: Transactions of the Royal Society of Tropical Medicine and Hygiene
- Published: 2002 Sep-Oct
- PubMed: [12474488](https://pubmed.ncbi.nlm.nih.gov/12474488/)
- System association ID: `PLz-8EBXFu`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
