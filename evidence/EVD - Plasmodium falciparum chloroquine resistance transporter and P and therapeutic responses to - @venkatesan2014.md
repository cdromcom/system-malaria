---
NodeFormality: draft
human_reviewed: no
aliases:
  - "EVD - Plasmodium falciparum chloroquine resistance transporter and P and therapeutic responses to artesunate-amodiaquine and showed an adjusted hazard ratio of 4.74 - @venkatesan2014"
tags:
  - "marker/pfcrt"
  - "marker/pfmdr1"
  - "theme/other"
  - "stat/adjusted_hazard_ratio"
  - "direction/positive"
  - "verification/api-only"
  - "year/2014"
created: 2026-11-14
updated: 2026-11-14
nodeID: 0602f872-ec44-4a70-8cdd-11b27ef29d20
title: Plasmodium falciparum chloroquine resistance transporter and P and therapeutic responses to artesunate-amodiaquine and showed an adjusted hazard ratio of 4.74 - @venkatesan2014
---

## Source

[[@venkatesan2014]]

## In plain terms

> [!info] What this finding says
> A study published in 2014 reported a statistical link between **Plasmodium falciparum chloroquine resistance transporter and P. falciparum multidrug resistance 1 (pfmdr1) genes** and **therapeutic responses to artesunate-amodiaquine and artemether-lumefantrine (AL)**.
> Plasmodium falciparum chloroquine resistance transporter and P and therapeutic responses to artesunate-amodiaquine and showed an adjusted hazard ratio of 4.74, p = 0.001. The confidence interval runs from 2.29 to 9.78.

## Statistic

| | |
|---|---|
| **Metric** | `adjusted_hazard_ratio` (System's normalised type; the paper reported `adjusted_hazard_ratio`) |
| **Estimate** | **4.74** |
| **p-value** | = 0.001 |
| **Confidence interval** | CI 2.29 to 9.78 (confidence level not recorded) |
| **Direction vs null of 0** | **positive** |
| **Data source** | API list, API detail |
| **In curated release** | No |
| **Source paper integrity** | a published erratum exists (checked against PubMed and Crossref) |

## Source paper screening

> [!info] Checked on 2026-11-14 against PubMed, Crossref, retractionrisk.com (Retraction Watch + Altmetric), OpenAlex and PMC full text.

| | |
|---|---|
| **Retraction status** | No retraction found (Retraction Watch via retractionrisk.com: Clean) |
| **Published erratum** | Yes — PubMed CommentsCorrections ErratumIn -> PMID 25948561; PubMed CommentsCorrections ErratumIn -> PMID 30698139 |
| **Formal published comments** | None |
| **Critical social posts** | None recorded — algorithmic sentiment; for these papers it often reflects alarm at the findings rather than doubt about the work |
| **PubPeer** | No PubPeer entry (checked by DOI and PubMed ID via the official PubPeer Foundation API; see [[CVT - What the post-publication screen covers and what it cannot]]) |
| **Open access** | Yes (hybrid) |
| **Open data** | A statement exists but is not explicit — WWARN |
| **Open code** | None found |
| **Public accessions** | None found |

## PICOST

| | |
|---|---|
| **Population** | 7,000 patients from 31 clinical trials who were treated with artesunate-amodiaquine (ASAQ) or artemether-lumefantrine (AL) for malaria. |
| **Intervention / exposure** | Not separable — see the direction warning below. |
| **Comparator** | Not recorded. |
| **Outcome** | Not separable — see the direction warning below. |
| **Setting** | Not stated separately — see Population above. |
| **Timeframe** | Published 2014. Fieldwork dates are not recorded in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> The record pairs `Plasmodium falciparum chloroquine resistance transporter and P. falciparum multidrug resistance 1 (pfmdr1) genes` with `therapeutic responses to artesunate-amodiaquine and artemether-lumefantrine (AL)` and reports a adjusted hazard ratio of 4.74. Nothing in the data says which was treated as the exposure, so this note does not claim that one caused the other. See [[CVT - The graph records no effect direction]].

> [!warning] The source paper has a published erratum
> PubMed CommentsCorrections ErratumIn -> PMID 25948561; PubMed CommentsCorrections ErratumIn -> PMID 30698139
> System extracted this statistic from the original article, and the graph records nothing about corrections. The number above may be one the erratum changed. Check the correction notice before citing it.

> [!warning] Units not recorded
> The graph gives no units for this value. For a prevalence or proportion it is most likely percentage points, but that is inference rather than data.

## Terms explained

- **PfCRT** — the malaria parasite's chloroquine-resistance transporter gene
- **Pfmdr1** — the malaria parasite's multidrug-resistance gene, which affects how well several antimalarial drugs work
- **artemether-lumefantrine** — a widely used artemisinin combination treatment, sold as Coartem
- **artesunate-amodiaquine** — an artemisinin combination treatment

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `Plasmodium falciparum chloroquine resistance transporter and P. falciparum multidrug resistance 1 (pfmdr1) genes`
> Variable 2: `therapeutic responses to artesunate-amodiaquine and artemether-lumefantrine (AL)`
> adjusted hazard ratio = 4.74, p = 0.001
> CI [2.29, 9.78]
> Direction against the statistic's null value of 0: **positive**

## Methods Context

### What?

The study related **Plasmodium falciparum chloroquine resistance transporter and P. falciparum multidrug resistance 1 (pfmdr1) genes** to **therapeutic responses to artesunate-amodiaquine and artemether-lumefantrine (AL)**, reported as a adjusted hazard ratio.

### How?

The graph records no study design for this paper. To judge how the finding was produced you have to read the source article.

### Who?

> 7,000 patients from 31 clinical trials who were treated with artesunate-amodiaquine (ASAQ) or artemether-lumefantrine (AL) for malaria.

## Provenance

- Source study: [[@venkatesan2014]]
- Paper: Polymorphisms in Plasmodium falciparum chloroquine resistance transporter and multidrug resistance 1 genes: parasite risk factors that affect treatment outcomes for P. falciparum malaria after artemether-lumefantrine and artesunate-amodiaquine.
- Journal: The American journal of tropical medicine and hygiene
- Published: 2014 Oct
- PubMed: [25048375](https://pubmed.ncbi.nlm.nih.gov/25048375/)
- System association ID: `SC8YvDjE97`
- Resistance gene(s): PfCRT, Pfmdr1
- Outcome theme(s): other malaria outcomes

## Verification

> [!warning] Not in the curated dataset — treat as unverified
> This finding is in the live API but not in System's curated Harvard Dataverse release. System's documentation says to discard such records, but that release is also much smaller in scope (2.0 million findings against the API's 5.9 million), so absence is a reason to check the source paper rather than proof the number is wrong. See [[CVT - The curated Dataverse deposit holds almost no resistance evidence]].

## Other Notes

> [!info] Extraction reliability
> System documents an approximate 20% error rate when its pipeline reads statistics out of papers. See [[CVT - Roughly 20 percent of API associations are mis-extracted]].
