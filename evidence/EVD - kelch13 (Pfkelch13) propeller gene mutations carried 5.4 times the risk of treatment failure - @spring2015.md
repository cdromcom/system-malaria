---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - kelch13 (Pfkelch13) propeller gene mutations carried 5.4 times the risk of treatment failure (hazard ratio) - @spring2015"
tags:
  - "marker/pfkelch13"
  - "theme/treatment-failure"
  - "stat/hazard_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: 6d78072e-794f-42f2-9d23-aa0c7ffc4e0b
title: kelch13 (Pfkelch13) propeller gene mutations carried 5.4 times the risk of treatment failure (hazard ratio) - @spring2015
---

## Source

[[@spring2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **kelch13 (Pfkelch13) propeller gene mutations** and **risk of treatment failure (of dihydroartemisinin-piperaquine treatment)**.
> Kelch13 (Pfkelch13) propeller gene mutations carried 5.4 times the risk of treatment failure (hazard ratio), p = 0.0001. The confidence interval runs from 2.4 to 12.

## Statistic

| | |
|---|---|
| **Metric** | `hazard_ratio` (System's normalised type; the paper reported `hazard_ratio`) |
| **Estimate** | **5.4** |
| **p-value** | = 0.0001 |
| **Confidence interval** | CI 2.4 to 12 (confidence level not recorded) |
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
| **Formal published comments** | 1 indexed in PubMed |
| **Critical social posts** | None recorded — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Adults aged 18-65 years presenting to Anlong Veng District Hospital, Oddar Meanchey Province, Cambodia, with uncomplicated P falciparum or mixed P falciparum/Plasmodium vivax infection of between 1000 and 200,000 parasites per μL of blood. |
| **Intervention / exposure** | kelch13 propeller gene mutations |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | risk of treatment failure (of dihydroartemisinin-piperaquine treatment) |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **dihydroartemisinin-piperaquine** — an artemisinin combination treatment

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `kelch13 propeller gene mutations`
> Variable 2: `risk of treatment failure (of dihydroartemisinin-piperaquine treatment)`
> hazard ratio = 5.4, p = 0.0001
> CI [2.4, 12]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **kelch13 (Pfkelch13) propeller gene mutations** to **risk of treatment failure (of dihydroartemisinin-piperaquine treatment)**, reported as a hazard ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Adults aged 18-65 years presenting to Anlong Veng District Hospital, Oddar Meanchey Province, Cambodia, with uncomplicated P falciparum or mixed P falciparum/Plasmodium vivax infection of between 1000 and 200,000 parasites per μL of blood.

## Provenance

- Source study: [[@spring2015]]
- Paper: Dihydroartemisinin-piperaquine failure associated with a triple mutant including kelch13 C580Y in Cambodia: an observational cohort study.
- Journal: The Lancet. Infectious diseases
- Published: 2015 Jun
- PubMed: [25877962](https://pubmed.ncbi.nlm.nih.gov/25877962/)
- System association ID: `eHEYHTH6Ia`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
