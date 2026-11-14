---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr1-86Y and weekly rainfall data showed an odds ratio of 1.07 - @ord2007"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2007"
created: 2026-11-14
updated: 2026-11-14
nodeID: 06395c64-3e91-4d13-8150-bb9de67bf35d
title: pfmdr1-86Y and weekly rainfall data showed an odds ratio of 1.07 - @ord2007
---

## Source

[[@ord2007]]

## In plain terms

> [!info] What this finding says
> A study published in 2007 reported a statistical link between **pfmdr1-86Y** and **weekly rainfall data**.
> Pfmdr1-86Y and weekly rainfall data showed an odds ratio of 1.07, p = 0.001.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **1.07** |
| **p-value** | = 0.001 |
| **Confidence interval** | Not recorded |
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
| **Population** | 441 children presenting with uncomplicated falciparum malaria in The Gambia over 5 seasons (1998-2002). |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2007. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `pfmdr1-86Y` with `weekly rainfall data` and reports a odds ratio of 1.07. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfmdr1-86Y`
> Variable 2: `weekly rainfall data`
> odds ratio = 1.07, p = 0.001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfmdr1-86Y** to **weekly rainfall data**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 441 children presenting with uncomplicated falciparum malaria in The Gambia over 5 seasons (1998-2002).

## Provenance

- Source study: [[@ord2007]]
- Paper: Seasonal carriage of pfcrt and pfmdr1 alleles in Gambian Plasmodium falciparum imply reduced fitness of chloroquine-resistant parasites.
- Journal: The Journal of infectious diseases
- Published: 2007 Dec 1
- PubMed: [18008244](https://pubmed.ncbi.nlm.nih.gov/18008244/)
- System association ID: `8WVa0tYc-a`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
