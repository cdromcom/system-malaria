---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Mutations in the Plasmodium falciparum genes Pfdhfr and Pfdhps and birth weight showed a mean difference unstandardized of -461 - @hansson2021"
tags:
  - "marker/pfdhfr"
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "theme/severe-illness"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/in-curated-deposit"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: 52420ca2-1dbc-41d6-8ed7-feaffc1b931a
title: Mutations in the Plasmodium falciparum genes Pfdhfr and Pfdhps and birth weight showed a mean difference unstandardized of -461 - @hansson2021
---

## Source

[[@hansson2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **Mutations in the Plasmodium falciparum genes Pfdhfr and Pfdhps, particularly the sextuple mutant haplotype** and **birth weight**.
> Mutations in the Plasmodium falciparum genes Pfdhfr and Pfdhps and birth weight showed a mean difference unstandardized of -461, p = 0.03. The confidence interval runs from -877 to -44.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-461** |
| **p-value** | = 0.03 |
| **Confidence interval** | CI -877 to -44 (confidence level not recorded) |
| **Direction vs null of 0** | **negative** |
| **Data source** | API list, API detail, Dataverse release |
| **In curated release** | Yes |
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
| **Population** | Pregnant women in malaria-endemic areas who were monitored from before conception or from the first trimester until delivery. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Mutations in the Plasmodium falciparum genes Pfdhfr and Pfdhps, particularly the sextuple mutant haplotype` with `birth weight` and reports a mean difference unstandardized of -461. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Mutations in the Plasmodium falciparum genes Pfdhfr and Pfdhps, particularly the sextuple mutant haplotype`
> Variable 2: `birth weight`
> mean difference unstandardized = -461, p = 0.03
> CI [-877, -44]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **Mutations in the Plasmodium falciparum genes Pfdhfr and Pfdhps, particularly the sextuple mutant haplotype** to **birth weight**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Pregnant women in malaria-endemic areas who were monitored from before conception or from the first trimester until delivery.

## Provenance

- Source study: [[@hansson2021]]
- Paper: Reduced Birth Weight Caused by Sextuple Drug-Resistant Plasmodium falciparum Infection in Early Second Trimester.
- Journal: The Journal of infectious diseases
- Published: 2021 Nov 16
- PubMed: [33684211](https://pubmed.ncbi.nlm.nih.gov/33684211/)
- System association ID: `489sn1mPQa`
- Resistance gene(s): PfDHFR, PfDHPS
- Outcome theme(s): how common the resistance mutation was, severe illness, death and birth weight

## Verification

> [!success] Checked against the curated dataset
> This finding also appears in System's curated Harvard Dataverse release, from which the extractions System had flagged as inaccurate were removed. That is the best available sign that the number was read correctly from the paper.

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
