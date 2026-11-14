---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of pfcrt T76 mutation differed by 18.7 between coastal areas foothills and highland areas (mean difference unstandardized) - @almekhlafi2011"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: e3af0ca7-c7da-4abd-88ee-0790d5c9f21a
title: prevalence of pfcrt T76 mutation differed by 18.7 between coastal areas foothills and highland areas (mean difference unstandardized) - @almekhlafi2011
---

## Source

[[@almekhlafi2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **coastal areas/foothills** and **prevalence of pfcrt T76 mutation**.
> Prevalence of pfcrt T76 mutation differed by 18.7 between coastal areas foothills and highland areas (mean difference unstandardized), p = 0.031.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **18.7** |
| **p-value** | = 0.031 |
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
| **Open access** | Yes (gold) |
| **Open data** | No availability statement found in the full text |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 511 participants from four governorates in Yemen. |
| **Intervention / exposure** | coastal areas/foothills |
| **Comparator** | highland areas |
| **Outcome** | prevalence of pfcrt T76 mutation |
| **Setting** | Yemen |
| **Timeframe** | Published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `coastal areas/foothills [vs highland areas]`
> Variable 2: `prevalence of pfcrt T76 mutation`
> mean difference unstandardized = 18.7, p = 0.031
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **coastal areas/foothills** to **prevalence of pfcrt T76 mutation**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 511 participants from four governorates in Yemen.

## Provenance

- Source study: [[@almekhlafi2011]]
- Paper: High frequency of Plasmodium falciparum chloroquine resistance marker (pfcrt T76 mutation) in Yemen: an urgent need to re-examine malaria drug policy.
- Journal: Parasites & vectors
- Published: 2011 May 27
- PubMed: [21619624](https://pubmed.ncbi.nlm.nih.gov/21619624/)
- System association ID: `Sl_2hE1X4i`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
