---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - PfCRT 76T differed by 16.4 between severe malaria cases and non-severe malaria cases (mean difference unstandardized) - @wl2011"
tags:
  - "marker/pfcrt"
  - "theme/severe-illness"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: 9be78e22-8a46-4172-8649-89535824af4d
title: PfCRT 76T differed by 16.4 between severe malaria cases and non-severe malaria cases (mean difference unstandardized) - @wl2011
---

## Source

[[@wl2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **severe malaria cases** and **PfCRT 76T**.
> PfCRT 76T differed by 16.4 between severe malaria cases and non-severe malaria cases (mean difference unstandardized), p = 0.0001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **16.4** |
| **p-value** | = 0.0001 |
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
| **Open access** | Yes (green) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 193 severe malaria cases and 386 non-severe malaria cases in Southern Mali, excluding those with G6PD deficiency and any known hemoglobin abnormality. |
| **Intervention / exposure** | severe malaria cases |
| **Comparator** | non-severe malaria cases |
| **Outcome** | PfCRT 76T |
| **Setting** | Southern Mali |
| **Timeframe** | Published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `severe malaria cases [vs non-severe malaria cases]`
> Variable 2: `PfCRT 76T`
> mean difference unstandardized = 16.4, p = 0.0001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **severe malaria cases** to **PfCRT 76T**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 193 severe malaria cases and 386 non-severe malaria cases in Southern Mali, excluding those with G6PD deficiency and any known hemoglobin abnormality.

## Provenance

- Source study: [[@wl2011]]
- Paper: High frequency of PfCRT 76T in two Malian villages and its prevalence in severe relative to non-severe malaria.
- Journal: Acta tropica
- Published: 2011 Jul
- PubMed: [21300016](https://pubmed.ncbi.nlm.nih.gov/21300016/)
- System association ID: `MJwnRyyznW`
- Resistance gene(s): PfCRT
- Outcome theme(s): severe illness, death and birth weight

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
