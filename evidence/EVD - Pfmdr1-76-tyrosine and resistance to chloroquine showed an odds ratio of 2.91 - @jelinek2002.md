---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Pfmdr1-76-tyrosine and resistance to chloroquine showed an odds ratio of 2.91 - @jelinek2002"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2002"
created: 2026-11-14
updated: 2026-11-14
nodeID: a4c970ac-abd3-4285-b3a1-601335bebdd2
title: Pfmdr1-76-tyrosine and resistance to chloroquine showed an odds ratio of 2.91 - @jelinek2002
---

## Source

[[@jelinek2002]]

## In plain terms

> [!info] What this finding says
> A study published in 2002 reported a statistical link between **Pfmdr1-76-tyrosine** and **resistance to chloroquine**.
> Pfmdr1-76-tyrosine and resistance to chloroquine showed an odds ratio of 2.91, p = 0.0195.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **2.91** |
| **p-value** | = 0.0195 |
| **Confidence interval** | Not recorded |
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
| **Population** | Non-endemic regions bordering the Saharan desert in Mauritania in 1998. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2002. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Pfmdr1-76-tyrosine` with `resistance to chloroquine` and reports a odds ratio of 2.91. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pfmdr1-76-tyrosine`
> Variable 2: `resistance to chloroquine`
> odds ratio = 2.91, p = 0.0195
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Pfmdr1-76-tyrosine** to **resistance to chloroquine**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Non-endemic regions bordering the Saharan desert in Mauritania in 1998.

## Provenance

- Source study: [[@jelinek2002]]
- Paper: Diagnostic value of molecular markers in chloroquine-resistant falciparum malaria in Southern Mauritania.
- Journal: The American journal of tropical medicine and hygiene
- Published: 2002 Nov
- PubMed: [12479542](https://pubmed.ncbi.nlm.nih.gov/12479542/)
- System association ID: `T9dTcai02j`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
