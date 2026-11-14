---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfdhps haplotype SGEGA at five codons and treatment failures (among the study participants) showed an odds ratio of 7.3 - @gadalla2013"
tags:
  - "marker/pfdhps"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2013"
created: 2026-11-14
updated: 2026-11-14
nodeID: 1fd94df3-93b8-4277-8f50-1ee51ff02158
title: pfdhps haplotype SGEGA at five codons and treatment failures (among the study participants) showed an odds ratio of 7.3 - @gadalla2013
---

## Source

[[@gadalla2013]]

## In plain terms

> [!info] What this finding says
> A study published in 2013 reported a statistical link between **pfdhps haplotype SGEGA at five codons** and **treatment failures (among the study participants)**.
> Pfdhps haplotype SGEGA at five codons and treatment failures (among the study participants) showed an odds ratio of 7.3. The confidence interval runs from 0.65 to 368.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **7.3** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 0.65 to 368 (confidence level not recorded) |
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
| **Critical social posts** | 1 negative X/Twitter, 0 Bluesky — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 63 patients in eastern Sudan during the 2012 transmission season. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2013. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `pfdhps haplotype SGEGA at five codons` with `treatment failures (among the study participants)` and reports a odds ratio of 7.3. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfdhps haplotype SGEGA at five codons`
> Variable 2: `treatment failures (among the study participants)`
> odds ratio = 7.3
> CI [0.65, 368]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfdhps haplotype SGEGA at five codons** to **treatment failures (among the study participants)**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 63 patients in eastern Sudan during the 2012 transmission season.

## Provenance

- Source study: [[@gadalla2013]]
- Paper: Selection of pfdhfr/pfdhps alleles and declining artesunate/sulphadoxine-pyrimethamine efficacy against Plasmodium falciparum eight years after deployment in eastern Sudan.
- Journal: Malaria journal
- Published: 2013 Jul 19
- PubMed: [23870667](https://pubmed.ncbi.nlm.nih.gov/23870667/)
- System association ID: `hb7U_0XS5L`
- Resistance gene(s): PfDHPS
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
