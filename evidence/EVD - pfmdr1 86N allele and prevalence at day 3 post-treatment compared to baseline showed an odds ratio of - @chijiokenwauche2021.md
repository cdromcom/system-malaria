---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr1 86N allele and prevalence at day 3 post-treatment compared to baseline showed an odds ratio of 8.77 - @chijiokenwauche2021"
tags:
  - "marker/pfmdr1"
  - "theme/parasite-clearance"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: 50728b63-213c-4fae-9d12-22358334c88a
title: pfmdr1 86N allele and prevalence at day 3 post-treatment compared to baseline showed an odds ratio of 8.77 - @chijiokenwauche2021
---

## Source

[[@chijiokenwauche2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **pfmdr1 86N allele** and **prevalence at day 3 post-treatment compared to baseline (among the HIV-positive and HIV-negative participants)**.
> Pfmdr1 86N allele and prevalence at day 3 post-treatment compared to baseline showed an odds ratio of 8.77, p = 0.001. The confidence interval runs from 1.21 to 380.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **8.77** |
| **p-value** | = 0.001 |
| **Confidence interval** | CI 1.21 to 380 (confidence level not recorded) |
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
| **Population** | HIV-positive adults attending a university hospital HIV clinic and HIV-negative adult volunteers from the university hospital community with a positive blood film. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `pfmdr1 86N allele` with `prevalence at day 3 post-treatment compared to baseline (among the HIV-positive and HIV-negative participants)` and reports a odds ratio of 8.77. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfmdr1 86N allele`
> Variable 2: `prevalence at day 3 post-treatment compared to baseline (among the HIV-positive and HIV-negative participants)`
> odds ratio = 8.77, p = 0.001
> CI [1.21, 380]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfmdr1 86N allele** to **prevalence at day 3 post-treatment compared to baseline (among the HIV-positive and HIV-negative participants)**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> HIV-positive adults attending a university hospital HIV clinic and HIV-negative adult volunteers from the university hospital community with a positive blood film.

## Provenance

- Source study: [[@chijiokenwauche2021]]
- Paper: Antimalarial drug resistance markers in human immunodeficiency virus (HIV)-positive and HIV-negative adults with asymptomatic malaria infections in Port Harcourt, Nigeria.
- Journal: Transactions of the Royal Society of Tropical Medicine and Hygiene
- Published: 2021 May 8
- PubMed: [33823558](https://pubmed.ncbi.nlm.nih.gov/33823558/)
- System association ID: `E0KQU_tOpl`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how fast malaria parasites cleared from the blood, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
