---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Presence of Plasmodium falciparum chloroquine resistance carried 2.6 times the Overall clinical failure rates (odds ratio) - @meissner2008"
tags:
  - "marker/pfcrt"
  - "theme/treatment-failure"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2008"
created: 2026-11-14
updated: 2026-11-14
nodeID: 873ee8c4-bff8-4b9e-874c-2adb70b3b301
title: Presence of Plasmodium falciparum chloroquine resistance carried 2.6 times the Overall clinical failure rates (odds ratio) - @meissner2008
---

## Source

[[@meissner2008]]

## In plain terms

> [!info] What this finding says
> A study published in 2008 reported a statistical link between **Presence of Plasmodium falciparum chloroquine resistance transporter gene T76 mutation** and **Overall clinical failure rates**.
> Presence of Plasmodium falciparum chloroquine resistance carried 2.6 times the Overall clinical failure rates (odds ratio), p = 0.005. The confidence interval runs from 1.33 to 5.16.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **2.6** |
| **p-value** | = 0.005 |
| **Confidence interval** | CI 1.33 to 5.16 (confidence level not recorded) |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Young children from urban and rural areas in Burkina Faso. |
| **Intervention / exposure** | Presence of Plasmodium falciparum chloroquine resistance transporter gene T76 mutation |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | Overall clinical failure rates |
| **Setting** | Burkina Faso |
| **Timeframe** | Published 2008. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Presence of Plasmodium falciparum chloroquine resistance transporter gene T76 mutation`
> Variable 2: `Overall clinical failure rates`
> odds ratio = 2.6, p = 0.005
> CI [1.33, 5.16]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Presence of Plasmodium falciparum chloroquine resistance transporter gene T76 mutation** to **Overall clinical failure rates**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Young children from urban and rural areas in Burkina Faso.

## Provenance

- Source study: [[@meissner2008]]
- Paper: Marked differences in the prevalence of chloroquine resistance between urban and rural communities in Burkina Faso.
- Journal: Acta tropica
- Published: 2008 Jan
- PubMed: [17904509](https://pubmed.ncbi.nlm.nih.gov/17904509/)
- System association ID: `SFOtKSALEi`
- Resistance gene(s): PfCRT
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
