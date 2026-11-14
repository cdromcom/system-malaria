---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - High parasite density and chloroquine resistance showed an odds ratio of 5 - @hess1996"
tags:
  - "marker/pfcrt"
  - "theme/parasite-clearance"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/in-curated-deposit"
  - "year/1996"
created: 2026-11-14
updated: 2026-11-14
nodeID: c734d582-59be-40ef-83a5-ea332c816653
title: High parasite density and chloroquine resistance showed an odds ratio of 5 - @hess1996
---

## Source

[[@hess1996]]

## In plain terms

> [!info] What this finding says
> A study published in 1996 reported a statistical link between **High parasite density** and **chloroquine resistance**.
> High parasite density and chloroquine resistance showed an odds ratio of 5. The confidence interval runs from 2 to 10.6.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **5** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 2 to 10.6 (confidence level not recorded) |
| **Direction vs null of 1** | **positive** |
| **Data source** | API list, API detail, Dataverse release |
| **In curated release** | Yes |
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
> The record pairs `High parasite density` with `chloroquine resistance` and reports a odds ratio of 5. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `High parasite density`
> Variable 2: `chloroquine resistance`
> odds ratio = 5
> CI [2, 10.6]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **High parasite density** to **chloroquine resistance**, reported as a odds ratio.

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
- System association ID: `_PEvyc4SXh`
- Resistance gene(s): PfCRT
- Outcome theme(s): how fast malaria parasites cleared from the blood

## Verification

> [!success] Checked against the curated dataset
> This finding also appears in System's curated Harvard Dataverse release, from which the extractions System had flagged as inaccurate were removed. That is the best available sign that the number was read correctly from the paper.

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
