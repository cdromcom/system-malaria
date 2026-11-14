---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - use of sulfadoxine-pyrimethamine used as intermittent preventive and Pfdhfr C59R mutation showed an odds ratio of 4.26 - @cisse2017"
tags:
  - "marker/pfdhfr"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2017"
created: 2026-11-14
updated: 2026-11-14
nodeID: 57dbe72a-88b7-4ef4-85f3-72fb631f28ec
title: use of sulfadoxine-pyrimethamine used as intermittent preventive and Pfdhfr C59R mutation showed an odds ratio of 4.26 - @cisse2017
---

## Source

[[@cisse2017]]

## In plain terms

> [!info] What this finding says
> A study published in 2017 reported a statistical link between **use of sulfadoxine-pyrimethamine used as intermittent preventive treatment during pregnancy (IPTp-SP)** and **Pfdhfr C59R mutation**.
> Use of sulfadoxine-pyrimethamine used as intermittent preventive and Pfdhfr C59R mutation showed an odds ratio of 4.26, p = 0.05. The confidence interval runs from 1.64 to 11.1.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **4.26** |
| **p-value** | = 0.05 |
| **Confidence interval** | CI 1.64 to 11.1 (confidence level not recorded) |
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
| **Open data** | Available from the authors on request only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Pregnant women with microscopically confirmed falciparum malaria infection in Burkina Faso from September to December 2010. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2017. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `use of sulfadoxine-pyrimethamine used as intermittent preventive treatment during pregnancy (IPTp-SP)` with `Pfdhfr C59R mutation` and reports a odds ratio of 4.26. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> The source paper offers its data only on request from the authors. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children
- **IPTp** — intermittent preventive treatment in pregnancy, where pregnant women are given antimalarial drugs at routine visits whether or not they are infected
- **C59R** — a mutation that swaps amino acid C for R at position 59 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `use of sulfadoxine-pyrimethamine used as intermittent preventive treatment during pregnancy (IPTp-SP)`
> Variable 2: `Pfdhfr C59R mutation`
> odds ratio = 4.26, p = 0.05
> CI [1.64, 11.1]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **use of sulfadoxine-pyrimethamine used as intermittent preventive treatment during pregnancy (IPTp-SP)** to **Pfdhfr C59R mutation**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Pregnant women with microscopically confirmed falciparum malaria infection in Burkina Faso from September to December 2010.

## Provenance

- Source study: [[@cisse2017]]
- Paper: Recent uptake of intermittent preventive treatment during pregnancy with sulfadoxine-pyrimethamine is associated with increased prevalence of Pfdhfr mutations in Bobo-Dioulasso, Burkina Faso.
- Journal: Malaria journal
- Published: 2017 Jan 23
- PubMed: [28114990](https://pubmed.ncbi.nlm.nih.gov/28114990/)
- System association ID: `fJzA8cE9X_`
- Resistance gene(s): PfDHFR
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
