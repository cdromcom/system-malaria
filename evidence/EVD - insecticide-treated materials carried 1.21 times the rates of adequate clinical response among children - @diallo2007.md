---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - insecticide-treated materials carried 1.21 times the rates of adequate clinical response among children carrying (odds ratio) - @diallo2007"
tags:
  - "marker/pfcrt"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2007"
created: 2026-11-14
updated: 2026-11-14
nodeID: 153c2974-d1bd-4c2d-9e53-2e22ebe965fa
title: insecticide-treated materials carried 1.21 times the rates of adequate clinical response among children carrying (odds ratio) - @diallo2007
---

## Source

[[@diallo2007]]

## In plain terms

> [!info] What this finding says
> A study published in 2007 reported a statistical link between **insecticide-treated materials** and **rates of adequate clinical response among children carrying parasites with the pfcrt-76T allele**.
> Insecticide-treated materials carried 1.21 times the rates of adequate clinical response among children carrying (odds ratio), p = 0.58. The confidence interval runs from 0.61 to 2.39.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **1.21** |
| **p-value** | = 0.58 |
| **Confidence interval** | CI 0.61 to 2.39 (confidence level not recorded) |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 1035 children aged 6-59 months with falciparum malaria living in villages in which insecticide-treated curtains (ITCs) had been used for 6-8 years and in unprotected villages. |
| **Intervention / exposure** | insecticide-treated materials |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | rates of adequate clinical response among children carrying parasites with the pfcrt-76T allele |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2007. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `insecticide-treated materials`
> Variable 2: `rates of adequate clinical response among children carrying parasites with the pfcrt-76T allele`
> odds ratio = 1.21, p = 0.58
> CI [0.61, 2.39]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **insecticide-treated materials** to **rates of adequate clinical response among children carrying parasites with the pfcrt-76T allele**, reported as a odds ratio.

### How?

Study design: Experimental Trial.

### Who?

> 1035 children aged 6-59 months with falciparum malaria living in villages in which insecticide-treated curtains (ITCs) had been used for 6-8 years and in unprotected villages.

## Provenance

- Source study: [[@diallo2007]]
- Paper: Children in Burkina Faso who are protected by insecticide-treated materials are able to clear drug-resistant parasites better than unprotected children.
- Journal: The Journal of infectious diseases
- Published: 2007 Jul 1
- PubMed: [17538894](https://pubmed.ncbi.nlm.nih.gov/17538894/)
- System association ID: `AB2e-yOAA6`
- Resistance gene(s): PfCRT
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
