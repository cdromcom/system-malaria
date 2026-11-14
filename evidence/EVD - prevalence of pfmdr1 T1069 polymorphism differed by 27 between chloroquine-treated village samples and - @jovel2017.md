---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of pfmdr1 T1069 polymorphism differed by 27 between chloroquine-treated village samples and other samples (mean difference unstandardized) - @jovel2017"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2017"
created: 2026-11-14
updated: 2026-11-14
nodeID: 8c1d7ee3-6d1d-4d05-9e14-ee0a5884149f
title: prevalence of pfmdr1 T1069 polymorphism differed by 27 between chloroquine-treated village samples and other samples (mean difference unstandardized) - @jovel2017
---

## Source

[[@jovel2017]]

## In plain terms

> [!info] What this finding says
> A study published in 2017 reported a statistical link between **chloroquine-treated village samples** and **prevalence of pfmdr1 T1069 polymorphism**.
> Prevalence of pfmdr1 T1069 polymorphism differed by 27 between chloroquine-treated village samples and other samples (mean difference unstandardized), p = 0.008.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **27** |
| **p-value** | = 0.008 |
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
| **Open data** | Available from the authors on request only — GenBank |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 191 children in four Liberian villages, 1976-78. |
| **Intervention / exposure** | chloroquine-treated village samples |
| **Comparator** | other samples |
| **Outcome** | prevalence of pfmdr1 T1069 polymorphism |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2017. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `chloroquine-treated village samples [vs other samples]`
> Variable 2: `prevalence of pfmdr1 T1069 polymorphism`
> mean difference unstandardized = 27, p = 0.008
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **chloroquine-treated village samples** to **prevalence of pfmdr1 T1069 polymorphism**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 191 children in four Liberian villages, 1976-78.

## Provenance

- Source study: [[@jovel2017]]
- Paper: Unexpected selections of Plasmodium falciparum polymorphisms in previously treatment-naïve areas after monthly presumptive administration of three different anti-malarial drugs in Liberia 1976-78.
- Journal: Malaria journal
- Published: 2017 Mar 13
- PubMed: [28288632](https://pubmed.ncbi.nlm.nih.gov/28288632/)
- System association ID: `PsAna1tmq_`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
