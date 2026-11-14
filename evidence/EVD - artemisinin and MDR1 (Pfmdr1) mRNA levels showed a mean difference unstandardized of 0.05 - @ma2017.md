---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - artemisinin and MDR1 (Pfmdr1) mRNA levels showed a mean difference unstandardized of 0.05 - @ma2017"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2017"
created: 2026-11-14
updated: 2026-11-14
nodeID: 8bfe1043-ccf4-4502-9e89-e0dfac4e8a4b
title: artemisinin and MDR1 (Pfmdr1) mRNA levels showed a mean difference unstandardized of 0.05 - @ma2017
---

## Source

[[@ma2017]]

## In plain terms

> [!info] What this finding says
> A study published in 2017 reported a statistical link between **artemisinin** and **MDR1 (Pfmdr1) mRNA levels**.
> Artemisinin and MDR1 (Pfmdr1) mRNA levels showed a mean difference unstandardized of 0.05, p = 0.05.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **0.05** |
| **p-value** | = 0.05 |
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
| **Open access** | Yes (hybrid) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Male ICR mice. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2017. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `artemisinin` with `MDR1 mRNA levels` and reports a mean difference unstandardized of 0.05. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `artemisinin`
> Variable 2: `MDR1 mRNA levels`
> mean difference unstandardized = 0.05, p = 0.05
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **artemisinin** to **MDR1 (Pfmdr1) mRNA levels**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Male ICR mice.

## Provenance

- Source study: [[@ma2017]]
- Paper: Chrysosplenetin inhibits artemisinin efflux in P-gp-over-expressing Caco-2 cells and reverses P-gp/MDR1 mRNA up-regulated expression induced by artemisinin in mouse small intestine.
- Journal: Pharmaceutical biology
- Published: 2017 Dec
- PubMed: [27931149](https://pubmed.ncbi.nlm.nih.gov/27931149/)
- System association ID: `pKFBTyjaur`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
