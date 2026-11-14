---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - no insecticide spray and pfcrt T76 mutation showed an odds ratio of 3.7 - @almekhlafi2011"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: abc17e0a-9e5e-44bd-b73c-7050a3e31f70
title: no insecticide spray and pfcrt T76 mutation showed an odds ratio of 3.7 - @almekhlafi2011
---

## Source

[[@almekhlafi2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **no insecticide spray** and **pfcrt T76 mutation**.
> No insecticide spray and pfcrt T76 mutation showed an odds ratio of 3.7, p = 0.025. The confidence interval runs from 1.16 to 11.9.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **3.7** |
| **p-value** | = 0.025 |
| **Confidence interval** | CI 1.16 to 11.9 (confidence level not recorded) |
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
| **Population** | 511 participants from four governorates in Yemen. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Yemen |
| **Timeframe** | Published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `no insecticide spray` with `pfcrt T76 mutation` and reports a odds ratio of 3.7. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `no insecticide spray`
> Variable 2: `pfcrt T76 mutation`
> odds ratio = 3.7, p = 0.025
> CI [1.16, 11.9]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **no insecticide spray** to **pfcrt T76 mutation**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 511 participants from four governorates in Yemen.

## Provenance

- Source study: [[@almekhlafi2011]]
- Paper: High frequency of Plasmodium falciparum chloroquine resistance marker (pfcrt T76 mutation) in Yemen: an urgent need to re-examine malaria drug policy.
- Journal: Parasites & vectors
- Published: 2011 May 27
- PubMed: [21619624](https://pubmed.ncbi.nlm.nih.gov/21619624/)
- System association ID: `u-2kH0747Q`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
