---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Proportion of isolates with at least a triple Pfdhfr mutation differed by 57.7 between Pregnant women in 2011 (after IPTp-SP (sulfadoxine-pyrimethamine) implementation) and Pregnant women in 2005 (mean difference unstandardized) - @bouyouakotet2015"
tags:
  - "marker/pfdhfr"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2015"
created: 2026-11-14
updated: 2026-11-14
nodeID: 2cafcc8c-d47f-447a-810b-3b828806e23c
title: Proportion of isolates with at least a triple Pfdhfr mutation differed by 57.7 between Pregnant women in 2011 (after IPTp-SP (sulfadoxine-pyrimethamine) implementation) and Pregnant women in 2005 (mean difference unstandardized) - @bouyouakotet2015
---

## Source

[[@bouyouakotet2015]]

## In plain terms

> [!info] What this finding says
> A study published in 2015 reported a statistical link between **Pregnant women in 2011 (after IPTp-SP (sulfadoxine-pyrimethamine) implementation)** and **Proportion of isolates with at least a triple Pfdhfr mutation**.
> Proportion of isolates with at least a triple Pfdhfr mutation differed by 57.7 between Pregnant women in 2011 (after IPTp-SP (sulfadoxine-pyrimethamine) implementation) and Pregnant women in 2005 (mean difference unstandardized), p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **57.7** |
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
| **Population** | Pregnant women living in Gabon in 2005 and 2011. |
| **Intervention / exposure** | Pregnant women in 2011 (after IPTp-SP implementation) |
| **Comparator** | Pregnant women in 2005 (before IPTp-SP implementation |
| **Outcome** | Proportion of isolates with at least a triple Pfdhfr mutation |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2015. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children
- **IPTp** — intermittent preventive treatment in pregnancy, where pregnant women are given antimalarial drugs at routine visits whether or not they are infected

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pregnant women in 2011 (after IPTp-SP implementation) [vs Pregnant women in 2005 (before IPTp-SP implementation)]`
> Variable 2: `Proportion of isolates with at least a triple Pfdhfr mutation`
> mean difference unstandardized = 57.7, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Pregnant women in 2011 (after IPTp-SP (sulfadoxine-pyrimethamine) implementation)** to **Proportion of isolates with at least a triple Pfdhfr mutation**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Pregnant women living in Gabon in 2005 and 2011.

## Provenance

- Source study: [[@bouyouakotet2015]]
- Paper: Frequencies of dhfr/dhps multiple mutations and Plasmodium falciparum submicroscopic gametocyte carriage in Gabonese pregnant women following IPTp-SP implementation.
- Journal: Acta parasitologica
- Published: 2015 Jun
- PubMed: [26203988](https://pubmed.ncbi.nlm.nih.gov/26203988/)
- System association ID: `RekfGhbfvJ`
- Resistance gene(s): PfDHFR
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
