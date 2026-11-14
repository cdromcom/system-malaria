---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - prevalence of Plasmodium falciparum dihydropteroate synthetase gene differed by 18 between group that took intermittent preventive treatment with and group that did not take intermittent (mean difference unstandardized) - @cohen2023"
tags:
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2023"
created: 2026-11-14
updated: 2026-11-14
nodeID: 99598119-1f7b-4c0d-8796-85d232d2bd00
title: prevalence of Plasmodium falciparum dihydropteroate synthetase gene differed by 18 between group that took intermittent preventive treatment with and group that did not take intermittent (mean difference unstandardized) - @cohen2023
---

## Source

[[@cohen2023]]

## In plain terms

> [!info] What this finding says
> A study published in 2023 reported a statistical link between **group that took intermittent preventive treatment with sulfadoxine-pyrimethamine (IPTp-SP)** and **prevalence of Plasmodium falciparum dihydropteroate synthetase gene vagKgs quintuple mutant**.
> Prevalence of Plasmodium falciparum dihydropteroate synthetase gene differed by 18 between group that took intermittent preventive treatment with and group that did not take intermittent (mean difference unstandardized), p = 0.001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **18** |
| **p-value** | = 0.001 |
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
| **Open access** | Yes (bronze) |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Pregnant women with malaria in Yaoundé, Cameroon. |
| **Intervention / exposure** | group that took intermittent preventive treatment with sulfadoxine-pyrimethamine (IPTp-SP) |
| **Comparator** | group that did not take intermittent preventive treatment with sulfadoxine-pyrimethamine (IPTp-SP |
| **Outcome** | prevalence of Plasmodium falciparum dihydropteroate synthetase gene vagKgs quintuple mutant |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2023. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children
- **IPTp** — intermittent preventive treatment in pregnancy, where pregnant women are given antimalarial drugs at routine visits whether or not they are infected

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `group that took intermittent preventive treatment with sulfadoxine-pyrimethamine (IPTp-SP) [vs group that did not take intermittent preventive treatment with sulfadoxine-pyrimethamine (IPTp-SP)]`
> Variable 2: `prevalence of Plasmodium falciparum dihydropteroate synthetase gene vagKgs quintuple mutant`
> mean difference unstandardized = 18, p = 0.001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **group that took intermittent preventive treatment with sulfadoxine-pyrimethamine (IPTp-SP)** to **prevalence of Plasmodium falciparum dihydropteroate synthetase gene vagKgs quintuple mutant**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Pregnant women with malaria in Yaoundé, Cameroon.

## Provenance

- Source study: [[@cohen2023]]
- Paper: Effect of sulfadoxine-pyrimethamine chemoprophylaxis in pregnant women on selection of the new P. falciparum dhps quintuple mutant carrying the I431V mutation.
- Journal: The Journal of antimicrobial chemotherapy
- Published: 2023 Mar 2
- PubMed: [36611259](https://pubmed.ncbi.nlm.nih.gov/36611259/)
- System association ID: `iJcN4hRRVc`
- Resistance gene(s): PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
