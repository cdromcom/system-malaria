---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - R622I mutation frequency differed by 17 between R622I mutation in Gondar Zuria and R622I mutation in Tach Armachiho (mean difference unstandardized) - @zeleke2025"
tags:
  - "marker/pfkelch13"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2025"
created: 2026-11-14
updated: 2026-11-14
nodeID: 75af16c1-8c92-4b53-9d01-317c3c587346
title: R622I mutation frequency differed by 17 between R622I mutation in Gondar Zuria and R622I mutation in Tach Armachiho (mean difference unstandardized) - @zeleke2025
---

## Source

[[@zeleke2025]]

## In plain terms

> [!info] What this finding says
> A study published in 2025 reported a statistical link between **R622I mutation in Gondar Zuria** and **R622I mutation frequency**.
> R622I mutation frequency differed by 17 between R622I mutation in Gondar Zuria and R622I mutation in Tach Armachiho (mean difference unstandardized), p = 0.001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **17** |
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
| **Open data** | Deposited in a public repository — MalariaGEN, Sequence Read Archive, SRA, zenodo |
| **Open code** | github.com/Mrc-ide/mipanalyzer, github.com/bailey-lab/MIPTools, github.com/bailey-lab/miplicorn, github.com/daniellyer/vcfR, github.com/gtollefson/Northern_Ethiopia_Pf_ARTR_2025_Project |
| **Public accessions** | PRJNA1269601 |

## PICOST

| | |
|---|---|
| **Population** | Not recorded in the graph. |
| **Intervention / exposure** | R622I mutation in Gondar Zuria |
| **Comparator** | R622I mutation in Tach Armachiho |
| **Outcome** | R622I mutation frequency |
| **Setting** | Not recorded in the graph. |
| **Timeframe** | Published 2025. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **R622I** — a mutation that swaps amino acid R for I at position 622 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `R622I mutation in Gondar Zuria [vs R622I mutation in Tach Armachiho]`
> Variable 2: `R622I mutation frequency`
> mean difference unstandardized = 17, p = 0.001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **R622I mutation in Gondar Zuria** to **R622I mutation frequency**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> The graph holds no description of who was studied.

## Provenance

- Source study: [[@zeleke2025]]
- Paper: High prevalence and emerging positive association of kelch13 R622I and HRP2-based RDT negativity in Plasmodium falciparum in northern Ethiopia.
- Journal: PLoS pathogens
- Published: 2025 Dec
- PubMed: [41379859](https://pubmed.ncbi.nlm.nih.gov/41379859/)
- System association ID: `liOkQhAwhXtm`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
