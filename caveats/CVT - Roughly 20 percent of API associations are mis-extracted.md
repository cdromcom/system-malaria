---
NodeFormality: draft
human_reviewed: no
aliases:
  - "Roughly 20 percent of API associations are mis-extracted"
tags:
  - "cvt/api/data-quality"
created: 2026-11-14
updated: 2026-11-14
nodeID: 38e5a682-5926-4e52-8b18-7a56226cc23e
title: Roughly 20 percent of API associations are mis-extracted
---

## Statement

System's documentation states that roughly 20% of the findings its API returns were read inaccurately out of the source papers — it gives wrong mean differences as the example. The records System had flagged were removed from its curated Harvard Dataverse release, and the documentation advises checking API results against that release.

## Why it limits the evidence

For an alert system this is the central threat. A number misread from a paper looks exactly like a genuinely surprising new result, which is precisely what the tool is built to spot. An alert that simply ranks findings by how surprising they are would work as a misextraction detector. Every finding must therefore carry its verification state, and no unverified number should ever be shown as a bare figure.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
