---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - mutant Plasmodium falciparum chloroquine resistance transporter and treatment failures (among children with uncomplicated malaria) showed a spearman correlation of 0.872 - @duah2007"
tags:
  - "marker/pfcrt"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/spearman_correlation"
  - "direction/positive"
  - "verification/api-only"
  - "year/2007"
created: 2026-11-14
updated: 2026-11-14
nodeID: ff7c3544-5af1-4931-94b3-9245c5907c96
title: mutant Plasmodium falciparum chloroquine resistance transporter and treatment failures (among children with uncomplicated malaria) showed a spearman correlation of 0.872 - @duah2007
---

## Source

[[@duah2007]]

## In plain terms

> [!info] What this finding says
> A study published in 2007 reported a statistical link between **mutant Plasmodium falciparum chloroquine resistance transporter prevalence** and **treatment failures (among children with uncomplicated malaria)**.
> Mutant Plasmodium falciparum chloroquine resistance transporter and treatment failures (among children with uncomplicated malaria) showed a spearman correlation of 0.872, p = 0.027.

## Statistic

| | |
|---|---|
| **Metric** | `spearman_correlation` (System's normalised type; the paper reported `spearman_correlation`) |
| **Estimate** | **0.872** |
| **p-value** | = 0.027 |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 406 children with uncomplicated malaria presenting at five sentinel health centres in Ghana. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Ghana |
| **Timeframe** | Published 2007. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `mutant Plasmodium falciparum chloroquine resistance transporter prevalence` with `treatment failures (among children with uncomplicated malaria)` and reports a spearman correlation of 0.872. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `mutant Plasmodium falciparum chloroquine resistance transporter prevalence`
> Variable 2: `treatment failures (among children with uncomplicated malaria)`
> spearman correlation = 0.872, p = 0.027
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **mutant Plasmodium falciparum chloroquine resistance transporter prevalence** to **treatment failures (among children with uncomplicated malaria)**, reported as a spearman correlation.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 406 children with uncomplicated malaria presenting at five sentinel health centres in Ghana.

## Provenance

- Source study: [[@duah2007]]
- Paper: Mutations in Plasmodium falciparum chloroquine resistance transporter and multidrug resistance genes, and treatment outcomes in Ghanaian children with uncomplicated malaria.
- Journal: Journal of tropical pediatrics
- Published: 2007 Feb
- PubMed: [17158810](https://pubmed.ncbi.nlm.nih.gov/17158810/)
- System association ID: `1WtBGgAkYN`
- Resistance gene(s): PfCRT
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
