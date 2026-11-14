---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - dhps A581G and birth weight showed a mean difference unstandardized of 252 - @taylor2020"
tags:
  - "marker/pfdhps"
  - "theme/severe-illness"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2020"
created: 2026-11-14
updated: 2026-11-14
nodeID: d152055b-2c47-49d9-85f8-1b0321c6d553
title: dhps A581G and birth weight showed a mean difference unstandardized of 252 - @taylor2020
---

## Source

[[@taylor2020]]

## In plain terms

> [!info] What this finding says
> A study published in 2020 reported a statistical link between **dhps A581G** and **birth weight**.
> Dhps A581G and birth weight showed a mean difference unstandardized of 252, p = 0.017. The confidence interval runs from 46 to 457.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **252** |
| **p-value** | = 0.017 |
| **Confidence interval** | CI 46 to 457 (confidence level not recorded) |
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
| **Open access** | Yes (bronze) |
| **Open data** | Cannot tell — PMC holds front matter only — ISRCTN |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 125 Malawian women participating in a trial comparing IPTp with SP against intermittent screening by rapid diagnostic tests (ISTp). |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2020. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `dhps A581G` with `birth weight` and reports a mean difference unstandardized of 252. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **A581G** — a mutation that swaps amino acid A for G at position 581 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `dhps A581G`
> Variable 2: `birth weight`
> mean difference unstandardized = 252, p = 0.017
> CI [46, 457]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **dhps A581G** to **birth weight**, reported as a mean difference unstandardized.

### How?

Study design: Experimental Trial.

### Who?

> 125 Malawian women participating in a trial comparing IPTp with SP against intermittent screening by rapid diagnostic tests (ISTp).

## Provenance

- Source study: [[@taylor2020]]
- Paper: Interactions Between Antenatal Sulfadoxine-Pyrimethamine, Drug-Resistant Plasmodium falciparum Parasites, and Delivery Outcomes in Malawi.
- Journal: The Journal of infectious diseases
- Published: 2020 Jul 23
- PubMed: [32221555](https://pubmed.ncbi.nlm.nih.gov/32221555/)
- System association ID: `_0IwC4n9Rv`
- Resistance gene(s): PfDHPS
- Outcome theme(s): severe illness, death and birth weight

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
