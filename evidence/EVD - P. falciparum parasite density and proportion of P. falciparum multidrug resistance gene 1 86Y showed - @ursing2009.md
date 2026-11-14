---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - P. falciparum parasite density and proportion of P. falciparum multidrug resistance gene 1 86Y showed an odds ratio of 0.92 - @ursing2009"
tags:
  - "marker/pfmdr1"
  - "theme/parasite-clearance"
  - "stat/odds_ratio"
  - "direction/negative"
  - "verification/api-only"
  - "year/2009"
created: 2026-11-14
updated: 2026-11-14
nodeID: e5c85f6b-70af-4290-abc4-6dda21cd8ed8
title: P. falciparum parasite density and proportion of P. falciparum multidrug resistance gene 1 86Y showed an odds ratio of 0.92 - @ursing2009
---

## Source

[[@ursing2009]]

## In plain terms

> [!info] What this finding says
> A study published in 2009 reported a statistical link between **P. falciparum parasite density** and **proportion of P. falciparum multidrug resistance gene 1 86Y**.
> P. falciparum parasite density and proportion of P. falciparum multidrug resistance gene 1 86Y showed an odds ratio of 0.92, p = 0.08. The confidence interval runs from 0.83 to 1.01.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **0.92** |
| **p-value** | = 0.08 |
| **Confidence interval** | CI 0.83 to 1.01 (confidence level not recorded) |
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
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text — ClinicalTrials.gov |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Children in Guinea-Bissau between 2002 and 2007. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2009. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `P. falciparum parasite density` with `proportion of P. falciparum multidrug resistance gene 1 86Y` and reports a odds ratio of 0.92. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `P. falciparum parasite density`
> Variable 2: `proportion of P. falciparum multidrug resistance gene 1 86Y`
> odds ratio = 0.92, p = 0.08
> CI [0.83, 1.01]
> Direction against the statistic's null value of 1: **negative**

## Methods Context

### What?

The study related **P. falciparum parasite density** to **proportion of P. falciparum multidrug resistance gene 1 86Y**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Children in Guinea-Bissau between 2002 and 2007.

## Provenance

- Source study: [[@ursing2009]]
- Paper: No seasonal accumulation of resistant P. falciparum when high-dose chloroquine is used.
- Journal: PloS one
- Published: 2009 Aug 31
- PubMed: [19718439](https://pubmed.ncbi.nlm.nih.gov/19718439/)
- System association ID: `lpY1NEhki0`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how fast malaria parasites cleared from the blood

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
