---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Plasmodium falciparum infections and chloroquine resistance-conferring amino acid codon 76 of the PfCRT showed an odds ratio of 9 - @mharakurwa2013"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2013"
created: 2026-11-14
updated: 2026-11-14
nodeID: e7c60a0f-dd46-43f4-8d78-7a8753949e48
title: Plasmodium falciparum infections and chloroquine resistance-conferring amino acid codon 76 of the PfCRT showed an odds ratio of 9 - @mharakurwa2013
---

## Source

[[@mharakurwa2013]]

## In plain terms

> [!info] What this finding says
> A study published in 2013 reported a statistical link between **Plasmodium falciparum infections** and **chloroquine resistance-conferring amino acid codon 76 of the PfCRT gene**.
> Plasmodium falciparum infections and chloroquine resistance-conferring amino acid codon 76 of the PfCRT showed an odds ratio of 9, p = 0.0005. The confidence interval runs from 3.7 to 20.2.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **9** |
| **p-value** | = 0.0005 |
| **Confidence interval** | CI 3.7 to 20.2 (confidence level not recorded) |
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
| **Open data** | A statement exists but is not explicit |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Human residents of all ages in southern Zambia during the 2006 malaria transmission season. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2013. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Plasmodium falciparum infections` with `chloroquine resistance-conferring amino acid codon 76 of the PfCRT gene` and reports a odds ratio of 9. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Plasmodium falciparum infections`
> Variable 2: `chloroquine resistance-conferring amino acid codon 76 of the PfCRT gene`
> odds ratio = 9, p = 0.0005
> CI [3.7, 20.2]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **Plasmodium falciparum infections** to **chloroquine resistance-conferring amino acid codon 76 of the PfCRT gene**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Human residents of all ages in southern Zambia during the 2006 malaria transmission season.

## Provenance

- Source study: [[@mharakurwa2013]]
- Paper: Selection for chloroquine-sensitive Plasmodium falciparum by wild Anopheles arabiensis in Southern Zambia.
- Journal: Malaria journal
- Published: 2013 Dec 19
- PubMed: [24354640](https://pubmed.ncbi.nlm.nih.gov/24354640/)
- System association ID: `GUZPjfA5yO`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
