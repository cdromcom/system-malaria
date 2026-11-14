---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - K13 (Pfkelch13) mutation differed by -11 between sites in western border regions and sites in east and north regions (mean difference unstandardized) - @win2016"
tags:
  - "marker/pfkelch13"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/negative"
  - "verification/api-only"
  - "year/2016"
created: 2026-11-14
updated: 2026-11-14
nodeID: ed281ca4-f5ac-418b-b47f-ff1ee6696d59
title: K13 (Pfkelch13) mutation differed by -11 between sites in western border regions and sites in east and north regions (mean difference unstandardized) - @win2016
---

## Source

[[@win2016]]

## In plain terms

> [!info] What this finding says
> A study published in 2016 reported a statistical link between **sites in western border regions** and **K13 (Pfkelch13) mutation**.
> K13 (Pfkelch13) mutation differed by -11 between sites in western border regions and sites in east and north regions (mean difference unstandardized), p = 0.0001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **-11** |
| **p-value** | = 0.0001 |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **negative** |
| **Data source** | API list, API detail |
| **In curated release** | No |
| **Source paper integrity** | a published erratum exists (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: Corrected) |
| **Published erratum** | Yes — PubMed CommentsCorrections ErratumIn -> PMID 27234815; Crossref updated-by: correction (10.1186/s12936-016-1346-y) |
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
| **Population** | Patients with Plasmodium falciparum malarial infection in five malaria-endemic areas across Myanmar. |
| **Intervention / exposure** | sites in western border regions |
| **Comparator** | sites in east and north regions |
| **Outcome** | K13 mutation |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2016. Fieldwork dates are not recorded in the graph. |

> [!warning] The source paper has a published erratum
> PubMed CommentsCorrections ErratumIn -> PMID 27234815; Crossref updated-by: correction (10.1186/s12936-016-1346-y)
> System extracted this statistic from the original article, and the graph records nothing about corrections. The number above may be one the erratum changed. Check the correction notice before citing it.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `sites in western border regions [vs sites in east and north regions]`
> Variable 2: `K13 mutation`
> mean difference unstandardized = -11, p = 0.0001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **negative**

## Methods Context

### What?

The study related **sites in western border regions** to **K13 (Pfkelch13) mutation**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Patients with Plasmodium falciparum malarial infection in five malaria-endemic areas across Myanmar.

## Provenance

- Source study: [[@win2016]]
- Paper: K13 mutations and pfmdr1 copy number variation in Plasmodium falciparum malaria in Myanmar.
- Journal: Malaria journal
- Published: 2016 Feb 24
- PubMed: [26911145](https://pubmed.ncbi.nlm.nih.gov/26911145/)
- System association ID: `PWhWrCHj38`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
