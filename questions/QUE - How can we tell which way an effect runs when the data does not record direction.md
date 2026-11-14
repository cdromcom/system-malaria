---
NodeFormality: draft
human_reviewed: no
aliases:
  - "QUE - How can we tell which way an effect runs when the data does not record a direction?"
tags:
  - "method/direction"
created: 2026-11-14
updated: 2026-11-14
nodeID: a627e572-ce07-459e-baf5-cb542d45a214
title: How can we tell which way an effect runs when the data does not record a direction?
---

## The question

**How can we tell which way an effect runs when the data does not record a direction?**

## Why it matters

Each finding in the graph is a pair of measured things and a number. Nothing says which of the two came first, which caused which, or whether the relationship is positive or negative. For an alert that is supposed to warn that resistance is worsening, that is a serious gap — 'worsening' is a direction.

## Where we have got to

> [!info] Current answer
> Partly solvable. Ratio statistics pivot around 1 and difference statistics around 0, so a rule can be written per statistic type. What cannot be recovered is which variable is the cause and which the effect, or the sign of comparisons that the extractor buried inside a variable name such as 'Laos (compared with Thailand)'.

## Supporting Claims (with their evidence)

> [!info] Each claim below counts how many published findings link one resistance gene to one kind of outcome. Auto-linked — check relevance before citing.

- [[CLM - Resistance-mutation prevalence in Pfmdr1 rises with drug pressure and over time across the settings studied|Resistance-mutation prevalence in Pfmdr1 rises with drug pressure and over time across the settings studied, though a minority of findings disagree]]
- [[CLM - Resistance-mutation prevalence in PfCRT rises with drug pressure and over time across the settings studied|Resistance-mutation prevalence in PfCRT rises with drug pressure and over time across the settings studied, though a minority of findings disagree]]
- [[CLM - Mutations in PfCRT are positively associated with a range of other malaria measures, though a minority of|Mutations in PfCRT are positively associated with a range of other malaria measures, though a minority of findings disagree]]
- [[CLM - Mutations in Pfmdr1 are positively associated with a range of other malaria measures, though a minority of|Mutations in Pfmdr1 are positively associated with a range of other malaria measures, though a minority of findings disagree]]
- [[CLM - Resistance-mutation prevalence in PfDHPS rises with drug pressure and over time across the settings studied —|Resistance-mutation prevalence in PfDHPS rises with drug pressure and over time across the settings studied — but the published evidence is contested]]
- [[CLM - Resistance-mutation prevalence in PfDHFR rises with drug pressure and over time across the settings studied|Resistance-mutation prevalence in PfDHFR rises with drug pressure and over time across the settings studied, though a minority of findings disagree]]
- [[CLM - Mutations in Pfmdr1 are associated with higher rates of antimalarial treatment failure, though a minority of|Mutations in Pfmdr1 are associated with higher rates of antimalarial treatment failure, though a minority of findings disagree]]
- [[CLM - Mutations in PfDHFR are positively associated with a range of other malaria measures, consistently across|Mutations in PfDHFR are positively associated with a range of other malaria measures, consistently across studies]]
- [[CLM - Mutations in Pfkelch13 are associated with slower clearance of malaria parasites after treatment, consistently|Mutations in Pfkelch13 are associated with slower clearance of malaria parasites after treatment, consistently across studies]]
- [[CLM - Mutations in PfDHFR are associated with higher rates of antimalarial treatment failure, consistently across|Mutations in PfDHFR are associated with higher rates of antimalarial treatment failure, consistently across studies]]
- [[CLM - Mutations in PfCRT are associated with higher rates of antimalarial treatment failure, consistently across|Mutations in PfCRT are associated with higher rates of antimalarial treatment failure, consistently across studies]]
- [[CLM - Mutations in PfDHPS are associated with higher rates of antimalarial treatment failure, consistently across|Mutations in PfDHPS are associated with higher rates of antimalarial treatment failure, consistently across studies]]
- [[CLM - Mutations in PfDHPS are associated with worse clinical outcomes, including severe malaria, death and low birth|Mutations in PfDHPS are associated with worse clinical outcomes, including severe malaria, death and low birth weight — but the published evidence is contested]]
- [[CLM - Mutations in Pfkelch13 are associated with higher rates of antimalarial treatment failure, though a minority of|Mutations in Pfkelch13 are associated with higher rates of antimalarial treatment failure, though a minority of findings disagree]]
- [[CLM - Mutations in Pfkelch13 are positively associated with a range of other malaria measures — but the published|Mutations in Pfkelch13 are positively associated with a range of other malaria measures — but the published evidence is contested]]
- [[CLM - Mutations in PfCRT are associated with slower clearance of malaria parasites after treatment, consistently|Mutations in PfCRT are associated with slower clearance of malaria parasites after treatment, consistently across studies]]
- [[CLM - Mutations in Pfmdr1 are associated with reduced parasite sensitivity to antimalarial drugs in laboratory|Mutations in Pfmdr1 are associated with reduced parasite sensitivity to antimalarial drugs in laboratory testing — but the published evidence is contested]]
- [[CLM - Resistance-mutation prevalence in Pfkelch13 rises with drug pressure and over time across the settings studied|Resistance-mutation prevalence in Pfkelch13 rises with drug pressure and over time across the settings studied, consistently across studies]]
- [[CLM - Mutations in PfCRT are associated with reduced parasite sensitivity to antimalarial drugs in laboratory|Mutations in PfCRT are associated with reduced parasite sensitivity to antimalarial drugs in laboratory testing, consistently across studies]]
- [[CLM - Mutations in PfCRT are associated with worse clinical outcomes, including severe malaria, death and low birth|Mutations in PfCRT are associated with worse clinical outcomes, including severe malaria, death and low birth weight — but the published evidence is contested]]
- [[CLM - Mutations in PfDHPS are positively associated with a range of other malaria measures, consistently across|Mutations in PfDHPS are positively associated with a range of other malaria measures, consistently across studies]]
- [[CLM - Mutations in Pfmdr1 are not associated with worse clinical outcomes such as severe malaria, death or low birth|Mutations in Pfmdr1 are not associated with worse clinical outcomes such as severe malaria, death or low birth weight — but the published evidence is contested]]
- [[CLM - Resistance-mutation prevalence in a group of less-studied resistance markers rises with drug pressure and over|Resistance-mutation prevalence in a group of less-studied resistance markers rises with drug pressure and over time across the settings studied — but the published evidence is contested]]
- [[CLM - Mutations in PfDHFR are not associated with worse clinical outcomes such as severe malaria, death or low birth|Mutations in PfDHFR are not associated with worse clinical outcomes such as severe malaria, death or low birth weight, consistently across studies]]
- [[CLM - Mutations in Pfmdr1 are associated with slower clearance of malaria parasites after treatment — but the|Mutations in Pfmdr1 are associated with slower clearance of malaria parasites after treatment — but the published evidence is contested]]
- [[CLM - Mutations in a group of less-studied resistance markers are associated with reduced parasite sensitivity to|Mutations in a group of less-studied resistance markers are associated with reduced parasite sensitivity to antimalarial drugs in laboratory testing, consistently across studies]]

## Limits on any answer

> [!warning] Read these before relying on anything above

- [[CVT - Roughly 20 percent of API associations are mis-extracted]]
- [[CVT - The graph records no effect direction]]
- [[CVT - List endpoints omit p-values and confidence intervals]]
- [[CVT - Variables are one-per-paper phrasings not canonical entities]]
- [[CVT - Pfkelch13 is the most important marker and the least covered]]
- [[CVT - Concept grounding is coarse and sometimes wrong]]
- [[CVT - The curated Dataverse deposit holds almost no resistance evidence]]
