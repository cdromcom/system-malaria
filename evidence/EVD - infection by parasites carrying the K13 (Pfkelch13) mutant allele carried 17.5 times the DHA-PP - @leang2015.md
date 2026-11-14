---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - infection by parasites carrying the K13 (Pfkelch13) mutant allele carried 17.5 times the DHA-PP treatment failure (odds ratio) - @leang2015"
tags:
  - "marker/pfkelch13"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: b3772eaf-7fff-4698-8b93-e7cbe482614e
title: infection by parasites carrying the K13 (Pfkelch13) mutant allele carried 17.5 times the DHA-PP treatment failure (odds ratio) - @leang2015
---

## Source

[[@leang2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **infection by parasites carrying the K13 (Pfkelch13) mutant allele** and **DHA-PP treatment failure**.
> Infection by parasites carrying the K13 (Pfkelch13) mutant allele carried 17.5 times the DHA-PP treatment failure (odds ratio). The confidence interval runs from 1 to 308.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **17.5** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 1 to 308 (confidence level not recorded) |
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
| **Critical social posts** | 1 negative X/Twitter, 0 Bluesky — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 425 patients recruited in western and eastern Cambodia from 2011 to 2013. |
| **Intervention / exposure** | infection by parasites carrying the K13 mutant allele |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | DHA-PP treatment failure |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2015. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `infection by parasites carrying the K13 mutant allele`
> Variable 2: `DHA-PP treatment failure`
> odds ratio = 17.5
> CI [1, 308]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **infection by parasites carrying the K13 (Pfkelch13) mutant allele** to **DHA-PP treatment failure**, reported as a odds ratio.

### How?

Study design: Experimental Trial.

### Who?

> 425 patients recruited in western and eastern Cambodia from 2011 to 2013.

## Provenance

- Source study: [[@leang2015]]
- Paper: Evidence of Plasmodium falciparum Malaria Multidrug Resistance to Artemisinin and Piperaquine in Western Cambodia: Dihydroartemisinin-Piperaquine Open-Label Multicenter Clinical Assessment.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2015 Aug
- PubMed: [26014949](https://pubmed.ncbi.nlm.nih.gov/26014949/)
- System association ID: `BxZPjVnuS0`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
