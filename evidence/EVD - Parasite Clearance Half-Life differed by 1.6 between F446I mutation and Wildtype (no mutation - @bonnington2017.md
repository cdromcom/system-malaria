---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Parasite Clearance Half-Life differed by 1.6 between F446I mutation and Wildtype (no mutation (mean difference unstandardized) - @bonnington2017"
tags:
  - "marker/pfkelch13"
  - "theme/parasite-clearance"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2017"
created: 2026-11-14
updated: 2026-11-14
nodeID: 605d451f-570e-4d2e-9363-5e77fce82dd0
title: Parasite Clearance Half-Life differed by 1.6 between F446I mutation and Wildtype (no mutation (mean difference unstandardized) - @bonnington2017
---

## Source

[[@bonnington2017]]

## In plain terms

> [!info] What this finding says
> A study published in 2017 reported a statistical link between **F446I mutation** and **Parasite Clearance Half-Life**.
> Parasite Clearance Half-Life differed by 1.6 between F446I mutation and Wildtype (no mutation (mean difference unstandardized), p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **1.6** |
| **p-value** | = 0.01 |
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
| **Open data** | Available from the authors on request only — WWARN |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 35 patients with uncomplicated P. falciparum treated with artesunate monotherapy followed by 3-day ACT in an isolated area on the Myanmar-Thai border. |
| **Intervention / exposure** | F446I mutation |
| **Comparator** | Wildtype (no mutation |
| **Outcome** | Parasite Clearance Half-Life |
| **Setting** | Myanmar-Thai border |
| **Timeframe** | Published 2017. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **F446I** — a mutation that swaps amino acid F for I at position 446 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `F446I mutation [vs Wildtype (no mutation)]`
> Variable 2: `Parasite Clearance Half-Life`
> mean difference unstandardized = 1.6, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **F446I mutation** to **Parasite Clearance Half-Life**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 35 patients with uncomplicated P. falciparum treated with artesunate monotherapy followed by 3-day ACT in an isolated area on the Myanmar-Thai border.

## Provenance

- Source study: [[@bonnington2017]]
- Paper: Plasmodium falciparum Kelch 13 mutations and treatment response in patients in Hpa-Pun District, Northern Kayin State, Myanmar.
- Journal: Malaria journal
- Published: 2017 Nov 25
- PubMed: [29178921](https://pubmed.ncbi.nlm.nih.gov/29178921/)
- System association ID: `3AImZkolot`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): how fast malaria parasites cleared from the blood

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
