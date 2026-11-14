---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - duration of artemisinin combination therapy and mutations in Plasmodium falciparum (Pfcrt) showed a pearson r of 0.78 - @buppan2018"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/pearson_r"
  - "direction/positive"
  - "verification/api-only"
  - "year/2018"
created: 2026-11-14
updated: 2026-11-14
nodeID: fbc73e36-2408-48eb-a99d-0cfb1d6bd50d
title: duration of artemisinin combination therapy and mutations in Plasmodium falciparum (Pfcrt) showed a pearson r of 0.78 - @buppan2018
---

## Source

[[@buppan2018]]

## In plain terms

> [!info] What this finding says
> A study published in 2018 reported a statistical link between **duration of artemisinin combination therapy** and **mutations in Plasmodium falciparum (Pfcrt)**.
> Duration of artemisinin combination therapy and mutations in Plasmodium falciparum (Pfcrt) showed a pearson r of 0.78, p = 0.038.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0.78** |
| **p-value** | = 0.038 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **positive** |
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
| **Population** | 189 Plasmodium falciparum isolates collected in Thailand during 1991 and 2016. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2018. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `duration of artemisinin combination therapy` with `mutations in Plasmodium falciparum (Pfcrt)` and reports a pearson r of 0.78. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `duration of artemisinin combination therapy`
> Variable 2: `mutations in Plasmodium falciparum (Pfcrt)`
> pearson r = 0.78, p = 0.038
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **duration of artemisinin combination therapy** to **mutations in Plasmodium falciparum (Pfcrt)**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 189 Plasmodium falciparum isolates collected in Thailand during 1991 and 2016.

## Provenance

- Source study: [[@buppan2018]]
- Paper: Multiple Novel Mutations in Plasmodium falciparum Chloroquine Resistance Transporter Gene during Implementation of Artemisinin Combination Therapy in Thailand.
- Journal: The American journal of tropical medicine and hygiene
- Published: 2018 Oct
- PubMed: [30141388](https://pubmed.ncbi.nlm.nih.gov/30141388/)
- System association ID: `hWO8XOfvoh`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
