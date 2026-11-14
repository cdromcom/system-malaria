---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr1 86Y-184Y-1246Y allele frequency differed by -15.1 between Infections contracted in countries implementing amodiaquine and Infections contracted in countries with (mean difference unstandardized) - @dippmann2008"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2008"
created: 2026-11-14
updated: 2026-11-14
nodeID: a0f0ea57-f52c-4b99-8f32-55db607b04cd
title: pfmdr1 86Y-184Y-1246Y allele frequency differed by -15.1 between Infections contracted in countries implementing amodiaquine and Infections contracted in countries with (mean difference unstandardized) - @dippmann2008
---

## Source

[[@dippmann2008]]

## In plain terms

> [!info] What this finding says
> A study published in 2008 reported a statistical link between **Infections contracted in countries implementing amodiaquine/artesunate** and **pfmdr1 86Y-184Y-1246Y allele frequency**.
> Pfmdr1 86Y-184Y-1246Y allele frequency differed by -15.1 between Infections contracted in countries implementing amodiaquine and Infections contracted in countries with (mean difference unstandardized), p = 0.03.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-15.1** |
| **p-value** | = 0.03 |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 111 African isolates imported to Germany between 1997 and 2005. |
| **Intervention / exposure** | Infections contracted in countries implementing amodiaquine/artesunate |
| **Comparator** | Infections contracted in countries with artemether/lumefantrine policy |
| **Outcome** | pfmdr1 86Y-184Y-1246Y allele frequency |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2008. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Infections contracted in countries implementing amodiaquine/artesunate [vs Infections contracted in countries with artemether/lumefantrine policy]`
> Variable 2: `pfmdr1 86Y-184Y-1246Y allele frequency`
> mean difference unstandardized = -15.1, p = 0.03
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **Infections contracted in countries implementing amodiaquine/artesunate** to **pfmdr1 86Y-184Y-1246Y allele frequency**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 111 African isolates imported to Germany between 1997 and 2005.

## Provenance

- Source study: [[@dippmann2008]]
- Paper: pfmdr1 mutations in imported African Plasmodium falciparum isolates.
- Journal: Transactions of the Royal Society of Tropical Medicine and Hygiene
- Published: 2008 Nov
- PubMed: [18513774](https://pubmed.ncbi.nlm.nih.gov/18513774/)
- System association ID: `H4hbyRhN_2`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
