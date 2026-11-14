---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Parasite clearance half-life differed by 0.65 between A675V mutation and C469Y mutation (mean difference unstandardized) - @balikagala2021"
tags:
  - "marker/pfkelch13"
  - "theme/parasite-clearance"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: 31ccba31-35a2-4347-aeae-bdf2ec85a9ec
title: Parasite clearance half-life differed by 0.65 between A675V mutation and C469Y mutation (mean difference unstandardized) - @balikagala2021
---

## Source

[[@balikagala2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **A675V mutation** and **Parasite clearance half-life**.
> Parasite clearance half-life differed by 0.65 between A675V mutation and C469Y mutation (mean difference unstandardized), p = 0.001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **0.65** |
| **p-value** | = 0.001 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **positive** |
| **Data source** | API list, API detail |
| **In curated release** | No |
| **Source paper integrity** | formal published comments exist (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: Clean) |
| **Published erratum** | None found |
| **Formal published comments** | 3 indexed in PubMed |
| **Critical social posts** | 52 negative X/Twitter, 0 Bluesky — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Yes (bronze) |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 240 patients with malaria infection in Northern Uganda from 2017 to 2019. |
| **Intervention / exposure** | A675V mutation |
| **Comparator** | C469Y mutation |
| **Outcome** | Parasite clearance half-life |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **A675V** — a mutation that swaps amino acid A for V at position 675 of the protein
- **C469Y** — a mutation that swaps amino acid C for Y at position 469 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `A675V mutation [vs C469Y mutation]`
> Variable 2: `Parasite clearance half-life`
> mean difference unstandardized = 0.65, p = 0.001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **A675V mutation** to **Parasite clearance half-life**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 240 patients with malaria infection in Northern Uganda from 2017 to 2019.

## Provenance

- Source study: [[@balikagala2021]]
- Paper: Evidence of Artemisinin-Resistant Malaria in Africa.
- Journal: The New England journal of medicine
- Published: 2021 Sep 23
- PubMed: [34551228](https://pubmed.ncbi.nlm.nih.gov/34551228/)
- System association ID: `pZ53dkSmxq`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): how fast malaria parasites cleared from the blood

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
