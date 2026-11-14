---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - presence of dihydrofolate reductase (DHFR) mutations at codons 108 and 51 carried 0.24 times the parasite clearance time, a reduction (hazard ratio) - @mndez2002"
tags:
  - "marker/pfdhfr"
  - "theme/parasite-clearance"
  - "stat/hazard_ratio"
  - "direction/negative"
  - "verification/api-only"
  - "year/2002"
created: 2026-11-14
updated: 2026-11-14
nodeID: 03c1de73-68ad-41ba-8f60-b9b45967fa9d
title: presence of dihydrofolate reductase (DHFR) mutations at codons 108 and 51 carried 0.24 times the parasite clearance time, a reduction (hazard ratio) - @mndez2002
---

## Source

[[@mndez2002]]

## In plain terms

> [!info] What this finding says
> A study published in 2002 reported a statistical link between **presence of dihydrofolate reductase (DHFR) mutations at codons 108 and 51** and **parasite clearance time**.
> Presence of dihydrofolate reductase (DHFR) mutations at codons 108 and 51 carried 0.24 times the parasite clearance time, a reduction (hazard ratio), p = 0.019.

## Statistic

| | |
|---|---|
| **Metric** | `hazard_ratio` (System's normalised type; the paper reported `relative hazard`) |
| **Estimate** | **0.24** |
| **p-value** | = 0.019 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 1** | **negative** |
| **Data source** | Dataverse release |
| **In curated release** | No |
| **Source paper integrity** | No retraction, erratum or expression of concern found (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: not returned) |
| **Published erratum** | None found |
| **Formal published comments** | None |
| **Critical social posts** | None recorded — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Not determined |
| **Open data** | Not determined |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Not recorded in the graph. |
| **Intervention / exposure** | presence of dihydrofolate reductase mutations at codons 108 and 51 |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | parasite clearance time |
| **Setting** | Not recorded in the graph. |
| **Timeframe** | Published 2002. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `presence of dihydrofolate reductase mutations at codons 108 and 51`
> Variable 2: `parasite clearance time`
> hazard ratio = 0.24, p = 0.019
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **negative**

## Methods Context

### What?

The study related **presence of dihydrofolate reductase (DHFR) mutations at codons 108 and 51** to **parasite clearance time**, reported as a hazard ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> The graph holds no description of who was studied.

## Provenance

- Source study: [[@mndez2002]]
- Paper: Determinants of treatment response to sulfadoxine-pyrimethamine and subsequent transmission potential in falciparum malaria.
- Journal: American journal of epidemiology
- Published: 2002 Aug 1
- PubMed: [12142257](https://pubmed.ncbi.nlm.nih.gov/12142257/)
- System association ID: `Sf4jTQSmj-`
- Resistance gene(s): PfDHFR
- Outcome theme(s): how fast malaria parasites cleared from the blood

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
