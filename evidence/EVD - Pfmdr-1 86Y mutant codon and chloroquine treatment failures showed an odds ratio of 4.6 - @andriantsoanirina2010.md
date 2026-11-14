---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Pfmdr-1 86Y mutant codon and chloroquine treatment failures showed an odds ratio of 4.6 - @andriantsoanirina2010"
tags:
  - "marker/pfmdr1"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2010"
created: 2026-11-14
updated: 2026-11-14
nodeID: 63992620-8de9-43de-be60-e58050fa0dac
title: Pfmdr-1 86Y mutant codon and chloroquine treatment failures showed an odds ratio of 4.6 - @andriantsoanirina2010
---

## Source

[[@andriantsoanirina2010]]

## In plain terms

> [!info] What this finding says
> A study published in 2010 reported a statistical link between **Pfmdr-1 86Y mutant codon** and **chloroquine treatment failures**.
> Pfmdr-1 86Y mutant codon and chloroquine treatment failures showed an odds ratio of 4.6.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **4.6** |
| **p-value** | Not recorded |
| **Confidence interval** | Not recorded |
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
| **Open data** | No availability statement found in the full text — GenBank, ISRCTN |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 249 Plasmodium falciparum samples collected from patients enrolled in a chloroquine in vivo efficacy study in Madagascar. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Madagascar |
| **Timeframe** | Published 2010. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Pfmdr-1 86Y mutant codon` with `chloroquine treatment failures` and reports a odds ratio of 4.6. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pfmdr-1 86Y mutant codon`
> Variable 2: `chloroquine treatment failures`
> odds ratio = 4.6
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Pfmdr-1 86Y mutant codon** to **chloroquine treatment failures**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 249 Plasmodium falciparum samples collected from patients enrolled in a chloroquine in vivo efficacy study in Madagascar.

## Provenance

- Source study: [[@andriantsoanirina2010]]
- Paper: Chloroquine clinical failures in P. falciparum malaria are associated with mutant Pfmdr-1, not Pfcrt in Madagascar.
- Journal: PloS one
- Published: 2010 Oct 13
- PubMed: [20967251](https://pubmed.ncbi.nlm.nih.gov/20967251/)
- System association ID: `MHlzEA9o6R`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
