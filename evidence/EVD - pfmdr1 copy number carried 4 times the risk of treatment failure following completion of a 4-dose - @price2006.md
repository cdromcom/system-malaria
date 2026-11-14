---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr1 copy number carried 4 times the risk of treatment failure following completion of a 4-dose regimen (hazard ratio) - @price2006"
tags:
  - "marker/pfmdr1"
  - "theme/treatment-failure"
  - "stat/hazard_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2006"
created: 2026-11-14
updated: 2026-11-14
nodeID: 5aa0b7d0-73aa-44d7-a342-49254fe28a1a
title: pfmdr1 copy number carried 4 times the risk of treatment failure following completion of a 4-dose regimen (hazard ratio) - @price2006
---

## Source

[[@price2006]]

## In plain terms

> [!info] What this finding says
> A study published in 2006 reported a statistical link between **pfmdr1 copy number** and **risk of treatment failure following completion of a 4-dose regimen**.
> Pfmdr1 copy number carried 4 times the risk of treatment failure following completion of a 4-dose regimen (hazard ratio), p = 0.008. The confidence interval runs from 1.4 to 11.

## Statistic

| | |
|---|---|
| **Metric** | `hazard_ratio` (System's normalised type; the paper reported `hazard_ratio`) |
| **Estimate** | **4** |
| **p-value** | = 0.008 |
| **Confidence interval** | CI 1.4 to 11 (confidence level not recorded) |
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
| **Open access** | Yes (bronze) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Adults with uncomplicated Plasmodium falciparum malaria on the northwest border of Thailand. |
| **Intervention / exposure** | pfmdr1 copy number |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | risk of treatment failure following completion of a 4-dose regimen |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2006. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfmdr1 copy number`
> Variable 2: `risk of treatment failure following completion of a 4-dose regimen`
> hazard ratio = 4, p = 0.008
> CI [1.4, 11]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfmdr1 copy number** to **risk of treatment failure following completion of a 4-dose regimen**, reported as a hazard ratio.

### How?

Study design: Experimental Trial.

### Who?

> Adults with uncomplicated Plasmodium falciparum malaria on the northwest border of Thailand.

## Provenance

- Source study: [[@price2006]]
- Paper: Molecular and pharmacological determinants of the therapeutic response to artemether-lumefantrine in multidrug-resistant Plasmodium falciparum malaria.
- Journal: Clinical infectious diseases : an official publication of the Infectious Diseases Society of America
- Published: 2006 Jun 1
- PubMed: [16652314](https://pubmed.ncbi.nlm.nih.gov/16652314/)
- System association ID: `doqmxO-XNs`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
