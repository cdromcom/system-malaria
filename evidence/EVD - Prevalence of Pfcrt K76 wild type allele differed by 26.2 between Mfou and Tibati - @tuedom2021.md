---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Prevalence of Pfcrt K76 wild type allele differed by 26.2 between Mfou and Tibati (mean difference unstandardized) - @tuedom2021"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: 003eeed2-fc4f-49b5-ab4a-e81a48007317
title: Prevalence of Pfcrt K76 wild type allele differed by 26.2 between Mfou and Tibati (mean difference unstandardized) - @tuedom2021
---

## Source

[[@tuedom2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **Mfou** and **Prevalence of Pfcrt K76 wild type allele**.
> Prevalence of Pfcrt K76 wild type allele differed by 26.2 between Mfou and Tibati (mean difference unstandardized), p = 0.0001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **26.2** |
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
| **Open access** | Yes (gold) |
| **Open data** | A statement exists but is not explicit |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Asymptomatic individuals in Cameroon in 2018 and 2019. |
| **Intervention / exposure** | Mfou |
| **Comparator** | Tibati |
| **Outcome** | Prevalence of Pfcrt K76 wild type allele |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

> [!warning] Possible extraction mismatch
> This record names **PfCRT**, but the source paper's title mentions pfmdr1, pfdhfr, pfdhps instead. The paper may well cover both, but check it against the article before citing.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Mfou [vs Tibati]`
> Variable 2: `Prevalence of Pfcrt K76 wild type allele`
> mean difference unstandardized = 26.2, p = 0.0001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Mfou** to **Prevalence of Pfcrt K76 wild type allele**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Asymptomatic individuals in Cameroon in 2018 and 2019.

## Provenance

- Source study: [[@tuedom2021]]
- Paper: Antimalarial drug resistance in the Central and Adamawa regions of Cameroon: Prevalence of mutations in P. falciparum crt, Pfmdr1, Pfdhfr and Pfdhps genes.
- Journal: PloS one
- Published: 2021
- PubMed: [34411157](https://pubmed.ncbi.nlm.nih.gov/34411157/)
- System association ID: `lDu8-xMHxo`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
