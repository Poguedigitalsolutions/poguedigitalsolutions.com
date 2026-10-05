"""Builds one HTML page per article in articles/*.md, plus resources.html listing them."""
import json, re, glob, os
import markdown
from parts import *

ART_DIR = os.path.join(os.path.dirname(__file__), "articles")
OUT = "."
PORTRAIT = "img/portrait-john-desk.jpg"

def parse(path):
    raw = open(path).read()
    _, fm, body = raw.split("---", 2)
    meta = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in fm.strip().splitlines())}
    # drop the H1; the page hero renders the title
    body = re.sub(r"^# .*\n", "", body.strip(), count=1)
    return meta, body

def link_ctas(html):
    """Turn the assessment and call references in article text into real links."""
    repl = {
        "Brand Voice Quick Check": '<a href="assessments.html#brand-voice">Brand Voice Quick Check</a>',
        "AI Readiness Assessment": '<a href="assessments.html#ai-readiness">AI Readiness Assessment</a>',
        "Business Systems Assessment": '<a href="assessments.html#continuity">Business Systems Assessment</a>',
        "book a strategy call": f'<a href="{CALENDLY}" target="_blank" rel="noopener">book a strategy call</a>',
        "Brand Voice AI foundation session": '<a href="solutions.html#brand-voice-ai">Brand Voice AI foundation session</a>',
    }
    for k, v in repl.items():
        html = html.replace(k, v, 1)
    return html

articles = []
for path in sorted(glob.glob(f"{ART_DIR}/*.md")):
    meta, body = parse(path)
    html_body = markdown.markdown(body)
    # style the opening "short answer" paragraph as a lede
    html_body = html_body.replace("<p><strong>The short answer:</strong>", '<p class="lede"><strong>The short answer:</strong>', 1)
    html_body = link_ctas(html_body)
    articles.append((meta, html_body))

    slug = meta["slug"]
    url = f"{SITE}/{slug}.html"
    ld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": meta["title"], "description": meta["description"],
         "author": {"@type": "Person", "name": "John M Pogue", "url": SITE + "/about.html"},
         "publisher": {"@type": "Organization", "name": "Pogue Digital Solutions, LLC", "logo": {"@type": "ImageObject", "url": SITE + "/img/logo-horizontal.png"}},
         "datePublished": meta["date"], "dateModified": meta["date"], "mainEntityOfPage": url,
         "image": SITE + "/img/hero-founder-composite.jpg", "articleSection": meta["category"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Resources", "item": SITE + "/resources.html"},
            {"@type": "ListItem", "position": 3, "name": meta["title"], "item": url}]}]}, indent=1)

    page = head(f'{meta["title"]} | Pogue Digital Solutions', meta["description"], f"{slug}.html", jsonld=[ld]) + header("resources.html") + f'''
<section class="on-ink tight" style="padding-top:56px; padding-bottom:64px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:820px;">
    <a href="resources.html" style="font-family:var(--font-mono); font-size:11.5px; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold-bright); text-decoration:none;">&larr; Resources</a>
    <span class="eyebrow" style="display:block; margin-top:22px;">{meta["category"]}</span>
    <h1 style="font-size:clamp(32px,4.6vw,54px); color:#fff; margin-top:14px;">{meta["title"]}</h1>
    <p style="font-size:17px; margin-top:18px; max-width:680px;">{meta["description"]}</p>
    <div class="article-meta" style="margin-top:28px;">
      <span class="article-byline"><img src="{PORTRAIT}" alt=""><strong>John M Pogue</strong></span>
      <span>Published {meta["date"]}</span>
      <span>{meta["reading_time"]} read</span>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <article class="article-body reveal">
{html_body}
    </article>
  </div>
</section>

<section class="on-paper-dim tight">
  <div class="wrap" style="max-width:760px;">
    <div class="author-card reveal">
      <img src="{PORTRAIT}" alt="John M Pogue">
      <div>
        <span class="eyebrow">About the author</span>
        <h3 style="font-size:20px; margin-top:8px;">John M Pogue</h3>
        <p style="font-size:14.5px; margin-top:8px;">Founder and Creative Strategist of Pogue Digital Solutions, LLC. Navy veteran and former Hospital Corpsman with an M.S. in Digital Marketing from Full Sail University. He builds AI-assisted business systems that keep the founder's knowledge and voice at the center.</p>
        <a href="about.html" style="font-family:var(--font-mono); font-size:11.5px; letter-spacing:0.08em; text-transform:uppercase; color:var(--gold-dim);">Read John&rsquo;s story &rarr;</a>
      </div>
    </div>
  </div>
</section>

{cta_band("Put This to Work", "Find out where your business stands with a free assessment, or talk it through with John.", primary=("Take an Assessment", "assessments.html"))}
''' + footer()
    open(f"{OUT}/{slug}.html", "w").write(page)
    print(slug, len(page))

# ---------------- resources.html ----------------
rows = ""
for meta, _ in articles:
    rows += f'''<a class="article-row" href="{meta["slug"]}.html">
  <div><span class="card-eyebrow">{meta["category"]} &middot; {meta["reading_time"]}</span><h3>{meta["title"]}</h3><p>{meta["description"]}</p></div>
  <span class="go">READ &rarr;</span>
</a>
'''

RES_LD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "CollectionPage", "name": "Resources", "url": SITE + "/resources.html",
     "description": "Articles and tools from Pogue Digital Solutions on brand voice, AI adoption, automation, and capturing founder knowledge.",
     "hasPart": [{"@type": "Article", "headline": m["title"], "url": f'{SITE}/{m["slug"]}.html'} for m, _ in articles]},
    json.loads(breadcrumb("Resources", "resources.html"))]}, indent=1)

page = head("Resources | Articles on Brand Voice, AI, and Business Systems",
            "Practical articles from John M Pogue on brand voice, what to automate first, and how to capture the knowledge inside a founder's head.",
            "resources.html", jsonld=[RES_LD]) + header("resources.html") + f'''
<section class="on-ink tight" style="padding-top:56px; padding-bottom:64px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:760px;">
    <span class="eyebrow">Resources</span>
    <h1 style="font-size:clamp(34px,5vw,60px); color:#fff; margin-top:16px;">Practical Resources for Building a More Consistent Business</h1>
    <p style="font-size:17px; max-width:600px; margin-top:18px;">Articles written to answer the questions founders ask before they hire anyone: what Brand Voice AI is, what to automate first, and how to get the knowledge out of your head and into a system.</p>
  </div>
</section>

<section>
  <div class="wrap" style="max-width:900px;">
    <div class="section-head reveal"><span class="eyebrow">Articles</span><h2>Start here.</h2></div>
    <div class="article-list reveal">
{rows}    </div>
  </div>
</section>

<section class="on-paper-dim">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Coming Next</span><h2>More is on the way.</h2><p>The Resource Center will grow into an answer library. Here is what is in the queue.</p></div>
    <div class="grid-3 reveal">
      <div class="card"><span class="card-eyebrow">Tools</span><h3 style="font-size:17px;">AI Toolbox</h3><p style="font-size:14px;">Recommended AI, marketing, automation, and business tools with plain-English explanations of who each one is for.</p></div>
      <div class="card"><span class="card-eyebrow">Tools</span><h3 style="font-size:17px;">Custom AI Assistants</h3><p style="font-size:14px;">Guided assistants for customer journey mapping, avatar research, email creation, and brand development.</p></div>
      <div class="card"><span class="card-eyebrow">Downloads</span><h3 style="font-size:17px;">Worksheets and Checklists</h3><p style="font-size:14px;">Brand voice worksheets, an AI readiness checklist, customer journey templates, and knowledge-capture exercises.</p></div>
    </div>
    <div class="reveal" style="margin-top:28px;"><a href="contact.html#general" class="btn btn-outline-navy">Ask to be notified <span class="btn-arrow">&rarr;</span></a></div>
  </div>
</section>

{cta_band("Not Sure Where to Start?", "Take a free assessment and the result will point you to the right article, tool, or conversation.", primary=("Take an Assessment", "assessments.html"))}
''' + footer()
open(f"{OUT}/resources.html", "w").write(page)
print("resources.html", len(page))
