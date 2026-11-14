---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - presence of polymorphisms in P. falciparum dihydrofolate reductase (DHFR) and in vivo treatment outcomes showed a relative risk ratio of 4.08 - @bacon2009"
tags:
  - "marker/pfdhfr"
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/relative_risk_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2009"
created: 2026-11-14
updated: 2026-11-14
nodeID: 4dd14888-386b-4be4-ba18-0414d91d8b08
title: presence of polymorphisms in P. falciparum dihydrofolate reductase (DHFR) and in vivo treatment outcomes showed a relative risk ratio of 4.08 - @bacon2009
---

## Source

[[@bacon2009]]

## In plain terms

> [!info] What this finding says
> A study published in 2009 reported a statistical link between **presence of polymorphisms in P. falciparum dihydrofolate reductase (DHFR) and dihydropteroate synthase** and **in vivo treatment outcomes (among the patients enrolled in the study)**.
> Presence of polymorphisms in P. falciparum dihydrofolate reductase (DHFR) and in vivo treatment outcomes showed a relative risk ratio of 4.08. The confidence interval runs from 2.45 to 7.46.

## Statistic

| | |
|---|---|
| **Metric** | `relative_risk_ratio` (System's normalised type; the paper reported `relative_risk_ratio`) |
| **Estimate** | **4.08** |
| **p-value** | Not recorded |
| **Confidence interval** | CI 2.45 to 7.46 (confidence level not recorded) |
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
| **Open data** | No availability statement found in the full text — ClinicalTrials.gov |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 99 patients in the Peruvian Amazon enrolled in an in vivo therapeutic efficacy trial of sulfadoxine-pyrimethamine. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2009. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `presence of polymorphisms in P. falciparum dihydrofolate reductase and dihydropteroate synthase` with `in vivo treatment outcomes (among the patients enrolled in the study)` and reports a relative risk ratio of 4.08. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **DHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `presence of polymorphisms in P. falciparum dihydrofolate reductase and dihydropteroate synthase`
> Variable 2: `in vivo treatment outcomes (among the patients enrolled in the study)`
> relative risk ratio = 4.08
> CI [2.45, 7.46]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **presence of polymorphisms in P. falciparum dihydrofolate reductase (DHFR) and dihydropteroate synthase** to **in vivo treatment outcomes (among the patients enrolled in the study)**, reported as a relative risk ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 99 patients in the Peruvian Amazon enrolled in an in vivo therapeutic efficacy trial of sulfadoxine-pyrimethamine.

## Provenance

- Source study: [[@bacon2009]]
- Paper: Effects of point mutations in Plasmodium falciparum dihydrofolate reductase and dihydropterate synthase genes on clinical outcomes and in vitro susceptibility to sulfadoxine and pyrimethamine.
- Journal: PloS one
- Published: 2009 Aug 26
- PubMed: [19707564](https://pubmed.ncbi.nlm.nih.gov/19707564/)
- System association ID: `9uTFvbAcu2`
- Resistance gene(s): PfDHFR, PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
