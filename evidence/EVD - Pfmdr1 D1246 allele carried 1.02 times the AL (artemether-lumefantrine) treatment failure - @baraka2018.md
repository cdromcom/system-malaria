---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Pfmdr1 D1246 allele carried 1.02 times the AL (artemether-lumefantrine) treatment failure (relative risk ratio) - @baraka2018"
tags:
  - "marker/pfmdr1"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/relative_risk_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2018"
created: 2026-11-14
updated: 2026-11-14
nodeID: 9df385be-aabb-427f-b93f-6768511cc255
title: Pfmdr1 D1246 allele carried 1.02 times the AL (artemether-lumefantrine) treatment failure (relative risk ratio) - @baraka2018
---

## Source

[[@baraka2018]]

## In plain terms

> [!info] What this finding says
> A study published in 2018 reported a statistical link between **Pfmdr1 D1246 allele** and **AL (artemether-lumefantrine) treatment failure**.
> Pfmdr1 D1246 allele carried 1.02 times the AL (artemether-lumefantrine) treatment failure (relative risk ratio), p = 1. The confidence interval runs from 0.42 to 2.47.

## Statistic

| | |
|---|---|
| **Metric** | `relative_risk_ratio` (System's normalised type; the paper reported `relative_risk_ratio`) |
| **Estimate** | **1.02** |
| **p-value** | = 1 |
| **Confidence interval** | CI 0.42 to 2.47 (confidence level not recorded) |
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
| **Open access** | Yes (gold) |
| **Open data** | Deposited in a public repository — dryad |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Children aged 12-59 months in a clinical trial in DR Congo and Uganda. |
| **Intervention / exposure** | Pfmdr1 D1246 allele |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | AL treatment failure |
| **Setting** | DR Congo |
| **Timeframe** | Experimental Trial, published 2018. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **artemether-lumefantrine** — a widely used artemisinin combination treatment, sold as Coartem

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pfmdr1 D1246 allele`
> Variable 2: `AL treatment failure`
> relative risk ratio = 1.02, p = 1
> CI [0.42, 2.47]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Pfmdr1 D1246 allele** to **AL (artemether-lumefantrine) treatment failure**, reported as a relative risk ratio.

### How?

Study design: Experimental Trial.

### Who?

> Children aged 12-59 months in a clinical trial in DR Congo and Uganda.

## Provenance

- Source study: [[@baraka2018]]
- Paper: Impact of treatment and re-treatment with artemether-lumefantrine and artesunate-amodiaquine on selection of Plasmodium falciparum multidrug resistance gene-1 polymorphisms in the Democratic Republic of Congo and Uganda.
- Journal: PloS one
- Published: 2018
- PubMed: [29390014](https://pubmed.ncbi.nlm.nih.gov/29390014/)
- System association ID: `gBDPp8tg68`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
