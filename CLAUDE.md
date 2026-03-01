# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Start development server with hot reload (requires PDM venv active)
./node_modules/.bin/myst start

# Build to _build/html/
./node_modules/.bin/myst build --html

# Generate RSS feed (run after myst build)
python plugins/rss_gen.py

# Full build (venv must be active for the blog plugin)
source .venv/bin/activate
./node_modules/.bin/myst build --html && python plugins/rss_gen.py
```

The PDM venv must be active whenever `myst build` or `myst start` runs, because the
`plugins/blog_listing.py` executable plugin requires `pyyaml` from the venv.

There is no test suite. The site deploys automatically via GitHub Actions on push to `master`.

## Architecture

This is a personal website ([ryandlewis.dev](https://ryandlewis.dev)) built with [MyST](https://mystmd.org/) v1.8+.

### Content Types

Content is written in Markdown with YAML front matter. MyST auto-discovers all `.md` files
(excludes listed in `myst.yml`). No layout files — MyST's `book-theme` handles all rendering.

**Blog posts** live in `posts/` (TTRPG logs in `posts/ttrpg/`).
**Project pages** live in `projects/`.
**Static pages**: `index.md`, `aboutme.md`, `aboutsite.md`, `support.md`, `404.md`.
**Listing pages**: `posts.md`, `projects.md` — use `postlist`/`projectlist` directives.

### Tags

Tags are used by the blog listing plugin and RSS generator:
- `post` — any blog post
- `dev` — posts also on dev.to (set `externalurl:` in front matter)
- `project` — project pages
- `dms_log` — TTRPG session reports
- `Adventures_in_Tech` — tech tutorial series
- `feed` — included in the Atom RSS feed at `/feed.xml`
- `quick_tech_tips` — quick tip posts

### Image Sizing

Use MyST's native `image` or `figure` directives with `:width:`:
```markdown
:::{image} /assets/images/photo.jpg
:width: 250px
:align: center
:::
```

Common widths: `80%` (full-width), `250px` (medium), `100px` (small).

### Plugins (`plugins/`)

- **`blog_listing.py`** — MyST executable plugin. Provides `postlist` and `projectlist`
  directives. Reads front matter from `posts/` and `projects/`, outputs MyST card-grid AST.
  Requires `pyyaml` (managed by PDM).

- **`rss_gen.py`** — Standalone script. Reads front matter from files tagged `feed`,
  generates `_build/html/feed.xml` (Atom format). Requires `pyyaml` + `feedgen` (PDM).

### Adding New Content

**New post:**
```markdown
---
title: Post Title
date: YYYY-MM-DD
description: "Short description for cards and SEO."
tags: [post, feed]
# For dev.to cross-posts also add:
# externalurl: https://dev.to/...
---
```

**New project:**
```markdown
---
title: Project Title
date: YYYY-MM-DD
description: "Short description."
projecturl: https://github.com/...
tags: [project, feed]
---
```

**New TTRPG log:** Same as post but add `dms_log` tag and place in `posts/ttrpg/`.

### Deployment

GitHub Actions (`.github/workflows/deploy.yml`) activates the PDM venv, runs
`myst build --html`, then `python plugins/rss_gen.py`, and deploys `_build/html/` to
GitHub Pages. The `CNAME` file sets the custom domain to `ryandlewis.dev`.
