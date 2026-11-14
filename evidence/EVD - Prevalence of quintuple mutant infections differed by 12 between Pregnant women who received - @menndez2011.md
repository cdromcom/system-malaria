---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Prevalence of quintuple mutant infections differed by 12 between Pregnant women who received sulphadoxine-pyrimethamine (sulfadoxine-pyrimethamine) and Pregnant women who received placebo (mean difference unstandardized) - @menndez2011"
tags:
  - "marker/pfdhps"
  - "theme/marker-prevalence"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2011"
created: 2026-11-14
updated: 2026-11-14
nodeID: 5f98e1e9-be3f-4746-9496-a2fab0c60352
title: Prevalence of quintuple mutant infections differed by 12 between Pregnant women who received sulphadoxine-pyrimethamine (sulfadoxine-pyrimethamine) and Pregnant women who received placebo (mean difference unstandardized) - @menndez2011
---

## Source

[[@menndez2011]]

## In plain terms

> [!info] What this finding says
> A study published in 2011 reported a statistical link between **Pregnant women who received sulphadoxine-pyrimethamine (sulfadoxine-pyrimethamine)** and **Prevalence of quintuple mutant infections**.
> Prevalence of quintuple mutant infections differed by 12 between Pregnant women who received sulphadoxine-pyrimethamine (sulfadoxine-pyrimethamine) and Pregnant women who received placebo (mean difference unstandardized), p = 0.031.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **12** |
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
| **Open access** | No |
| **Open data** | Cannot tell — not deposited in PMC |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Pregnant women enrolled in a randomized, placebo-controlled trial of IPTp in Manhiça, Mozambique. |
| **Intervention / exposure** | Pregnant women who received sulphadoxine-pyrimethamine |
| **Comparator** | Pregnant women who received placebo |
| **Outcome** | Prevalence of quintuple mutant infections |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Experimental Trial, published 2011. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfDHPS** — dihydropteroate synthase, the parasite enzyme that the drug sulfadoxine blocks
- **sulfadoxine-pyrimethamine** — an older antimalarial drug pair, still used to protect pregnant women and young children

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Pregnant women who received sulphadoxine-pyrimethamine [vs Pregnant women who received placebo]`
> Variable 2: `Prevalence of quintuple mutant infections`
> mean difference unstandardized = 12, p = 0.031
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Pregnant women who received sulphadoxine-pyrimethamine (sulfadoxine-pyrimethamine)** to **Prevalence of quintuple mutant infections**, reported as a mean difference unstandardized.

### How?

Study design: Experimental Trial.

### Who?

> Pregnant women enrolled in a randomized, placebo-controlled trial of IPTp in Manhiça, Mozambique.

## Provenance

- Source study: [[@menndez2011]]
- Paper: HIV and placental infection modulate the appearance of drug-resistant Plasmodium falciparum in pregnant women who receive intermittent preventive treatment.
- Journal: Clinical infectious diseases : an official publication of the Infectious Diseases Society of America
- Published: 2011 Jan 1
- PubMed: [21148518](https://pubmed.ncbi.nlm.nih.gov/21148518/)
- System association ID: `kWNskGOE75`
- Resistance gene(s): PfDHPS
- Outcome theme(s): how common the resistance mutation was

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
