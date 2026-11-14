---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - artemisinin-resistant K13 (Pfkelch13) mutants carried 32 times the risk of recrudescence (relative risk ratio) - @duru2015"
tags:
  - "marker/pfkelch13"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/relative_risk_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: 16b50d5f-3173-4395-8dda-903bade8b294
title: artemisinin-resistant K13 (Pfkelch13) mutants carried 32 times the risk of recrudescence (relative risk ratio) - @duru2015
---

## Source

[[@duru2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **artemisinin-resistant K13 (Pfkelch13) mutants** and **risk of recrudescence**.
> Artemisinin-resistant K13 (Pfkelch13) mutants carried 32 times the risk of recrudescence (relative risk ratio), p = 0.0005. The confidence interval runs from 4.5 to 224.

## Statistic

| | |
|---|---|
| **Metric** | `relative_risk_ratio` (System's normalised type; the paper reported `relative_risk_ratio`) |
| **Estimate** | **32** |
| **p-value** | = 0.0005 |
| **Confidence interval** | CI 4.5 to 224 (confidence level not recorded) |
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
| **Open data** | A statement exists but is not explicit — WWARN |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 32 culture-adapted, C580Y-K13 mutant parasites collected at enrolment from patients treated with a 3-day course of dihydroartemisinin-piperaquine and having presented or not with a recrudescence at day 42, as well as isolates collected from patients enrolled in an open-label study with dihydroartemisinin-piperaquine for uncomplicated P. falciparum malaria in Cambodia. |
| **Intervention / exposure** | artemisinin-resistant K13 mutants |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | risk of recrudescence |
| **Setting** | Cambodia |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **recrudescence** — the original infection returning after treatment, as opposed to a fresh mosquito bite

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `artemisinin-resistant K13 mutants`
> Variable 2: `risk of recrudescence`
> relative risk ratio = 32, p = 0.0005
> CI [4.5, 224]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **artemisinin-resistant K13 (Pfkelch13) mutants** to **risk of recrudescence**, reported as a relative risk ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 32 culture-adapted, C580Y-K13 mutant parasites collected at enrolment from patients treated with a 3-day course of dihydroartemisinin-piperaquine and having presented or not with a recrudescence at day 42, as well as isolates collected from patients enrolled in an open-label study with dihydroartemisinin-piperaquine for uncomplicated P. falciparum malaria in Cambodia.

## Provenance

- Source study: [[@duru2015]]
- Paper: Plasmodium falciparum dihydroartemisinin-piperaquine failures in Cambodia are associated with mutant K13 parasites presenting high survival rates in novel piperaquine in vitro assays: retrospective and prospective investigations.
- Journal: BMC medicine
- Published: 2015 Dec 22
- PubMed: [26695060](https://pubmed.ncbi.nlm.nih.gov/26695060/)
- System association ID: `52WQ7_30Nu`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
