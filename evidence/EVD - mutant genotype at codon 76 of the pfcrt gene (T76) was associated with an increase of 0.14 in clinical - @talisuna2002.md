---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - mutant genotype at codon 76 of the pfcrt gene (T76) was associated with an increase of 0.14 in clinical (early and late treatment failure ETF + LTF) (pearson r) - @talisuna2002"
tags:
  - "marker/pfcrt"
  - "theme/treatment-failure"
  - "theme/marker-prevalence"
  - "stat/pearson_r"
  - "direction/positive"
  - "verification/api-only"
  - "year/2002"
created: 2026-11-14
updated: 2026-11-14
nodeID: 0c214530-fb9c-434b-aa09-fce64b7bb5ed
title: mutant genotype at codon 76 of the pfcrt gene (T76) was associated with an increase of 0.14 in clinical (early and late treatment failure ETF + LTF) (pearson r) - @talisuna2002
---

## Source

[[@talisuna2002]]

## In plain terms

> [!info] What this finding says
> A study published in 2002 reported a statistical link between **mutant genotype at codon 76 of the pfcrt gene (T76)** and **clinical (early and late treatment failure: ETF + LTF)**.
> Mutant genotype at codon 76 of the pfcrt gene (T76) was associated with an increase of 0.14 in clinical (early and late treatment failure ETF + LTF) (pearson r), p = 0.78.

## Statistic

| | |
|---|---|
| **Metric** | `pearson_r` (System's normalised type; the paper reported `pearson_r`) |
| **Estimate** | **0.14** |
| **p-value** | = 0.78 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **positive** |
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
| **Population** | 6-59-month-old children with clinical malaria in 6 Ugandan sentinel sites in 1998-99. |
| **Intervention / exposure** | mutant genotype at codon 76 of the pfcrt gene (T76) |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | clinical (early and late treatment failure: ETF + LTF) |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2002. Fieldwork dates are not recorded in the graph. |

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `mutant genotype at codon 76 of the pfcrt gene (T76)`
> Variable 2: `clinical (early and late treatment failure: ETF + LTF)`
> pearson r = 0.14, p = 0.78
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **mutant genotype at codon 76 of the pfcrt gene (T76)** to **clinical (early and late treatment failure: ETF + LTF)**, reported as a pearson r.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 6-59-month-old children with clinical malaria in 6 Ugandan sentinel sites in 1998-99.

## Provenance

- Source study: [[@talisuna2002]]
- Paper: Role of the pfcrt codon 76 mutation as a molecular marker for population-based surveillance of chloroquine (CQ)-resistant Plasmodium falciparum malaria in Ugandan sentinel sites with high CQ resistance.
- Journal: Transactions of the Royal Society of Tropical Medicine and Hygiene
- Published: 2002 Sep-Oct
- PubMed: [12474488](https://pubmed.ncbi.nlm.nih.gov/12474488/)
- System association ID: `2rbiQOXd4S`
- Resistance gene(s): PfCRT
- Outcome theme(s): whether malaria treatment failed, how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
