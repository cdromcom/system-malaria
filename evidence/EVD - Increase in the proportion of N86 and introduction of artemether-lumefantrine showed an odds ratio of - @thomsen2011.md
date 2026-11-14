---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Increase in the proportion of N86 and introduction of artemether-lumefantrine showed an odds ratio of 1.35 - @thomsen2011"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: 3dd16557-0642-48a0-b681-9eac64ac1080
title: Increase in the proportion of N86 and introduction of artemether-lumefantrine showed an odds ratio of 1.35 - @thomsen2011
---

## Source

[[@thomsen2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **Increase in the proportion of N86 (amino acid substitution at codon 86) in Pfmdr-1 gene associated with artemether-lumefantrine resistance** and **introduction of artemether-lumefantrine**.
> Increase in the proportion of N86 and introduction of artemether-lumefantrine showed an odds ratio of 1.35, p = 0.01. The confidence interval runs from 1.07 to 1.71.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **1.35** |
| **p-value** | = 0.01 |
| **Confidence interval** | CI 1.07 to 1.71 (confidence level not recorded) |
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
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 830 Plasmodium falciparum-positive samples collected between 2003 and 2010 in Tanzania. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Tanzania |
| **Timeframe** | 0, published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Increase in the proportion of N86 (amino acid substitution at codon 86) in Pfmdr-1 gene associated with artemether-lumefantrine resistance` with `introduction of artemether-lumefantrine` and reports a odds ratio of 1.35. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **artemether-lumefantrine** — a widely used artemisinin combination treatment, sold as Coartem

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Increase in the proportion of N86 (amino acid substitution at codon 86) in Pfmdr-1 gene associated with artemether-lumefantrine resistance`
> Variable 2: `introduction of artemether-lumefantrine`
> odds ratio = 1.35, p = 0.01
> CI [1.07, 1.71]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Increase in the proportion of N86 (amino acid substitution at codon 86) in Pfmdr-1 gene associated with artemether-lumefantrine resistance** to **introduction of artemether-lumefantrine**, reported as a odds ratio.

### How?

Study design: 0.

### Who?

> 830 Plasmodium falciparum-positive samples collected between 2003 and 2010 in Tanzania.

## Provenance

- Source study: [[@thomsen2011]]
- Paper: Prevalence of single nucleotide polymorphisms in the Plasmodium falciparum multidrug resistance gene (Pfmdr-1) in Korogwe District in Tanzania before and after introduction of artemisinin-based combination therapy.
- Journal: The American journal of tropical medicine and hygiene
- Published: 2011 Dec
- PubMed: [22144430](https://pubmed.ncbi.nlm.nih.gov/22144430/)
- System association ID: `uwXl6i83ot`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
