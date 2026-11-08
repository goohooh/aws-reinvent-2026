# Validation checklist

Use local JSON processing to check the following invariants before delivering changes. No maintained executable script is required. Validate only changed datasets plus references affected by the change.

## Session data

- Parse source as a nonempty list; require nonempty unique occurrence codes and titles.
- Check expected string fields, string-array tags, and boolean `walkUpOnly` as documented in `docs/data-guide.md`.
- Compare source bytes' SHA-256 with `data/provenance.json` and `data/stats.json`.
- Resolve all codes in recommendations, overview flows, forecasts, shortlist, keynotes, counterbalance, and supporting sessions.
- Recompute grouping, exclusion, tag counts, percentages, and cross-topic intersections; compare the complete result with stored statistics.

## External events

- Parse `data/reinvent2026_parties.json` as an object with a source, taxonomy, statistics, quality issues, recommendations, and event list.
- Require unique IDs, known categories, valid ISO dates, nonempty title, raw source fields, and source URLs. Missing timezone remains null unless established by a cited source.
- Recompute IDs according to `events.md`, category/day counts, and at-capacity count.
- Resolve every recommendation, issue, and related-listing reference to a real event ID.
- Verify each retained extraction row maps to exactly one event. Do not merge rows just to make counts look unique.
- Check complete Markdown tables cover all event IDs once, under the matching categories. A separate recommendation table may repeat selected events.
- Verify links were present in captured event cells. Banner-only links must not become fabricated event listings.

## Skill and repository

- Ensure SKILL.md has `name` and `description` frontmatter and every linked reference exists.
- Read a realistic task such as “find the agent security private sessions and show both dates” against the skill, checking that it can be completed solely from repo data.
- Check Markdown local links and cited session codes. Inspect the staged diff for stale references to removed scripts, personal paths, or credentials; do not print secret values.
- Run `git diff --check`. Publishing, when authorized, is complete only when the intended remote branch matches the local commit.
