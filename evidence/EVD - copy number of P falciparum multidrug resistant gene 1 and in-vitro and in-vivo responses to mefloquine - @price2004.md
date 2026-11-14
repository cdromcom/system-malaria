---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - copy number of P falciparum multidrug resistant gene 1 and in-vitro and in-vivo responses to mefloquine showed a hazard ratio of 6.3 - @price2004"
tags:
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/hazard_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2004"
created: 2026-11-14
updated: 2026-11-14
nodeID: 9be2a44b-4adc-4e81-b180-bcd52d31b133
title: copy number of P falciparum multidrug resistant gene 1 and in-vitro and in-vivo responses to mefloquine showed a hazard ratio of 6.3 - @price2004
---

## Source

[[@price2004]]

## In plain terms

> [!info] What this finding says
> A study published in 2004 reported a statistical link between **copy number of P falciparum multidrug resistant gene 1** and **in-vitro and in-vivo responses to mefloquine**.
> Copy number of P falciparum multidrug resistant gene 1 and in-vitro and in-vivo responses to mefloquine showed a hazard ratio of 6.3, p = 0.001. The confidence interval runs from 2.9 to 13.8.

## Statistic

| | |
|---|---|
| **Metric** | `hazard_ratio` (System's normalised type; the paper reported `hazard_ratio`) |
| **Estimate** | **6.3** |
| **p-value** | = 0.001 |
| **Confidence interval** | CI 2.9 to 13.8 (confidence level not recorded) |
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
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 618 patients with falciparum malaria studied prospectively over 12 years in Thailand. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Thailand |
| **Timeframe** | Published 2004. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `copy number of P falciparum multidrug resistant gene 1` with `in-vitro and in-vivo responses to mefloquine` and reports a hazard ratio of 6.3. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `copy number of P falciparum multidrug resistant gene 1`
> Variable 2: `in-vitro and in-vivo responses to mefloquine`
> hazard ratio = 6.3, p = 0.001
> CI [2.9, 13.8]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **copy number of P falciparum multidrug resistant gene 1** to **in-vitro and in-vivo responses to mefloquine**, reported as a hazard ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 618 patients with falciparum malaria studied prospectively over 12 years in Thailand.

## Provenance

- Source study: [[@price2004]]
- Paper: Mefloquine resistance in Plasmodium falciparum and increased pfmdr1 gene copy number.
- Journal: Lancet (London, England)
- Published: 2004 Jul 31-Aug 6
- PubMed: [15288742](https://pubmed.ncbi.nlm.nih.gov/15288742/)
- System association ID: `sZgO2yB9kp`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
