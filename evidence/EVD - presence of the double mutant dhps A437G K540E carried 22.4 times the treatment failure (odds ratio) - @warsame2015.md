---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - presence of the double mutant dhps A437G K540E carried 22.4 times the treatment failure (odds ratio) - @warsame2015"
tags:
  - "marker/pfdhps"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: c899c0ea-5932-478d-9779-9ad02a32eecf
title: presence of the double mutant dhps A437G K540E carried 22.4 times the treatment failure (odds ratio) - @warsame2015
---

## Source

[[@warsame2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **presence of the double mutant dhps A437G/K540E** and **treatment failure (among the patients with the presence of the double mutant dhps A437G/K540E)**.
> Presence of the double mutant dhps A437G K540E carried 22.4 times the treatment failure (odds ratio). The confidence interval runs from 5.1 to 98.1.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **22.4** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 5.1 to 98.1 (confidence level not recorded) |
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
| **Open access** | Yes (bronze) |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Adults and children aged 6 months to 14 years with uncomplicated malaria in Somalia in 2011. |
| **Intervention / exposure** | presence of the double mutant dhps A437G/K540E |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | treatment failure (among the patients with the presence of the double mutant dhps A437G/K540E) |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **A437G** — a mutation that swaps amino acid A for G at position 437 of the protein
- **K540E** — a mutation that swaps amino acid K for E at position 540 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `presence of the double mutant dhps A437G/K540E`
> Variable 2: `treatment failure (among the patients with the presence of the double mutant dhps A437G/K540E)`
> odds ratio = 22.4
> CI [5.1, 98.1]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **presence of the double mutant dhps A437G/K540E** to **treatment failure (among the patients with the presence of the double mutant dhps A437G/K540E)**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Adults and children aged 6 months to 14 years with uncomplicated malaria in Somalia in 2011.

## Provenance

- Source study: [[@warsame2015]]
- Paper: Treatment of uncomplicated malaria with artesunate plus sulfadoxine-pyrimethamine is failing in Somalia: evidence from therapeutic efficacy studies and Pfdhfr and Pfdhps mutant alleles.
- Journal: Tropical medicine & international health : TM & IH
- Published: 2015 Apr
- PubMed: [25583123](https://pubmed.ncbi.nlm.nih.gov/25583123/)
- System association ID: `ZPGDdrkvVI`
- Resistance gene(s): PfDHPS
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
