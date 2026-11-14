---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - in vitro chloroquine resistance and inhibitory endpoints for quinine showed a pearson r of 0.64 - @nguyendinh1987"
tags:
  - "marker/pfcrt"
  - "theme/drug-susceptibility"
  - "stat/pearson_r"
  - "direction/positive"
  - "verification/in-curated-deposit"
  - "year/1987"
created: 2026-11-14
updated: 2026-11-14
nodeID: 7b120a2d-08c2-4dcb-8f8f-1dd230ffac3e
title: in vitro chloroquine resistance and inhibitory endpoints for quinine showed a pearson r of 0.64 - @nguyendinh1987
---

## Source

[[@nguyendinh1987]]

## In plain terms

> [!info] What this finding says
> A study published in 1987 reported a statistical link between **in vitro chloroquine resistance** and **inhibitory endpoints for quinine**.
> In vitro chloroquine resistance and inhibitory endpoints for quinine showed a pearson r of 0.64.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0.64** |
| **p-value** | Not recorded |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **positive** |
| **Data source** | API list, API detail, Dataverse release |
| **In curated release** | Yes |
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
| **Population** | 33 children presenting at the Mama Yemo Hospital in Kinshasa (Zaire) in June 1986. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 1987. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `in vitro chloroquine resistance` with `inhibitory endpoints for quinine` and reports a pearson r of 0.64. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **in vitro** — tested on parasites grown in the laboratory

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `in vitro chloroquine resistance`
> Variable 2: `inhibitory endpoints for quinine`
> pearson r = 0.64
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **in vitro chloroquine resistance** to **inhibitory endpoints for quinine**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 33 children presenting at the Mama Yemo Hospital in Kinshasa (Zaire) in June 1986.

## Provenance

- Source study: [[@nguyendinh1987]]
- Paper: Plasmodium falciparum in Kinshasa, Zaire: in vitro drug susceptibility studies.
- Journal: The American journal of tropical medicine and hygiene
- Published: 1987 Sep
- PubMed: [3310676](https://pubmed.ncbi.nlm.nih.gov/3310676/)
- System association ID: `p1xI2bQ0bc`
- Resistance gene(s): PfCRT
- Outcome theme(s): how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!success] Checked against the curated dataset
> This finding also appears in System's curated Harvard Dataverse release, from which the extractions System had flagged as inaccurate were removed. That is the best available sign that the number was read correctly from the paper.

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
