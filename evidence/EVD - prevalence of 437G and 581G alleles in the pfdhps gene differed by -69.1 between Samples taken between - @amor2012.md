---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of 437G and 581G alleles in the pfdhps gene differed by -69.1 between Samples taken between November 2008 and August 2010 (n = 46) and Samples taken between June 2002 and June (mean difference unstandardized) - @amor2012"
tags:
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2012"
created: 2026-11-14
updated: 2026-11-14
nodeID: 716c1d9b-c906-4291-ada2-188c8b0ba996
title: prevalence of 437G and 581G alleles in the pfdhps gene differed by -69.1 between Samples taken between November 2008 and August 2010 (n = 46) and Samples taken between June 2002 and June (mean difference unstandardized) - @amor2012
---

## Source

[[@amor2012]]

## In plain terms

> [!info] What this finding says
> A study published in 2012 reported a statistical link between **Samples taken between November 2008 and August 2010 (n = 46)** and **prevalence of 437G and 581G alleles in the pfdhps gene**.
> Prevalence of 437G and 581G alleles in the pfdhps gene differed by -69.1 between Samples taken between November 2008 and August 2010 (n = 46) and Samples taken between June 2002 and June (mean difference unstandardized), p = 0.024.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-69.1** |
| **p-value** | = 0.024 |
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
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Plasmodium falciparum isolates imported from Africa in two groups, one taken between June 2002 and June 2006 (n = 113) and the other between November 2008 and August 2010 (n = 46). |
| **Intervention / exposure** | Samples taken between November 2008 and August 2010 (n = 46) |
| **Comparator** | Samples taken between June 2002 and June 2006 (n = 113 |
| **Outcome** | prevalence of 437G and 581G alleles in the pfdhps gene |
| **Setting** | Africa in two groups |
| **Timeframe** | Published 2012. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Samples taken between November 2008 and August 2010 (n = 46) [vs Samples taken between June 2002 and June 2006 (n = 113)]`
> Variable 2: `prevalence of 437G and 581G alleles in the pfdhps gene`
> mean difference unstandardized = -69.1, p = 0.024
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **Samples taken between November 2008 and August 2010 (n = 46)** to **prevalence of 437G and 581G alleles in the pfdhps gene**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Plasmodium falciparum isolates imported from Africa in two groups, one taken between June 2002 and June 2006 (n = 113) and the other between November 2008 and August 2010 (n = 46).

## Provenance

- Source study: [[@amor2012]]
- Paper: Molecular markers in plasmodium falciparum linked to resistance to anti-malarial drugs in samples imported from Africa over an eight-year period (2002-2010): impact of the introduction of artemisinin combination therapy.
- Journal: Malaria journal
- Published: 2012 Mar 30
- PubMed: [22462737](https://pubmed.ncbi.nlm.nih.gov/22462737/)
- System association ID: `iA0zb6Dzku`
- Resistance gene(s): PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
