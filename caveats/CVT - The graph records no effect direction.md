---
NodeFormality: draft
human_reviewed: no
aliases:
  - "The graph records no effect direction"
tags:
  - "cvt/api/schema"
created: 2026-11-14
updated: 2026-11-14
nodeID: 30ac12bd-46f3-4e60-a547-88cf02abf6dd
title: The graph records no effect direction
---

## Statement

Findings carry a statistic type and a value but no field saying which way the relationship runs, and no field saying which of the two variables is the cause. The harvested set mixes odds ratios, adjusted odds ratios, risk ratios, hazard ratios, prevalence ratios, incidence rate ratios, unstandardised mean differences, regression coefficients and correlations.

## Why it limits the evidence

Direction has to be inferred from the statistic type — ratios pivot at 1, differences and correlations at 0. Two things stay unrecoverable: which variable is cause and which is effect, and the sign of a comparison the extractor folded into a variable name, as in 'Laos (compared with Thailand)'. Reading such a name backwards flips the finding.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
