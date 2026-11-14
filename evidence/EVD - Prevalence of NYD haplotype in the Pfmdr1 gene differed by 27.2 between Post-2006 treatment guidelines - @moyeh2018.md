---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Prevalence of NYD haplotype in the Pfmdr1 gene differed by 27.2 between Post-2006 treatment guidelines (2009-2013) and Pre-2006 treatment guidelines (2003-2005) (mean difference unstandardized) - @moyeh2018"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2018"
created: 2026-11-14
updated: 2026-11-14
nodeID: a112d9b0-43da-47c2-a0ff-1cad1ea81a77
title: Prevalence of NYD haplotype in the Pfmdr1 gene differed by 27.2 between Post-2006 treatment guidelines (2009-2013) and Pre-2006 treatment guidelines (2003-2005) (mean difference unstandardized) - @moyeh2018
---

## Source

[[@moyeh2018]]

## In plain terms

> [!info] What this finding says
> A study published in 2018 reported a statistical link between **Post-2006 treatment guidelines (2009-2013) (artemisinin-based combination (artemisinin-based combination therapy) therapy)** and **Prevalence of NYD haplotype in the Pfmdr1 gene**.
> Prevalence of NYD haplotype in the Pfmdr1 gene differed by 27.2 between Post-2006 treatment guidelines (2009-2013) and Pre-2006 treatment guidelines (2003-2005) (mean difference unstandardized), p = 0.0001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **27.2** |
| **p-value** | = 0.0001 |
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
| **Open access** | Yes (diamond) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Individuals from Mutengene, Cameroon who provided dry blood samples for parasite DNA extraction from 2003-2005 and 2009-2013. |
| **Intervention / exposure** | Post-2006 treatment guidelines (2009-2013) (artemisinin-based combination therapy) |
| **Comparator** | Pre-2006 treatment guidelines (2003-2005) (nonartemisinin monotherapy |
| **Outcome** | Prevalence of NYD haplotype in the Pfmdr1 gene |
| **Setting** | Mutengene |
| **Timeframe** | Published 2018. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **artemisinin-based combination therapy** — the standard first-line malaria treatment, pairing artemisinin with a longer-acting partner drug

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Post-2006 treatment guidelines (2009-2013) (artemisinin-based combination therapy) [vs Pre-2006 treatment guidelines (2003-2005) (nonartemisinin monotherapy)]`
> Variable 2: `Prevalence of NYD haplotype in the Pfmdr1 gene`
> mean difference unstandardized = 27.2, p = 0.0001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Post-2006 treatment guidelines (2009-2013) (artemisinin-based combination (artemisinin-based combination therapy) therapy)** to **Prevalence of NYD haplotype in the Pfmdr1 gene**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Individuals from Mutengene, Cameroon who provided dry blood samples for parasite DNA extraction from 2003-2005 and 2009-2013.

## Provenance

- Source study: [[@moyeh2018]]
- Paper: Effects of Drug Policy Changes on Evolution of Molecular Markers of Plasmodium falciparum Resistance to Chloroquine, Amodiaquine, and Sulphadoxine-Pyrimethamine in the South West Region of Cameroon.
- Journal: Malaria research and treatment
- Published: 2018
- PubMed: [29854394](https://pubmed.ncbi.nlm.nih.gov/29854394/)
- System association ID: `cYLmh4l7Rb`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
