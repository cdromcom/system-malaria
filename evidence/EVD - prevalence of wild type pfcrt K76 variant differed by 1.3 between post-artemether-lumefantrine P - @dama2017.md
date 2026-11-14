---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of wild type pfcrt K76 variant differed by 1.3 between post-artemether-lumefantrine P. falciparum isolates and baseline P. falciparum isolates (mean difference unstandardized) - @dama2017"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2017"
created: 2026-11-14
updated: 2026-11-14
nodeID: 5a189b54-eb26-467d-ae50-c70ab9165260
title: prevalence of wild type pfcrt K76 variant differed by 1.3 between post-artemether-lumefantrine P. falciparum isolates and baseline P. falciparum isolates (mean difference unstandardized) - @dama2017
---

## Source

[[@dama2017]]

## In plain terms

> [!info] What this finding says
> A study published in 2017 reported a statistical link between **post-artemether-lumefantrine P. falciparum isolates** and **prevalence of wild type pfcrt K76 variant**.
> Prevalence of wild type pfcrt K76 variant differed by 1.3 between post-artemether-lumefantrine P. falciparum isolates and baseline P. falciparum isolates (mean difference unstandardized), p = 0.9.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **1.3** |
| **p-value** | = 0.9 |
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
| **Open data** | Available from the authors on request only — Genbank |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 61 Plasmodium falciparum samples collected during a large WANECAM study in Mali. |
| **Intervention / exposure** | post-artemether-lumefantrine P. falciparum isolates |
| **Comparator** | baseline P. falciparum isolates |
| **Outcome** | prevalence of wild type pfcrt K76 variant |
| **Setting** | Mali |
| **Timeframe** | Published 2017. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **artemether-lumefantrine** — a widely used artemisinin combination treatment, sold as Coartem

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `post-artemether-lumefantrine P. falciparum isolates [vs baseline P. falciparum isolates]`
> Variable 2: `prevalence of wild type pfcrt K76 variant`
> mean difference unstandardized = 1.3, p = 0.9
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **post-artemether-lumefantrine P. falciparum isolates** to **prevalence of wild type pfcrt K76 variant**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 61 Plasmodium falciparum samples collected during a large WANECAM study in Mali.

## Provenance

- Source study: [[@dama2017]]
- Paper: Reduced ex vivo susceptibility of Plasmodium falciparum after oral artemether-lumefantrine treatment in Mali.
- Journal: Malaria journal
- Published: 2017 Feb 2
- PubMed: [28148267](https://pubmed.ncbi.nlm.nih.gov/28148267/)
- System association ID: `Z0eH3h3ump`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
