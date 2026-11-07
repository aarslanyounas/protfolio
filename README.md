# Arslan Younas – SEO & AI Search (Framer site backup)

A copy of the live Framer site **https://arslanyounas.framer.website**, downloaded on 7 Nov 2026.

## What's here

| Folder | Contents |
|---|---|
| `site/index.html` | Home page |
| `site/work/*.html` | The 5 case study pages (eye-clinic, hack-recovery, indexing-at-scale, recruitment-schema, saas-launch-from-zero) |
| `framerusercontent.com/` | Images, fonts and the Framer scripts the pages need |
| `test.html` | Earlier portfolio draft (unchanged) |

## Viewing it locally

The pages load scripts as modules, so open them through a small local server, not by double-clicking:

```bash
python3 -m http.server 8000
```

Then go to http://localhost:8000/site/index.html

## Important

- The real site is still edited and published in **Framer**. This folder is a snapshot, not the source.
  Changes made here do **not** update the live site.
- To refresh the snapshot after changing the site in Framer, download it again (ask Claude to "re-sync the Framer backup").
- Some fonts and images are still loaded from Framer's CDN at runtime.
