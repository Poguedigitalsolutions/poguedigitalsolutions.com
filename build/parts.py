"""Shared page parts for the Pogue Digital Solutions site.
Pages are assembled by build.py from these parts so header/footer/head never drift."""

SITE = "https://poguedigitalsolutions.com"
CALENDLY = "https://calendly.com/poguedigitalsolutions/30min"
EMAIL = "poguedigitalsolutions@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/johnpogue"

# Only pages that actually exist are navigable. Unbuilt pages get added here when they ship.
NAV = [
    ("index.html", "Home"),
    ("solutions.html", "Solutions"),
    ("assessments.html", "Assessments"),
    ("resources.html", "Resources"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

def head(title, description, path, jsonld=None, og_image="img/hero-founder-composite.jpg"):
    canonical = f"{SITE}/{'' if path == 'index.html' else path}"
    ld = ""
    if jsonld:
        for block in jsonld:
            ld += f'<script type="application/ld+json">\n{block}\n</script>\n'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Pogue Digital Solutions, LLC">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE}/{og_image}">
{ld}<link rel="stylesheet" href="css/styles.css">
</head>
<body>
'''

def header(active):
    links = "".join(
        f'<a href="{href}"{" class=\"active\"" if href == active else ""}>{label}</a>'
        for href, label in NAV
    )
    drawer = "".join(
        f'<a href="{href}"{" class=\"active\"" if href == active else ""}>{label}<span>{i+1:02d}</span></a>'
        for i, (href, label) in enumerate(NAV)
    )
    return f'''<header class="site-header">
  <div class="nav-shell">
    <a href="index.html" class="brand" aria-label="Pogue Digital Solutions, LLC home">
      <img src="img/logo-horizontal.png" alt="Pogue Digital Solutions, LLC" class="brand-logo">
    </a>
    <nav class="main-nav" aria-label="Primary">{links}</nav>
    <a href="{CALENDLY}" class="nav-cta nav-cta-desktop" target="_blank" rel="noopener">Book a Call</a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-drawer">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<div class="nav-drawer" id="nav-drawer">
  {drawer}
  <a href="{CALENDLY}" class="btn btn-gold drawer-cta" target="_blank" rel="noopener">Book a Strategy Call</a>
  <div class="drawer-foot">POGUE DIGITAL SOLUTIONS, LLC &middot; CONROE, TX</div>
</div>
'''

LINKEDIN_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0z"/></svg>'

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img src="img/logo-full.png" alt="Pogue Digital Solutions, LLC. Strategy. Systems. Solutions." class="footer-logo">
        <p style="color:rgba(255,255,255,0.55); font-size:14px; max-width:270px;">Pogue Digital Solutions, LLC helps founder-led businesses and organizations organize their knowledge, clarify their brand voice, and build practical AI-assisted systems.</p>
        <p class="footer-motto">&ldquo;Don&rsquo;t tell me it can&rsquo;t be done.&rdquo;</p>
        <div class="footer-social">
          <a href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="John M Pogue on LinkedIn">{LINKEDIN_ICON}</a>
        </div>
      </div>
      <div>
        <h4>Pages</h4>
        <a href="index.html">Home</a>
        <a href="solutions.html">Solutions</a>
        <a href="assessments.html">Assessments</a>
        <a href="resources.html">Resources</a>
        <a href="about.html">About John M Pogue</a>
        <a href="contact.html">Contact</a>
      </div>
      <div>
        <h4>Solutions</h4>
        <a href="solutions.html#brand-voice-ai">Brand Voice AI</a>
        <a href="solutions.html#ai-automation">AI and Automation</a>
        <a href="solutions.html#digital-strategy">Digital Strategy</a>
        <a href="solutions.html#training">Training and Workshops</a>
        <a href="solutions.html#organizations">Government and Organizational Services</a>
      </div>
      <div>
        <h4>Connect</h4>
        <a href="{CALENDLY}" target="_blank" rel="noopener">Book a Strategy Call</a>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
        <a href="contact.html">Request a Workshop</a>
        <a href="contact.html">Government Contracting</a>
        <p style="color:rgba(255,255,255,0.45); font-size:13px; margin-top:14px;">Conroe, Texas<br>Serving Greater Houston and clients nationwide</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Pogue Digital Solutions, LLC. All rights reserved.</span>
      <span class="footer-seal"><img src="img/logo-seal-sm.png" alt="">VETERAN-OWNED &middot; CONROE, TX</span>
    </div>
  </div>
</footer>

<script src="js/site.js"></script>
</body>
</html>
'''

def compass_svg():
    """Decorative rotating compass rose used behind hero sections."""
    ticks = ""
    for i in range(72):
        ang = i * 5
        L = 14 if i % 18 == 0 else (9 if i % 6 == 0 else 5)
        ticks += f'<line x1="400" y1="{400-330}" x2="400" y2="{400-330+L}" transform="rotate({ang} 400 400)"/>'
    return f'''<svg class="compass-bg" viewBox="0 0 800 800" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="cg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#D4AF37" stop-opacity="0.18"/>
      <stop offset="60%" stop-color="#D4AF37" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#D4AF37" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sweepg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F2D680" stop-opacity="0"/>
      <stop offset="100%" stop-color="#F2D680" stop-opacity="0.55"/>
    </linearGradient>
  </defs>
  <circle cx="400" cy="400" r="360" fill="url(#cg)"/>
  <g class="ring-outer" fill="none" stroke="#D4AF37" stroke-opacity="0.45" stroke-width="1">
    <circle cx="400" cy="400" r="330"/>
    <circle cx="400" cy="400" r="318" stroke-dasharray="2 10"/>
    <g stroke-width="1.2">{ticks}</g>
  </g>
  <g class="ring-inner" fill="none" stroke="#D4AF37" stroke-opacity="0.3" stroke-width="1">
    <circle cx="400" cy="400" r="230"/>
    <circle cx="400" cy="400" r="150" stroke-dasharray="1 6"/>
    <path d="M400 170 L412 388 L400 400 L388 388 Z M400 630 L412 412 L400 400 L388 412 Z M170 400 L388 388 L400 400 L388 412 Z M630 400 L412 388 L400 400 L412 412 Z" fill="#D4AF37" fill-opacity="0.12" stroke-opacity="0.5"/>
  </g>
  <g class="sweep">
    <path d="M400 400 L400 70 A330 330 0 0 1 560 110 Z" fill="url(#sweepg)" opacity="0.5"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="18" fill="#F2D680" fill-opacity="0.7" text-anchor="middle">
    <text x="400" y="52">N</text><text x="754" y="407">E</text><text x="400" y="760">S</text><text x="46" y="407">W</text>
  </g>
  <circle cx="400" cy="400" r="5" fill="#F2D680"/>
</svg>'''

def hero_portrait(caption="Founder &amp; Creative Strategist", name="John M Pogue"):
    return f'''<div class="portrait-lockup reveal">
  <img src="img/logo-seal.png" alt="" class="seal">
  <div class="photo-card no-fade">
    <img src="img/portrait-john-desk.jpg" alt="{name}, founder of Pogue Digital Solutions, LLC, at his desk working on AI strategy and business systems" width="520" height="916" loading="eager">
  </div>
  <div class="badge"><strong>{name}</strong><span>{caption}</span></div>
</div>'''

def cta_band(eyebrow, heading, primary=("Take an Assessment", "assessments.html"), secondary=("Schedule a Strategy Conversation", CALENDLY), closing=None):
    sec_attrs = ' target="_blank" rel="noopener"' if secondary and secondary[1].startswith("http") else ""
    sec = f'<a href="{secondary[1]}" class="btn btn-outline-gold"{sec_attrs}>{secondary[0]}</a>' if secondary else ""
    close = f'<p style="font-family:var(--font-display); font-style:italic; font-size:clamp(18px,2vw,22px); color:var(--gold-bright); margin-top:32px;">{closing}</p>' if closing else ""
    return f'''<section>
  <div class="wrap">
    <div class="reveal" style="position:relative; overflow:hidden; text-align:center; background:linear-gradient(135deg, var(--ink) 0%, var(--navy) 100%); border-radius:28px; padding:64px 48px;">
      <div class="glow-blob" style="width:420px; height:420px; background:radial-gradient(circle, rgba(212,175,55,0.3), transparent 70%); top:-160px; left:50%; transform:translateX(-50%);"></div>
      <div style="position:relative; z-index:1; max-width:680px; margin:0 auto;">
        <span class="eyebrow" style="color:var(--gold-bright);">{eyebrow}</span>
        <h2 style="color:#fff; font-size:clamp(26px,3.2vw,38px); margin-top:12px;">{heading}</h2>
        <div style="display:flex; gap:16px; justify-content:center; margin-top:28px; flex-wrap:wrap;">
          <a href="{primary[1]}" class="btn btn-gold">{primary[0]} <span class="btn-arrow">&rarr;</span></a>
          {sec}
        </div>
        {close}
      </div>
    </div>
  </div>
</section>
'''

def faq(items):
    out = '<div class="faq reveal">'
    for q, a in items:
        out += f'<details><summary>{q}</summary><p>{a}</p></details>'
    return out + '</div>'

def faq_jsonld(items):
    import json, html
    ent = [{"@type": "Question", "name": html.unescape(q).replace("’", "'"),
            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a).replace("’", "'")}} for q, a in items]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ent}, indent=1)

def breadcrumb(name, path):
    import json
    return json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": f"{SITE}/{path}"}]}, indent=1)
