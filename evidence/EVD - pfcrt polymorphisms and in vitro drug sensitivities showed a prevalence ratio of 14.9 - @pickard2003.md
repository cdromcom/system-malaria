---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfcrt polymorphisms and in vitro drug sensitivities showed a prevalence ratio of 14.9 - @pickard2003"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "theme/drug-susceptibility"
  - "stat/prevalence_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2003"
created: 2026-11-14
updated: 2026-11-14
nodeID: 6dc213c8-6cf0-48ef-b8e3-0fccf538cf09
title: pfcrt polymorphisms and in vitro drug sensitivities showed a prevalence ratio of 14.9 - @pickard2003
---

## Source

[[@pickard2003]]

## In plain terms

> [!info] What this finding says
> A study published in 2003 reported a statistical link between **pfcrt polymorphisms** and **in vitro drug sensitivities**.
> Pfcrt polymorphisms and in vitro drug sensitivities showed a prevalence ratio of 14.9, p = 0.01. The confidence interval runs from 3.88 to 57.6.

## Statistic

| | |
|---|---|
| **Metric** | `prevalence_ratio` (System's normalised type; the paper reported `prevalence_ratio`) |
| **Estimate** | **14.9** |
| **p-value** | = 0.01 |
| **Confidence interval** | CI 3.88 to 57.6 (confidence level not recorded) |
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
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 65 Plasmodium falciparum isolates from Thailand, Myanmar, Vietnam, and Bangladesh. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Thailand |
| **Timeframe** | Published 2003. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `pfcrt polymorphisms` with `in vitro drug sensitivities` and reports a prevalence ratio of 14.9. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Possible extraction mismatch
> This record names **PfCRT**, but the source paper's title mentions pfmdr1 instead. The paper may well cover both, but check it against the article before citing.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **in vitro** — tested on parasites grown in the laboratory

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfcrt polymorphisms`
> Variable 2: `in vitro drug sensitivities`
> prevalence ratio = 14.9, p = 0.01
> CI [3.88, 57.6]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfcrt polymorphisms** to **in vitro drug sensitivities**, reported as a prevalence ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 65 Plasmodium falciparum isolates from Thailand, Myanmar, Vietnam, and Bangladesh.

## Provenance

- Source study: [[@pickard2003]]
- Paper: Resistance to antimalarials in Southeast Asia and genetic polymorphisms in pfmdr1.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2003 Aug
- PubMed: [12878499](https://pubmed.ncbi.nlm.nih.gov/12878499/)
- System association ID: `JzhUAIbYEe`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was, how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
