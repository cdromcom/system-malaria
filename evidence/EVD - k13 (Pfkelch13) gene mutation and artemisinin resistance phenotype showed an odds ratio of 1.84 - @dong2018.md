---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - k13 (Pfkelch13) gene mutation and artemisinin resistance phenotype showed an odds ratio of 1.84 - @dong2018"
tags:
  - "marker/pfkelch13"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2018"
created: 2026-11-14
updated: 2026-11-14
nodeID: b73430af-6fa5-4219-8a18-1c7c56b88107
title: k13 (Pfkelch13) gene mutation and artemisinin resistance phenotype showed an odds ratio of 1.84 - @dong2018
---

## Source

[[@dong2018]]

## In plain terms

> [!info] What this finding says
> A study published in 2018 reported a statistical link between **k13 (Pfkelch13) gene mutation** and **artemisinin resistance phenotype**.
> K13 (Pfkelch13) gene mutation and artemisinin resistance phenotype showed an odds ratio of 1.84, p = 0.001.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **1.84** |
| **p-value** | = 0.001 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 1** | **positive** |
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
| **Open data** | A statement exists but is not explicit — GenBank |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 202 blood samples collected from Yunnan Province and 382 blood samples collected from falciparum malaria cases in Myanmar. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Yunnan Province |
| **Timeframe** | Published 2018. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `k13 gene mutation` with `artemisinin resistance phenotype` and reports a odds ratio of 1.84. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `k13 gene mutation`
> Variable 2: `artemisinin resistance phenotype`
> odds ratio = 1.84, p = 0.001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **k13 (Pfkelch13) gene mutation** to **artemisinin resistance phenotype**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 202 blood samples collected from Yunnan Province and 382 blood samples collected from falciparum malaria cases in Myanmar.

## Provenance

- Source study: [[@dong2018]]
- Paper: Genetic association between the Pfk13 gene mutation and artemisinin resistance phenotype in Plasmodium falciparum isolates from Yunnan Province, China.
- Journal: Malaria journal
- Published: 2018 Dec 18
- PubMed: [30563521](https://pubmed.ncbi.nlm.nih.gov/30563521/)
- System association ID: `0JOAjP20zg`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
