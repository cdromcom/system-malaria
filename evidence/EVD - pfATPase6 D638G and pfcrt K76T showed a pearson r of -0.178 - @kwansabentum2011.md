---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfATPase6 D638G and pfcrt K76T showed a pearson r of -0.178 - @kwansabentum2011"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/pearson_r"
  - "direction/negative"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: 16fcbb55-9e0d-4e4a-83c0-d1147bdc3e9e
title: pfATPase6 D638G and pfcrt K76T showed a pearson r of -0.178 - @kwansabentum2011
---

## Source

[[@kwansabentum2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **pfATPase6 D638G** and **pfcrt K76T**.
> PfATPase6 D638G and pfcrt K76T showed a pearson r of -0.178, p = 0.05.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **-0.178** |
| **p-value** | = 0.05 |
| **Confidence interval** | Not recorded |
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
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text — GenBank |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Individuals with uncomplicated malaria in Ghana. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Ghana |
| **Timeframe** | Published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `pfATPase6 D638G` with `pfcrt K76T` and reports a pearson r of -0.178. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **D638G** — a mutation that swaps amino acid D for G at position 638 of the protein
- **K76T** — a mutation that swaps amino acid K for T at position 76 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfATPase6 D638G`
> Variable 2: `pfcrt K76T`
> pearson r = -0.178, p = 0.05
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **pfATPase6 D638G** to **pfcrt K76T**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Individuals with uncomplicated malaria in Ghana.

## Provenance

- Source study: [[@kwansabentum2011]]
- Paper: Plasmodium falciparum isolates from southern Ghana exhibit polymorphisms in the SERCA-type PfATPase6 though sensitive to artesunate in vitro.
- Journal: Malaria journal
- Published: 2011 Jul 11
- PubMed: [21745377](https://pubmed.ncbi.nlm.nih.gov/21745377/)
- System association ID: `l5m5Hjmxco`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
