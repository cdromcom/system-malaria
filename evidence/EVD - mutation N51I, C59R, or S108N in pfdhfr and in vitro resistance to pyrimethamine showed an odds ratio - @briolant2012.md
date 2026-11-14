---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - mutation N51I, C59R, or S108N in pfdhfr and in vitro resistance to pyrimethamine showed an odds ratio of 42.3 - @briolant2012"
tags:
  - "marker/pfdhfr"
  - "theme/drug-susceptibility"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/in-curated-deposit"
  - "year/2012"
created: 2026-11-14
updated: 2026-11-14
nodeID: 3a2d1917-3abf-4317-9cc7-896448fa86bf
title: mutation N51I, C59R, or S108N in pfdhfr and in vitro resistance to pyrimethamine showed an odds ratio of 42.3 - @briolant2012
---

## Source

[[@briolant2012]]

## In plain terms

> [!info] What this finding says
> A study published in 2012 reported a statistical link between **mutation N51I, C59R, or S108N in pfdhfr** and **in vitro resistance to pyrimethamine**.
> Mutation N51I, C59R, or S108N in pfdhfr and in vitro resistance to pyrimethamine showed an odds ratio of 42.3, p = 0.0003. The confidence interval runs from 5.52 to 325.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **42.3** |
| **p-value** | = 0.0003 |
| **Confidence interval** | CI 5.52 to 325 (confidence level not recorded) |
| **Direction vs null of 1** | **positive** |
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
| **Open access** | Yes (hybrid) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 140 Plasmodium falciparum isolates. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2012. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `mutation N51I, C59R, or S108N in pfdhfr` with `in vitro resistance to pyrimethamine` and reports a odds ratio of 42.3. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **in vitro** — tested on parasites grown in the laboratory
- **N51I** — a mutation that swaps amino acid N for I at position 51 of the protein
- **C59R** — a mutation that swaps amino acid C for R at position 59 of the protein
- **S108N** — a mutation that swaps amino acid S for N at position 108 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `mutation N51I, C59R, or S108N in pfdhfr`
> Variable 2: `in vitro resistance to pyrimethamine`
> odds ratio = 42.3, p = 0.0003
> CI [5.52, 325]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **mutation N51I, C59R, or S108N in pfdhfr** to **in vitro resistance to pyrimethamine**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 140 Plasmodium falciparum isolates.

## Provenance

- Source study: [[@briolant2012]]
- Paper: The F423Y mutation in the pfmdr2 gene and mutations N51I, C59R, and S108N in the pfdhfr gene are independently associated with pyrimethamine resistance in Plasmodium falciparum isolates.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2012 May
- PubMed: [22314533](https://pubmed.ncbi.nlm.nih.gov/22314533/)
- System association ID: `Irv77AV2iz`
- Resistance gene(s): PfDHFR
- Outcome theme(s): how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!success] Checked against the curated dataset
> This finding also appears in System's curated Harvard Dataverse release, from which the extractions System had flagged as inaccurate were removed. That is the best available sign that the number was read correctly from the paper.

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
