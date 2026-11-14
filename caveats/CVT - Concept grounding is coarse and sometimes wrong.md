---
NodeFormality: draft
human_reviewed: no
aliases:
  - "Concept grounding is coarse and sometimes wrong"
tags:
  - "cvt/graph/grounding"
created: 2026-11-14
updated: 2026-11-14
nodeID: e64d0027-9477-4645-ba36-4835e8fc4f6f
title: Concept grounding is coarse and sometimes wrong
---

## Statement

The graph can link a variable to a shared concept in Wikidata, which should let different wordings collapse together. Only 732 of 2,055 marker variables (36%) carry such a link, and they spread across 193 different concepts, including ones as broad as `mutation` and `antimicrobial resistance`, ones plainly wrong such as `postoperative complications` and `induction chemotherapy`, and one actively misleading: `5,10-methylenetetrahydrofolate reductase`, which is the human MTHFR enzyme, standing in for the parasite's DHFR.

## Why it limits the evidence

The concept layer cannot be used to group synonyms. The MTHFR case is worse than no link at all, because it would silently merge human folate-pathway research with malaria resistance research. Expanding outward through these concepts returned 18,380 sibling variables, of which exactly one was malaria-related.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
