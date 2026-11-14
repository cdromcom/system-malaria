---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Presence of parasitemia (parasitaemia) on Day 3 after dihydroartemisinin was associated with an increase of 13 in ex vivo survival rates to artemisinin compounds and prevalence of (mean difference unstandardized) - @roviravallbona2020"
tags:
  - "marker/pfkelch13"
  - "theme/parasite-clearance"
  - "theme/marker-prevalence"
  - "theme/drug-susceptibility"
  - "stat/mean_difference_unstandardized"
  - "direction/positive"
  - "verification/api-only"
  - "year/2020"
created: 2026-11-14
updated: 2026-11-14
nodeID: e7ae40c2-7471-410b-a68f-163fbfeab6a7
title: Presence of parasitemia (parasitaemia) on Day 3 after dihydroartemisinin was associated with an increase of 13 in ex vivo survival rates to artemisinin compounds and prevalence of (mean difference unstandardized) - @roviravallbona2020
---

## Source

[[@roviravallbona2020]]

## In plain terms

> [!info] What this finding says
> A study published in 2020 reported a statistical link between **Presence of parasitemia (parasitaemia) on Day 3 after dihydroartemisinin/piperaquine treatment (positive vs negative)** and **ex vivo survival rates to artemisinin compounds and prevalence of kelch13 (Pfkelch13) mutations**.
> Presence of parasitemia (parasitaemia) on Day 3 after dihydroartemisinin was associated with an increase of 13 in ex vivo survival rates to artemisinin compounds and prevalence of (mean difference unstandardized), p = 0.048.

## Statistic

| | |
|---|---|
| **Metric** | `mean_difference_unstandardized` (System's normalised type; the paper reported `mean_difference_unstandardized`) |
| **Estimate** | **13** |
| **p-value** | = 0.048 |
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
| **Open data** | Cannot tell — PMC holds front matter only — ClinicalTrials.gov |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | Sixty patients with uncomplicated P. falciparum malaria in Gia Lai, Central Vietnam. |
| **Intervention / exposure** | Presence of parasitemia on Day 3 after dihydroartemisinin/piperaquine treatment (positive vs negative) |
| **Comparator** | Implied but not named in the record. |
| **Outcome** | ex vivo survival rates to artemisinin compounds and prevalence of kelch13 mutations |
| **Setting** | Gia Lai |
| **Timeframe** | Published 2020. Fieldwork dates are not recorded in the graph. |

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **Pfkelch13** — the malaria parasite gene whose mutations cause partial resistance to artemisinin, the backbone of modern malaria treatment
- **parasitaemia** — the density of malaria parasites in the blood
- **ex vivo** — tested on fresh parasites taken straight from patients

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Presence of parasitemia on Day 3 after dihydroartemisinin/piperaquine treatment (positive vs negative)`
> Variable 2: `ex vivo survival rates to artemisinin compounds and prevalence of kelch13 mutations`
> mean difference unstandardized = 13, p = 0.048
> Confidence interval not available from the list endpoint — see [[CVT - List endpoints omit p-values and confidence intervals]]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Presence of parasitemia (parasitaemia) on Day 3 after dihydroartemisinin/piperaquine treatment (positive vs negative)** to **ex vivo survival rates to artemisinin compounds and prevalence of kelch13 (Pfkelch13) mutations**, reported as a mean difference unstandardized.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> Sixty patients with uncomplicated P. falciparum malaria in Gia Lai, Central Vietnam.

## Provenance

- Source study: [[@roviravallbona2020]]
- Paper: Efficacy of dihydroartemisinin/piperaquine and artesunate monotherapy for the treatment of uncomplicated Plasmodium falciparum malaria in Central Vietnam.
- Journal: The Journal of antimicrobial chemotherapy
- Published: 2020 Aug 1
- PubMed: [32437557](https://pubmed.ncbi.nlm.nih.gov/32437557/)
- System association ID: `Di4rKuuc2u`
- Resistance gene(s): Pfkelch13
- Outcome theme(s): how fast malaria parasites cleared from the blood, how common the resistance mutation was, how well antimalarial drugs killed the parasite in the laboratory

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
