---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - chloroquine resistance and amodiaquine resistance showed a pearson r of 0.93 - @caramello2005"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/pearson_r"
  - "direction/positive"
  - "verification/in-curated-deposit"
  - "year/2005"
created: 2026-11-14
updated: 2026-11-14
nodeID: 102720bb-97ec-48c9-903c-c9c4c5b854b7
title: chloroquine resistance and amodiaquine resistance showed a pearson r of 0.93 - @caramello2005
---

## Source

[[@caramello2005]]

## In plain terms

> [!info] What this finding says
> A study published in 2005 reported a statistical link between **chloroquine resistance** and **amodiaquine resistance**.
> Chloroquine resistance and amodiaquine resistance showed a pearson r of 0.93, p = 0.0001.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0.93** |
| **p-value** | = 0.0001 |
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
| **Population** | Imported Plasmodium falciparum isolates from Africa. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Africa |
| **Timeframe** | Published 2005. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `chloroquine resistance` with `amodiaquine resistance` and reports a pearson r of 0.93. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `chloroquine resistance`
> Variable 2: `amodiaquine resistance`
> pearson r = 0.93, p = 0.0001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **chloroquine resistance** to **amodiaquine resistance**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Imported Plasmodium falciparum isolates from Africa.

## Provenance

- Source study: [[@caramello2005]]
- Paper: Chemosusceptibility analysis of Plasmodium falciparum imported malaria in Italy.
- Journal: Diagnostic microbiology and infectious disease
- Published: 2005 Jun
- PubMed: [15964498](https://pubmed.ncbi.nlm.nih.gov/15964498/)
- System association ID: `cTaIoBN6Sh`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!success] Checked against the curated dataset
> This finding also appears in System's curated Harvard Dataverse release, from which the extractions System had flagged as inaccurate were removed. That is the best available sign that the number was read correctly from the paper.

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
