---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - C580Y and C580 infections was associated with a decrease of 13 in incidence of recrudescence (mean difference unstandardized = -13) - @s2018"
tags:
  - "marker/pfkelch13"
  - "theme/treatment-failure"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2018"
created: 2026-11-14
updated: 2026-11-14
nodeID: a55443a5-fd29-40b7-a424-2b1cd3b651bc
title: C580Y and C580 infections was associated with a decrease of 13 in incidence of recrudescence (mean difference unstandardized = -13) - @s2018
---

## Source

[[@s2018]]

## In plain terms

> [!info] What this finding says
> A study published in 2018 reported a statistical link between **C580Y and C580 infections** and **incidence of recrudescence**.
> C580Y and C580 infections was associated with a decrease of 13 in incidence of recrudescence (mean difference unstandardized = -13). The confidence interval runs from -58 to 35.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-13** |
| **p-value** | Not recorded |
| **Confidence interval** | CI -58 to 35 (confidence level not recorded) |
| **Direction vs null of 0** | **negative** |
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
| **Outcome** | incidence of recrudescence |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2018. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **recrudescence** — the original infection returning after treatment, as opposed to a fresh mosquito bite
- **C580Y** — a mutation that swaps amino acid C for Y at position 580 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `C580Y and C580 infections`
> Variable 2: `incidence of recrudescence`
> mean difference unstandardized = -13
> CI [-58, 35]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **C580Y and C580 infections** to **incidence of recrudescence**, reported as a mean difference unstandardized.

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
- System association ID: `4G-NnH9IY9`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
