---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - combined presence of the quadruple mutant pvdhfr 57L+58R+61M+117T carried 8.56 times the treatment failure (among the studied patients) (odds ratio) - @marfurt2008b"
tags:
  - "marker/pfdhfr"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2008"
created: 2026-11-14
updated: 2026-11-14
nodeID: 37ed20b5-03cd-4d80-a418-acd74151f688
title: combined presence of the quadruple mutant pvdhfr 57L+58R+61M+117T carried 8.56 times the treatment failure (among the studied patients) (odds ratio) - @marfurt2008b
---

## Source

[[@marfurt2008b]]

## In plain terms

> [!info] What this finding says
> A study published in 2008 reported a statistical link between **combined presence of the quadruple mutant pvdhfr 57L+58R+61M+117T and pvmdr1 mutation 976F** and **treatment failure (among the studied patients)**.
> Combined presence of the quadruple mutant pvdhfr 57L+58R+61M+117T carried 8.56 times the treatment failure (among the studied patients) (odds ratio), p = 0.01.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **8.56** |
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
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 94 patients in Papua New Guinea who received amodiaquine plus sulfadoxine-pyrimethamine. |
| **Intervention / exposure** | combined presence of the quadruple mutant pvdhfr 57L+58R+61M+117T and pvmdr1 mutation 976F |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | treatment failure (among the studied patients) |
| **Setting** | Papua New Guinea |
| **Timeframe** | Published 2008. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `combined presence of the quadruple mutant pvdhfr 57L+58R+61M+117T and pvmdr1 mutation 976F`
> Variable 2: `treatment failure (among the studied patients)`
> odds ratio = 8.56, p = 0.01
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **combined presence of the quadruple mutant pvdhfr 57L+58R+61M+117T and pvmdr1 mutation 976F** to **treatment failure (among the studied patients)**, reported as a odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 94 patients in Papua New Guinea who received amodiaquine plus sulfadoxine-pyrimethamine.

## Provenance

- Source study: [[@marfurt2008b]]
- Paper: Molecular markers of in vivo Plasmodium vivax resistance to amodiaquine plus sulfadoxine-pyrimethamine: mutations in pvdhfr and pvmdr1.
- Journal: The Journal of infectious diseases
- Published: 2008 Aug 1
- PubMed: [18582193](https://pubmed.ncbi.nlm.nih.gov/18582193/)
- System association ID: `gfCfTEfUH0`
- Resistance gene(s): PfDHFR
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
