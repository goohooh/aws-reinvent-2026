# Data guide

This guide defines the catalog schema, reproducible statistics, and machine-readable curation. All dataset files use UTF-8 JSON.

## Source catalog

`data/reinvent2026_sessions.json` is an unchanged copy of the user-supplied source. It contains 2,468 objects with unique `code` values. `data/provenance.json` records its SHA-256. No private account export or conversation transcript is included.

| Fields | Meaning |
|---|---|
| `code` | Exact occurrence identifier, including any repeat or sponsor suffix |
| `title`, `title_ko` | English and Korean titles |
| `abstract`, `summary_ko` | Original English description and supplied Korean summary |
| `type`, `level` | Catalog session format and level; some levels are empty |
| `topic`, `areaOfInterest`, `services` | Arrays of labels; multiple labels per record |
| `role`, `industry`, `features` | Additional arrays of catalog labels |
| `walkUpOnly` | Catalog boolean; not a live availability check |
| `date`, `day` | Supplied date and display-day string |
| `startTime`, `endTime` | Supplied time strings, with different formats |
| `venue`, `room` | Supplied location strings |

The source has no per-session URL or explicit timezone field. Do not invent either. The event spans 2026-11-29 through 2026-12-04 in this snapshot. `startTime` uses values such as `19:00`; `endTime` uses values such as `09:00 PM`. This repository preserves both strings and does not create timezone-aware calendar events. Verify event timezone, updated schedules, walking time, and repeat occurrences before constructing an attendance plan.

## Statistics

1. Count every object as one scheduled record: 2,468.
2. Group by **exact English title**, retaining first-seen order: 1,849 groups. This is a reproducible grouping convention, not a guarantee of 1,849 editorially distinct talks.
3. Exclude groups whose representative first record has `type` equal to `Featured experience`, `Expo`, or `Event service`: 1,790 included groups. The retained set includes keynotes, mainstage talks, labs, bootcamps, and exam prep.
4. For each retained group, take the union of its occurrences' tags. A group counts once per tag. Topic percentages use 1,790 as the denominator and overlap.
5. For cross-topic statistics, count groups with both the specified topic and the `Agentic AI` area-of-interest tag. The denominator is the count for the specified topic.
6. Sponsored sessions are included in the overall statistics. The main practical shortlist does not use sponsored sessions.

`scripts/catalog.py stats --write` regenerates `data/stats.json` deterministically. There are no keyword-inferred tags and no model calls in this calculation.

## Curation

`data/curation.json` is editorial input, not generated statistics. It contains:

- `analysis_date`, `prepared_on`, `forecast_horizon_months`, and the intended audience.
- `overview_flows`: the five main program themes and exact supporting session codes.
- `recommendations`: category, priority, rationale, and expected takeaway for each selected session. Priorities apply within a category. Additional categories are supplementary, not ranks below all other sessions.
- `shortlist_six`: six codes in recommendation order, not a feasible chronological itinerary.
- `keynote_reading_order` and `counterbalance`: orientation sessions and a perspective that tests autonomy claims.
- `trends`: interpretive forecasts, confidence labels, reasoning, and supporting codes. Confidence is qualitative, not a statistical probability.
- `supporting_sessions`: additional codes discussed in the analysis.

The catalog is the source for titles, abstracts, times, and venues. `shortlist` joins each recommendation with all matching-title occurrences, preserving the original metadata. `show CODE --repeats` similarly expands a single code to its repeat group.

## Validation

`python3 scripts/catalog.py validate` checks source integrity, nonempty and unique codes, required field types, every curated session reference, and consistency of stored versus regenerated statistics. It does not validate the catalog against a live AWS website or guarantee that recommendations remain current.
