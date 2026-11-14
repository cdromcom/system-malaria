---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Presence of K540 E in dihydropteroate synthase (DHPS) and Patent infection in placental blood showed a prevalence ratio of 3.28 - @gutman2015"
tags:
  - "marker/pfdhps"
  - "theme/other"
  - "stat/prevalence_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: ddafdb78-a81d-47e1-82f1-d1d5241050c2
title: Presence of K540 E in dihydropteroate synthase (DHPS) and Patent infection in placental blood showed a prevalence ratio of 3.28 - @gutman2015
---

## Source

[[@gutman2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **Presence of K540 E: in dihydropteroate synthase (DHPS)** and **Patent infection in placental blood**.
> Presence of K540 E in dihydropteroate synthase (DHPS) and Patent infection in placental blood showed a prevalence ratio of 3.28. The confidence interval runs from 1.88 to 5.78.

## Statistic

| | |
|---|---|
| **Metric** | `prevalence_ratio` (System's normalised type; the paper reported `prevalence_ratio`) |
| **Estimate** | **3.28** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 1.88 to 5.78 (confidence level not recorded) |
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
| **Critical social posts** | None recorded — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Yes (hybrid) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 1809 pregnant women without HIV infection in Malawi between 2009 and 2011. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Presence of K540 E: in dihydropteroate synthase` with `Patent infection in placental blood` and reports a prevalence ratio of 3.28. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Presence of K540 E: in dihydropteroate synthase`
> Variable 2: `Patent infection in placental blood`
> prevalence ratio = 3.28
> CI [1.88, 5.78]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Presence of K540 E: in dihydropteroate synthase (DHPS)** to **Patent infection in placental blood**, reported as a prevalence ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 1809 pregnant women without HIV infection in Malawi between 2009 and 2011.

## Provenance

- Source study: [[@gutman2015]]
- Paper: The A581G Mutation in the Gene Encoding Plasmodium falciparum Dihydropteroate Synthetase Reduces the Effectiveness of Sulfadoxine-Pyrimethamine Preventive Therapy in Malawian Pregnant Women.
- Journal: The Journal of infectious diseases
- Published: 2015 Jun 15
- PubMed: [25564249](https://pubmed.ncbi.nlm.nih.gov/25564249/)
- System association ID: `AeI-laBxXr`
- Resistance gene(s): PfDHPS
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
