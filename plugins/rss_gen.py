#!/usr/bin/env python3
"""
Post-build script: generates an Atom RSS feed at _build/html/feed.xml.

Run from the repo root after `myst build --html`:
    python plugins/rss_gen.py
"""

import os
import datetime
from pathlib import Path

import yaml
from feedgen.feed import FeedGenerator


REPO_ROOT = Path(__file__).parent.parent.resolve()
SEARCH_DIRS = ["posts", "projects"]
OUTPUT_PATH = REPO_ROOT / "_build" / "html" / "feed.xml"
BASE_URL = "https://ryandlewis.dev"
FEED_URL = f"{BASE_URL}/feed.xml"
MAX_ENTRIES = 10


def parse_front_matter(filepath: Path) -> dict | None:
    """
    Parse YAML front matter from a Markdown file.

    Returns the parsed dict, or None if the file has no front matter or
    parsing fails.
    """
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    # Split on the closing --- delimiter
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None

    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None


def url_path_from_file(filepath: Path) -> str:
    """
    Compute the URL path for a file relative to the repo root.

    Examples:
        posts/helloworld.md              -> /posts/helloworld
        posts/ttrpg/thebandoleers026.md  -> /posts/ttrpg/thebandoleers026
        projects/website.md              -> /projects/website
    """
    relative = filepath.relative_to(REPO_ROOT)
    # Drop the .md suffix and prepend /
    return "/" + str(relative.with_suffix(""))


def to_aware_datetime(value) -> datetime.datetime:
    """
    Convert a date or datetime value (as returned by yaml.safe_load) to a
    timezone-aware datetime in UTC.
    """
    if isinstance(value, datetime.datetime):
        if value.tzinfo is None:
            return value.replace(tzinfo=datetime.timezone.utc)
        return value
    if isinstance(value, datetime.date):
        return datetime.datetime(
            value.year, value.month, value.day, tzinfo=datetime.timezone.utc
        )
    raise TypeError(f"Cannot convert {type(value)!r} to datetime")


def collect_entries() -> list[dict]:
    """
    Walk SEARCH_DIRS for Markdown files, parse their front matter, and return
    a list of entry dicts for files whose tags list contains 'feed'.
    """
    entries = []

    for dir_name in SEARCH_DIRS:
        search_dir = REPO_ROOT / dir_name
        if not search_dir.is_dir():
            continue

        for md_file in search_dir.rglob("*.md"):
            # Skip projects/README.md
            if md_file.name == "README.md":
                continue

            front_matter = parse_front_matter(md_file)
            if front_matter is None:
                continue

            tags = front_matter.get("tags", [])
            # tags may be a string or a list
            if isinstance(tags, str):
                tags = [tags]

            if "feed" not in tags:
                continue

            date_value = front_matter.get("date")
            if date_value is None:
                continue

            try:
                dt = to_aware_datetime(date_value)
            except (TypeError, ValueError):
                print(f"Warning: could not parse date in {md_file}, skipping.")
                continue

            title = front_matter.get("title", md_file.stem)
            description = front_matter.get("description", "")
            url_path = url_path_from_file(md_file)

            entries.append(
                {
                    "title": title,
                    "description": description,
                    "url_path": url_path,
                    "dt": dt,
                }
            )

    return entries


def build_feed(entries: list[dict]) -> FeedGenerator:
    """Construct and return a configured FeedGenerator populated with entries."""
    fg = FeedGenerator()
    fg.id(FEED_URL)
    fg.title("Ryan D. Lewis")
    fg.subtitle(
        "The humble internet home of Ryan D. Lewis, general Technomancer and well-rounded nerd."
    )
    fg.link(href=BASE_URL, rel="alternate")
    fg.link(href=FEED_URL, rel="self")
    fg.author({"name": "Ryan D. Lewis"})

    for entry in entries:
        full_url = BASE_URL + entry["url_path"]
        fe = fg.add_entry()
        fe.id(full_url)
        fe.title(entry["title"])
        fe.link(href=full_url)
        fe.summary(entry["description"])
        fe.published(entry["dt"])
        fe.updated(entry["dt"])
        fe.author({"name": "Ryan D. Lewis"})

    return fg


def main() -> None:
    entries = collect_entries()

    # Sort by date descending and take the 10 most recent
    entries.sort(key=lambda e: e["dt"], reverse=True)
    entries = entries[:MAX_ENTRIES]

    fg = build_feed(entries)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fg.atom_file(str(OUTPUT_PATH), pretty=True)

    print(f"Generated feed.xml with {len(entries)} entries")


if __name__ == "__main__":
    main()
