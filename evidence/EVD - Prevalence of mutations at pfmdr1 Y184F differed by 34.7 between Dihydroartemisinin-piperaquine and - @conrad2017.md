---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Prevalence of mutations at pfmdr1 Y184F differed by 34.7 between Dihydroartemisinin-piperaquine and Sulfadoxine-pyrimethamine (mean difference unstandardized) - @conrad2017"
tags:
  - "marker/pfmdr1"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2017"
created: 2026-11-14
updated: 2026-11-14
nodeID: cf57bc40-7e9d-4230-b169-12fc4bb6544f
title: Prevalence of mutations at pfmdr1 Y184F differed by 34.7 between Dihydroartemisinin-piperaquine and Sulfadoxine-pyrimethamine (mean difference unstandardized) - @conrad2017
---

## Source

[[@conrad2017]]

## In plain terms

> [!info] What this finding says
> A study published in 2017 reported a statistical link between **Dihydroartemisinin-piperaquine** and **Prevalence of mutations at pfmdr1 Y184F**.
> Prevalence of mutations at pfmdr1 Y184F differed by 34.7 between Dihydroartemisinin-piperaquine and Sulfadoxine-pyrimethamine (mean difference unstandardized), p = 0.001.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **34.7** |
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
| **Open data** | Cannot tell — PMC holds front matter only |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Pregnant women in Uganda receiving either dihydroartemisinin-piperaquine (DP) or sulfadoxine-pyrimethamine (SP) as part of a trial of intermittent preventive treatment in pregnancy (IPTp). |
| **Intervention / exposure** | Dihydroartemisinin-piperaquine |
| **Comparator** | Sulfadoxine-pyrimethamine |
| **Outcome** | Prevalence of mutations at pfmdr1 Y184F |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2017. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children
- **dihydroartemisinin-piperaquine** — an artemisinin combination treatment
- **Y184F** — a mutation that swaps amino acid Y for F at position 184 of the protein

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Dihydroartemisinin-piperaquine [vs Sulfadoxine-pyrimethamine ]`
> Variable 2: `Prevalence of mutations at pfmdr1 Y184F`
> mean difference unstandardized = 34.7, p = 0.001
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Dihydroartemisinin-piperaquine** to **Prevalence of mutations at pfmdr1 Y184F**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Pregnant women in Uganda receiving either dihydroartemisinin-piperaquine (DP) or sulfadoxine-pyrimethamine (SP) as part of a trial of intermittent preventive treatment in pregnancy (IPTp).

## Provenance

- Source study: [[@conrad2017]]
- Paper: Impact of Intermittent Preventive Treatment During Pregnancy on Plasmodium falciparum Drug Resistance-Mediating Polymorphisms in Uganda.
- Journal: The Journal of infectious diseases
- Published: 2017 Nov 15
- PubMed: [28968782](https://pubmed.ncbi.nlm.nih.gov/28968782/)
- System association ID: `vIWK-ebDqW`
- Resistance gene(s): Pfmdr1
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
