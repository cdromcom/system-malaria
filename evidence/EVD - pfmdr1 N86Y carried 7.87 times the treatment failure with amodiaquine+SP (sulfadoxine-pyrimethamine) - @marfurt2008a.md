---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfmdr1 N86Y carried 7.87 times the treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine) (odds ratio) - @marfurt2008a"
tags:
  - "marker/pfmdr1"
  - "theme/treatment-failure"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2008"
created: 2026-11-14
updated: 2026-11-14
nodeID: 57156f3f-0373-49c2-b631-85e36f70afdb
title: pfmdr1 N86Y carried 7.87 times the treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine) (odds ratio) - @marfurt2008a
---

## Source

[[@marfurt2008a]]

## In plain terms

> [!info] What this finding says
> A study published in 2008 reported a statistical link between **pfmdr1 N86Y** and **treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine)**.
> Pfmdr1 N86Y carried 7.87 times the treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine) (odds ratio), p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **7.87** |
| **p-value** | = 0.01 |
| **Confidence interval** | Not recorded |
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
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Adults in Papua New Guinea with uncomplicated malaria in 2004. |
| **Intervention / exposure** | pfmdr1 N86Y |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | treatment failure with amodiaquine+SP |
| **Setting** | Papua New Guinea |
| **Timeframe** | Published 2008. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children
- **N86Y** — a mutation that swaps amino acid N for Y at position 86 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfmdr1 N86Y`
> Variable 2: `treatment failure with amodiaquine+SP`
> odds ratio = 7.87, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfmdr1 N86Y** to **treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine)**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Adults in Papua New Guinea with uncomplicated malaria in 2004.

## Provenance

- Source study: [[@marfurt2008a]]
- Paper: The usefulness of twenty-four molecular markers in predicting treatment outcome with combination therapy of amodiaquine plus sulphadoxine-pyrimethamine against falciparum malaria in Papua New Guinea.
- Journal: Malaria journal
- Published: 2008 Apr 19
- PubMed: [18423045](https://pubmed.ncbi.nlm.nih.gov/18423045/)
- System association ID: `EdZvePW6vv`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
