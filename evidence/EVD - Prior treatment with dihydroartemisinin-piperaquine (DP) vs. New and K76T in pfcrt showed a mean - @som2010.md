---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Prior treatment with dihydroartemisinin-piperaquine (DP) vs. New and K76T in pfcrt showed a mean difference unstandardized of 7.2 - @som2010"
tags:
  - "marker/pfcrt"
  - "theme/other"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2010"
created: 2026-11-14
updated: 2026-11-14
nodeID: a3dc33ce-5911-4b19-94d3-00d1b0361566
title: Prior treatment with dihydroartemisinin-piperaquine (DP) vs. New and K76T in pfcrt showed a mean difference unstandardized of 7.2 - @som2010
---

## Source

[[@som2010]]

## In plain terms

> [!info] What this finding says
> A study published in 2010 reported a statistical link between **Prior treatment with dihydroartemisinin-piperaquine (DP) vs. New infections** and **K76T in pfcrt**.
> Prior treatment with dihydroartemisinin-piperaquine (DP) vs. New and K76T in pfcrt showed a mean difference unstandardized of 7.2, p = 0.43.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **7.2** |
| **p-value** | = 0.43 |
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
| **Open access** | Yes (green) |
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 559 children in Burkina Faso in 2006 and 378 additional treatments with DP in 2007. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2010. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Prior treatment with dihydroartemisinin-piperaquine (DP) vs. New infections` with `K76T in pfcrt` and reports a mean difference unstandardized of 7.2. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **dihydroartemisinin-piperaquine** — an artemisinin combination treatment
- **K76T** — a mutation that swaps amino acid K for T at position 76 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Prior treatment with dihydroartemisinin-piperaquine (DP) vs. New infections`
> Variable 2: `K76T in pfcrt`
> mean difference unstandardized = 7.2, p = 0.43
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Prior treatment with dihydroartemisinin-piperaquine (DP) vs. New infections** to **K76T in pfcrt**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 559 children in Burkina Faso in 2006 and 378 additional treatments with DP in 2007.

## Provenance

- Source study: [[@som2010]]
- Paper: Selection of known Plasmodium falciparum resistance-mediating polymorphisms by artemether-lumefantrine and amodiaquine-sulfadoxine-pyrimethamine but not dihydroartemisinin-piperaquine in Burkina Faso.
- Journal: Antimicrobial agents and chemotherapy
- Published: 2010 May
- PubMed: [20231394](https://pubmed.ncbi.nlm.nih.gov/20231394/)
- System association ID: `D2vIU_xqV4`
- Resistance gene(s): PfCRT
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
