---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfdhps mutations carried 2.1 times the efficacy of chlorproguanil-dapsone plus artesunate (CPG-DDS+A) (odds ratio) - @karema2010"
tags:
  - "marker/pfdhps"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2010"
created: 2026-11-14
updated: 2026-11-14
nodeID: 87904c57-0f27-48e8-b523-474b2bfb2c69
title: pfdhps mutations carried 2.1 times the efficacy of chlorproguanil-dapsone plus artesunate (CPG-DDS+A) (odds ratio) - @karema2010
---

## Source

[[@karema2010]]

## In plain terms

> [!info] What this finding says
> A study published in 2010 reported a statistical link between **pfdhps mutations** and **efficacy of chlorproguanil-dapsone plus artesunate (CPG-DDS+A)**.
> Pfdhps mutations carried 2.1 times the efficacy of chlorproguanil-dapsone plus artesunate (CPG-DDS+A) (odds ratio), p = 0.008. The confidence interval runs from 1.21 to 3.54.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **2.1** |
| **p-value** | = 0.008 |
| **Confidence interval** | CI 1.21 to 3.54 (confidence level not recorded) |
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
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Children with uncomplicated malaria caused by Plasmodium falciparum parasites in two areas of Rwanda. |
| **Intervention / exposure** | pfdhps mutations |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | efficacy of chlorproguanil-dapsone plus artesunate (CPG-DDS+A) |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2010. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfdhps mutations`
> Variable 2: `efficacy of chlorproguanil-dapsone plus artesunate (CPG-DDS+A)`
> odds ratio = 2.1, p = 0.008
> CI [1.21, 3.54]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfdhps mutations** to **efficacy of chlorproguanil-dapsone plus artesunate (CPG-DDS+A)**, reported as a odds ratio.

### How?

Study design: Experimental Trial.

### Who?

> Children with uncomplicated malaria caused by Plasmodium falciparum parasites in two areas of Rwanda.

## Provenance

- Source study: [[@karema2010]]
- Paper: Molecular correlates of high-level antifolate resistance in Rwandan children with Plasmodium falciparum malaria.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2010 Jan
- PubMed: [19841150](https://pubmed.ncbi.nlm.nih.gov/19841150/)
- System association ID: `xuL1x4ORrj`
- Resistance gene(s): PfDHPS
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
