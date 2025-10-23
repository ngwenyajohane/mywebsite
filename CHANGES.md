# CHANGES — mywebsite

Date: 2025-10-22

Summary of edits performed during this session:

- Implemented a retracting header across the site (hides on scroll down, shows on scroll up). Added defensive JS and small CSS transition.
- Centralized header behavior into shared assets under `/mywebsite/assets/`:
  - `header.js` — initializes lucide icons, dark-mode toggle, and retracting header behavior.
  - `header.css` — shared CSS for `header.retractable` and `is-hidden` classes.
  - `includes/header.html` — canonical header markup (kept for reference; pages still contain markup for static sites).
- Updated pages to use shared assets:
  - `/mywebsite/index.html` — now loads `/mywebsite/assets/header.css` and `/mywebsite/assets/header.js`.
  - `/article.html` (root) — replaced with a small redirect page to `/mywebsite/article.html` to avoid duplication.
  - `/mywebsite/article.html` — canonical article page (no changes to content beyond header/style consolidation).
  - `/mywebsite/kweku-article.html` — updated to include shared header assets.
- Removed duplicated inline retracting header scripts from individual pages and centralized logic in `header.js` to reduce duplication and maintenance surface.

How to preview locally

1. From the repository root run a simple static server:

```bash
python3 -m http.server 8000
```

2. Open these pages in your browser:

- http://localhost:8000/mywebsite/index.html
- http://localhost:8000/mywebsite/article.html
- http://localhost:8000/mywebsite/kweku-article.html

Notes & next steps

- If you use a static site generator or server-side includes, consider replacing the duplicated header HTML with an include that pulls in `includes/header.html`.
- If you want the root `/article.html` removed entirely instead of a redirect, tell me and I will delete it.
- The Bitdocs article import remains pending — paste the article text or ask me to attempt another fetch.
