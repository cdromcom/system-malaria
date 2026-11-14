---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - intermittent preventive treatment during pregnancy with and prevalence of quintuple mutant infections showed an odds ratio of 8.13 - @menndez2011"
tags:
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/odds_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: c4661101-ac26-410e-a8d2-3611169b5e9d
title: intermittent preventive treatment during pregnancy with and prevalence of quintuple mutant infections showed an odds ratio of 8.13 - @menndez2011
---

## Source

[[@menndez2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **intermittent preventive treatment during pregnancy with sulphadoxine-pyrimethamine (sulfadoxine-pyrimethamine)** and **prevalence of quintuple mutant infections**.
> Intermittent preventive treatment during pregnancy with and prevalence of quintuple mutant infections showed an odds ratio of 8.13, p = 0.031. The confidence interval runs from 1.69 to 39.1.

## Statistic

| | |
|---|---|
| **Metric** | `odds_ratio` (System's normalised type; the paper reported `odds_ratio`) |
| **Estimate** | **8.13** |
| **p-value** | = 0.031 |
| **Confidence interval** | CI 1.69 to 39.1 (confidence level not recorded) |
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
| **Population** | Pregnant women enrolled in a randomized, placebo-controlled trial of IPTp in Manhiça, Mozambique. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `intermittent preventive treatment during pregnancy with sulphadoxine-pyrimethamine` with `prevalence of quintuple mutant infections` and reports a odds ratio of 8.13. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `intermittent preventive treatment during pregnancy with sulphadoxine-pyrimethamine`
> Variable 2: `prevalence of quintuple mutant infections`
> odds ratio = 8.13, p = 0.031
> CI [1.69, 39.1]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **intermittent preventive treatment during pregnancy with sulphadoxine-pyrimethamine (sulfadoxine-pyrimethamine)** to **prevalence of quintuple mutant infections**, reported as a odds ratio.

### How?

Study design: Experimental Trial.

### Who?

> Pregnant women enrolled in a randomized, placebo-controlled trial of IPTp in Manhiça, Mozambique.

## Provenance

- Source study: [[@menndez2011]]
- Paper: HIV and placental infection modulate the appearance of drug-resistant Plasmodium falciparum in pregnant women who receive intermittent preventive treatment.
- Journal: Clinical infectious diseases : an official publication of the Infectious Diseases Society of America
- Published: 2011 Jan 1
- PubMed: [21148518](https://pubmed.ncbi.nlm.nih.gov/21148518/)
- System association ID: `pT7vv2JN1x`
- Resistance gene(s): PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
