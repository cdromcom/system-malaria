---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Tanzania implementation of artemether-lumefantrine and frequency of single nucleotide polymorphisms in the Pfmdr-1 gene showed an odds ratio of 1.01 - @thomsen2011"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: 0556fbcf-bc83-40bb-ba58-7251e8a274b2
title: Tanzania implementation of artemether-lumefantrine and frequency of single nucleotide polymorphisms in the Pfmdr-1 gene showed an odds ratio of 1.01 - @thomsen2011
---

## Source

[[@thomsen2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **Tanzania implementation of artemether-lumefantrine** and **frequency of single nucleotide polymorphisms in the Pfmdr-1 gene associated with artemether-lumefantrine resistance**.
> Tanzania implementation of artemether-lumefantrine and frequency of single nucleotide polymorphisms in the Pfmdr-1 gene showed an odds ratio of 1.01, p = 0.9. The confidence interval runs from 0.8 to 1.28.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **1.01** |
| **p-value** | = 0.9 |
| **Confidence interval** | CI 0.8 to 1.28 (confidence level not recorded) |
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
> The record pairs `Tanzania implementation of artemether-lumefantrine` with `frequency of single nucleotide polymorphisms in the Pfmdr-1 gene associated with artemether-lumefantrine resistance` and reports a odds ratio of 1.01. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **artemether-lumefantrine** — a widely used artemisinin combination treatment, sold as Coartem

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Tanzania implementation of artemether-lumefantrine`
> Variable 2: `frequency of single nucleotide polymorphisms in the Pfmdr-1 gene associated with artemether-lumefantrine resistance`
> odds ratio = 1.01, p = 0.9
> CI [0.8, 1.28]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Tanzania implementation of artemether-lumefantrine** to **frequency of single nucleotide polymorphisms in the Pfmdr-1 gene associated with artemether-lumefantrine resistance**, reported as a odds ratio.

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
- System association ID: `hMu8oaGFFm`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
