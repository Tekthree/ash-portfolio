#!/usr/bin/env python3
"""Generate the portfolio index (work.html) and per-project case-study
pages (work/<slug>.html) for the Ash Riffe prototype.

Shares the concept-b design language: paper texture, terracotta accents,
skeena-display/arboria type, Lumos fluid tokens, container-query toggles.
Re-run after editing PROJECTS below.
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = json.load(open(os.path.join(ROOT, 'assets/projects/manifest.json')))

# Statements marked real=True are Ash's own words from her current site.
# The rest are grounded placeholders pending her concept statements.
PROJECTS = [
    dict(slug='carmel', title='Carmel by the Sea', sub='Furniture &amp; Lighting Selection and Procurement',
         type='Residential &middot; Built Work', real=False,
         statement="A residence in Carmel-by-the-Sea, California. Ash selected and procured the furniture and lighting throughout the home, pairing warm, modern pieces with the architecture's wood ceilings and walls of glass."),
    dict(slug='healing-womb', title='The Healing Womb', sub='Homes &amp; a Community of Support',
         type='Housing Design &middot; Concept', real=True,
         statement="The design enables restoration and autonomy through tranquil, secure environments and easily navigable layouts. Long-term housing for survivors emphasizes private, comfortable spaces with flexible, adaptive seating, and durable, yet refined furniture, complemented by meaningful vintage pieces, and storytelling accents. Greenery and soothing color palettes set a calm stage for healing, while thoughtfully arranged communal areas foster safe social interaction, peer support, and trusted connections."),
    dict(slug='alden-library', title='Alden Fine Art Library', sub='A University Fine Art Library',
         type='Academic &middot; Concept', real=True,
         statement="The future Alden Fine Arts Library will be a hub for student study, research, collaboration, and advancement in the arts; to align with this vision, the design will modernize, integrate, brighten and &ldquo;breathe life&rdquo; into the space, making it adaptable and accessible, while sparking curiosity and inspiration to its users, yet providing plenty of quiet contemplation areas as well. New acoustic ceiling adornments, modern LED linear recessed lighting, vertical pendant lights, and new desk units with integrated lighting and power outlets will modernize the space. Natural light will fill the space, the stack end caps will be replaced with a semi-transparent material, and terrazzo flooring of different light and muted colors brightens the entire space. Adaptable and accessible small study pods, which are ADA friendly, create spaces for quiet solo study and transparent walled &ldquo;rooms&rdquo; help foster small group collaboration. Life is breathed into the space by incorporating living plant walls, while curiosity and inspiration is sparked by the rotating display of student art."),
    dict(slug='next-law-firm', title='Next Law Firm', sub='Los Angeles Law Firm',
         type='Commercial &middot; Concept', real=False,
         statement="A workplace concept for a Los Angeles law firm: a commercial interior designed to feel considered and confident, from reception through the working floors."),
    dict(slug='ridges-commercial', title='The Ridges: Commercial Spaces', sub='Building Connections',
         type='Commercial &middot; Concept', real=False,
         statement="The commercial floors of The Ridges, a multi-use development concept. Public-facing spaces designed to bring the historic building back to life and draw the community inside."),
    dict(slug='ridges-residential', title='The Ridges: Residential Spaces', sub='Soothing Residential Spaces',
         type='Residential &middot; Concept', real=True,
         statement="The residential design of The Ridges delivers timeless, accessible, and neutral, yet distinctive units, that are cohesive with the historic building and the first-floor commercial spaces. The light neutral color palette and hints of light green gives the historic building a fresh feel. The neutral spaces invite families and singles of all ages to envision themselves in the units, and put their own design touches on their homes. Classic, quality, and enduring furniture and fixtures reiterate the timeless design. Universally designed units gives equal access to all spaces for the young and old. Each unit has a unique &ldquo;front porch&rdquo; created with arches and nooks of varying color ways, which gives each unit a distinctive, yet cohesive look, and provides an opportunity for conversation and further user customization."),
    dict(slug='aracari', title='The Aracari Cocktail Bar &amp; Bistro', sub='Bar &amp; Bistro',
         type='Hospitality &middot; Concept', real=False,
         statement="A dark, moody cocktail bar and bistro concept. Forest green, black marble, brass, and warm wood set the stage for evening service."),
]

BASE_CSS = """
    *, *::before, *::after { box-sizing: border-box; }
    html { scroll-behavior: smooth; background: #F6F1E9; }
    :root {
      --paper: #F6F1E9; --paper-deep: #EEE5D8;
      --ink: #1A1614; --ink-soft: #6B5E58;
      --terracotta: #C07B68; --blush: #EDD4CB;
      --line: rgba(26,22,20,.14); --line-light: rgba(246,241,233,.16);
      --serif: "Cormorant Garamond", "skeena-display", serif;
      --space-3xs: clamp(0.75rem, 0.38vw + 0.66rem, 1rem);
      --space-2xs: clamp(1rem, 0.75vw + 0.82rem, 1.5rem);
      --space-xs:  clamp(1.25rem, 1.13vw + 0.99rem, 2rem);
      --space-sm:  clamp(1.5rem, 1.88vw + 1.06rem, 2.75rem);
      --space-md:  clamp(2rem, 3vw + 1.3rem, 4rem);
      --space-lg:  clamp(2.5rem, 4.51vw + 1.44rem, 5.5rem);
      --space-xl:  clamp(3.5rem, 4.51vw + 2.44rem, 6.5rem);
      --space-2xl: clamp(4rem, 8.08vw + 2.11rem, 9.375rem);
      --r-large: 1; --r-medium: 0; --r-small: 0;
      --pair-col: 1fr 1fr;
      --feature-col: 1.15fr .85fr;
    }
    body {
      margin: 0; background-color: var(--paper);
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
      color: var(--ink); font-family: "arboria", system-ui, sans-serif;
      -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility;
      container-type: inline-size; width: 100%; overflow-x: clip;
    }
    img { display: block; max-width: 100%; }
    a { color: inherit; }
    ::selection { background: var(--blush); color: var(--ink); }
    @container (width < 900px) {
      * { --r-large: 0; --r-medium: 1; --pair-col: 1fr; --feature-col: 1fr; }
    }
    @container (width < 600px) { * { --r-medium: 0; --r-small: 1; } }
    .contain { max-width: 84rem; margin: 0 auto; padding: 0 var(--space-md); }
    #siteNav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 50;
      background: rgba(246,241,233,.9);
      backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--line);
    }
    .nav-inner {
      max-width: 84rem; margin: 0 auto; padding: var(--space-2xs) var(--space-md);
      display: flex; align-items: center; justify-content: space-between;
    }
    .nav-logo {
      font-family: var(--serif); font-weight: 600;
      font-size: clamp(1.125rem, 0.56vw + 1rem, 1.5rem); letter-spacing: .2em;
      text-decoration: none; color: var(--ink);
    }
    .nav-links { display: flex; align-items: center; gap: clamp(0.875rem, 2.2vw, 2.75rem); }
    .nav-link {
      font-family: "arboria", sans-serif; font-weight: 400;
      font-size: clamp(0.6875rem, 0.35vw + 0.61rem, 0.8125rem); letter-spacing: .03em;
      text-decoration: none; color: var(--ink);
      opacity: .82; transition: opacity .2s, color .2s;
    }
    .nav-link:hover, .nav-link.is-here { opacity: 1; color: var(--terracotta); }
    .js-ready [data-reveal] { opacity: 0; transform: translateY(22px); transition: opacity .7s ease, transform .7s ease; }
    .js-ready [data-reveal].revealed { opacity: 1; transform: none; }
    @media (prefers-reduced-motion: reduce) { .js-ready [data-reveal] { opacity: 1; transform: none; transition: none; } }
    footer { background: var(--ink); color: var(--paper); margin-top: var(--space-2xl); }
    .footer-inner {
      max-width: 84rem; margin: 0 auto; padding: var(--space-xl) var(--space-md);
      text-align: center;
    }
    .footer-headline {
      font-family: var(--serif); font-weight: 600;
      font-size: clamp(2rem, 1.88vw + 1.56rem, 3.25rem);
      line-height: 0.96; margin: 0 0 var(--space-sm);
    }
    .footer-headline em { font-style: italic; font-weight: 400; color: var(--blush); }
    .btn-book {
      display: inline-flex; align-items: center;
      font-family: "arboria", sans-serif; font-weight: 600;
      font-size: 0.8125rem; letter-spacing: .07em; text-transform: uppercase;
      text-decoration: none; color: var(--ink); background: var(--paper);
      padding: 1.125rem 2.75rem; transition: background .25s, transform .25s;
    }
    .btn-book:hover { background: var(--blush); transform: translateY(-2px); }
    .footer-meta {
      margin-top: var(--space-sm); padding-top: var(--space-sm);
      border-top: 1px solid var(--line-light);
      display: flex; justify-content: center; gap: var(--space-md); flex-wrap: wrap;
      font-size: 0.8125rem; color: rgba(246,241,233,.5);
    }
    .footer-meta a { text-decoration: none; color: rgba(246,241,233,.7); }
    .footer-meta a:hover { color: var(--terracotta); }
"""

REVEAL_JS = """
    document.documentElement.classList.add('js-ready');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) { entry.target.classList.add('revealed'); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
"""

def nav(prefix, here):
    def cls(name):
        return 'nav-link is-here' if name == here else 'nav-link'
    return f"""  <nav id="siteNav">
    <div class="nav-inner">
      <a href="{prefix}concept-b.html" class="nav-logo">ASH RIFFE</a>
      <div class="nav-links">
        <a href="{prefix}work.html" class="{cls('work')}">Work</a>
        <a href="{prefix}concept-b.html#ethos" class="nav-link">Ethos</a>
        <a href="{prefix}concept-b.html#about" class="nav-link">About</a>
        <a href="{prefix}concept-b.html#contact" class="nav-link">Contact</a>
      </div>
    </div>
  </nav>"""

def footer():
    return """  <footer>
    <div class="footer-inner" data-reveal>
      <h2 class="footer-headline">Ready to start the <em>conversation?</em></h2>
      <a href="https://tidycal.com" target="_blank" rel="noopener" class="btn-book">Book a Free Consultation</a>
      <div class="footer-meta">
        <p style="margin:0">&copy; 2026 Ash Riffe</p>
        <a href="mailto:hello@ashriffe.com">hello@ashriffe.com</a>
        <p style="margin:0">Seattle, WA</p>
      </div>
    </div>
  </footer>"""

# ---------- case study pages ----------
CASE_CSS = BASE_CSS + """
    #casehead { padding: clamp(7rem, 11vw, 11.5rem) 0 var(--space-lg); }
    .case-eyebrow {
      font-family: "arboria", sans-serif; font-size: 0.6875rem;
      letter-spacing: .32em; text-transform: uppercase;
      color: var(--ink-soft); margin: 0 0 var(--space-xs);
    }
    .case-title {
      font-family: var(--serif); font-weight: 500;
      /* 40px at 375 -> 76px at 1440 */
      font-size: clamp(2.5rem, 3.38vw + 1.71rem, 4.75rem);
      line-height: 1; letter-spacing: .04em; text-transform: uppercase;
      margin: 0 0 var(--space-2xs); max-width: 18ch;
    }
    .case-sub {
      font-family: var(--serif); font-style: italic; font-weight: 500;
      font-size: clamp(1.25rem, 0.66vw + 1.1rem, 1.75rem);
      color: var(--terracotta); margin: 0 0 var(--space-sm);
    }
    .case-meta {
      display: flex; gap: var(--space-md); flex-wrap: wrap;
      padding: var(--space-2xs) 0;
      border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);
    }
    .case-meta p { margin: 0; font-size: 0.6875rem; letter-spacing: .14em; text-transform: uppercase; color: var(--ink-soft); }
    #statement { padding: var(--space-lg) 0 var(--space-md); }
    .statement-layout { display: grid; grid-template-columns: var(--feature-col); gap: var(--space-md) var(--space-xl); align-items: start; }
    .statement-label {
      font-family: var(--serif); font-style: italic; font-weight: 500;
      font-size: clamp(1.25rem, 0.66vw + 1.1rem, 1.75rem); margin: 0;
    }
    .statement-body {
      font-family: "arboria", sans-serif;
      font-size: clamp(1.0625rem, 0.18vw + 1rem, 1.1875rem); line-height: 1.85;
      color: var(--ink-soft); margin: 0;
    }
    #gallery { padding: var(--space-md) 0 0; }
    .g-full { margin: 0 0 var(--space-md); }
    .g-pair { display: grid; grid-template-columns: var(--pair-col); gap: var(--space-md); margin: 0 0 var(--space-md); }
    .g-pair figure, .g-full figure { margin: 0; }
    /* Presentation boards carry small text — never crop them */
    #gallery img { width: 100%; height: auto; box-shadow: 0 24px 55px -34px rgba(26,22,20,.4); }
    #pn { border-top: 1px solid var(--line); margin-top: var(--space-xl); }
    .pn-inner { display: flex; justify-content: space-between; gap: var(--space-md); padding: var(--space-sm) 0; }
    .pn-link { text-decoration: none; max-width: 46%; }
    .pn-label { font-size: 0.6875rem; letter-spacing: .18em; text-transform: uppercase; color: var(--ink-soft); margin: 0 0 6px; }
    .pn-title {
      font-family: var(--serif); font-weight: 600;
      font-size: clamp(1.125rem, 0.47vw + 1.02rem, 1.4375rem); margin: 0;
      transition: color .25s;
    }
    .pn-link:hover .pn-title { color: var(--terracotta); }
    .pn-next { text-align: right; margin-left: auto; }
"""

def gallery_html(slug, n_imgs, exts):
    """01 is the header hero; the rest alternate full / pair."""
    figs = [f'../assets/projects/{slug}/{i:02d}{exts[i]}' for i in range(2, n_imgs + 1)]
    out, i = [], 0
    toggle_full = True
    while i < len(figs):
        if toggle_full or i == len(figs) - 1:
            out.append(f'      <div class="g-full" data-reveal><figure><img src="{figs[i]}" alt="Project image" loading="lazy"></figure></div>')
            i += 1
        else:
            out.append('      <div class="g-pair" data-reveal>')
            out.append(f'        <figure><img src="{figs[i]}" alt="Project image" loading="lazy"></figure>')
            out.append(f'        <figure><img src="{figs[i+1]}" alt="Project image" loading="lazy"></figure>')
            out.append('      </div>')
            i += 2
        toggle_full = not toggle_full
    return '\n'.join(out)

def build_case(idx):
    p = PROJECTS[idx]
    slug = p['slug']
    files = MANIFEST[slug]
    n = len(files)
    exts = {i: os.path.splitext(f['file'])[1].replace('.png', '.jpg') for i, f in enumerate(files, 1)}
    prev_p = PROJECTS[(idx - 1) % len(PROJECTS)]
    next_p = PROJECTS[(idx + 1) % len(PROJECTS)]
    placeholder_note = '' if p['real'] else '\n  <!-- PLACEHOLDER STATEMENT: pending Ash\'s concept statement for this project -->'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p['title'].replace('&amp;', '&')} | Ash Riffe</title>
  <meta name="description" content="{p['title'].replace('&amp;', '&')}, a project by Ash Riffe Interior Architecture.">
  <link rel="stylesheet" href="https://use.typekit.net/nil8axf.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
  <style>{CASE_CSS}</style>
</head>
<body>
{nav('../', 'work')}{placeholder_note}
  <section id="casehead">
    <div class="contain">
      <p class="case-eyebrow" data-reveal>{p['type']}</p>
      <h1 class="case-title" data-reveal>{p['title']}</h1>
      <p class="case-sub" data-reveal>{p['sub']}</p>
      <div class="case-meta" data-reveal>
        <p>{p['type']}</p>
        <p>Ash Riffe Interior Architecture</p>
      </div>
    </div>
  </section>

  <section id="statement">
    <div class="contain">
      <div class="statement-layout">
        <div data-reveal>
          <p class="statement-label">The design concept.</p>
        </div>
        <p class="statement-body" data-reveal>{p['statement']}</p>
      </div>
    </div>
  </section>

  <section id="gallery">
    <div class="contain">
      <div class="g-full" data-reveal><figure><img src="../assets/projects/{slug}/01{exts[1]}" alt="{p['title'].replace('&amp;', '&')} cover image" loading="eager"></figure></div>
{gallery_html(slug, n, exts)}
    </div>
  </section>

  <section id="pn">
    <div class="contain">
      <div class="pn-inner">
        <a class="pn-link" href="{prev_p['slug']}.html">
          <p class="pn-label">&larr; Previous</p>
          <p class="pn-title">{prev_p['title']}</p>
        </a>
        <a class="pn-link pn-next" href="{next_p['slug']}.html">
          <p class="pn-label">Next &rarr;</p>
          <p class="pn-title">{next_p['title']}</p>
        </a>
      </div>
    </div>
  </section>

{footer()}

  <script>{REVEAL_JS}</script>
</body>
</html>
"""

# ---------- portfolio index ----------
INDEX_CSS = BASE_CSS + """
    #workhead { padding: clamp(7rem, 11vw, 11.5rem) 0 var(--space-lg); }
    .work-eyebrow {
      font-family: "arboria", sans-serif; font-size: 0.6875rem;
      letter-spacing: .32em; text-transform: uppercase;
      color: var(--ink-soft); margin: 0 0 var(--space-xs);
    }
    .work-title {
      font-family: var(--serif); font-weight: 600;
      font-size: clamp(2.75rem, 3.38vw + 1.96rem, 5rem);
      line-height: 0.96; letter-spacing: -.015em; margin: 0 0 var(--space-2xs);
    }
    .work-title em { font-style: normal; text-transform: uppercase; letter-spacing: .05em; color: var(--terracotta); }
    .work-title i { font-style: italic; font-weight: 500; }
    .work-intro {
      font-family: "arboria", sans-serif;
      font-size: clamp(1rem, 0.09vw + 0.98rem, 1.0625rem); line-height: 1.75;
      color: var(--ink-soft); max-width: 52ch; margin: 0;
    }
    #grid { padding: var(--space-lg) 0 0; }
    .feature-card { display: grid; grid-template-columns: var(--feature-col); gap: var(--space-md) var(--space-xl); align-items: end; text-decoration: none; margin-bottom: var(--space-xl); }
    .feature-card figure, .card figure { margin: 0; overflow: clip; }
    .feature-card img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; transition: transform .9s cubic-bezier(.2,.6,.2,1); }
    .feature-card:hover img, .card:hover img { transform: scale(1.045); }
    .card-num {
      font-family: "aquavit", sans-serif; font-weight: 300;
      font-size: 0.6875rem; letter-spacing: .26em; color: var(--terracotta); margin: 0 0 var(--space-3xs);
    }
    .card-title {
      font-family: var(--serif); font-weight: 500;
      font-size: clamp(1.5rem, 1.13vw + 1.24rem, 2.25rem);
      line-height: 1.05; letter-spacing: .04em; text-transform: uppercase;
      margin: 0 0 var(--space-3xs); color: var(--ink);
      transition: color .25s;
    }
    .feature-card:hover .card-title, .card:hover .card-title { color: var(--terracotta); }
    .card-type {
      font-family: "arboria", sans-serif; font-size: 0.6875rem;
      letter-spacing: .14em; text-transform: uppercase; color: #9A8878; margin: 0;
    }
    .cards { display: grid; grid-template-columns: var(--pair-col); gap: var(--space-xl) var(--space-md); }
    .card { text-decoration: none; }
    .card img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; transition: transform .9s cubic-bezier(.2,.6,.2,1); }
    .card figcaption, .feature-caption { padding-top: var(--space-2xs); }
"""

def build_index():
    feature = PROJECTS[0]
    f_ext = os.path.splitext(MANIFEST[feature['slug']][0]['file'])[1].replace('.png', '.jpg')
    cards = []
    for i, p in enumerate(PROJECTS[1:], 2):
        ext = os.path.splitext(MANIFEST[p['slug']][0]['file'])[1].replace('.png', '.jpg')
        cards.append(f"""        <a class="card" href="work/{p['slug']}.html" data-reveal>
          <figure>
            <img src="assets/projects/{p['slug']}/01{ext}" alt="{p['title'].replace('&amp;', '&')} cover" loading="lazy">
            <figcaption>
              <p class="card-num">{i:02d}</p>
              <h2 class="card-title">{p['title']}</h2>
              <p class="card-type">{p['type']}</p>
            </figcaption>
          </figure>
        </a>""")
    cards_html = '\n'.join(cards)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Work | Ash Riffe</title>
  <meta name="description" content="Selected residential and commercial projects by Ash Riffe Interior Architecture, Seattle.">
  <link rel="stylesheet" href="https://use.typekit.net/nil8axf.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
  <style>{INDEX_CSS}</style>
</head>
<body>
{nav('', 'work')}

  <section id="workhead">
    <div class="contain">
      <p class="work-eyebrow" data-reveal>Portfolio</p>
      <h1 class="work-title" data-reveal><i>The</i> <em>work.</em></h1>
      <p class="work-intro" data-reveal>Residential and commercial projects, from a built home on the California coast to concepts for housing, libraries, workplaces, and hospitality. Each tells a story of creativity, collaboration, and results.</p>
    </div>
  </section>

  <section id="grid">
    <div class="contain">
      <a class="feature-card" href="work/{feature['slug']}.html" data-reveal>
        <figure>
          <img src="assets/projects/{feature['slug']}/01{f_ext}" alt="{feature['title']} cover" loading="eager">
        </figure>
        <div class="feature-caption">
          <p class="card-num">01</p>
          <h2 class="card-title">{feature['title']}</h2>
          <p class="card-type">{feature['type']}</p>
        </div>
      </a>
      <div class="cards">
{cards_html}
      </div>
    </div>
  </section>

{footer()}

  <script>{REVEAL_JS}</script>
</body>
</html>
"""

os.makedirs(os.path.join(ROOT, 'work'), exist_ok=True)
for i in range(len(PROJECTS)):
    path = os.path.join(ROOT, 'work', PROJECTS[i]['slug'] + '.html')
    open(path, 'w').write(build_case(i))
    print('wrote', path)
open(os.path.join(ROOT, 'work.html'), 'w').write(build_index())
print('wrote work.html')
