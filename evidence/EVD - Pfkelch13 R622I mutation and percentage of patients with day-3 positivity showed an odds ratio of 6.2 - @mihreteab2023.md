---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Pfkelch13 R622I mutation and percentage of patients with day-3 positivity showed an odds ratio of 6.2 - @mihreteab2023"
tags:
  - "marker/pfkelch13"
  - "theme/parasite-clearance"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2023"
created: 2026-11-14
updated: 2026-11-14
nodeID: 3012ac74-dffb-4d83-b22e-cc2b98733bd2
title: Pfkelch13 R622I mutation and percentage of patients with day-3 positivity showed an odds ratio of 6.2 - @mihreteab2023
---

## Source

[[@mihreteab2023]]

## In plain terms

> [!info] What this finding says
> A study published in 2023 reported a statistical link between **Pfkelch13 R622I mutation** and **percentage of patients with day-3 positivity**.
> Pfkelch13 R622I mutation and percentage of patients with day-3 positivity showed an odds ratio of 6.2. The confidence interval runs from 2.5 to 15.5.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **6.2** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 2.5 to 15.5 (confidence level not recorded) |
| **Direction vs null of 1** | **positive** |
| **Data source** | API list, API detail |
| **In curated release** | No |
| **Source paper integrity** | formal published comments exist (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: Clean) |
| **Published erratum** | None found |
| **Formal published comments** | 2 indexed in PubMed |
| **Critical social posts** | 74 negative X/Twitter, 0 Bluesky — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Yes (green) |
| **Open data** | A statement exists but is not explicit — MalariaGEN |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Adults and those younger than 15 years of age infected with Plasmodium falciparum in Eritrea between 2016 and 2019. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2023. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Pfkelch13 R622I mutation` with `percentage of patients with day-3 positivity` and reports a odds ratio of 6.2. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **R622I** — a mutation that swaps amino acid R for I at position 622 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pfkelch13 R622I mutation`
> Variable 2: `percentage of patients with day-3 positivity`
> odds ratio = 6.2
> CI [2.5, 15.5]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Pfkelch13 R622I mutation** to **percentage of patients with day-3 positivity**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Adults and those younger than 15 years of age infected with Plasmodium falciparum in Eritrea between 2016 and 2019.

## Provenance

- Source study: [[@mihreteab2023]]
- Paper: Increasing Prevalence of Artemisinin-Resistant HRP2-Negative Malaria in Eritrea.
- Journal: The New England journal of medicine
- Published: 2023 Sep 28
- PubMed: [37754284](https://pubmed.ncbi.nlm.nih.gov/37754284/)
- System association ID: `WqvCfvctC4`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): how fast malaria parasites cleared from the blood

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
