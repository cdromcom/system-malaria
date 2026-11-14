---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of chloroquine resistance differed by 11 between Tororo district and Busia district (mean difference unstandardized) - @tumwebaze2021"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: 90417d7c-8592-4aba-a597-2ab12bf665e1
title: prevalence of chloroquine resistance differed by 11 between Tororo district and Busia district (mean difference unstandardized) - @tumwebaze2021
---

## Source

[[@tumwebaze2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **Tororo district** and **prevalence of chloroquine resistance**.
> Prevalence of chloroquine resistance differed by 11 between Tororo district and Busia district (mean difference unstandardized), p = 0.0017.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **11** |
| **p-value** | = 0.0017 |
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
| **Open data** | Deposited in a public repository — Sequence Read Archive, sra, WWARN |
| **Open code** | github.com/bailey-lab |
| **Public accessions** | PRJNA660547 |

## PICOST

| | |
|---|---|
| **Population** | 440 patients aged 6 months or older presenting with clinical symptoms of malaria, a positive Giemsa-stained blood film for , and no signs of severe disease from Tororo and Busia districts in Uganda. |
| **Intervention / exposure** | Tororo district |
| **Comparator** | Busia district |
| **Outcome** | prevalence of chloroquine resistance |
| **Setting** | Tororo |
| **Timeframe** | Published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Tororo district [vs Busia district]`
> Variable 2: `prevalence of chloroquine resistance`
> mean difference unstandardized = 11, p = 0.0017
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Tororo district** to **prevalence of chloroquine resistance**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 440 patients aged 6 months or older presenting with clinical symptoms of malaria, a positive Giemsa-stained blood film for , and no signs of severe disease from Tororo and Busia districts in Uganda.

## Provenance

- Source study: [[@tumwebaze2021]]
- Paper: Drug susceptibility of Plasmodium falciparum in eastern Uganda: a longitudinal phenotypic and genotypic study.
- Journal: The Lancet. Microbe
- Published: 2021 Sep
- PubMed: [34553183](https://pubmed.ncbi.nlm.nih.gov/34553183/)
- System association ID: `wK0-67YYs8`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
