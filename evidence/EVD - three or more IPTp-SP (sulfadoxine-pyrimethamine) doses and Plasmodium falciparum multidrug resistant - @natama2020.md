---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - three or more IPTp-SP (sulfadoxine-pyrimethamine) doses and Plasmodium falciparum multidrug resistant gene 1 86Y mutant allele showed an adjusted odds ratio of 0.25 - @natama2020"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/adjusted_odds_ratio"
  - "direction/negative"
  - "verification/api-only"
  - "year/2020"
created: 2026-11-14
updated: 2026-11-14
nodeID: 8317b93f-32fc-4fb2-b556-7e0decb3e0b5
title: three or more IPTp-SP (sulfadoxine-pyrimethamine) doses and Plasmodium falciparum multidrug resistant gene 1 86Y mutant allele showed an adjusted odds ratio of 0.25 - @natama2020
---

## Source

[[@natama2020]]

## In plain terms

> [!info] What this finding says
> A study published in 2020 reported a statistical link between **three or more IPTp-SP (sulfadoxine-pyrimethamine) doses** and **Plasmodium falciparum multidrug resistant gene 1 86Y mutant allele carriage**.
> Three or more IPTp-SP (sulfadoxine-pyrimethamine) doses and Plasmodium falciparum multidrug resistant gene 1 86Y mutant allele showed an adjusted odds ratio of 0.25, p = 0.04. The confidence interval runs from 0.07 to 0.92.

## Statistic

| | |
|---|---|
| **Metric** | `adjusted_odds_ratio` (System's normalised type; the paper reported `adjusted_odds_ratio`) |
| **Estimate** | **0.25** |
| **p-value** | = 0.04 |
| **Confidence interval** | CI 0.07 to 0.92 (confidence level not recorded) |
| **Direction vs null of 1** | **negative** |
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
| **Population** | Pregnant women participating in the COSMIC trial in the Nanoro Health District of Burkina Faso. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2020. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `three or more IPTp-SP doses` with `Plasmodium falciparum multidrug resistant gene 1 86Y mutant allele carriage` and reports a adjusted odds ratio of 0.25. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children
- **IPTp** — intermittent preventive treatment in pregnancy, where pregnant women are given antimalarial drugs at routine visits whether or not they are infected

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `three or more IPTp-SP doses`
> Variable 2: `Plasmodium falciparum multidrug resistant gene 1 86Y mutant allele carriage`
> adjusted odds ratio = 0.25, p = 0.04
> CI [0.07, 0.92]
> Direction against the statistic's null value of 1: **negative**

## Methods Context

### What?

The study related **three or more IPTp-SP (sulfadoxine-pyrimethamine) doses** to **Plasmodium falciparum multidrug resistant gene 1 86Y mutant allele carriage**, reported as a adjusted odds ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Pregnant women participating in the COSMIC trial in the Nanoro Health District of Burkina Faso.

## Provenance

- Source study: [[@natama2020]]
- Paper: Prevalence and factors associated with carriage of Pfmdr1 polymorphisms among pregnant women receiving intermittent preventive treatment with sulfadoxine-pyrimethamine (IPTp-SP) and artemether-lumefantrine for malaria treatment in Burkina Faso.
- Journal: Malaria journal
- Published: 2020 Nov 10
- PubMed: [33172485](https://pubmed.ncbi.nlm.nih.gov/33172485/)
- System association ID: `kwJ8LM3Tod`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
