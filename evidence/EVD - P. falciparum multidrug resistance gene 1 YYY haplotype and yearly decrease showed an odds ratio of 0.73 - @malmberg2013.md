---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - P. falciparum multidrug resistance gene 1 YYY haplotype and yearly decrease showed an odds ratio of 0.73 - @malmberg2013"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/negative"
  - "verification/api-only"
  - "year/2013"
created: 2026-11-14
updated: 2026-11-14
nodeID: 421ed45c-4d8f-4636-9245-c72cc78ad87b
title: P. falciparum multidrug resistance gene 1 YYY haplotype and yearly decrease showed an odds ratio of 0.73 - @malmberg2013
---

## Source

[[@malmberg2013]]

## In plain terms

> [!info] What this finding says
> A study published in 2013 reported a statistical link between **P. falciparum multidrug resistance gene 1 YYY haplotype** and **yearly decrease**.
> P. falciparum multidrug resistance gene 1 YYY haplotype and yearly decrease showed an odds ratio of 0.73, p = 0.018. The confidence interval runs from 0.56 to 0.98.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **0.73** |
| **p-value** | = 0.018 |
| **Confidence interval** | CI 0.56 to 0.98 (confidence level not recorded) |
| **Direction vs null of 1** | **negative** |
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
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text — ClinicalTrials.gov, ISRCTN |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Children with uncomplicated P. falciparum malaria in Fukayosi village, Bagamoyo District, Tanzania, between 2004-2011. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Fukayosi village |
| **Timeframe** | Published 2013. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `P. falciparum multidrug resistance gene 1 YYY haplotype` with `yearly decrease` and reports a odds ratio of 0.73. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `P. falciparum multidrug resistance gene 1 YYY haplotype`
> Variable 2: `yearly decrease`
> odds ratio = 0.73, p = 0.018
> CI [0.56, 0.98]
> Direction against the statistic's null value of 1: **negative**

## Methods Context

### What?

The study related **P. falciparum multidrug resistance gene 1 YYY haplotype** to **yearly decrease**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Children with uncomplicated P. falciparum malaria in Fukayosi village, Bagamoyo District, Tanzania, between 2004-2011.

## Provenance

- Source study: [[@malmberg2013]]
- Paper: Temporal trends of molecular markers associated with artemether-lumefantrine tolerance/resistance in Bagamoyo district, Tanzania.
- Journal: Malaria journal
- Published: 2013 Mar 18
- PubMed: [23506218](https://pubmed.ncbi.nlm.nih.gov/23506218/)
- System association ID: `mEH4oLZu08`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
