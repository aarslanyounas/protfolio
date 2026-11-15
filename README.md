# Arslan Younas — site builds per hosting platform

One repository, one folder per hosting platform. Each folder under `sites/` is a complete,
self-contained static site (HTML, assets, SEO files and that platform's config), so every
platform can deploy its folder independently and have its own design.

```
sites/
  vercel/    → https://arslanyounas.vercel.app        (light "crawl console" design, FormSubmit form)
  netlify/   → https://arslanyounas.netlify.app       (dark "search results" design, Netlify Forms)
  cloudflare/→ https://www.arslanyounas.workers.dev (radar hero, dark only, FormSubmit form)
  github-pages/→ https://aarslanyounas.github.io/protfolio (light "build in public" heatmap + git log, FormSubmit form)
  _template/ → starting point for the next platform
```

## How each platform is connected

| Platform | Project / site | Branch | Root / base directory | Build command | Output |
|---|---|---|---|---|---|
| Vercel  | `arslanyounas` | `main` | `sites/vercel`  | none | `.` |
| Netlify | `arslanyounas` | `main` | `sites/netlify` | none | `sites/netlify` |
| GitHub Pages | repo Settings → Pages (Source: GitHub Actions) | `main` | `sites/github-pages` via `.github/workflows/github-pages.yml` | none | `sites/github-pages` |
| Cloudflare Workers | `www` | `main` | repo root (`wrangler.jsonc` → `sites/cloudflare`) | none | `npx wrangler deploy` |

Pushing to `main` deploys only the platforms whose folder changed (both hosts are set to
watch their own directory).

## Shared rules for every site

- **Canonical URL:** `https://arslanyounas.vercel.app/` is the primary address. Netlify
  points its canonical there; Cloudflare uses its own URL (self-canonical).
- **Contact:** arslanyounas@zohomail.com · https://www.linkedin.com/in/arslanyounas/ ·
  https://calendly.com/arslanyounas/30min
- **Markets:** USA · UK · UAE · Europe
- **Brand:** orange `#FF4F12`, ink `#121211`, off-white `#FAFAF8`; fonts Inter Tight, Geist,
  Geist Mono, Caveat.
- **No fake metrics or testimonials.**

## Add a new platform

1. Copy `sites/_template` to `sites/<platform>` (e.g. `sites/cloudflare`).
2. Design the page in `sites/<platform>/index.html` (give each platform its own look).
3. Pick a form backend that works on that host (see `sites/_template/README.md`).
4. Add the platform's config file if it needs one (headers, 404, redirects).
5. In the platform's dashboard, connect this repo, branch `main`, root/base directory
   `sites/<platform>`, no build command, output `.`.
6. Add a row to the table above.

## Run a site locally

```bash
cd sites/netlify            # or sites/vercel
python -m http.server 8000  # Windows: py -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000. Forms only send once deployed on their platform.
