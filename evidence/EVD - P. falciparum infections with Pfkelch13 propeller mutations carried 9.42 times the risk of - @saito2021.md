---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - P. falciparum infections with Pfkelch13 propeller mutations carried 9.42 times the risk of recrudescence (relative risk ratio) - @saito2021"
tags:
  - "marker/pfkelch13"
  - "theme/treatment-failure"
  - "stat/relative_risk_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: 62ebba00-b6e0-4ce1-b6fd-225e408e2ac8
title: P. falciparum infections with Pfkelch13 propeller mutations carried 9.42 times the risk of recrudescence (relative risk ratio) - @saito2021
---

## Source

[[@saito2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **P. falciparum infections with Pfkelch13 propeller mutations** and **risk of recrudescence**.
> P. falciparum infections with Pfkelch13 propeller mutations carried 9.42 times the risk of recrudescence (relative risk ratio). The confidence interval runs from 1.3 to 68.3.

## Statistic

| | |
|---|---|
| **Metric** | `relative_risk_ratio` (System's normalised type; the paper reported `relative_risk_ratio`) |
| **Estimate** | **9.42** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 1.3 to 68.3 (confidence level not recorded) |
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
| **Open access** | Yes (gold) |
| **Open data** | Available from the authors on request only — ClinicalTrials.gov |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Pregnant women with uncomplicated malaria on the Thailand-Myanmar border. |
| **Intervention / exposure** | P. falciparum infections with Pfkelch13 propeller mutations |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | risk of recrudescence |
| **Setting** | Thailand-Myanmar border |
| **Timeframe** | Experimental Trial, published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **recrudescence** — the original infection returning after treatment, as opposed to a fresh mosquito bite

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `P. falciparum infections with Pfkelch13 propeller mutations`
> Variable 2: `risk of recrudescence`
> relative risk ratio = 9.42
> CI [1.3, 68.3]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **P. falciparum infections with Pfkelch13 propeller mutations** to **risk of recrudescence**, reported as a relative risk ratio.

### How?

Study design: Experimental Trial.

### Who?

> Pregnant women with uncomplicated malaria on the Thailand-Myanmar border.

## Provenance

- Source study: [[@saito2021]]
- Paper: A randomized controlled trial of dihydroartemisinin-piperaquine, artesunate-mefloquine and extended artemether-lumefantrine treatments for malaria in pregnancy on the Thailand-Myanmar border.
- Journal: BMC medicine
- Published: 2021 Jun 10
- PubMed: [34107963](https://pubmed.ncbi.nlm.nih.gov/34107963/)
- System association ID: `F9jA7aoM7m`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
