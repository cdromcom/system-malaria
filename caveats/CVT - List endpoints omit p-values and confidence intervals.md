---
NodeFormality: draft
human_reviewed: no
aliases:
  - "List endpoints omit p-values and confidence intervals"
tags:
  - "cvt/api/schema"
created: 2026-11-14
updated: 2026-11-14
nodeID: 6514af52-730d-4ccb-9218-4eec09deb528
title: List endpoints omit p-values and confidence intervals
---

## Statement

A list request to the API returns 10 fields per finding. The p-value, the confidence interval and the concept identifiers exist only when a single finding is fetched on its own. The documented `fields` parameter that would widen the list response returns an HTTP 500 error.

## Why it limits the evidence

Statistical precision costs one extra request per finding against a 10,000-per-day budget, so most evidence notes in this vault record no p-value or interval. The curated Dataverse release does carry all 19 columns in one file, which is its main practical advantage.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
