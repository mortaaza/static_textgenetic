# TextGenetic AI Inc. — Static Website

A fast, fully static corporate website for **TextGenetic AI Inc.** ("Pioneering Integrated AI"),
featuring its flagship product **Axion Fleet**. Design inspired by modern corporate-parent sites
(e.g. WELL Health Technologies). No build step, no backend — just HTML, CSS, and a little vanilla JS.

## Structure
```
textgenetic-website/
├── index.html          # the whole page (single-page sections)
├── css/styles.css      # all styling (brand colors at the top as CSS variables)
├── js/main.js          # mobile nav, back-to-top, footer year
├── assets/favicon.svg  # browser tab icon / brand mark
└── README.md
```

## Preview locally
Open `index.html` in any browser, or run a tiny local server:
```bash
cd textgenetic-website
python3 -m http.server 8080      # then visit http://localhost:8080
```

## Edit the content
- **Text & sections:** all in `index.html` — clearly grouped by `<!-- comments -->`.
- **Brand colors:** top of `css/styles.css`, under `:root` (`--navy`, `--blue`, `--cyan`, …).
- **Contact email:** search `info@textgenetic.com` in `index.html` and replace as needed
  (currently used for the company; Axion Fleet links go to https://axionfleetai.com).
- **Announcement bar:** first block in `index.html`.

## Deploy (pick one — all free)
**Netlify (drag & drop):** netlify.com → drag the `textgenetic-website` folder onto the dashboard.
**GitHub Pages:** push this folder to a repo → Settings → Pages → deploy from `main` / root.
**Vercel:** `vercel` in this folder, or import the repo at vercel.com.
**Your own domain:** upload the folder's contents to your web host's public root
(`public_html` / `www`). Point `textgenetic.com` DNS at your chosen host.

## Notes
- Uses the Inter font via Google Fonts (with a system-font fallback if offline).
- Content was drafted from publicly available info about TextGenetic AI Inc. and Axion Fleet —
  review and adjust the copy, team details, and stats before going live.
