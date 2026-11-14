---
NodeFormality: draft
human_reviewed: no
aliases:
tags:
created:
updated:
nodeID:
title:
---

## Source

`[[@surnameYEAR]]`

## In plain terms

> [!info] What this finding says
> One sentence naming both things related, with the number, written for a non-specialist.

## PICOST

| | |
|---|---|
| **Population** | Who was studied, verbatim from the graph's population string. |
| **Intervention / exposure** | The first variable, with any `[vs …]` comparator split out. |
| **Comparator** | What it was compared against. "Implied but not named" when the statistic needs one but the record omits it. |
| **Outcome** | The second variable. |
| **Setting** | Country or site, parsed from the population string. "Not stated separately" when parsing fails. |
| **Timeframe** | Study design and publication year. Fieldwork dates are never in the graph. |

> [!warning] Which is cause and which is effect cannot be determined
> Include this whenever the record does not clearly name an exposure and an outcome.

> [!warning] Units not recorded
> Include this for any difference, coefficient or correlation, where the graph gives no units.

> [!warning] Possible extraction mismatch
> Include this when the gene named in the record does not appear in the source paper's title.

## Terms explained

- **Term** — plain-English gloss. Always include the gene, even when it was matched only
  through a mutation code.

## Description

> [!info] The finding exactly as System extracted it
> Variable 1: `raw name`
> Variable 2: `raw name`
> statistic = value, p = value
> Direction against the statistic's null value of 1 or 0: **positive / negative / null**

## Methods Context

### What?
### How?
### Who?

## Provenance

## Verification

## Other Notes
