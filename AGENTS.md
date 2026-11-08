# Agent guide

This is a public research and session-curation repository for AWS re:Invent 2026. It is not an AWS product or an official event catalog. Keep the repository usable without access to the original conversation or a particular user's machine.

## Start here

1. Read `README.md` for scope and usage.
2. Read `docs/analysis.ko.md` for the existing Korean synthesis.
3. Read `data/curation.json` for structured recommendations, priorities, themes, and forecasts.
4. Resolve evidence from `data/reinvent2026_sessions.json`. Use the English `abstract` as the primary session-description field; Korean summaries may omit details.
5. Read `docs/data-guide.md` before changing statistics or interpreting schedules.

## Evidence and interpretation

- Distinguish catalog facts, recommendations, forecasts, and claims made by session presenters.
- The analysis date is 2026-11-05. Publication preparation was 2026-11-08. The exact catalog collection timestamp and collection method are unknown.
- Do not treat planned sessions as delivered talks, verified product capabilities, available recordings, or confirmed customer outcomes.
- Cite exact session codes and titles. Do not invent session URLs or normalize codes by stripping arbitrary suffixes.
- Group repeated sessions by exact title for topic statistics; retain every occurrence when planning attendance.
- Forecasts describe a 6–12 month horizon from the analysis date, not from the date a future agent happens to read this repo.
- Personalization targets AI Ops, Security, CLI agents, skills, MCP, and QA automation. It does not establish a particular production stack or employer.

## Commands

```bash
python3 scripts/catalog.py validate
python3 scripts/catalog.py stats
python3 scripts/catalog.py show SEC343
python3 scripts/catalog.py show COP401-R --repeats
python3 scripts/catalog.py search 'incident' --unique --limit 20
python3 scripts/catalog.py shortlist --category ai_ops
```

Commands produce JSON and work from any working directory. Python 3.10+ is sufficient; there are no third-party dependencies.

## Updating

- Keep source data unchanged unless a new source snapshot is explicitly supplied. Record a new SHA-256 and source provenance when replacing it.
- Update `data/curation.json` and `docs/analysis.ko.md` together when priorities or conclusions change.
- Regenerate `data/stats.json` with `python3 scripts/catalog.py stats --write` after changing source data or methodology, then run `validate` and reconcile documented counts.
- Preserve `analysis_date` as the date of the actual analysis; do not silently refresh it when merely republishing.
- Keep secrets, local account configuration, credentials, personal filesystem paths, and private conversation transcripts out of this public repo.
- Do not broaden the license of third-party session text. See the provenance notice in README.
- Do not book sessions, change calendars, or publish messages merely because the repository recommends a session.
