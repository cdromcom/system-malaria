---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Chloroquine resistance (treatment failure) and parasite reduction ratio showed a mean difference unstandardized of 12.6 - @ketema2011"
tags:
  - "marker/pfcrt"
  - "theme/treatment-failure"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/in-curated-deposit"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: 9e7103ba-cd91-44b6-8ab7-0798000fd897
title: Chloroquine resistance (treatment failure) and parasite reduction ratio showed a mean difference unstandardized of 12.6 - @ketema2011
---

## Source

[[@ketema2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **Chloroquine resistance (treatment failure)** and **parasite reduction ratio**.
> Chloroquine resistance (treatment failure) and parasite reduction ratio showed a mean difference unstandardized of 12.6.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **12.6** |
| **p-value** | Not recorded |
| **Confidence interval** | Not recorded |
| **Direction vs null of 0** | **positive** |
| **Data source** | API list, API detail, Dataverse release |
| **In curated release** | Yes |
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
| **Population** | The 87 malaria patients enrolled in the study conducted in Halaba district, South Ethiopia. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Halaba district |
| **Timeframe** | Experimental Trial, published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Chloroquine resistance (treatment failure)` with `parasite reduction ratio` and reports a mean difference unstandardized of 12.6. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] This finding is unlikely to be independently reproducible
> No data-availability statement was found in the paper's full text. Nobody can re-derive this statistic from public material, so it rests entirely on System's extraction being correct and on the paper's own analysis.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Chloroquine resistance (treatment failure)`
> Variable 2: `parasite reduction ratio`
> mean difference unstandardized = 12.6
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Chloroquine resistance (treatment failure)** to **parasite reduction ratio**, reported as a mean difference unstandardized.

### How?

Study design: Experimental Trial.

### Who?

> The 87 malaria patients enrolled in the study conducted in Halaba district, South Ethiopia.

## Provenance

- Source study: [[@ketema2011]]
- Paper: Therapeutic efficacy of chloroquine for treatment of Plasmodium vivax malaria cases in Halaba district, South Ethiopia.
- Journal: Parasites & vectors
- Published: 2011 Mar 31
- PubMed: [21453465](https://pubmed.ncbi.nlm.nih.gov/21453465/)
- System association ID: `YnFZFejqfB`
- Resistance gene(s): PfCRT
- Outcome theme(s): whether malaria treatment failed

## Verification

> [!success] Checked against the curated dataset
> This finding also appears in System's curated Harvard Dataverse release, from which the extractions System had flagged as inaccurate were removed. That is the best available sign that the number was read correctly from the paper.

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
