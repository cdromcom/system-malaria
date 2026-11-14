---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence differed by -13 between Pfcrt wild-type haplotype in 2019 and Pfcrt wild-type haplotype in 2020 (mean difference unstandardized) - @traore2025"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2025"
created: 2026-11-14
updated: 2026-11-14
nodeID: 11cb3a8a-67a2-45c4-a8ef-888050a3b914
title: prevalence differed by -13 between Pfcrt wild-type haplotype in 2019 and Pfcrt wild-type haplotype in 2020 (mean difference unstandardized) - @traore2025
---

## Source

[[@traore2025]]

## In plain terms

> [!info] What this finding says
> A study published in 2025 reported a statistical link between **Pfcrt wild-type haplotype in 2019** and **prevalence (of Pfcrt wild-type haplotype in 2019 vs Pfcrt wild-type haplotype in 2020)**.
> Prevalence differed by -13 between Pfcrt wild-type haplotype in 2019 and Pfcrt wild-type haplotype in 2020 (mean difference unstandardized), p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-13** |
| **p-value** | = 0.01 |
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
| **Open access** | Yes (diamond) |
| **Open data** | Deposited in a public repository — ClinicalTrials.gov, Sequence Read Archive, SRA |
| **Open code** | None found |
| **Public accessions** | PRJNA1299543 |

## PICOST

| | |
|---|---|
| **Population** | Plasmodium falciparum-positive samples from Koulikoro (Mali) analyzed for molecular markers of resistance to SP + AQ and DHA + PQ. |
| **Intervention / exposure** | Pfcrt wild-type haplotype in 2019 |
| **Comparator** | Pfcrt wild-type haplotype in 2020 |
| **Outcome** | prevalence (of Pfcrt wild-type haplotype in 2019 vs Pfcrt wild-type haplotype in 2020) |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2025. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pfcrt wild-type haplotype in 2019 [vs Pfcrt wild-type haplotype in 2020]`
> Variable 2: `prevalence (of Pfcrt wild-type haplotype in 2019 vs Pfcrt wild-type haplotype in 2020)`
> mean difference unstandardized = -13, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **Pfcrt wild-type haplotype in 2019** to **prevalence (of Pfcrt wild-type haplotype in 2019 vs Pfcrt wild-type haplotype in 2020)**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Plasmodium falciparum-positive samples from Koulikoro (Mali) analyzed for molecular markers of resistance to SP + AQ and DHA + PQ.

## Provenance

- Source study: [[@traore2025]]
- Paper: Frequencies of molecular markers of drug resistance in the context of two different Seasonal Malaria Chemoprevention (SMC) treatment regimens in the Koulikoro health district, Mali.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2025 Oct
- PubMed: [40823868](https://pubmed.ncbi.nlm.nih.gov/40823868/)
- System association ID: `3Lc88bCxxp`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
