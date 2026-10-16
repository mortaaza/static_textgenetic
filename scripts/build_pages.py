#!/usr/bin/env python3
"""Generate the topic pages, glossary and sitemap for textgenetic.com.

Run from the repo root:  python3 scripts/build_pages.py
Content lives in scripts/content.py; this file only renders it.
"""
import datetime, html, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SITE, TOPICS, GLOSSARY  # noqa: E402

TODAY = datetime.date.today().isoformat()


def esc(s):
    return html.escape(s, quote=True)


def head(title, description, path, jsonld):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <link rel="canonical" href="{url}" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/assets/og-image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#0a1533" />
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png" />
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/css/styles.css?v=4" />
  <style>html{{scroll-snap-type:none}}</style>
  <script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
</head>
<body>
  <header class="site-header">
    <div class="container header__inner">
      <a class="brand" href="/" aria-label="TextGenetic AI home">
        <img class="brand__mark" src="/assets/logo-mark.png" alt="" width="29" height="40" />
        <img class="brand__wordmark" src="/assets/logo-wordmark.png" alt="TextGenetic" width="198" height="28" />
      </a>
      <nav class="nav nav--inline"><a href="/neuroanalytics/">Neuroanalytics</a><a href="/predictive-maintenance-ai/">Case study</a><a href="/glossary/">Glossary</a><a href="/about/">About</a><a class="nav__cta" href="/#contact">Talk to us</a></nav>
    </div>
  </header>
"""


def footer():
    return """  <footer class="page--footer"><div class="container footer__inner">
    <span class="footer__copy">© <span id="year">2026</span> TextGenetic AI Inc. · Kitchener, Ontario, Canada</span>
    <nav class="footer__nav"><a href="/">Home</a><a href="/glossary/">Glossary</a><a href="/about/">About</a><a href="/privacy.html">Privacy</a><a href="/terms.html">Terms</a></nav>
  </div></footer>
  <script>document.getElementById('year').textContent=new Date().getFullYear();</script>
</body>
</html>
"""


def crumbs(items):
    """items: [(name, path)] — last is current page."""
    lis = []
    for i, (name, path) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li aria-current="page">{esc(name)}</li>')
        else:
            lis.append(f'<li><a href="{path}">{esc(name)}</a></li>')
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)]}
    return '<ol class="crumbs">' + "".join(lis) + "</ol>", ld


def cta_box():
    return """<aside class="cta-box">
      <strong>Working on something similar?</strong>
      <p>Tell us about the problem and we'll come back with a practical next step — usually a scoped pilot on your real data.</p>
      <a class="btn btn--primary" href="/#contact">Talk to us →</a>
    </aside>"""


def related(slugs, exclude=None):
    items = [g for g in GLOSSARY if g["slug"] in slugs and g["slug"] != exclude]
    if not items:
        return ""
    lis = "".join(f'<li><a href="/glossary/{g["slug"]}/">{esc(g["term"])}</a><span>{esc(g["short"])}</span></li>' for g in items)
    return f'<section class="related"><h2>Related terms</h2><ul class="term-list">{lis}</ul></section>'


def write(path, content):
    full = os.path.join(ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


urls = ["/", "/privacy.html", "/terms.html"]

# ---- Topic pages -------------------------------------------------------------
for t in TOPICS:
    path = f"/{t['slug']}/"
    crumb_html, crumb_ld = crumbs([("Home", "/"), (t["crumb"], path)])
    article_ld = {"@context": "https://schema.org", "@type": "Article", "headline": t["h1"], "description": t["description"],
                  "author": {"@type": "Organization", "name": "TextGenetic AI Inc."}, "publisher": {"@type": "Organization", "name": "TextGenetic AI Inc.", "logo": {"@type": "ImageObject", "url": SITE + "/assets/favicon-512.png"}},
                  "mainEntityOfPage": SITE + path, "dateModified": TODAY}
    body = f"""  <main class="page page--topic">
    {crumb_html}
    <p class="kicker">{esc(t['kicker'])}</p>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    {t['body']}
    {cta_box()}
    {related(t.get('related', []))}
  </main>
"""
    write(path, head(t["title"], t["description"], path, [article_ld, crumb_ld]) + body + footer())
    urls.append(path)

# ---- Glossary index ----------------------------------------------------------
gpath = "/glossary/"
crumb_html, crumb_ld = crumbs([("Home", "/"), ("Glossary", gpath)])
terms_sorted = sorted(GLOSSARY, key=lambda g: g["term"].lower())
lis = "".join(f'<li><a href="/glossary/{g["slug"]}/">{esc(g["term"])}</a><span>{esc(g["short"])}</span></li>' for g in terms_sorted)
index_ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "TextGenetic AI glossary", "url": SITE + gpath,
            "hasDefinedTerm": [{"@type": "DefinedTerm", "name": g["term"], "url": SITE + f"/glossary/{g['slug']}/"} for g in terms_sorted]}
body = f"""  <main class="page page--topic">
    {crumb_html}
    <p class="kicker">Glossary</p>
    <h1>Brain-health AI and applied-AI glossary</h1>
    <p class="lead">Plain-language definitions of the terms we use in neuroanalytics, clinical workflow automation and predictive AI — written for clinicians, public-sector buyers and partners, not just engineers.</p>
    <ul class="term-list term-list--index">{lis}</ul>
    {cta_box()}
  </main>
"""
write(gpath, head("Glossary of brain-health AI and applied-AI terms — TextGenetic AI", "Clear definitions of digital biomarkers, neuroanalytics, freezing of gait, Technology Readiness Levels, the ISC Testing Stream, predictive maintenance and more.", gpath, [index_ld, crumb_ld]) + body + footer())
urls.append(gpath)

# ---- Glossary entries --------------------------------------------------------
for g in GLOSSARY:
    path = f"/glossary/{g['slug']}/"
    crumb_html, crumb_ld = crumbs([("Home", "/"), ("Glossary", gpath), (g["term"], path)])
    term_ld = {"@context": "https://schema.org", "@type": "DefinedTerm", "name": g["term"], "description": g["short"], "url": SITE + path,
               "inDefinedTermSet": {"@type": "DefinedTermSet", "name": "TextGenetic AI glossary", "url": SITE + gpath}}
    why = f'<section class="why-box"><h2>Why it matters to our work</h2><p>{g["why"]}</p></section>' if g.get("why") else ""
    body = f"""  <main class="page page--topic">
    {crumb_html}
    <p class="kicker">Glossary</p>
    <h1>{esc(g['term'])}</h1>
    <p class="lead">{g['short']}</p>
    {g['body']}
    {why}
    {related(g.get('related', []), exclude=g['slug'])}
    {cta_box()}
  </main>
"""
    write(path, head(f"{g['term']} — definition | TextGenetic AI glossary", g["short"], path, [term_ld, crumb_ld]) + body + footer())
    urls.append(path)

# ---- sitemap + robots --------------------------------------------------------
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    prio = "1.0" if u == "/" else ("0.8" if not u.startswith("/glossary/") and not u.endswith(".html") else "0.6")
    sm.append(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>")
sm.append("</urlset>")
open(os.path.join(ROOT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print(f"built {len(TOPICS)} topic pages, {len(GLOSSARY)} glossary terms, sitemap with {len(urls)} URLs")
