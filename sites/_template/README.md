# New platform template

Copy this folder to `sites/<platform>` and build the page in `index.html`.

## Checklist
- [ ] Unique design for this platform (same brand colours and fonts).
- [ ] `<link rel="canonical" href="https://arslanyounas.vercel.app/">`
- [ ] Email arslanyounas@zohomail.com, LinkedIn, Calendly, USA · UK · UAE · Europe.
- [ ] Working enquiry form for this host (options below).
- [ ] 404 page, robots.txt, sitemap.xml, llms.txt if the site should be indexed.
- [ ] Host config file (headers, redirects) if the platform uses one.

## Form backends by platform
| Platform | Form option |
|---|---|
| Netlify | Netlify Forms (`data-netlify="true"`), email via Site → Forms → Notifications |
| Vercel, GitHub Pages, Cloudflare Pages, Render, Surge, Firebase | FormSubmit (`https://formsubmit.co/ajax/<email>`), Formspree, or Web3Forms |
| Cloudflare Pages | also Pages Functions + an email API |
| Firebase / Azure SWA | also a serverless function + an email API |

## Config files by platform
| Platform | File |
|---|---|
| Vercel | `vercel.json` |
| Netlify | `netlify.toml` (or `_headers` / `_redirects`) |
| Cloudflare Pages | `_headers`, `_redirects` |
| GitHub Pages | none (`404.html` is picked up automatically) |
| Firebase Hosting | `firebase.json` |
| Azure Static Web Apps | `staticwebapp.config.json` |
| Render | settings in dashboard (or `render.yaml` at repo root) |
