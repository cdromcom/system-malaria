---
NodeFormality: draft
human_reviewed: no
aliases:
  - "The curated Dataverse deposit holds almost no resistance evidence"
tags:
  - "cvt/source/dataverse"
created: 2026-11-14
updated: 2026-11-14
nodeID: fa1a3c61-7230-4252-8947-32ebb354d6bc
title: The curated Dataverse deposit holds almost no resistance evidence
---

## Statement

System's curated release on Harvard Dataverse (doi:10.7910/DVN/7V6JDO) is the cleaned version, with flagged mis-extractions removed. Its findings file holds 1,999,877 rows against the API's 5,944,001 (34%), and its variables file 1,774,551 against 5,654,715 (31%). A regex sweep of all 1,999,877 findings turned up just 25 that pair a resistance gene with malaria context, against 1,184 harvested from the API. Only 272 of those 1,184 (23%) appear in the release at all — below the ~34% a uniform random subset would give.

## Why it limits the evidence

The curated release cannot be the main data source for this topic; the API has roughly fifty times more. Its value is as a verification layer, since presence in it is the best available signal that a number was read correctly, and for the statistical columns the API withholds from list responses. Note that System's advice to discard anything absent from the release would throw away 77% of this vault, and that absence reflects the release's narrower scope as much as data quality.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
