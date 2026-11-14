---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Frequency of Pfdhps double mutation in 2005 and Pfdhps double mutation showed a mean difference unstandardized of 13.8 - @tessema2015"
tags:
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: 8737c31b-01c2-49f4-80a3-28e66b82c2b8
title: Frequency of Pfdhps double mutation in 2005 and Pfdhps double mutation showed a mean difference unstandardized of 13.8 - @tessema2015
---

## Source

[[@tessema2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **Frequency of Pfdhps double mutation in 2005 (Pawe hospital, North Western Ethiopia) vs. Frequency of Pfdhps double mutation in 2007/08 (Pawe hospital, North Western Ethiopia)** and **Pfdhps double mutation**.
> Frequency of Pfdhps double mutation in 2005 and Pfdhps double mutation showed a mean difference unstandardized of 13.8, p = 0.08.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **13.8** |
| **p-value** | = 0.08 |
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
| **Open access** | Yes (gold) |
| **Open data** | A statement exists but is not explicit |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 159 isolates collected from Pawe hospital in North Western Ethiopia in 2005 and 2007/08. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Frequency of Pfdhps double mutation in 2005 (Pawe hospital, North Western Ethiopia) vs. Frequency of Pfdhps double mutation in 2007/08 (Pawe hospital, North Western Ethiopia)` with `Pfdhps double mutation` and reports a mean difference unstandardized of 13.8. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Frequency of Pfdhps double mutation in 2005 (Pawe hospital, North Western Ethiopia) vs. Frequency of Pfdhps double mutation in 2007/08 (Pawe hospital, North Western Ethiopia)`
> Variable 2: `Pfdhps double mutation`
> mean difference unstandardized = 13.8, p = 0.08
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Frequency of Pfdhps double mutation in 2005 (Pawe hospital, North Western Ethiopia) vs. Frequency of Pfdhps double mutation in 2007/08 (Pawe hospital, North Western Ethiopia)** to **Pfdhps double mutation**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 159 isolates collected from Pawe hospital in North Western Ethiopia in 2005 and 2007/08.

## Provenance

- Source study: [[@tessema2015]]
- Paper: Declining trend of Plasmodium falciparum dihydrofolate reductase (dhfr) and dihydropteroate synthase (dhps) mutant alleles after the withdrawal of Sulfadoxine-Pyrimethamine in North Western Ethiopia.
- Journal: PloS one
- Published: 2015
- PubMed: [26431464](https://pubmed.ncbi.nlm.nih.gov/26431464/)
- System association ID: `Zh360F19Yv`
- Resistance gene(s): PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
