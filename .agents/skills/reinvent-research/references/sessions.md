# Session catalog workflow

Read `data/reinvent2026_sessions.json` and the applicable parts of `data/curation.json`. The source is a list of occurrence objects. The curation is an object containing recommendations and other reference lists.

## Search and explain

- Match a requested code exactly. `COP401-R` and `COP401-R1` are different scheduled occurrences.
- For free-text search, match case-insensitively across English/Korean titles, abstracts, summaries, and metadata. Use the English abstract for detailed interpretation.
- For topic exploration, return one first-seen representative per exact English title. For attendance planning, return every occurrence with that title.
- Join `recommendations[].code` to source records; retain category, rank, rationale, and takeaway. Priority is within a category, not a global ranking.
- Give exact codes and titles with the reason they fit the requested objective. Include dates, times, venues, and repeat choices when scheduling is relevant.
- Do not infer recording URLs or live registration availability from the snapshot.

Example invocation: “Use `$reinvent-research` to find MCP security sessions and explain which one is best for protecting tool integrations.” The result should distinguish SEC343's tool supply-chain focus from SEC407-R's authorization enforcement using their abstracts.

## Recompute statistics

Follow `docs/data-guide.md`: group by exact title; exclude the three specified types using the first record's type; union tags across occurrences. Sort tag counts by descending count and then tag name. Percentages use included title groups, rounded to one decimal. For the three agentic cross-topic rows, the denominator is each topic's group count.

Retain `data/stats.json`'s schema and use the SHA-256 of the unchanged source bytes. This snapshot should yield 2,468 records, 1,849 title groups, and 1,790 included title groups. These counts describe this snapshot; they are not invariants for a future replacement snapshot.

Change forecasts or recommendations only when the task calls for new analysis. Keep factual recomputation separate from editorial changes.
