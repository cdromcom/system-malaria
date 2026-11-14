---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Presence of chloroquine-sensitive P. falciparum markers (pfcrt K76) and likelihood to detect pfmdr1 showed an odds ratio of 2.03 - @asare2021"
tags:
  - "marker/pfcrt"
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: 600b99c6-85b8-4050-a3b5-19f6a2c131e7
title: Presence of chloroquine-sensitive P. falciparum markers (pfcrt K76) and likelihood to detect pfmdr1 showed an odds ratio of 2.03 - @asare2021
---

## Source

[[@asare2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **Presence of chloroquine-sensitive P. falciparum markers (pfcrt K76) at Cape Coast** and **likelihood to detect pfmdr1**.
> Presence of chloroquine-sensitive P. falciparum markers (pfcrt K76) and likelihood to detect pfmdr1 showed an odds ratio of 2.03, p = 0.001. The confidence interval runs from 1.06 to 3.79.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **2.03** |
| **p-value** | = 0.001 |
| **Confidence interval** | CI 1.06 to 3.79 (confidence level not recorded) |
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
| **Open data** | A statement exists but is not explicit |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 184 individuals from the Central Region of Ghana. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Presence of chloroquine-sensitive P. falciparum markers (pfcrt K76) at Cape Coast` with `likelihood to detect pfmdr1` and reports a odds ratio of 2.03. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Presence of chloroquine-sensitive P. falciparum markers (pfcrt K76) at Cape Coast`
> Variable 2: `likelihood to detect pfmdr1`
> odds ratio = 2.03, p = 0.001
> CI [1.06, 3.79]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Presence of chloroquine-sensitive P. falciparum markers (pfcrt K76) at Cape Coast** to **likelihood to detect pfmdr1**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 184 individuals from the Central Region of Ghana.

## Provenance

- Source study: [[@asare2021]]
- Paper: The emergence of chloroquine-sensitive Plasmodium falciparum is influenced by selected communities in some parts of the Central Region of Ghana.
- Journal: Malaria journal
- Published: 2021 Nov 25
- PubMed: [34823528](https://pubmed.ncbi.nlm.nih.gov/34823528/)
- System association ID: `2teE52Tx25`
- Resistance gene(s): PfCRT, Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
