# External-event workflow

Default source: `https://conferenceparties.com/reinvent2026/`. It is an unofficial directory. The capture scope is its event table, not banner ads, organizer landing pages, maps, or the Guide of Guides.

## Capture and preserve

1. Observe the page with a semantic snapshot. Locate the event table from its date headings and five columns: Time, Sponsor, Event & RSVP Link, Location, Added.
2. Extract each populated event row, carrying forward the most recent full date heading. Skip headers, blank separator rows, and image-only promotional rows. Preserve text-cell contents and event-cell links. Do not collect unrelated page HTML or assets.
3. Record the capture timestamp and source URL. Count visible event rows independently and compare with the extraction. If the page structure changes, inspect it instead of assuming the same selectors or row count.
4. Preserve source strings for time, sponsor, location, added date, and event text. Normalize only whitespace and remove registration call-to-action labels from the display title. Keep those labels in the raw event text.
5. Generate a listing ID from date, raw time, whitespace-normalized sponsor, cleaned title, raw location, and registration URLs: join in that order with `|`, hash UTF-8 with SHA-256, and prefix the first 12 hex digits with `cp26-`. Content changes may change IDs; update all references together.

## Classify

Use one primary category from `classification.categories` for each listing. This taxonomy describes event format, independently of topic. For hybrid formats, choose the dominant advertised activity; meal-centered panels can remain breakfast/lunch/dinner, and outings with dinner can be experiences. Explicit labels outrank guesses based on a venue. Mark uncertain interpretations instead of asserting hidden details.

Topic tags describe explicit keywords in the title: AI/agents, security, observability, FinOps, development, and cloud/platform. Do not label every event by a known vendor's business area. A recommendation may use sponsor-based networking relevance if it says so explicitly.

Preserve all source rows even when apparently duplicated. Mark matching date/time/sponsor/location/registration-link rows as duplicates; mark similar named events on incompatible dates as potential conflicts. Different VIP or partner invitation links at the same event may be related access paths, not separate events or confirmed duplicates.

Distinguish “invite-request link listed”, “registration link listed”, “at capacity”, and “not listed”. A request link does not mean approved attendance, remaining capacity, free admission, or public eligibility. Preserve explicit CTO-only, partner-only, jacket, and similar restrictions.

Preserve malformed registration URLs in JSON with a quality flag. Render only observed HTTP(S) URLs as active Markdown links; do not silently turn source typos such as `hhttps://` into a supposedly verified link.

## Markdown guide

Update `docs/parties.ko.md` with capture date, counts by category and day, source limitations, unresolved conflicts, focused AI Ops/Security picks, and the complete list under category headings. Include dates, raw times, sponsors, locations, and observed RSVP links. Reference the JSON for machine-readable identifiers and flags.

Keep recommendations editorial and separate from the full directory. Do not claim organizer pages were checked unless they were actually read; attach any additional verification to the relevant event and leave directory facts unchanged when sources conflict.
