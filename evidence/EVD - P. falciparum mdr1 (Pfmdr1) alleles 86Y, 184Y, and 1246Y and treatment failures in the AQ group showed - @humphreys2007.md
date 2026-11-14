---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - P. falciparum mdr1 (Pfmdr1) alleles 86Y, 184Y, and 1246Y and treatment failures in the AQ group showed an odds ratio of 33.2 - @humphreys2007"
tags:
  - "marker/pfmdr1"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2007"
created: 2026-11-14
updated: 2026-11-14
nodeID: 59015f7b-652a-4fb9-8ca5-77bbf0d4db5c
title: P. falciparum mdr1 (Pfmdr1) alleles 86Y, 184Y, and 1246Y and treatment failures in the AQ group showed an odds ratio of 33.2 - @humphreys2007
---

## Source

[[@humphreys2007]]

## In plain terms

> [!info] What this finding says
> A study published in 2007 reported a statistical link between **P. falciparum mdr1 (Pfmdr1) alleles 86Y, 184Y, and 1246Y** and **treatment failures in the AQ group**.
> P. falciparum mdr1 (Pfmdr1) alleles 86Y, 184Y, and 1246Y and treatment failures in the AQ group showed an odds ratio of 33.2, p = 0.001. The confidence interval runs from 4.17 to 1441.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **33.2** |
| **p-value** | = 0.001 |
| **Confidence interval** | CI 4.17 to 1441 (confidence level not recorded) |
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
| **Population** | 300 Tanzanian children presenting with uncomplicated falciparum malaria, who were enrolled in a clinical trial of antimalarial therapy. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2007. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `P. falciparum mdr1 alleles 86Y, 184Y, and 1246Y` with `treatment failures in the AQ group` and reports a odds ratio of 33.2. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `P. falciparum mdr1 alleles 86Y, 184Y, and 1246Y`
> Variable 2: `treatment failures in the AQ group`
> odds ratio = 33.2, p = 0.001
> CI [4.17, 1441]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **P. falciparum mdr1 (Pfmdr1) alleles 86Y, 184Y, and 1246Y** to **treatment failures in the AQ group**, reported as a odds ratio.

### How?

Study design: Experimental Trial.

### Who?

> 300 Tanzanian children presenting with uncomplicated falciparum malaria, who were enrolled in a clinical trial of antimalarial therapy.

## Provenance

- Source study: [[@humphreys2007]]
- Paper: Amodiaquine and artemether-lumefantrine select distinct alleles of the Plasmodium falciparum mdr1 gene in Tanzanian children treated for uncomplicated malaria.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2007 Mar
- PubMed: [17194834](https://pubmed.ncbi.nlm.nih.gov/17194834/)
- System association ID: `-9R6QPMGh1`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
