---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Prevalence of DHFR-mutation I164L and P. falciparum showed a mean difference unstandardized of 0.061 - @wichmann2003"
tags:
  - "marker/pfdhfr"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2003"
created: 2026-11-14
updated: 2026-11-14
nodeID: d6cbbb0f-9f25-4f8f-b73f-dec8f37d5621
title: Prevalence of DHFR-mutation I164L and P. falciparum showed a mean difference unstandardized of 0.061 - @wichmann2003
---

## Source

[[@wichmann2003]]

## In plain terms

> [!info] What this finding says
> A study published in 2003 reported a statistical link between **Prevalence of DHFR-mutation I164L (in African isolates of Plasmodium falciparum imported into Europe through travellers)** and **P. falciparum**.
> Prevalence of DHFR-mutation I164L and P. falciparum showed a mean difference unstandardized of 0.061.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **0.061** |
| **p-value** | Not recorded |
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
| **Open data** | A statement exists but is not explicit |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 277 imported African isolates of Plasmodium falciparum. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2003. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Prevalence of DHFR-mutation I164L (in African isolates of Plasmodium falciparum imported into Europe through travellers)` with `P. falciparum` and reports a mean difference unstandardized of 0.061. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHFR** — dihydrofolate reductase, the parasite enzyme that the drug pyrimethamine blocks
- **I164L** — a mutation that swaps amino acid I for L at position 164 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Prevalence of DHFR-mutation I164L (in African isolates of Plasmodium falciparum imported into Europe through travellers)`
> Variable 2: `P. falciparum`
> mean difference unstandardized = 0.061
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Prevalence of DHFR-mutation I164L (in African isolates of Plasmodium falciparum imported into Europe through travellers)** to **P. falciparum**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 277 imported African isolates of Plasmodium falciparum.

## Provenance

- Source study: [[@wichmann2003]]
- Paper: Molecular surveillance of the antifolate-resistant mutation I164L in imported African isolates of Plasmodium falciparum in Europe: sentinel data from TropNetEurop.
- Journal: Malaria journal
- Published: 2003 Jun 25
- PubMed: [12869209](https://pubmed.ncbi.nlm.nih.gov/12869209/)
- System association ID: `5X6oiy-CDs`
- Resistance gene(s): PfDHFR
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
