---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - presence of Pfmrp1 1466K allele differed by 32.5 between children with recrudescent (recrudescence) infections and baseline samples from children with acute (mean difference unstandardized) - @dahlstrm2009"
tags:
  - "marker/other-markers"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2009"
created: 2026-11-14
updated: 2026-11-14
nodeID: ad5516db-1151-4aaa-bfab-38a522437dc3
title: presence of Pfmrp1 1466K allele differed by 32.5 between children with recrudescent (recrudescence) infections and baseline samples from children with acute (mean difference unstandardized) - @dahlstrm2009
---

## Source

[[@dahlstrm2009]]

## In plain terms

> [!info] What this finding says
> A study published in 2009 reported a statistical link between **children with recrudescent (recrudescence) infections** and **presence of Pfmrp1 1466K allele**.
> Presence of Pfmrp1 1466K allele differed by 32.5 between children with recrudescent (recrudescence) infections and baseline samples from children with acute (mean difference unstandardized), p = 0.017.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **32.5** |
| **p-value** | = 0.017 |
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
| **Population** | Children with acute uncomplicated P. falciparum malaria in Tanzania. |
| **Intervention / exposure** | children with recrudescent infections |
| **Comparator** | baseline samples from children with acute uncomplicated P. falciparum malaria in Tanzania |
| **Outcome** | presence of Pfmrp1 1466K allele |
| **Setting** | Tanzania |
| **Timeframe** | Experimental Trial, published 2009. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **recrudescence** — the original infection returning after treatment, as opposed to a fresh mosquito bite

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `children with recrudescent infections [vs baseline samples from children with acute uncomplicated P. falciparum malaria in Tanzania]`
> Variable 2: `presence of Pfmrp1 1466K allele`
> mean difference unstandardized = 32.5, p = 0.017
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **children with recrudescent (recrudescence) infections** to **presence of Pfmrp1 1466K allele**, reported as a mean difference unstandardized.

### How?

Study design: Experimental Trial.

### Who?

> Children with acute uncomplicated P. falciparum malaria in Tanzania.

## Provenance

- Source study: [[@dahlstrm2009]]
- Paper: Polymorphism in PfMRP1 (Plasmodium falciparum multidrug resistance protein 1) amino acid 1466 associated with resistance to sulfadoxine-pyrimethamine treatment.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2009 Jun
- PubMed: [19364873](https://pubmed.ncbi.nlm.nih.gov/19364873/)
- System association ID: `uWlhfFjB6L`
- Resistance gene(s): Other markers
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
