---
name: harvest-system-graph
description: API recipe for the System Public Graph — endpoints, parameters, measured limits, known breakage, and the request-cost model. Companion to Skill.md.
allowed-tools: Read, Write, Bash
---

# Skill — harvesting the System Public Graph

Everything here was measured against the live API on 14 November 2026, not taken from the
documentation. Where the two disagree, the measurement wins and the disagreement is noted.

## Connection

Base `https://public-api.system.com`, version prefix `/v1`, header `x-api-key`.
**10,000 requests per day per key.** Keys are issued per applicant, so a team of five has 50,000.
If an approach needs more, the organisers say to ask in the `#help` Slack channel.

```bash
curl -s -H "x-api-key: $SYSTEM_API_KEY" \
  "https://public-api.system.com/v1/variables?search=name:pfmdr1&limit=200"
```

## Table sizes

| Table | API rows | Dataverse deposit rows |
| --- | --- | --- |
| associations | 5,944,001 | 1,999,877 (34%) |
| variables | 5,654,715 | 1,774,551 (31%) |
| concepts | 108,624 | 45,721 (42%) |
| studies | 40,307,952 | 844,435 |
| relationships | — | 839,872 |

## The endpoints that matter

| Call | Purpose | Cost |
| --- | --- | --- |
| `GET /v1/variables?search=name:<term>` | find variables by name substring | 1 per term |
| `GET /v1/variables/{id}/associations` | associations on **either** side — the workhorse | 1 per variable |
| `GET /v1/associations?filter=variable_1_id:{id}` | fallback for the above | 2 per variable |
| `GET /v1/associations/{id}` | **only** source of p-values and CIs | 1 per finding |
| `GET /v1/studies/{id}` | `doi`, `pubmed_id`, `population`, `study_type` | 1 per study |
| `GET /v1/relationships?sort=num_studies:desc` | concept-pair aggregates, carries `last_published_date` | 1 |

## Parameters, as they actually behave

- **`limit` defaults to 10.** The single easiest way to lose 95% of your data silently. Set it
  on every call. Values above the match count are harmless.
- **`search=field:value` is case-insensitive substring matching.** Not tokens, not embeddings, no
  stemming. The complete match set returns in one page.
- **`filter=field:value` is exact matching**, one field at a time.
- **`offset`** works within a result set and returns `[]` past the end.
- **`include_total=true` is broken with `search`** — always reports the global table count.
- **`fields` returns HTTP 500.** Unusable.
- **`sort`** exists on relationships only.

## Known breakage

| What | Behaviour | Handling |
| --- | --- | --- |
| `fields` parameter | always 500 | don't use |
| `/v1/concepts?search=` | 500 after the first term | fail fast, skip |
| `search=wikidata_aliases:` | always 500 | don't use |
| concept IDs starting `-` | 500 on direct fetch | fail fast, skip |
| `/v1/variables/{id}/associations` | **intermittent** 500s | **retry** — 8 attempts, 0.4s × attempt |
| `include_total` with `search` | global count | detect end of set by short page |

> [!danger] The expensive mistake
> These two 500 classes look identical and need opposite handling. Treating the flaky ones as
> permanent once discarded **62% of the data** in a single run — 575 of 923 variables "failed",
> which read as thin coverage rather than a client bug. Retrying dropped failures to 4.5% and
> nearly tripled the dataset. Always test whether a failure reproduces on immediate retry before
> changing retry policy.

## Field availability

List endpoint, 10 fields:

```
system_id, variable_1_id, variable_2_id, variable_1_name, variable_2_name,
study_id, statistic_type, statistic_value, pubmed_id, system_statistic_type
```

Detail endpoint adds 9:

```
p_value, p_value_equality, ci_level, ci_lower, ci_upper,
variable_1_concept_id, variable_1_wikidata_id, variable_2_concept_id, variable_2_wikidata_id
```

**No publication date and no effect direction anywhere in the graph.**

The Dataverse `associations.csv` carries all 19 columns in one file, which is its main practical
advantage.

## Dates, from PubMed

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<comma-separated>&retmode=json
```

200 IDs per request, 3 requests/second without a key and 10 with one. At this scale batching
makes the key unnecessary: 695 IDs resolved in 4 requests. Dates arrive as `2015 Jul 20`,
`2015 Jul` or `2015`, so extract the year with a regex rather than a date parser.

## Request-cost model

| Stage | Requests | Time |
| --- | --- | --- |
| probe | 4 | 2s |
| 1 — variable sweep, 202 terms | 289 | 38s |
| 2 — concepts and grounding | 475 | 89s |
| 3 — associations, 923 anchors with retries | 1,271 | 804s |
| 4 — 696 studies + PubMed | 712 | 94s |
| **total** | **~2,750** | ~17 min |

Add one request per finding if you want p-values.

## Two spelling rules

Because search is substring matching with no stemming, American and British forms are different
queries and both must be run: parasitemia/parasitaemia, anemia/anaemia, hemoglobin/haemoglobin,
hematocrit/haematocrit, gametocytemia/gametocytaemia, sulfadoxine/sulphadoxine,
hospitalization/hospitalisation.

And any marker abbreviation under five characters needs a `pf` prefix or a malaria-vocabulary
guard on its results. Bare `crt` returns cardiac resynchronization therapy; `IPT` returns
isoniazid preventive therapy from the tuberculosis literature. See
[[CVT - Variables are one-per-paper phrasings not canonical entities]].
