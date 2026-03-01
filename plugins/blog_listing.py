#!/usr/bin/env python3
"""
MyST executable plugin: blog_listing

Provides two directives:
  - postlist   : renders a grid of blog post cards from posts/
  - projectlist: renders a grid of project cards from projects/

Protocol (mystmd executable plugin)
-------------------------------------
When invoked without arguments, print the plugin spec JSON and exit.
When invoked with --directive <name>, read directive data as JSON from stdin
and write a list of MyST AST nodes as JSON to stdout.
"""

import argparse
import json
import os
import sys

import yaml

# ---------------------------------------------------------------------------
# Plugin spec
# ---------------------------------------------------------------------------

plugin = {
    "name": "blog-listing",
    "directives": [
        {
            "name": "postlist",
            "doc": "Display a grid of blog post cards, optionally filtered by tag.",
            "arg": {"type": "string", "doc": "Optional tag to filter by (e.g. dms_log, dev, Adventures_in_Tech)"},
            "options": {
                "number": {"type": "int", "doc": "Maximum number of posts to display"}
            },
        },
        {
            "name": "projectlist",
            "doc": "Display a grid of project cards.",
            "arg": {},
            "options": {
                "number": {"type": "int", "doc": "Maximum number of projects to display"}
            },
        },
    ],
}

# ---------------------------------------------------------------------------
# Front matter helpers
# ---------------------------------------------------------------------------

def parse_front_matter(text):
    """Return (front_matter_dict, body_text) for a Markdown file."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, parts[2]


def read_md_files(directory):
    """Walk directory and yield (relative_path, front_matter) for every .md file."""
    repo_root = os.getcwd()
    for dirpath, _dirnames, filenames in os.walk(directory):
        for filename in sorted(filenames):
            if not filename.endswith(".md"):
                continue
            abs_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(abs_path, repo_root)
            try:
                with open(abs_path, "r", encoding="utf-8") as fh:
                    text = fh.read()
            except OSError:
                continue
            fm, _ = parse_front_matter(text)
            yield rel_path, fm


def date_str(value):
    """Normalize a date/datetime/string to a YYYY-MM-DD string."""
    if value is None:
        return ""
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value)


def url_from_path(rel_path):
    """Turn a relative file path like posts/foo.md into /posts/foo."""
    without_ext = os.path.splitext(rel_path)[0]
    forward = without_ext.replace(os.sep, "/")
    return forward if forward.startswith("/") else "/" + forward


# ---------------------------------------------------------------------------
# MyST AST node builders
# ---------------------------------------------------------------------------

def text_node(value):
    return {"type": "text", "value": value}


def paragraph(*children):
    return {"type": "paragraph", "children": list(children)}


def card_title(title_text):
    return {"type": "cardTitle", "children": [text_node(title_text)]}


def build_post_card(rel_path, fm):
    title = fm.get("title") or os.path.splitext(os.path.basename(rel_path))[0]
    description = fm.get("description") or ""
    date = date_str(fm.get("date"))
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    # Show all tags except the core routing ones
    display_tags = [str(t) for t in tags if t not in ("post", "feed")]
    tag_str = ", ".join(display_tags)
    external_url = fm.get("externalurl") or ""

    url = url_from_path(rel_path)
    children = [card_title(title)]

    meta_parts = [p for p in [date, tag_str] if p]
    if meta_parts:
        children.append(paragraph(text_node(" · ".join(meta_parts))))
    if description:
        children.append(paragraph(text_node(description)))
    if external_url.strip():
        children.append(paragraph(text_node("Also on dev.to")))

    return {"type": "card", "url": url, "children": children}


def build_project_card(rel_path, fm):
    title = fm.get("title") or os.path.splitext(os.path.basename(rel_path))[0]
    description = fm.get("description") or ""
    project_url = fm.get("projecturl") or ""

    url = url_from_path(rel_path)
    children = [card_title(title)]

    if description:
        children.append(paragraph(text_node(description)))
    if project_url.strip():
        children.append(
            paragraph({"type": "link", "url": project_url, "children": [text_node("View project →")]})
        )

    return {"type": "card", "url": url, "children": children}


def build_grid(cards):
    return {"type": "grid", "columns": [1, 2, 2, 2], "children": cards}


# ---------------------------------------------------------------------------
# Directive handlers
# ---------------------------------------------------------------------------

def handle_postlist(data):
    tag_filter = (data.get("arg") or "").strip() or None
    options = data.get("options") or {}
    try:
        limit = int(options.get("number") or 0)
    except (ValueError, TypeError):
        limit = 0

    entries = []
    for rel_path, fm in read_md_files("posts"):
        tags = fm.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        tags = [str(t) for t in tags]
        if tag_filter and tag_filter not in tags:
            continue
        entries.append((rel_path, fm))

    entries.sort(key=lambda item: date_str(item[1].get("date")), reverse=True)
    if limit > 0:
        entries = entries[:limit]

    cards = [build_post_card(rel_path, fm) for rel_path, fm in entries]
    return [build_grid(cards)]


def handle_projectlist(data):
    options = data.get("options") or {}
    try:
        limit = int(options.get("number") or 0)
    except (ValueError, TypeError):
        limit = 0

    entries = []
    for rel_path, fm in read_md_files("projects"):
        if os.path.basename(rel_path).lower() == "readme.md":
            continue
        entries.append((rel_path, fm))

    entries.sort(key=lambda item: date_str(item[1].get("date")), reverse=True)
    if limit > 0:
        entries = entries[:limit]

    cards = [build_project_card(rel_path, fm) for rel_path, fm in entries]
    return [build_grid(cards)]


HANDLERS = {
    "postlist": handle_postlist,
    "projectlist": handle_projectlist,
}

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--role")
    group.add_argument("--directive")
    group.add_argument("--transform")
    args = parser.parse_args()

    if args.directive:
        data = json.load(sys.stdin)
        handler = HANDLERS.get(args.directive)
        result = handler(data) if handler else []
        json.dump(result, sys.stdout)
    else:
        json.dump(plugin, sys.stdout)
