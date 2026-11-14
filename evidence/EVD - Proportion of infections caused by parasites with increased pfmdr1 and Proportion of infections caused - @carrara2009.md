---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Proportion of infections caused by parasites with increased pfmdr1 and Proportion of infections caused by parasites with increased pfmdr1 showed a mean difference unstandardized of -23 - @carrara2009"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2009"
created: 2026-11-14
updated: 2026-11-14
nodeID: 44ad22eb-5ae2-49ae-a309-8a1aba272807
title: Proportion of infections caused by parasites with increased pfmdr1 and Proportion of infections caused by parasites with increased pfmdr1 showed a mean difference unstandardized of -23 - @carrara2009
---

## Source

[[@carrara2009]]

## In plain terms

> [!info] What this finding says
> A study published in 2009 reported a statistical link between **Proportion of infections caused by parasites with increased pfmdr1 copy number in 1996 (30.0) vs. Proportion of infections caused by parasites with increased pfmdr1 copy number in 2006 (53.0)** and **Proportion of infections caused by parasites with increased pfmdr1 copy number**.
> Proportion of infections caused by parasites with increased pfmdr1 and Proportion of infections caused by parasites with increased pfmdr1 showed a mean difference unstandardized of -23, p = 0.012.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-23** |
| **p-value** | = 0.012 |
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
| **Open data** | A statement exists but is not explicit |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 3,264 patients enrolled in prospective treatment trials between 1995 and 2007 and treated with MAS(3) along the Thai-Myanmar border. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2009. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Proportion of infections caused by parasites with increased pfmdr1 copy number in 1996 (30.0) vs. Proportion of infections caused by parasites with increased pfmdr1 copy number in 2006 (53.0)` with `Proportion of infections caused by parasites with increased pfmdr1 copy number` and reports a mean difference unstandardized of -23. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Proportion of infections caused by parasites with increased pfmdr1 copy number in 1996 (30.0) vs. Proportion of infections caused by parasites with increased pfmdr1 copy number in 2006 (53.0)`
> Variable 2: `Proportion of infections caused by parasites with increased pfmdr1 copy number`
> mean difference unstandardized = -23, p = 0.012
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **Proportion of infections caused by parasites with increased pfmdr1 copy number in 1996 (30.0) vs. Proportion of infections caused by parasites with increased pfmdr1 copy number in 2006 (53.0)** to **Proportion of infections caused by parasites with increased pfmdr1 copy number**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 3,264 patients enrolled in prospective treatment trials between 1995 and 2007 and treated with MAS(3) along the Thai-Myanmar border.

## Provenance

- Source study: [[@carrara2009]]
- Paper: Changes in the treatment responses to artesunate-mefloquine on the northwestern border of Thailand during 13 years of continuous deployment.
- Journal: PloS one
- Published: 2009
- PubMed: [19234601](https://pubmed.ncbi.nlm.nih.gov/19234601/)
- System association ID: `WyN2L9WXwq`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
