---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - transmission intensity of different locations and genetic admixture analysis and F-statistics showed a pearson r of 0.49 - @mallick2013"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/pearson_r"
  - "direction/positive"
  - "verification/api-only"
  - "year/2013"
created: 2026-11-14
updated: 2026-11-14
nodeID: b941ef80-22ca-4718-b840-e86ebcc3af64
title: transmission intensity of different locations and genetic admixture analysis and F-statistics showed a pearson r of 0.49 - @mallick2013
---

## Source

[[@mallick2013]]

## In plain terms

> [!info] What this finding says
> A study published in 2013 reported a statistical link between **transmission intensity of different locations (measured by malaria prevalence and chloroquine resistance)** and **genetic admixture analysis and F-statistics**.
> Transmission intensity of different locations and genetic admixture analysis and F-statistics showed a pearson r of 0.49, p = 0.003.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0.49** |
| **p-value** | = 0.003 |
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
| **Open access** | Yes (green) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 13 different locations in India with varying transmission intensity of malaria. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | India |
| **Timeframe** | Published 2013. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `transmission intensity of different locations (measured by malaria prevalence and chloroquine resistance)` with `genetic admixture analysis and F-statistics` and reports a pearson r of 0.49. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `transmission intensity of different locations (measured by malaria prevalence and chloroquine resistance)`
> Variable 2: `genetic admixture analysis and F-statistics`
> pearson r = 0.49, p = 0.003
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **transmission intensity of different locations (measured by malaria prevalence and chloroquine resistance)** to **genetic admixture analysis and F-statistics**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 13 different locations in India with varying transmission intensity of malaria.

## Provenance

- Source study: [[@mallick2013]]
- Paper: Microsatellite analysis of chloroquine resistance associated alleles and neutral loci reveal genetic structure of Indian Plasmodium falciparum.
- Journal: Infection, genetics and evolution : journal of molecular epidemiology and evolutionary genetics in infectious diseases
- Published: 2013 Oct
- PubMed: [23871774](https://pubmed.ncbi.nlm.nih.gov/23871774/)
- System association ID: `vopIO4zpnq`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
