---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - proportion of multicopy plasmepsin 2 parasites was associated with an increase of 0.89 in dihydroartemisinin-piperaquine treatment failure rates (spearman correlation) - @witkowski2017"
tags:
  - "marker/plasmepsin"
  - "theme/treatment-failure"
  - "stat/spearman_correlation"
  - "direction/positive"
  - "verification/api-only"
  - "year/2017"
created: 2026-11-14
updated: 2026-11-14
nodeID: e0466cec-c584-44a9-b796-fdb32e5ee427
title: proportion of multicopy plasmepsin 2 parasites was associated with an increase of 0.89 in dihydroartemisinin-piperaquine treatment failure rates (spearman correlation) - @witkowski2017
---

## Source

[[@witkowski2017]]

## In plain terms

> [!info] What this finding says
> A study published in 2017 reported a statistical link between **proportion of multicopy plasmepsin 2 parasites** and **dihydroartemisinin-piperaquine treatment failure rates**.
> Proportion of multicopy plasmepsin 2 parasites was associated with an increase of 0.89 in dihydroartemisinin-piperaquine treatment failure rates (spearman correlation), p = 0.0001. The confidence interval runs from 0.77 to 0.95.

## Statistic

| | |
|---|---|
| **Metric** | `spearman_correlation` (System's normalised type; the paper reported `spearman_correlation`) |
| **Estimate** | **0.89** |
| **p-value** | = 0.0001 |
| **Confidence interval** | CI 0.77 to 0.95 (confidence level not recorded) |
| **Direction vs null of 0** | **positive** |
| **Data source** | API list, API detail |
| **In curated release** | No |
| **Source paper integrity** | formal published comments exist, a published erratum exists (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: Corrected) |
| **Published erratum** | Yes — PubMed CommentsCorrections ErratumIn -> PMID 29907497 |
| **Formal published comments** | 1 indexed in PubMed |
| **Critical social posts** | None recorded — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Yes (hybrid) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Cambodian patients infected with Plasmodium falciparum and treated with dihydroartemisinin-piperaquine between 2009 and 2015. |
| **Intervention / exposure** | proportion of multicopy plasmepsin 2 parasites |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | dihydroartemisinin-piperaquine treatment failure rates |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2017. Fieldwork dates are not recorded in the graph. |

> [!warning] The source paper has a published erratum
> PubMed CommentsCorrections ErratumIn -> PMID 29907497; Crossref updated-by: erratum (10.1016/s1473-3099(18)30396-7)
> System extracted this statistic from the original article, and the graph records nothing about corrections. The number above may be one the erratum changed. Check the correction notice before citing it.

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **plasmepsin** — a parasite enzyme whose extra gene copies are linked to piperaquine resistance
- **dihydroartemisinin-piperaquine** — an artemisinin combination treatment

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `proportion of multicopy plasmepsin 2 parasites`
> Variable 2: `dihydroartemisinin-piperaquine treatment failure rates`
> spearman correlation = 0.89, p = 0.0001
> CI [0.77, 0.95]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **proportion of multicopy plasmepsin 2 parasites** to **dihydroartemisinin-piperaquine treatment failure rates**, reported as a spearman correlation.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Cambodian patients infected with Plasmodium falciparum and treated with dihydroartemisinin-piperaquine between 2009 and 2015.

## Provenance

- Source study: [[@witkowski2017]]
- Paper: A surrogate marker of piperaquine-resistant Plasmodium falciparum malaria: a phenotype-genotype association study.
- Journal: The Lancet. Infectious diseases
- Published: 2017 Feb
- PubMed: [27818097](https://pubmed.ncbi.nlm.nih.gov/27818097/)
- System association ID: `_PZsDTedwc`
- Resistance gene(s): Plasmepsin
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
