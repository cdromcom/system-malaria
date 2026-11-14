---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Changes in prevalence of pfcrt-K76T mutation between 2019 and 2017 and pfcrt-K76T mutation prevalence showed a mean difference unstandardized of -5.8 - @yobi2022"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2022"
created: 2026-11-14
updated: 2026-11-14
nodeID: b3bfddf8-aa2a-4e44-930e-bbed405f8e32
title: Changes in prevalence of pfcrt-K76T mutation between 2019 and 2017 and pfcrt-K76T mutation prevalence showed a mean difference unstandardized of -5.8 - @yobi2022
---

## Source

[[@yobi2022]]

## In plain terms

> [!info] What this finding says
> A study published in 2022 reported a statistical link between **Changes in prevalence of pfcrt-K76T mutation between 2019 and 2017 studies (Democratic Republic of Congo)** and **pfcrt-K76T mutation prevalence**.
> Changes in prevalence of pfcrt-K76T mutation between 2019 and 2017 and pfcrt-K76T mutation prevalence showed a mean difference unstandardized of -5.8, p = 0.069.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-5.8** |
| **p-value** | = 0.069 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **negative** |
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
| **Population** | Patients with P. falciparum malaria in the Democratic Republic of Congo. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2022. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Changes in prevalence of pfcrt-K76T mutation between 2019 and 2017 studies (Democratic Republic of Congo)` with `pfcrt-K76T mutation prevalence` and reports a mean difference unstandardized of -5.8. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **K76T** — a mutation that swaps amino acid K for T at position 76 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Changes in prevalence of pfcrt-K76T mutation between 2019 and 2017 studies (Democratic Republic of Congo)`
> Variable 2: `pfcrt-K76T mutation prevalence`
> mean difference unstandardized = -5.8, p = 0.069
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **Changes in prevalence of pfcrt-K76T mutation between 2019 and 2017 studies (Democratic Republic of Congo)** to **pfcrt-K76T mutation prevalence**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Patients with P. falciparum malaria in the Democratic Republic of Congo.

## Provenance

- Source study: [[@yobi2022]]
- Paper: Biennial surveillance of Plasmodium falciparum anti-malarial drug resistance markers in Democratic Republic of Congo, 2017 and 2019.
- Journal: BMC infectious diseases
- Published: 2022 Feb 10
- PubMed: [35144535](https://pubmed.ncbi.nlm.nih.gov/35144535/)
- System association ID: `T3F3H87Ojb`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
