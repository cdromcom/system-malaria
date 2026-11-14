---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - pfcrt, pfmdr1 and pfdhfr and Osogbo and Lafia showed a relative risk ratio of 1.08 - @ojurongbe2010"
tags:
  - "marker/pfcrt"
  - "marker/pfmdr1"
  - "marker/pfdhfr"
  - "theme/other"
  - "stat/relative_risk_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2010"
created: 2026-11-14
updated: 2026-11-14
nodeID: a5883fc1-5ffe-43c7-b14d-2b994f3f4890
title: pfcrt, pfmdr1 and pfdhfr and Osogbo and Lafia showed a relative risk ratio of 1.08 - @ojurongbe2010
---

## Source

[[@ojurongbe2010]]

## In plain terms

> [!info] What this finding says
> A study published in 2010 reported a statistical link between **pfcrt, pfmdr1 and pfdhfr** and **Osogbo and Lafia**.
> Pfcrt, pfmdr1 and pfdhfr and Osogbo and Lafia showed a relative risk ratio of 1.08.

## Statistic

| | |
|---|---|
| **Metric** | `relative_risk_ratio` (System's normalised type; the paper reported `relative_risk_ratio`) |
| **Estimate** | **1.08** |
| **p-value** | Not recorded |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | P. falciparum isolates collected from two geographically distinct areas of Nigeria. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2010. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `pfcrt, pfmdr1 and pfdhfr` with `Osogbo and Lafia` and reports a relative risk ratio of 1.08. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **DHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `pfcrt, pfmdr1 and pfdhfr`
> Variable 2: `Osogbo and Lafia`
> relative risk ratio = 1.08
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 1: **positive**

## Methods Context

### What?

The study related **pfcrt, pfmdr1 and pfdhfr** to **Osogbo and Lafia**, reported as a relative risk ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> P. falciparum isolates collected from two geographically distinct areas of Nigeria.

## Provenance

- Source study: [[@ojurongbe2010]]
- Paper: Molecular surveillance of drug-resistant Plasmodium falciparum in two distinct geographical areas of Nigeria.
- Journal: Wiener klinische Wochenschrift
- Published: 2010 Dec
- PubMed: [21120702](https://pubmed.ncbi.nlm.nih.gov/21120702/)
- System association ID: `D6UJg7nq0D`
- Resistance gene(s): PfCRT, Pfmdr1, PfDHFR
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
