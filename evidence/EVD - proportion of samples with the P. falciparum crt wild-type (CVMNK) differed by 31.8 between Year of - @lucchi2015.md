---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - proportion of samples with the P. falciparum crt wild-type (CVMNK) differed by 31.8 between Year of Study (2013) and Year of Study (2010 (mean difference unstandardized) - @lucchi2015"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: 3fff8021-38ee-4758-bcef-130dbf96f75c
title: proportion of samples with the P. falciparum crt wild-type (CVMNK) differed by 31.8 between Year of Study (2013) and Year of Study (2010 (mean difference unstandardized) - @lucchi2015
---

## Source

[[@lucchi2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **Year of Study (2013)** and **proportion of samples with the P. falciparum crt wild-type (CVMNK) genotype**.
> Proportion of samples with the P. falciparum crt wild-type (CVMNK) differed by 31.8 between Year of Study (2013) and Year of Study (2010 (mean difference unstandardized), p = 0.0001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **31.8** |
| **p-value** | = 0.0001 |
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
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 203 Plasmodium falciparum malaria-positive children in western Kenya between 2010 and 2013. |
| **Intervention / exposure** | Year of Study (2013) |
| **Comparator** | Year of Study (2010 |
| **Outcome** | proportion of samples with the P. falciparum crt wild-type (CVMNK) genotype |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Year of Study (2013) [vs Year of Study (2010)]`
> Variable 2: `proportion of samples with the P. falciparum crt wild-type (CVMNK) genotype`
> mean difference unstandardized = 31.8, p = 0.0001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Year of Study (2013)** to **proportion of samples with the P. falciparum crt wild-type (CVMNK) genotype**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 203 Plasmodium falciparum malaria-positive children in western Kenya between 2010 and 2013.

## Provenance

- Source study: [[@lucchi2015]]
- Paper: In Vitro and Molecular Surveillance for Antimalarial Drug Resistance in Plasmodium falciparum Parasites in Western Kenya Reveals Sustained Artemisinin Sensitivity and Increased Chloroquine Sensitivity.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2015 Dec
- PubMed: [26392510](https://pubmed.ncbi.nlm.nih.gov/26392510/)
- System association ID: `h4cMm5Zg-k`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
