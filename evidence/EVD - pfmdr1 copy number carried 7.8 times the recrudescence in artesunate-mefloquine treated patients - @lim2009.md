---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr1 copy number carried 7.8 times the recrudescence in artesunate-mefloquine treated patients (hazard ratio) - @lim2009"
tags:
  - "marker/pfmdr1"
  - "theme/treatment-failure"
  - "stat/hazard_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2009"
created: 2026-11-14
updated: 2026-11-14
nodeID: e0939b5d-9254-43a2-8053-58bcbe2a8bfe
title: pfmdr1 copy number carried 7.8 times the recrudescence in artesunate-mefloquine treated patients (hazard ratio) - @lim2009
---

## Source

[[@lim2009]]

## In plain terms

> [!info] What this finding says
> A study published in 2009 reported a statistical link between **pfmdr1 copy number** and **recrudescence in artesunate-mefloquine treated patients**.
> Pfmdr1 copy number carried 7.8 times the recrudescence in artesunate-mefloquine treated patients (hazard ratio), p = 0.002. The confidence interval runs from 2.09 to 29.1.

## Statistic

| | |
|---|---|
| **Metric** | `hazard_ratio` (System's normalised type; the paper reported `hazard_ratio`) |
| **Estimate** | **7.8** |
| **p-value** | = 0.002 |
| **Confidence interval** | CI 2.09 to 29.1 (confidence level not recorded) |
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
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 135 patients treated with artemether-lumefantrine and 140 patients treated with artesunate-mefloquine in Cambodia. |
| **Intervention / exposure** | pfmdr1 copy number |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | recrudescence in artesunate-mefloquine treated patients |
| **Setting** | Cambodia |
| **Timeframe** | Published 2009. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **recrudescence** — the original infection returning after treatment, as opposed to a fresh mosquito bite

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfmdr1 copy number`
> Variable 2: `recrudescence in artesunate-mefloquine treated patients`
> hazard ratio = 7.8, p = 0.002
> CI [2.09, 29.1]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfmdr1 copy number** to **recrudescence in artesunate-mefloquine treated patients**, reported as a hazard ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 135 patients treated with artemether-lumefantrine and 140 patients treated with artesunate-mefloquine in Cambodia.

## Provenance

- Source study: [[@lim2009]]
- Paper: Pfmdr1 copy number and arteminisin derivatives combination therapy failure in falciparum malaria in Cambodia.
- Journal: Malaria journal
- Published: 2009 Jan 12
- PubMed: [19138391](https://pubmed.ncbi.nlm.nih.gov/19138391/)
- System association ID: `x3-qekGwDc`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
