---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - QN IC50 and pfmdr1 copy number showed a pearson r of 0.099 - @poyomtip2012"
tags:
  - "marker/pfmdr1"
  - "theme/drug-susceptibility"
  - "stat/pearson_r"
  - "direction/positive"
  - "verification/api-only"
  - "year/2012"
created: 2026-11-14
updated: 2026-11-14
nodeID: a2c5cc63-4b4c-43eb-9891-5d40ac6ba992
title: QN IC50 and pfmdr1 copy number showed a pearson r of 0.099 - @poyomtip2012
---

## Source

[[@poyomtip2012]]

## In plain terms

> [!info] What this finding says
> A study published in 2012 reported a statistical link between **QN IC50** and **pfmdr1 copy number**.
> QN IC50 and pfmdr1 copy number showed a pearson r of 0.099.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0.099** |
| **p-value** | Not recorded |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **positive** |
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
| **Population** | 85 Thai isolates of Plasmodium falciparum collected from the Thai-Myanmar and Thai-Cambodia borders between 2003-2008. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2012. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `QN IC50` with `pfmdr1 copy number` and reports a pearson r of 0.099. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **IC50** — the drug concentration needed to halve parasite growth in the laboratory; a higher value means the parasite is less sensitive to the drug

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `QN IC50`
> Variable 2: `pfmdr1 copy number`
> pearson r = 0.099
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **QN IC50** to **pfmdr1 copy number**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 85 Thai isolates of Plasmodium falciparum collected from the Thai-Myanmar and Thai-Cambodia borders between 2003-2008.

## Provenance

- Source study: [[@poyomtip2012]]
- Paper: Polymorphisms of the pfmdr1 but not the pfnhe-1 gene is associated with in vitro quinine sensitivity in Thai isolates of Plasmodium falciparum.
- Journal: Malaria journal
- Published: 2012 Jan 5
- PubMed: [22221394](https://pubmed.ncbi.nlm.nih.gov/22221394/)
- System association ID: `W0jU6YkPpz`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
