---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Y184F in pfmdr1 differed by 11.1 between New infections and Prior dihydroartemisinin-piperaquine (mean difference unstandardized) - @som2010"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2010"
created: 2026-11-14
updated: 2026-11-14
nodeID: cfc4d585-771a-4bbd-bac9-7d7912b10337
title: Y184F in pfmdr1 differed by 11.1 between New infections and Prior dihydroartemisinin-piperaquine (mean difference unstandardized) - @som2010
---

## Source

[[@som2010]]

## In plain terms

> [!info] What this finding says
> A study published in 2010 reported a statistical link between **New infections** and **Y184F in pfmdr1**.
> Y184F in pfmdr1 differed by 11.1 between New infections and Prior dihydroartemisinin-piperaquine (mean difference unstandardized), p = 0.009.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **11.1** |
| **p-value** | = 0.009 |
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
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 559 children in Burkina Faso in 2006 and 378 additional treatments with DP in 2007. |
| **Intervention / exposure** | New infections |
| **Comparator** | Prior dihydroartemisinin-piperaquine therapy (pretreatment |
| **Outcome** | Y184F in pfmdr1 |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2010. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **dihydroartemisinin-piperaquine** — an artemisinin combination treatment
- **Y184F** — a mutation that swaps amino acid Y for F at position 184 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `New infections [vs Prior dihydroartemisinin-piperaquine therapy (pretreatment)]`
> Variable 2: `Y184F in pfmdr1`
> mean difference unstandardized = 11.1, p = 0.009
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **New infections** to **Y184F in pfmdr1**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 559 children in Burkina Faso in 2006 and 378 additional treatments with DP in 2007.

## Provenance

- Source study: [[@som2010]]
- Paper: Selection of known Plasmodium falciparum resistance-mediating polymorphisms by artemether-lumefantrine and amodiaquine-sulfadoxine-pyrimethamine but not dihydroartemisinin-piperaquine in Burkina Faso.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2010 May
- PubMed: [20231394](https://pubmed.ncbi.nlm.nih.gov/20231394/)
- System association ID: `r3wSm0y64A`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
