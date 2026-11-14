---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - frequency of mutation point pfcrt 76T differed by 23.8 between after treatment with Artesunate-Amodiaquine (AS+AQ) and before treatment (mean difference unstandardized) - @beavogui2021"
tags:
  - "marker/pfcrt"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2021"
created: 2026-11-14
updated: 2026-11-14
nodeID: dc4b6eeb-2f9b-43f2-be8a-830733c472b5
title: frequency of mutation point pfcrt 76T differed by 23.8 between after treatment with Artesunate-Amodiaquine (AS+AQ) and before treatment (mean difference unstandardized) - @beavogui2021
---

## Source

[[@beavogui2021]]

## In plain terms

> [!info] What this finding says
> A study published in 2021 reported a statistical link between **after treatment with Artesunate-Amodiaquine (AS+AQ)** and **frequency of mutation point pfcrt 76T**.
> Frequency of mutation point pfcrt 76T differed by 23.8 between after treatment with Artesunate-Amodiaquine (AS+AQ) and before treatment (mean difference unstandardized), p = 0.142.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **23.8** |
| **p-value** | = 0.142 |
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
| **Population** | 170 subjects in Guinea with uncomplicated malaria. |
| **Intervention / exposure** | after treatment with Artesunate-Amodiaquine (AS+AQ) |
| **Comparator** | before treatment |
| **Outcome** | frequency of mutation point pfcrt 76T |
| **Setting** | Guinea |
| **Timeframe** | Experimental Trial, published 2021. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **artesunate-amodiaquine** — an artemisinin combination treatment

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `after treatment with Artesunate-Amodiaquine (AS+AQ) [vs before treatment]`
> Variable 2: `frequency of mutation point pfcrt 76T`
> mean difference unstandardized = 23.8, p = 0.142
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **after treatment with Artesunate-Amodiaquine (AS+AQ)** to **frequency of mutation point pfcrt 76T**, reported as a mean difference unstandardized.

### How?

Study design: Experimental Trial.

### Who?

> 170 subjects in Guinea with uncomplicated malaria.

## Provenance

- Source study: [[@beavogui2021]]
- Paper: SELECTION OF PFCRT 76T AND PFMDR1 86Y MUTANT PLASMODIUM FALCIPARUM AFTER TREATMENT OF UNCOMPLICATED MALARIA WITH ARTESUNATE-AMODIAQUINE IN REPUBLIC OF GUINEA.
- Journal: The Journal of parasitology
- Published: 2021 Sep 1
- PubMed: [34581793](https://pubmed.ncbi.nlm.nih.gov/34581793/)
- System association ID: `w_p_ohQJag`
- Resistance gene(s): PfCRT
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
