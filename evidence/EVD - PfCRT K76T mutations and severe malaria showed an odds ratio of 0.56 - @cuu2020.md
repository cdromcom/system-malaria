---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - PfCRT K76T mutations and severe malaria showed an odds ratio of 0.56 - @cuu2020"
tags:
  - "marker/pfcrt"
  - "theme/severe-illness"
  - "stat/odds_ratio"
  - "direction/negative"
  - "verification/api-only"
  - "year/2020"
created: 2026-11-14
updated: 2026-11-14
nodeID: 3a786b01-e296-4d36-855f-86dc9f5f95ba
title: PfCRT K76T mutations and severe malaria showed an odds ratio of 0.56 - @cuu2020
---

## Source

[[@cuu2020]]

## In plain terms

> [!info] What this finding says
> A study published in 2020 reported a statistical link between **PfCRT K76T mutations** and **severe malaria**.
> PfCRT K76T mutations and severe malaria showed an odds ratio of 0.56, p = 0.031. The confidence interval runs from 0.32 to 0.97.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **0.56** |
| **p-value** | = 0.031 |
| **Confidence interval** | CI 0.32 to 0.97 (confidence level not recorded) |
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
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 274 cases with severe malaria matched by age and geography to 275 uncomplicated malaria controls and 179 asymptomatic parasitemic controls in Uganda. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Uganda |
| **Timeframe** | Published 2020. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `PfCRT K76T mutations` with `severe malaria` and reports a odds ratio of 0.56. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **K76T** — a mutation that swaps amino acid K for T at position 76 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `PfCRT K76T mutations`
> Variable 2: `severe malaria`
> odds ratio = 0.56, p = 0.031
> CI [0.32, 0.97]
> Direction against the statistic's null value of 1: **negative**

## Methods Context

### What?

The study related **PfCRT K76T mutations** to **severe malaria**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 274 cases with severe malaria matched by age and geography to 275 uncomplicated malaria controls and 179 asymptomatic parasitemic controls in Uganda.

## Provenance

- Source study: [[@cuu2020]]
- Paper: Associations between Aminoquinoline Resistance Genotypes and Clinical Presentations of Plasmodium falciparum Infection in Uganda.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2020 Sep 21
- PubMed: [32660999](https://pubmed.ncbi.nlm.nih.gov/32660999/)
- System association ID: `tpQ0o65p8R`
- Resistance gene(s): PfCRT
- Outcome theme(s): severe illness, death and birth weight

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
