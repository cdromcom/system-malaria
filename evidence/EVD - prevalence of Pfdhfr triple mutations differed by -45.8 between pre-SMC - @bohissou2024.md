---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of Pfdhfr triple mutations differed by -45.8 between pre-SMC (seasonal malaria chemoprevention) and post-SMC (mean difference unstandardized) - @bohissou2024"
tags:
  - "marker/pfdhfr"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2024"
created: 2026-11-14
updated: 2026-11-14
nodeID: a001c122-8c2b-48d0-89ea-6d58a2de2331
title: prevalence of Pfdhfr triple mutations differed by -45.8 between pre-SMC (seasonal malaria chemoprevention) and post-SMC (mean difference unstandardized) - @bohissou2024
---

## Source

[[@bohissou2024]]

## In plain terms

> [!info] What this finding says
> A study published in 2024 reported a statistical link between **pre-SMC (seasonal malaria chemoprevention)** and **prevalence of Pfdhfr triple mutations**.
> Prevalence of Pfdhfr triple mutations differed by -45.8 between pre-SMC (seasonal malaria chemoprevention) and post-SMC (mean difference unstandardized), p = 0.0001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-45.8** |
| **p-value** | = 0.0001 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **negative** |
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
| **Open data** | Available from the authors on request only — ClinicalTrials.gov |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Not recorded in the graph. |
| **Intervention / exposure** | pre-SMC |
| **Comparator** | post-SMC |
| **Outcome** | prevalence of Pfdhfr triple mutations |
| **Setting** | Not recorded in the graph. |
| **Timeframe** | Published 2024. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **seasonal malaria chemoprevention** — monthly antimalarial drug courses given to young children through the rainy season

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pre-SMC [vs post-SMC]`
> Variable 2: `prevalence of Pfdhfr triple mutations`
> mean difference unstandardized = -45.8, p = 0.0001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **pre-SMC (seasonal malaria chemoprevention)** to **prevalence of Pfdhfr triple mutations**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> The graph holds no description of who was studied.

## Provenance

- Source study: [[@bohissou2024]]
- Paper: Evolution of Pfdhps and Pfdhfr mutations before and after adopting seasonal malaria chemoprevention in Nanoro, Burkina Faso.
- Journal: Scientific reports
- Published: 2024 Oct 16
- PubMed: [39414909](https://pubmed.ncbi.nlm.nih.gov/39414909/)
- System association ID: `T_GHc6Idp3`
- Resistance gene(s): PfDHFR
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
