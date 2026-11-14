---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr1 86+184 NF frequency differed by 27 between 2003 (change in treatment regimen) and Pre-2007 (no change in treatment regimen (mean difference unstandardized) - @jovel2015"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: 909de3cf-1d94-4353-9809-4e3e06a4a8a7
title: pfmdr1 86+184 NF frequency differed by 27 between 2003 (change in treatment regimen) and Pre-2007 (no change in treatment regimen (mean difference unstandardized) - @jovel2015
---

## Source

[[@jovel2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **2003 (change in treatment regimen)** and **pfmdr1 86+184 NF frequency**.
> Pfmdr1 86+184 NF frequency differed by 27 between 2003 (change in treatment regimen) and Pre-2007 (no change in treatment regimen (mean difference unstandardized), p = 0.004.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **27** |
| **p-value** | = 0.004 |
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
| **Open access** | Yes (bronze) |
| **Open data** | Cannot tell — PMC holds front matter only — ClinicalTrials.gov |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 1,806 children under 15 years of age with uncomplicated Plasmodium falciparum monoinfection in suburban Bissau from 2003 to 2012. |
| **Intervention / exposure** | 2003 (change in treatment regimen) |
| **Comparator** | Pre-2007 (no change in treatment regimen |
| **Outcome** | pfmdr1 86+184 NF frequency |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2015. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `2003 (change in treatment regimen) [vs Pre-2007 (no change in treatment regimen)]`
> Variable 2: `pfmdr1 86+184 NF frequency`
> mean difference unstandardized = 27, p = 0.004
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **2003 (change in treatment regimen)** to **pfmdr1 86+184 NF frequency**, reported as a mean difference unstandardized.

### How?

Study design: Experimental Trial.

### Who?

> 1,806 children under 15 years of age with uncomplicated Plasmodium falciparum monoinfection in suburban Bissau from 2003 to 2012.

## Provenance

- Source study: [[@jovel2015]]
- Paper: Temporal and seasonal changes of genetic polymorphisms associated with altered drug susceptibility to chloroquine, lumefantrine, and quinine in Guinea-Bissau between 2003 and 2012.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2015 Feb
- PubMed: [25421474](https://pubmed.ncbi.nlm.nih.gov/25421474/)
- System association ID: `gYuUviWERD`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
