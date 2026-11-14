---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Young age and chloroquine resistance showed an odds ratio of 0.8 - @hess1996"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/negative"
  - "verification/api-only"
  - "year/1996"
created: 2026-11-14
updated: 2026-11-14
nodeID: 4fc6b3ff-dcba-47c5-9e04-31e11cacb3e2
title: Young age and chloroquine resistance showed an odds ratio of 0.8 - @hess1996
---

## Source

[[@hess1996]]

## In plain terms

> [!info] What this finding says
> A study published in 1996 reported a statistical link between **Young age** and **chloroquine resistance**.
> Young age and chloroquine resistance showed an odds ratio of 0.8. The confidence interval runs from 0.6 to 0.9.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **0.8** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 0.6 to 0.9 (confidence level not recorded) |
| **Direction vs null of 1** | **negative** |
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
| **Population** | 38 individuals with chloroquine resistant infections and 125 individuals with chloroquine sensitive infections from randomly selected schools in North Guadalcanal, Solomon Islands. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | North Guadalcanal |
| **Timeframe** | Published 1996. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Young age` with `chloroquine resistance` and reports a odds ratio of 0.8. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Young age`
> Variable 2: `chloroquine resistance`
> odds ratio = 0.8
> CI [0.6, 0.9]
> Direction against the statistic's null value of 1: **negative**

## Methods Context

### What?

The study related **Young age** to **chloroquine resistance**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 38 individuals with chloroquine resistant infections and 125 individuals with chloroquine sensitive infections from randomly selected schools in North Guadalcanal, Solomon Islands.

## Provenance

- Source study: [[@hess1996]]
- Paper: Risk factors of chloroquine resistance in Plasmodium falciparum malaria.
- Journal: Acta tropica
- Published: 1996 Aug
- PubMed: [8910654](https://pubmed.ncbi.nlm.nih.gov/8910654/)
- System association ID: `spF70z1Uhf`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
