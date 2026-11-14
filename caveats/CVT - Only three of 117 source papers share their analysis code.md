---
NodeFormality: draft
human_reviewed: no
aliases:
  - "Only three of 117 source papers share their analysis code"
tags:
  - "cvt/source/reproducibility"
created: 2026-11-14
updated: 2026-11-14
nodeID: 529116c9-adbf-489c-8910-a033257cf6ec
title: Only three of 117 source papers share their analysis code
---

## Statement

Open-access status, data availability and code availability were checked for all 117 source papers on 14 November 2026 using OpenAlex, NCBI's ID converter and PMC full text. **89 of 117 are open access** in some form (gold 44, green 21, bronze 13, hybrid 7, diamond 4) and 27 are closed. Only **58 have full text deposited in PMC**, which is what makes an availability statement readable at all. Of the 58 that could be assessed, only **6 clearly deposited their data in a public repository**, 9 offer it on request only, 18 have a statement too vague to classify and 25 have none at all. **Just 3 papers share analysis code**, all on GitHub: `Mrc-ide/mipanalyzer`, `bailey-lab/MIPTools` and `EPPIcenter/moire`. Only 4 cite an unambiguous public sequence accession, though 26 name a repository such as GenBank, the Sequence Read Archive or MalariaGEN in their text.

An earlier run of this check reported 35 papers as having deposited data and 46 as citing accessions. That was wrong: the accession pattern included a generic two-letter plus six-digit form that matched ordinary words such as `Mc080501`, and any paper with a spurious match was classified as having deposited data. Tightening the pattern to named formats only (PRJNA, PRJEB, ERP, SRP, SRR, GSE, ERS) cut deposits from 35 to 6.

## Why it limits the evidence

This is the reproducibility picture for the evidence base, and it is poor in a specific way: hardly anything is shared. Six papers in 117 deposited data and three published code, so the analysis that turned raw observations into the statistic in this vault is almost never replayable, and usually neither are the observations. Worse, **for 59 papers (51%) the question cannot be answered at all** — 36 are not in PMC and 23 have only front matter there — so 'no statement found' and 'cannot tell' must not be read as the same thing. Findings whose source offers data on request or has no statement carry an explicit warning, because nobody can re-derive them from public material: they rest entirely on System's extraction being right and on the paper's own analysis being right.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
