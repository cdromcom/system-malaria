---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfdhps A437G carried 3.44 times the treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine) (odds ratio) - @marfurt2008a"
tags:
  - "marker/pfdhps"
  - "theme/treatment-failure"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2008"
created: 2026-11-14
updated: 2026-11-14
nodeID: f1076e74-efa0-498f-b78a-b7ed445d5ff4
title: pfdhps A437G carried 3.44 times the treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine) (odds ratio) - @marfurt2008a
---

## Source

[[@marfurt2008a]]

## In plain terms

> [!info] What this finding says
> A study published in 2008 reported a statistical link between **pfdhps A437G** and **treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine)**.
> Pfdhps A437G carried 3.44 times the treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine) (odds ratio), p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **3.44** |
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
| **Intervention / exposure** | pfdhps A437G |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | treatment failure with amodiaquine+SP |
| **Setting** | Papua New Guinea |
| **Timeframe** | Published 2008. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children
- **A437G** — a mutation that swaps amino acid A for G at position 437 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfdhps A437G`
> Variable 2: `treatment failure with amodiaquine+SP`
> odds ratio = 3.44, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfdhps A437G** to **treatment failure with amodiaquine+SP (sulfadoxine-pyrimethamine)**, reported as a odds ratio.

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
- System association ID: `ntTxGcZt2J`
- Resistance gene(s): PfDHPS
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
