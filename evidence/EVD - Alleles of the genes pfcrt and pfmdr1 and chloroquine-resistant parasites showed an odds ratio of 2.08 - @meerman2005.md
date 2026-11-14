---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Alleles of the genes pfcrt and pfmdr1 and chloroquine-resistant parasites showed an odds ratio of 2.08 - @meerman2005"
tags:
  - "marker/pfcrt"
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2005"
created: 2026-11-14
updated: 2026-11-14
nodeID: 8634ed44-f2b6-4cd1-a2ac-b96c47975de3
title: Alleles of the genes pfcrt and pfmdr1 and chloroquine-resistant parasites showed an odds ratio of 2.08 - @meerman2005
---

## Source

[[@meerman2005]]

## In plain terms

> [!info] What this finding says
> A study published in 2005 reported a statistical link between **Alleles of the genes pfcrt and pfmdr1** and **chloroquine-resistant parasites**.
> Alleles of the genes pfcrt and pfmdr1 and chloroquine-resistant parasites showed an odds ratio of 2.08, p = 0.039. The confidence interval runs from 1.04 to 4.38.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **2.08** |
| **p-value** | = 0.039 |
| **Confidence interval** | CI 1.04 to 4.38 (confidence level not recorded) |
| **Direction vs null of 1** | **positive** |
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
| **Population** | 234 Gambian children with severe falciparum malaria admitted to the pediatric ward of a rural district hospital and 234 same-sex controls presenting as outpatients with uncomplicated falciparum malaria. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2005. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Alleles of the genes pfcrt and pfmdr1` with `chloroquine-resistant parasites` and reports a odds ratio of 2.08. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Alleles of the genes pfcrt and pfmdr1`
> Variable 2: `chloroquine-resistant parasites`
> odds ratio = 2.08, p = 0.039
> CI [1.04, 4.38]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Alleles of the genes pfcrt and pfmdr1** to **chloroquine-resistant parasites**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 234 Gambian children with severe falciparum malaria admitted to the pediatric ward of a rural district hospital and 234 same-sex controls presenting as outpatients with uncomplicated falciparum malaria.

## Provenance

- Source study: [[@meerman2005]]
- Paper: Carriage of chloroquine-resistant parasites and delay of effective treatment increase the risk of severe malaria in Gambian children.
- Journal: The Journal of infectious diseases
- Published: 2005 Nov 1
- PubMed: [16206082](https://pubmed.ncbi.nlm.nih.gov/16206082/)
- System association ID: `861NyEbb83`
- Resistance gene(s): PfCRT, Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
