---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of dhfr dhps quintuple mutant differed by 20 between 2007 samples from Asembo, Gem, and Karemo and 2001 samples from Asembo (mean difference unstandardized) - @shah2015"
tags:
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: e02f13e4-ec36-46a9-97dd-ab9c8654483d
title: prevalence of dhfr dhps quintuple mutant differed by 20 between 2007 samples from Asembo, Gem, and Karemo and 2001 samples from Asembo (mean difference unstandardized) - @shah2015
---

## Source

[[@shah2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **2007 samples from Asembo, Gem, and Karemo** and **prevalence of dhfr/dhps quintuple mutant**.
> Prevalence of dhfr dhps quintuple mutant differed by 20 between 2007 samples from Asembo, Gem, and Karemo and 2001 samples from Asembo (mean difference unstandardized), p = 0.03.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **20** |
| **p-value** | = 0.03 |
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
| **Population** | 253 children in western Kenya in 2007. |
| **Intervention / exposure** | 2007 samples from Asembo, Gem, and Karemo |
| **Comparator** | 2001 samples from Asembo |
| **Outcome** | prevalence of dhfr/dhps quintuple mutant |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `2007 samples from Asembo, Gem, and Karemo [vs 2001 samples from Asembo]`
> Variable 2: `prevalence of dhfr/dhps quintuple mutant`
> mean difference unstandardized = 20, p = 0.03
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **2007 samples from Asembo, Gem, and Karemo** to **prevalence of dhfr/dhps quintuple mutant**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 253 children in western Kenya in 2007.

## Provenance

- Source study: [[@shah2015]]
- Paper: Assessment of molecular markers for anti-malarial drug resistance after the introduction and scale-up of malaria control interventions in western Kenya.
- Journal: Malaria journal
- Published: 2015 Feb 14
- PubMed: [25889220](https://pubmed.ncbi.nlm.nih.gov/25889220/)
- System association ID: `Id34AYaZpE`
- Resistance gene(s): PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
