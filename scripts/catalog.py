#!/usr/bin/env python3
"""Offline catalog search, curation joins, statistics, and validation (Python 3.10+)."""

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SOURCE = DATA / "reinvent2026_sessions.json"
EXCLUDED_TYPES = {"Featured experience", "Expo", "Event service"}
TAG_FIELDS = ("topic", "areaOfInterest", "services", "role", "industry", "features")


def read(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2))


def groups(sessions):
    result = {}
    for session in sessions:
        result.setdefault(session["title"], []).append(session)
    return list(result.values())


def tags(group, field):
    return {tag for session in group for tag in session[field]}


def stats(sessions):
    grouped = groups(sessions)
    included = [g for g in grouped if g[0]["type"] not in EXCLUDED_TYPES]
    tag_counts = {}
    for field in TAG_FIELDS:
        counts = Counter(tag for group in included for tag in tags(group, field))
        tag_counts[field] = [
            {"tag": tag, "count": count, "percent": round(count / len(included) * 100, 1)}
            for tag, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        ]
    cross = []
    for topic in ("Security & Identity", "Cloud Operations", "Developer Tools"):
        selected = [g for g in included if topic in tags(g, "topic")]
        agentic = sum("Agentic AI" in tags(g, "areaOfInterest") for g in selected)
        cross.append({"topic": topic, "count": agentic, "denominator": len(selected),
                      "percent": round(agentic / len(selected) * 100, 1) if selected else 0})
    return {
        "schema_version": 1,
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "record_count": len(sessions),
        "unique_title_count": len(grouped),
        "excluded_types": sorted(EXCLUDED_TYPES),
        "included_title_count": len(included),
        "group_by": "exact title; first record supplies group type; union of tags",
        "tag_counts": tag_counts,
        "agentic_ai_cross_topics": cross,
    }


def references(curation):
    yield from curation["shortlist_six"]
    yield from curation["keynote_reading_order"]
    yield from curation["supporting_sessions"]
    yield curation["counterbalance"]["code"]
    for item in curation["recommendations"]:
        yield item["code"]
    for item in curation["overview_flows"] + curation["trends"]:
        yield from item["session_codes"]


def validate(sessions):
    if not isinstance(sessions, list) or not sessions:
        raise ValueError("Catalog must be a nonempty list")
    required_strings = ("code", "title", "title_ko", "abstract", "summary_ko", "type",
                        "level", "date", "day", "startTime", "endTime", "venue", "room")
    codes = []
    for index, session in enumerate(sessions):
        for field in required_strings:
            if not isinstance(session.get(field), str):
                raise ValueError(f"Record {index}: invalid string field {field}")
        if not session["code"] or not session["title"]:
            raise ValueError(f"Record {index}: empty code or title")
        for field in TAG_FIELDS:
            value = session.get(field)
            if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
                raise ValueError(f"Record {index}: invalid tag array {field}")
        if not isinstance(session.get("walkUpOnly"), bool):
            raise ValueError(f"Record {index}: invalid walkUpOnly")
        codes.append(session["code"])
    if len(codes) != len(set(codes)):
        raise ValueError("Duplicate occurrence codes")
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != read("provenance.json")["source_sha256"]:
        raise ValueError("Source SHA-256 differs from provenance")
    refs = set(references(read("curation.json")))
    missing = refs - set(codes)
    if missing:
        raise ValueError("Missing curated session codes: " + ", ".join(sorted(missing)))
    if read("stats.json") != stats(sessions):
        raise ValueError("Stored statistics differ; run stats --write and review changes")
    return {"valid": True, "records": len(sessions), "curated_codes": len(refs),
            "source_sha256": digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("stats", help="Compute deterministic title-level statistics")
    p.add_argument("--write", action="store_true", help="Update data/stats.json")
    p = commands.add_parser("search", help="Case-insensitive substring search across catalog text")
    p.add_argument("query")
    p.add_argument("--unique", action="store_true", help="Return first matching occurrence per title")
    p.add_argument("--limit", type=int, default=20)
    p = commands.add_parser("show", help="Look up an exact occurrence code")
    p.add_argument("code")
    p.add_argument("--repeats", action="store_true", help="Include every occurrence with the same title")
    p = commands.add_parser("shortlist", help="Join editorial recommendations with catalog evidence")
    p.add_argument("--category", choices=("ai_ops", "security", "workflow", "supplement"))
    commands.add_parser("validate", help="Validate source, references, and generated statistics")
    args = parser.parse_args()
    sessions = read("reinvent2026_sessions.json")
    if args.command == "stats":
        result = stats(sessions)
        if args.write:
            (DATA / "stats.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        emit(result)
    elif args.command == "search":
        if args.limit < 1:
            parser.error("--limit must be positive")
        query = args.query.casefold()
        matched = [s for s in sessions if query in json.dumps(s, ensure_ascii=False).casefold()]
        if args.unique:
            matched = [g[0] for g in groups(matched)]
        emit({"query": args.query, "total_matches": len(matched), "results": matched[:args.limit]})
    elif args.command == "show":
        selected = next((s for s in sessions if s["code"] == args.code), None)
        if selected is None:
            parser.error(f"Unknown exact session code: {args.code}")
        emit([s for s in sessions if s["title"] == selected["title"]] if args.repeats else selected)
    elif args.command == "shortlist":
        by_code = {s["code"]: s for s in sessions}
        result = []
        for recommendation in read("curation.json")["recommendations"]:
            if args.category and recommendation["category"] != args.category:
                continue
            session = by_code[recommendation["code"]]
            result.append({**recommendation, "occurrences": [s for s in sessions if s["title"] == session["title"]]})
        emit(result)
    else:
        emit(validate(sessions))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
