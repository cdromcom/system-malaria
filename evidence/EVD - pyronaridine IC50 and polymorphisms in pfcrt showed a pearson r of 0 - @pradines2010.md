---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pyronaridine IC50 and polymorphisms in pfcrt showed a pearson r of 0 - @pradines2010"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "theme/drug-susceptibility"
  - "stat/pearson_r"
  - "direction/null"
  - "verification/in-curated-deposit"
  - "year/2010"
created: 2026-11-14
updated: 2026-11-14
nodeID: ffa23f13-e049-4723-9a43-5977d8fda2bd
title: pyronaridine IC50 and polymorphisms in pfcrt showed a pearson r of 0 - @pradines2010
---

## Source

[[@pradines2010]]

## In plain terms

> [!info] What this finding says
> A study published in 2010 reported a statistical link between **pyronaridine IC50** and **polymorphisms in pfcrt**.
> Pyronaridine IC50 and polymorphisms in pfcrt showed a pearson r of 0.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0** |
| **p-value** | Not recorded |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **null** |
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
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 23 strains of Plasmodium falciparum assessed by the standard 42-hour 3H-hypoxanthine uptake inhibition method. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2010. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `pyronaridine IC50` with `polymorphisms in pfcrt` and reports a pearson r of 0. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **IC50** — the drug concentration needed to halve parasite growth in the laboratory; a higher value means the parasite is less sensitive to the drug

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pyronaridine IC50`
> Variable 2: `polymorphisms in pfcrt`
> pearson r = 0
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **null**

## Methods Context

### What?

The study related **pyronaridine IC50** to **polymorphisms in pfcrt**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 23 strains of Plasmodium falciparum assessed by the standard 42-hour 3H-hypoxanthine uptake inhibition method.

## Provenance

- Source study: [[@pradines2010]]
- Paper: Absence of association between pyronaridine in vitro responses and polymorphisms in genes involved in quinoline resistance in Plasmodium falciparum.
- Journal: Malaria journal
- Published: 2010 Nov 25
- PubMed: [21108786](https://pubmed.ncbi.nlm.nih.gov/21108786/)
- System association ID: `sldKH5O0JZ`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was, how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!success] Checked against the curated dataset
> This finding also appears in System's curated Harvard Dataverse release, from which the extractions System had flagged as inaccurate were removed. That is the best available sign that the number was read correctly from the paper.

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
