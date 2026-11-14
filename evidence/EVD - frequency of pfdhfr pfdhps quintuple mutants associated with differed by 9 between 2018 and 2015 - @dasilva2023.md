---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - frequency of pfdhfr pfdhps quintuple mutants associated with differed by 9 between 2018 and 2015 (mean difference unstandardized) - @dasilva2023"
tags:
  - "marker/pfdhfr"
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2023"
created: 2026-11-14
updated: 2026-11-14
nodeID: 30709fc6-041c-4825-8ea8-2dca8adfeb59
title: frequency of pfdhfr pfdhps quintuple mutants associated with differed by 9 between 2018 and 2015 (mean difference unstandardized) - @dasilva2023
---

## Source

[[@dasilva2023]]

## In plain terms

> [!info] What this finding says
> A study published in 2023 reported a statistical link between **2018** and **frequency of pfdhfr/pfdhps quintuple mutants associated with sulfadoxine-pyrimethamine resistance**.
> Frequency of pfdhfr pfdhps quintuple mutants associated with differed by 9 between 2018 and 2015 (mean difference unstandardized), p = 0.001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **9** |
| **p-value** | = 0.001 |
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
| **Open data** | Deposited in a public repository — ENA, European Nucleotide Archive, Figshare, MalariaGEN, Sequence Read Archive, SRA |
| **Open code** | github.com/EPPIcenter/moire |
| **Public accessions** | PRJEB2136, PRJNA910151 |

## PICOST

| | |
|---|---|
| **Population** | 2251 malaria-infected blood samples collected in 2015 and 2018 in seven provinces of Mozambique. |
| **Intervention / exposure** | 2018 |
| **Comparator** | 2015 |
| **Outcome** | frequency of pfdhfr/pfdhps quintuple mutants associated with sulfadoxine-pyrimethamine resistance |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2023. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `2018 [vs 2015]`
> Variable 2: `frequency of pfdhfr/pfdhps quintuple mutants associated with sulfadoxine-pyrimethamine resistance`
> mean difference unstandardized = 9, p = 0.001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **2018** to **frequency of pfdhfr/pfdhps quintuple mutants associated with sulfadoxine-pyrimethamine resistance**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 2251 malaria-infected blood samples collected in 2015 and 2018 in seven provinces of Mozambique.

## Provenance

- Source study: [[@dasilva2023]]
- Paper: Targeted and whole-genome sequencing reveal a north-south divide in P. falciparum drug resistance markers and genetic structure in Mozambique.
- Journal: Communications biology
- Published: 2023 Jun 8
- PubMed: [37291425](https://pubmed.ncbi.nlm.nih.gov/37291425/)
- System association ID: `TIBuU6xBZ3`
- Resistance gene(s): PfDHFR, PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
