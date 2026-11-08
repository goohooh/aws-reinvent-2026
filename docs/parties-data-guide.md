# External event data guide

`data/reinvent2026_parties.json` contains external-event listings from [Conference Parties](https://conferenceparties.com/reinvent2026/). It is independent of the AWS session catalog, curation, and statistics. The accompanying [Korean guide](parties.ko.md) groups the complete list by event format.

## Scope and provenance

- Captured at `2026-11-08T13:07:46.466Z` with ego-browser semantic observation and DOM table extraction.
- Includes all 178 populated five-column event rows beneath six dated headings. Counts represent source listings, including duplicate entries.
- Excludes navigation, image-only sponsor banners, site HTML and assets, Guide of Guides, and Maps & Tools.
- Organizer landing pages were not checked. Registration links, capacity status, eligibility, and locations reflect the directory snapshot only.
- The directory describes itself as unofficial and unaffiliated with Amazon or AWS. Its factual listings are not confirmation of official event status.

## Top-level structure

| Field | Purpose |
|---|---|
| `schema_version` | Schema version, currently 1 |
| `dataset_kind` | `external_event_listings`; distinguishes this object from the session catalog array |
| `source` | URL, capture time, extraction method, scope, verification status, affiliation, and attribution notice |
| `classification` | Editorial taxonomy and title-based topic-tag method |
| `statistics` | Listing count, date/category counts, and at-capacity count |
| `quality_issues` | Duplicate, date-conflict, and related-registration groups with event references |
| `recommendations` | Editorial AI Ops/Security-related picks with rationale and event ID |
| `events` | All 178 source listings, in original table order |

## Event fields

| Field | Meaning |
|---|---|
| `id` | `cp26-` plus 12 hex characters from a content-based SHA-256; no AWS session code is implied |
| `source_url`, `source_row_index` | Directory URL and zero-based DOM table-row position observed during capture |
| `date`, `day_raw` | ISO date parsed from the nearest date heading; original English weekday |
| `time_raw`, `timezone` | Source time text and null timezone; no timezone was explicitly established |
| `title` | Display title with registration CTA removed and whitespace collapsed |
| `sponsor_raw`, `location_raw`, `added_raw` | Source cell text; spelling, missing fields, and formatting anomalies preserved |
| `listing_text_raw` | Original event-cell text, including invitation/capacity labels |
| `registration_urls` | Observed event-cell links, in source order with exact duplicates removed; an empty array means no event link was listed. Invalid schemes are preserved and flagged, not silently repaired. |
| `registration_status` | `invite_request_link_listed`, `registration_link_listed`, `at_capacity`, or `not_listed` |
| `restrictions_raw` | Explicit source restrictions such as CTOs Only Please, Tech Execs Only, Partners Only, or Jacket Required; not an exhaustive check of organizer eligibility |
| `category` | One editorial primary-format category |
| `category_confidence`, `category_basis` | Qualitative classification confidence and the visible evidence used; medium marks an inferred format |
| `topic_tags` | Keywords explicitly present in the event title; vendor identity alone does not assign a topic |
| `quality_flags`, `related_listing_ids` | Missing information, malformed added date, duplicates, conflicts, and relationships |

IDs hash the following `|`-joined values in order: ISO date, raw time, whitespace-normalized sponsor, cleaned title, raw location, then each registration URL. Changes to any of these values may change the ID; update all recommendations, issues, and Markdown references together.

`time_raw` may contain incomplete ranges (`10AM–`), words (`Evening`), or a shuttle note. AM/PM inheritance and overnight end dates have not been normalized. Do not convert to calendar events without establishing timezone and resolving incomplete ranges. The `Added` column is the directory's month/day label, not a reliable full timestamp; preserve malformed values such as `10//22`.

## Editorial categories

| ID | Korean label | Current count |
|---|---|---:|
| `technical_discussion` | 기술 세션·토론·쇼케이스 | 10 |
| `breakfast_coffee` | 조식·커피 | 14 |
| `lunch` | 점심 | 18 |
| `dinner` | 저녁 | 26 |
| `happy_hour_reception` | 해피아워·리셉션·네트워킹 | 59 |
| `party_nightlife` | 파티·공연·나이트라이프 | 27 |
| `experience_sports` | 체험·스포츠 | 23 |
| `keynote_watch` | 키노트 공동 시청 | 1 |

A listing appears once in this taxonomy. Some events combine food, presentations, games, or nightlife; the category represents the primary advertised format and may be uncertain. These categories are not supplied by Conference Parties. Topic tags are separate from format: `ai_agents`, `security`, `observability`, `finops`, `development`, and `cloud_platform`.

## Known relationships

- Datadog Off Leash has two listings with the same date, time, sponsor, venue, and RSVP URL. Both are retained with a duplicate flag.
- ClickHouse / The Chainsmokers has similar listings on different days with different registration URLs. The date conflict remains unresolved.
- House of Kube and Qodo VIP have distinct invitation paths to the same time and venue. They are marked related, not merged.
- Two rows say “At Capacity”. That is a snapshot label, not a live capacity check.
- InnovatHERs Networking Breakfast has an `hhttps://` registration URL in the source. It is preserved with `malformed_registration_url` and not rendered as a working Markdown link.

## Maintenance

Use the [project skill](../.agents/skills/reinvent-research/SKILL.md), reading its event and validation references. Refresh through the installed ego-browser skill and CLI, retain all source event rows, preserve raw fields, and regenerate counts and the complete Markdown list together. Record a new capture timestamp for each refresh. Do not change the separately sourced session catalog when refreshing this directory.
