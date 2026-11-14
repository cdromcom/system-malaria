---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - C580Y and C580 infections was associated with an increase of 0.8 in time to clearance (among P. falciparum infections treated with ARTs) (mean difference unstandardized) - @s2018"
tags:
  - "marker/pfkelch13"
  - "theme/parasite-clearance"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2018"
created: 2026-11-14
updated: 2026-11-14
nodeID: f7b48b73-8069-467b-b2ae-8658255fdb9b
title: C580Y and C580 infections was associated with an increase of 0.8 in time to clearance (among P. falciparum infections treated with ARTs) (mean difference unstandardized) - @s2018
---

## Source

[[@s2018]]

## In plain terms

> [!info] What this finding says
> A study published in 2018 reported a statistical link between **C580Y and C580 infections** and **time to clearance (among P. falciparum infections treated with ARTs)**.
> C580Y and C580 infections was associated with an increase of 0.8 in time to clearance (among P. falciparum infections treated with ARTs) (mean difference unstandardized). The confidence interval runs from -0.92 to 2.53.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **0.8** |
| **p-value** | Not recorded |
| **Confidence interval** | CI -0.92 to 2.53 (confidence level not recorded) |
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
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Splenectomized monkeys treated with three daily doses of i.v. artesunate. |
| **Intervention / exposure** | C580Y and C580 infections |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | time to clearance (among P. falciparum infections treated with ARTs) |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2018. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **C580Y** — a mutation that swaps amino acid C for Y at position 580 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `C580Y and C580 infections`
> Variable 2: `time to clearance (among P. falciparum infections treated with ARTs)`
> mean difference unstandardized = 0.8
> CI [-0.92, 2.53]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **C580Y and C580 infections** to **time to clearance (among P. falciparum infections treated with ARTs)**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Splenectomized monkeys treated with three daily doses of i.v. artesunate.

## Provenance

- Source study: [[@s2018]]
- Paper: Artemisinin resistance phenotypes and K13 inheritance in a Plasmodium falciparum cross and Aotus model.
- Journal: Proceedings of the National Academy of Sciences of the United States of America
- Published: 2018 Dec 4
- PubMed: [30455312](https://pubmed.ncbi.nlm.nih.gov/30455312/)
- System association ID: `2GvCxgUNC3`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): how fast malaria parasites cleared from the blood

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
