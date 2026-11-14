---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Chloroquine treatment type and manufacturer and Chloroquine resistant Plasmodium falciparum showed a mean difference unstandardized of -18.8 - @antiaobong1997"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/1997"
created: 2026-11-14
updated: 2026-11-14
nodeID: 427e929f-a36d-4a65-ad4e-69082e7c1757
title: Chloroquine treatment type and manufacturer and Chloroquine resistant Plasmodium falciparum showed a mean difference unstandardized of -18.8 - @antiaobong1997
---

## Source

[[@antiaobong1997]]

## In plain terms

> [!info] What this finding says
> A study published in 1997 reported a statistical link between **Chloroquine treatment type and manufacturer (Pharma Deko suppository vs May & Baker syrup)** and **Chloroquine resistant Plasmodium falciparum**.
> Chloroquine treatment type and manufacturer and Chloroquine resistant Plasmodium falciparum showed a mean difference unstandardized of -18.8, p = 0.05.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-18.8** |
| **p-value** | = 0.05 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **negative** |
| **Data source** | API list, API detail |
| **In curated release** | No |
| **Source paper integrity** | a published erratum exists (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: Clean) |
| **Published erratum** | Yes — PubMed CommentsCorrections ErratumIn |
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
| **Population** | Sixty-nine children aged between 6 and 60 months with parasitologically proven Plasmodium falciparum malaria who were treated with chloroquine in the Children's Emergency Room of the University of Calabar Teaching Hospital (UCTH) in 1993. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 1997. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Chloroquine treatment type and manufacturer (Pharma Deko suppository vs May & Baker syrup)` with `Chloroquine resistant Plasmodium falciparum` and reports a mean difference unstandardized of -18.8. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] The source paper has a published erratum
> PubMed CommentsCorrections ErratumIn
> System extracted this statistic from the original article, and the graph records nothing about corrections. The number above may be one the erratum changed. Check the correction notice before citing it.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Chloroquine treatment type and manufacturer (Pharma Deko suppository vs May & Baker syrup)`
> Variable 2: `Chloroquine resistant Plasmodium falciparum`
> mean difference unstandardized = -18.8, p = 0.05
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **Chloroquine treatment type and manufacturer (Pharma Deko suppository vs May & Baker syrup)** to **Chloroquine resistant Plasmodium falciparum**, reported as a mean difference unstandardized.

### How?

Study design: Experimental Trial.

### Who?

> Sixty-nine children aged between 6 and 60 months with parasitologically proven Plasmodium falciparum malaria who were treated with chloroquine in the Children's Emergency Room of the University of Calabar Teaching Hospital (UCTH) in 1993.

## Provenance

- Source study: [[@antiaobong1997]]
- Paper: Chloroquine-resistant Plasmodium falciparum among children in Calabar, south eastern Nigeria.
- Journal: Tropical doctor
- Published: 1997 Jul
- PubMed: [9227007](https://pubmed.ncbi.nlm.nih.gov/9227007/)
- System association ID: `WP6sNL9mFo`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
