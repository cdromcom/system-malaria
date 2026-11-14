---
NodeFormality: draft
human_reviewed: no
aliases:
  - "What the post-publication screen covers and what it cannot"
tags:
  - "cvt/source/integrity"
created: 2026-11-14
updated: 2026-11-14
nodeID: 2d1c40ce-66d2-4f73-9829-f792824aa8d4
title: What the post-publication screen covers and what it cannot
---

## Statement

All 117 source papers were screened on 14 November 2026 against four sources: PubMed's CommentsCorrections records, Crossref's update metadata, Retraction Watch via retractionrisk.com, and **PubPeer via the official PubPeer Foundation extension API** (`POST https://pubpeer.com/v3/publications`, the endpoint published in their own MIT-licensed browser extension).

Results: **none is retracted and none carries an expression of concern.** Four carry a published erratum (Witkowski 2017, Win 2016, Venkatesan 2014, Antia-Obong 1997). Eight attracted formal published comments, including three of the highest-profile artemisinin-resistance papers in the set (Balikagala 2021, Mihreteab 2023, Spring 2015). Five carry negatively-scored social posts. And **not one of the 117 has any PubPeer entry at all**, queried both by DOI and by PubMed ID.

The PubPeer zero was verified rather than assumed: a known heavily-commented retraction placed inside a full 20-DOI batch alongside 19 of our papers came back with its 34 comments and four update types, while ours returned nothing. The batching path works, so the absence is real.

## Why it limits the evidence

**Zero PubPeer coverage is not evidence of quality.** PubPeer's attention concentrates on high-profile papers and on suspected image or statistics problems, largely in cell biology and psychology. A specialist malaria-genotyping literature having no threads most plausibly means nobody has looked, not that nothing is wrong. Read the silence as absence of scrutiny, not as endorsement.

Two genuine limits remain. First, an erratum means the article was corrected after publication and System extracted its statistics from the original, so a corrected value may still sit in this vault unchanged; those four papers' findings carry a warning. Second, informal critique — journal clubs, conference corridors, correspondence — leaves no machine-readable trace anywhere, so no screen can reach it.

On the Retraction Watch comparison: retractionrisk.com reported 2 corrections where PubMed's own records show 4, so the aggregator is the less sensitive of the two sources. Its Altmetric feed did add something no other source here provides — 74 negatively-scored posts for Mihreteab 2023, 52 for Balikagala 2021, 3 for Landier 2018, 1 each for two others. Treat that carefully: the sentiment is algorithmic, and for papers announcing that artemisinin resistance has reached Africa a negative score most plausibly reflects alarm at the finding rather than doubt about the work. Its own PubPeer counts are always 0, because its backend is blocked by PubPeer from cloud IP addresses.

## Affects

- Every evidence note in this vault, unless stated otherwise.

## Provenance

Established by direct measurement against the live API and the curated Dataverse release on 2026-11-14. See `LOG.md` and `scripts/`.
