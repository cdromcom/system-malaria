---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - polymorphisms in pfmdr1 and pfcrt and prevalences of polymorphisms in Tororo, Uganda showed an odds ratio of 1.41 - @conrad2014"
tags:
  - "marker/pfcrt"
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2014"
created: 2026-11-14
updated: 2026-11-14
nodeID: 349a0a95-68e8-42d5-a32f-5fe2c8828532
title: polymorphisms in pfmdr1 and pfcrt and prevalences of polymorphisms in Tororo, Uganda showed an odds ratio of 1.41 - @conrad2014
---

## Source

[[@conrad2014]]

## In plain terms

> [!info] What this finding says
> A study published in 2014 reported a statistical link between **polymorphisms in pfmdr1 and pfcrt** and **prevalences of polymorphisms in Tororo, Uganda**.
> Polymorphisms in pfmdr1 and pfcrt and prevalences of polymorphisms in Tororo, Uganda showed an odds ratio of 1.41, p = 0.001. The confidence interval runs from 1.25 to 1.57.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **1.41** |
| **p-value** | = 0.001 |
| **Confidence interval** | CI 1.25 to 1.57 (confidence level not recorded) |
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
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 312 children randomized to AL or DP for each episode of uncomplicated malaria in Tororo, Uganda from 2008 to 2012. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Tororo |
| **Timeframe** | Published 2014. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `polymorphisms in pfmdr1 and pfcrt` with `prevalences of polymorphisms in Tororo, Uganda` and reports a odds ratio of 1.41. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `polymorphisms in pfmdr1 and pfcrt`
> Variable 2: `prevalences of polymorphisms in Tororo, Uganda`
> odds ratio = 1.41, p = 0.001
> CI [1.25, 1.57]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **polymorphisms in pfmdr1 and pfcrt** to **prevalences of polymorphisms in Tororo, Uganda**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 312 children randomized to AL or DP for each episode of uncomplicated malaria in Tororo, Uganda from 2008 to 2012.

## Provenance

- Source study: [[@conrad2014]]
- Paper: Comparative impacts over 5 years of artemisinin-based combination therapies on Plasmodium falciparum polymorphisms that modulate drug sensitivity in Ugandan children.
- Journal: The Journal of infectious diseases
- Published: 2014 Aug 1
- PubMed: [24610872](https://pubmed.ncbi.nlm.nih.gov/24610872/)
- System association ID: `b_di_XIsnv`
- Resistance gene(s): PfCRT, Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
