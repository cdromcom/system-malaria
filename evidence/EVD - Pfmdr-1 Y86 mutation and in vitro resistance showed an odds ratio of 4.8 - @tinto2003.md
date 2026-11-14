---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Pfmdr-1 Y86 mutation and in vitro resistance showed an odds ratio of 4.8 - @tinto2003"
tags:
  - "marker/pfmdr1"
  - "theme/drug-susceptibility"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2003"
created: 2026-11-14
updated: 2026-11-14
nodeID: 73831348-c11a-4f60-8e17-0b5d24ab5944
title: Pfmdr-1 Y86 mutation and in vitro resistance showed an odds ratio of 4.8 - @tinto2003
---

## Source

[[@tinto2003]]

## In plain terms

> [!info] What this finding says
> A study published in 2003 reported a statistical link between **Pfmdr-1 Y86 mutation** and **in vitro resistance**.
> Pfmdr-1 Y86 mutation and in vitro resistance showed an odds ratio of 4.8, p = 0.01. The confidence interval runs from 1.4 to 16.5.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **4.8** |
| **p-value** | = 0.01 |
| **Confidence interval** | CI 1.4 to 16.5 (confidence level not recorded) |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Patients with uncomplicated malaria in Burkina Faso. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Burkina Faso |
| **Timeframe** | Published 2003. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Pfmdr-1 Y86 mutation` with `in vitro resistance` and reports a odds ratio of 4.8. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **in vitro** — tested on parasites grown in the laboratory

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pfmdr-1 Y86 mutation`
> Variable 2: `in vitro resistance`
> odds ratio = 4.8, p = 0.01
> CI [1.4, 16.5]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Pfmdr-1 Y86 mutation** to **in vitro resistance**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Patients with uncomplicated malaria in Burkina Faso.

## Provenance

- Source study: [[@tinto2003]]
- Paper: Relationship between the Pfcrt T76 and the Pfmdr-1 Y86 mutations in Plasmodium falciparum and in vitro/in vivo chloroquine resistance in Burkina Faso, West Africa.
- Journal: Infection, genetics and evolution : journal of molecular epidemiology and evolutionary genetics in infectious diseases
- Published: 2003 Nov
- PubMed: [14636690](https://pubmed.ncbi.nlm.nih.gov/14636690/)
- System association ID: `CkKdMtRaBB`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
