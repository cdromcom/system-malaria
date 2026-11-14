---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Pfcrt 76T mutations differed by 3.2 between Adama and Metehara (mean difference unstandardized) - @hassen2022"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2022"
created: 2026-11-14
updated: 2026-11-14
nodeID: 6a4287f0-97b4-4a37-8c46-c3748003cc56
title: Pfcrt 76T mutations differed by 3.2 between Adama and Metehara (mean difference unstandardized) - @hassen2022
---

## Source

[[@hassen2022]]

## In plain terms

> [!info] What this finding says
> A study published in 2022 reported a statistical link between **Adama** and **Pfcrt 76T mutations**.
> Pfcrt 76T mutations differed by 3.2 between Adama and Metehara (mean difference unstandardized), p = 0.388.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **3.2** |
| **p-value** | = 0.388 |
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
| **Open data** | Available from the authors on request only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 121 microscopically confirmed P. falciparum infected patients from Adama, Olenchiti, and Metehara sites of East Shewa zone, Oromia Regional State, Ethiopia. |
| **Intervention / exposure** | Adama |
| **Comparator** | Metehara |
| **Outcome** | Pfcrt 76T mutations |
| **Setting** | Adama |
| **Timeframe** | Published 2022. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Adama [vs Metehara]`
> Variable 2: `Pfcrt 76T mutations`
> mean difference unstandardized = 3.2, p = 0.388
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Adama** to **Pfcrt 76T mutations**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 121 microscopically confirmed P. falciparum infected patients from Adama, Olenchiti, and Metehara sites of East Shewa zone, Oromia Regional State, Ethiopia.

## Provenance

- Source study: [[@hassen2022]]
- Paper: High prevalence of Pfcrt 76T and Pfmdr1 N86 genotypes in malaria infected patients attending health facilities in East Shewa zone, Oromia Regional State, Ethiopia.
- Journal: Malaria journal
- Published: 2022 Oct 7
- PubMed: [36207750](https://pubmed.ncbi.nlm.nih.gov/36207750/)
- System association ID: `xqrAKDyVnk`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
