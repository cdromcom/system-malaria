---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr 1 mutation resulting in the substitution of tyrosine for carried 3.2 times the response to chloroquine treatment in patients with uncomplicated (odds ratio) - @djimd2001"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2001"
created: 2026-11-14
updated: 2026-11-14
nodeID: 6e1fc4e7-ee84-47dd-98a0-5a1841f9d8a0
title: pfmdr 1 mutation resulting in the substitution of tyrosine for carried 3.2 times the response to chloroquine treatment in patients with uncomplicated (odds ratio) - @djimd2001
---

## Source

[[@djimd2001]]

## In plain terms

> [!info] What this finding says
> A study published in 2001 reported a statistical link between **pfmdr 1 mutation resulting in the substitution of tyrosine for asparagine at position 86** and **response to chloroquine treatment in patients with uncomplicated falciparum malaria in Mali**.
> Pfmdr 1 mutation resulting in the substitution of tyrosine for carried 3.2 times the response to chloroquine treatment in patients with uncomplicated (odds ratio), p = 0.001. The confidence interval runs from 1.5 to 6.8.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **3.2** |
| **p-value** | = 0.001 |
| **Confidence interval** | CI 1.5 to 6.8 (confidence level not recorded) |
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
| **Open access** | Yes (bronze) |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Patients with uncomplicated falciparum malaria in Mali. |
| **Intervention / exposure** | pfmdr 1 mutation resulting in the substitution of tyrosine for asparagine at position 86 |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | response to chloroquine treatment in patients with uncomplicated falciparum malaria in Mali |
| **Setting** | Mali |
| **Timeframe** | Published 2001. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfmdr 1 mutation resulting in the substitution of tyrosine for asparagine at position 86`
> Variable 2: `response to chloroquine treatment in patients with uncomplicated falciparum malaria in Mali`
> odds ratio = 3.2, p = 0.001
> CI [1.5, 6.8]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfmdr 1 mutation resulting in the substitution of tyrosine for asparagine at position 86** to **response to chloroquine treatment in patients with uncomplicated falciparum malaria in Mali**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Patients with uncomplicated falciparum malaria in Mali.

## Provenance

- Source study: [[@djimd2001]]
- Paper: A molecular marker for chloroquine-resistant falciparum malaria.
- Journal: The New England journal of medicine
- Published: 2001 Jan 25
- PubMed: [11172152](https://pubmed.ncbi.nlm.nih.gov/11172152/)
- System association ID: `S1v-R1asok`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
