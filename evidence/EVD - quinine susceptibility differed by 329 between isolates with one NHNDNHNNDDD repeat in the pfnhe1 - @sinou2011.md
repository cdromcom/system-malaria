---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - quinine susceptibility differed by 329 between isolates with one NHNDNHNNDDD repeat in the pfnhe1 microsatellite and isolates with two NHNDNHNNDDD repeats in (mean difference unstandardized) - @sinou2011"
tags:
  - "marker/other-markers"
  - "theme/drug-susceptibility"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: e24f4210-7beb-4885-8d56-e4ac7b85cb3b
title: quinine susceptibility differed by 329 between isolates with one NHNDNHNNDDD repeat in the pfnhe1 microsatellite and isolates with two NHNDNHNNDDD repeats in (mean difference unstandardized) - @sinou2011
---

## Source

[[@sinou2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **isolates with one NHNDNHNNDDD repeat in the pfnhe1 microsatellite ms4760 locus** and **quinine susceptibility**.
> Quinine susceptibility differed by 329 between isolates with one NHNDNHNNDDD repeat in the pfnhe1 microsatellite and isolates with two NHNDNHNNDDD repeats in (mean difference unstandardized), p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **329** |
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
| **Open data** | Deposited in a public repository — Genbank |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 98 isolates of Plasmodium falciparum obtained from three different regions of the Binh Phuoc and Dak Nong provinces in Vietnam during 2006-2008. |
| **Intervention / exposure** | isolates with one NHNDNHNNDDD repeat in the pfnhe1 microsatellite ms4760 locus |
| **Comparator** | isolates with two NHNDNHNNDDD repeats in the pfnhe1 microsatellite ms4760 locus |
| **Outcome** | quinine susceptibility |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `isolates with one NHNDNHNNDDD repeat in the pfnhe1 microsatellite ms4760 locus [vs isolates with two NHNDNHNNDDD repeats in the pfnhe1 microsatellite ms4760 locus]`
> Variable 2: `quinine susceptibility`
> mean difference unstandardized = 329, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **isolates with one NHNDNHNNDDD repeat in the pfnhe1 microsatellite ms4760 locus** to **quinine susceptibility**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 98 isolates of Plasmodium falciparum obtained from three different regions of the Binh Phuoc and Dak Nong provinces in Vietnam during 2006-2008.

## Provenance

- Source study: [[@sinou2011]]
- Paper: Polymorphism of Plasmodium falciparum Na(+)/H(+) exchanger is indicative of a low in vitro quinine susceptibility in isolates from Viet Nam.
- Journal: Malaria journal
- Published: 2011 Jun 14
- PubMed: [21669011](https://pubmed.ncbi.nlm.nih.gov/21669011/)
- System association ID: `9i2DZZxfiF`
- Resistance gene(s): Other markers
- Outcome theme(s): how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
