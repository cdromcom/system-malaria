---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Prevalence of the dhfr59Arg mutant-type (2005) vs. Prevalence of and Prevalence of sulfadoxine-pyrimethamine resistance-associated showed a mean difference unstandardized of 23.9 - @hailemeskel2013"
tags:
  - "marker/pfdhfr"
  - "marker/other-markers"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2013"
created: 2026-11-14
updated: 2026-11-14
nodeID: 717d3143-f55c-4a56-b44a-68d437af74bc
title: Prevalence of the dhfr59Arg mutant-type (2005) vs. Prevalence of and Prevalence of sulfadoxine-pyrimethamine resistance-associated showed a mean difference unstandardized of 23.9 - @hailemeskel2013
---

## Source

[[@hailemeskel2013]]

## In plain terms

> [!info] What this finding says
> A study published in 2013 reported a statistical link between **Prevalence of the dhfr59Arg mutant-type (2005) vs. Prevalence of the wild type dhfr59Cys haplotypes (2008)** and **Prevalence of sulfadoxine-pyrimethamine resistance-associated mutations in dhfr and dhps genes of P. falciparum**.
> Prevalence of the dhfr59Arg mutant-type (2005) vs. Prevalence of and Prevalence of sulfadoxine-pyrimethamine resistance-associated showed a mean difference unstandardized of 23.9, p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **23.9** |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 165 patients infected with Plasmodium falciparum in Bahir Dar, Northwest Ethiopia in 2005 and 2008. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Bahir Dar |
| **Timeframe** | Published 2013. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Prevalence of the dhfr59Arg mutant-type (2005) vs. Prevalence of the wild type dhfr59Cys haplotypes (2008)` with `Prevalence of sulfadoxine-pyrimethamine resistance-associated mutations in dhfr and dhps genes of P. falciparum` and reports a mean difference unstandardized of 23.9. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Prevalence of the dhfr59Arg mutant-type (2005) vs. Prevalence of the wild type dhfr59Cys haplotypes (2008)`
> Variable 2: `Prevalence of sulfadoxine-pyrimethamine resistance-associated mutations in dhfr and dhps genes of P. falciparum`
> mean difference unstandardized = 23.9, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Prevalence of the dhfr59Arg mutant-type (2005) vs. Prevalence of the wild type dhfr59Cys haplotypes (2008)** to **Prevalence of sulfadoxine-pyrimethamine resistance-associated mutations in dhfr and dhps genes of P. falciparum**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 165 patients infected with Plasmodium falciparum in Bahir Dar, Northwest Ethiopia in 2005 and 2008.

## Provenance

- Source study: [[@hailemeskel2013]]
- Paper: Prevalence of sulfadoxine-pyrimethamine resistance-associated mutations in dhfr and dhps genes of Plasmodium falciparum three years after SP withdrawal in Bahir Dar, Northwest Ethiopia.
- Journal: Acta tropica
- Published: 2013 Dec
- PubMed: [24055717](https://pubmed.ncbi.nlm.nih.gov/24055717/)
- System association ID: `y5nghPrl5_`
- Resistance gene(s): PfDHFR, Other markers
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
