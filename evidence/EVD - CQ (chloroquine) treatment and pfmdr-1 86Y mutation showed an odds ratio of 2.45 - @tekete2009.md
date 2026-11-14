---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - CQ (chloroquine) treatment and pfmdr-1 86Y mutation showed an odds ratio of 2.45 - @tekete2009"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2009"
created: 2026-11-14
updated: 2026-11-14
nodeID: c91c9c47-286e-46cd-baec-e069b8ce5409
title: CQ (chloroquine) treatment and pfmdr-1 86Y mutation showed an odds ratio of 2.45 - @tekete2009
---

## Source

[[@tekete2009]]

## In plain terms

> [!info] What this finding says
> A study published in 2009 reported a statistical link between **CQ (chloroquine) treatment** and **pfmdr-1 86Y mutation**.
> CQ (chloroquine) treatment and pfmdr-1 86Y mutation showed an odds ratio of 2.45, p = 0.14. The confidence interval runs from 0.59 to 10.8.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **2.45** |
| **p-value** | = 0.14 |
| **Confidence interval** | CI 0.59 to 10.8 (confidence level not recorded) |
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
| **Population** | Children between six and 59 months of age with uncomplicated malaria in Kolle, Mali, during the malaria transmission seasons of 2002 and 2003. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Kolle |
| **Timeframe** | Experimental Trial, published 2009. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `CQ treatment` with `pfmdr-1 86Y mutation` and reports a odds ratio of 2.45. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **chloroquine** — a cheap older antimalarial, now largely defeated by resistance

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `CQ treatment`
> Variable 2: `pfmdr-1 86Y mutation`
> odds ratio = 2.45, p = 0.14
> CI [0.59, 10.8]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **CQ (chloroquine) treatment** to **pfmdr-1 86Y mutation**, reported as a odds ratio.

### How?

Study design: Experimental Trial.

### Who?

> Children between six and 59 months of age with uncomplicated malaria in Kolle, Mali, during the malaria transmission seasons of 2002 and 2003.

## Provenance

- Source study: [[@tekete2009]]
- Paper: Efficacy of chloroquine, amodiaquine and sulphadoxine-pyrimethamine for the treatment of uncomplicated falciparum malaria: revisiting molecular markers in an area of emerging AQ and SP resistance in Mali.
- Journal: Malaria journal
- Published: 2009 Feb 26
- PubMed: [19245687](https://pubmed.ncbi.nlm.nih.gov/19245687/)
- System association ID: `Dlb2N8BnFW`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
