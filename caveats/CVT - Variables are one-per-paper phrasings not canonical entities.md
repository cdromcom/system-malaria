---
NodeFormality: draft
human_reviewed: no
aliases:
  - "Variables are one-per-paper phrasings not canonical entities"
tags:
  - "cvt/graph/data-model"
created: 2026-11-14
updated: 2026-11-14
nodeID: 32964eb7-49be-4631-9648-1ebfd112eb1f
title: Variables are one-per-paper phrasings not canonical entities
---

## Statement

A 'variable' in this graph is one paper's exact wording — `Pfmdr1 N86`, `isolates with crt T76`, `Patients with k13 F446I mutation [vs Patients without k13 mutations]`. The graph holds 5,654,715 variables against 5,944,001 findings, roughly one new variable per finding.

## Why it limits the evidence

There is no single node for a gene, so nothing adds itself up. Assembling the evidence on one gene means matching patterns against millions of free-text strings, and every count in this vault depends on the specific patterns used, which live in `scripts/build_vault.py`. Different patterns would give different numbers. A related trap: the search is plain substring matching, so the abbreviation `crt` also matches cardiac resynchronisation therapy and chemoradiotherapy, and `IPT` matches isoniazid preventive therapy from the tuberculosis literature.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
