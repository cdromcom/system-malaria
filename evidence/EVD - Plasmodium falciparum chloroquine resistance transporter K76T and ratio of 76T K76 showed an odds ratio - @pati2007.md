---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Plasmodium falciparum chloroquine resistance transporter K76T and ratio of 76T K76 showed an odds ratio of 3.1 - @pati2007"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2007"
created: 2026-11-14
updated: 2026-11-14
nodeID: b19e551e-9b45-429f-a459-b0094ce68610
title: Plasmodium falciparum chloroquine resistance transporter K76T and ratio of 76T K76 showed an odds ratio of 3.1 - @pati2007
---

## Source

[[@pati2007]]

## In plain terms

> [!info] What this finding says
> A study published in 2007 reported a statistical link between **Plasmodium falciparum chloroquine resistance transporter K76T mutation and haplotype (amino acids 72-76)** and **ratio of 76T:K76**.
> Plasmodium falciparum chloroquine resistance transporter K76T and ratio of 76T K76 showed an odds ratio of 3.1. The confidence interval runs from 0.9 to 11.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **3.1** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 0.9 to 11 (confidence level not recorded) |
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
| **Population** | Adults and children from two sites of different intensities of malaria transmission in Sundergarh district of Orissa, India. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Sundergarh district of Orissa |
| **Timeframe** | Published 2007. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Plasmodium falciparum chloroquine resistance transporter K76T mutation and haplotype (amino acids 72-76)` with `ratio of 76T:K76` and reports a odds ratio of 3.1. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **K76T** — a mutation that swaps amino acid K for T at position 76 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Plasmodium falciparum chloroquine resistance transporter K76T mutation and haplotype (amino acids 72-76)`
> Variable 2: `ratio of 76T:K76`
> odds ratio = 3.1
> CI [0.9, 11]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Plasmodium falciparum chloroquine resistance transporter K76T mutation and haplotype (amino acids 72-76)** to **ratio of 76T:K76**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Adults and children from two sites of different intensities of malaria transmission in Sundergarh district of Orissa, India.

## Provenance

- Source study: [[@pati2007]]
- Paper: Pfcrt haplotypes and in-vivo chloroquine response in Sundergarh district, Orissa, India.
- Journal: Transactions of the Royal Society of Tropical Medicine and Hygiene
- Published: 2007 Jul
- PubMed: [17428514](https://pubmed.ncbi.nlm.nih.gov/17428514/)
- System association ID: `SVdS5z0yhC`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
