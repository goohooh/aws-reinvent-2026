---
name: reinvent-research
description: Search and curate this repository's AWS re:Invent 2026 sessions and external events, refresh the Conference Parties dataset, and maintain JSON evidence with Korean Markdown guides. Use for session recommendations, AI Ops and Security research, or party and networking-event classification.
---

# re:Invent research

Use the repository's session catalog and external-event directory as separate evidence sources. Produce portable JSON for reuse and Korean Markdown for people. This is a project skill; it replaces the standalone catalog CLI and requires no global installation or saved executable scripts.

## Locate the project

The skill lives at `.agents/skills/reinvent-research/SKILL.md`. Resolve the repository root from this location or the current Git worktree. Paths below are relative to that root; do not assume a particular home directory, account, or checkout path.

- `data/reinvent2026_sessions.json`: unchanged user-supplied session catalog.
- `data/curation.json`: existing editorial session recommendations and forecasts.
- `data/stats.json`, `data/provenance.json`: session statistics and source provenance.
- `data/reinvent2026_parties.json`: separately sourced external-event listings, classifications, registration links, and quality flags.
- `docs/analysis.ko.md`: session analysis.
- `docs/parties.ko.md`: external events grouped by kind, with focused picks and source limitations.

## Choose the workflow

**Session search, recommendations, or statistics:** read [references/sessions.md](references/sessions.md) and `docs/data-guide.md`. Search the source JSON locally, join curated entries by exact code, and expand repeats by exact title when needed. No browser is needed to analyze the existing snapshot.

**External-event search, classification, or refresh:** read [references/events.md](references/events.md) and `docs/parties-data-guide.md`. Read existing JSON locally for snapshot questions. For a refresh, inspect the requested directory using `ego-browser`, extract factual event rows, classify them, and update the external-event JSON and Markdown together.

**Verification or changes to either dataset:** follow [references/validation.md](references/validation.md). Use available local JSON processing or temporary in-memory Python as needed; do not add a standalone command-line script as the interface.

## Research decisions

- Keep catalog facts, editorial recommendations, and forecasts distinguishable. Presenter claims and directory listings are not independent confirmation of outcomes or availability.
- Sessions and external events use different schemas and identifiers. Do not add external events to session counts or pretend they have AWS session codes.
- Preserve source times, dates, names, and links. Missing fields stay null or explicitly unknown. Do not silently repair conflicting dates, sponsor typos, malformed added dates, or ambiguous AM/PM ranges.
- A party hosted by a security vendor is not necessarily a security training session. Topic tags use explicit title evidence; sponsor-based networking relevance must be labeled as inference.
- Recommendations should explain the benefit for the requested goal, format, eligibility, and relevant uncertainties. A ranked list is not an attendance schedule.
- Keep existing analysis dates unless actually reanalyzing the material. Record a separate timestamp for each external-event capture.

## Browser refresh

Use the installed `ego-browser` skill and CLI for browser work. Run `ego-browser skill` and read the full installed guide before operating. Create or reuse one task space for the user goal; preserve it across rounds. Prefer semantic snapshots and documented DOM extraction for the directory table. Record the source URL and capture time. Do not bypass browser control handoffs or authentication prompts.

If the browser capability is unavailable, continue offline analysis of the existing snapshot and report that it was not refreshed. Do not imply live verification.

## Delivery

For data updates, provide the JSON and Markdown file links, counts, classification method, and unresolved conflicts. Update README and agent guidance when file locations or usage changes. Do not register for events, alter calendars, or publish changes solely because this skill is invoked; follow the user's actual authorization. When publication is requested, validate locally, preserve unrelated work, and verify the remote commit after pushing.
