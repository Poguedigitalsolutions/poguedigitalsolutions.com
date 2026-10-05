"""Builds the blog: blog/index.html, one blog/<slug>.html per articles/*.md,
blog/feed.xml (RSS), and resources.html (which points into the blog).

Article front matter: title, slug, description, author, date, category, reading_time,
optional updated (YYYY-MM-DD) and keywords (comma list).

AEO hooks in the Markdown:
  - Open with a paragraph starting "**The short answer:**". It becomes the styled lede
    and the speakable / answer passage in the schema.
  - Every "## " heading gets a stable anchor and appears in the "In this article" list,
    so search and answer engines can link straight to a passage.
  - An optional final section "## Frequently Asked Questions" with "### Question" subheads
    renders as an accordion and FAQPage schema. Leave it out until the answers are approved.
"""
import json, re, glob, os, html as htmlmod
from datetime import datetime, timezone
from email.utils import format_datetime
import markdown
from parts import *

ART_DIR = os.path.join(os.path.dirname(__file__), "articles")
PORTRAIT = "img/portrait-john-desk.jpg"
BLOG_ID = SITE + "/blog/#blog"
os.makedirs("blog", exist_ok=True)


def parse(path):
    raw = open(path).read()
    _, fm, body = raw.split("---", 2)
    meta = {k.strip(): v.strip() for k, v in (l.split(":", 1) for l in fm.strip().splitlines() if ":" in l)}
    meta.setdefault("updated", meta["date"])
    body = re.sub(r"^# .*\n", "", body.strip(), count=1)  # the hero renders the title
    return meta, body


def split_faq(body):
    """Pull an optional '## Frequently Asked Questions' section out of the body."""
    m = re.search(r"^## Frequently Asked Questions\s*$", body, re.M)
    if not m:
        return body, []
    faq_md = body[m.end():]
    items = []
    for q, a in re.findall(r"^### (.+?)\n(.*?)(?=^### |\Z)", faq_md, re.S | re.M):
        a_html = markdown.markdown(a.strip())
        a_html = re.sub(r"^<p>|</p>$", "", a_html.strip())
        items.append((htmlmod.escape(q.strip()), a_html))
    return body[: m.start()].rstrip(), items


def link_ctas(h):
    """Turn assessment and call references in article text into real links."""
    repl = {
        "Brand Voice Quick Check": '<a href="assessments.html#brand-voice">Brand Voice Quick Check</a>',
        "AI Readiness Assessment": '<a href="assessments.html#ai-readiness">AI Readiness Assessment</a>',
        "Business Systems Assessment": '<a href="assessments.html#continuity">Business Systems Assessment</a>',
        "book a strategy call": f'<a href="{CALENDLY}" target="_blank" rel="noopener">book a strategy call</a>',
        "Brand Voice AI foundation session": '<a href="solutions.html#brand-voice-ai">Brand Voice AI foundation session</a>',
    }
    for k, v in repl.items():
        h = h.replace(k, v, 1)
    return h


def plain(s):
    return htmlmod.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def nice_date(d):
    return datetime.strptime(d, "%Y-%m-%d").strftime("%B %-d, %Y")


def post_url(slug):
    return f"{SITE}/blog/{slug}"


AUTHOR = {"@type": "Person", "@id": PERSON_ID, "name": "John M Pogue", "url": SITE + "/about",
          "jobTitle": "Founder & Creative Strategist", "sameAs": [LINKEDIN],
          "worksFor": {"@id": ORG_ID}}
PUBLISHER = {"@type": "Organization", "@id": ORG_ID, "name": "Pogue Digital Solutions, LLC", "url": SITE + "/",
             "logo": {"@type": "ImageObject", "url": SITE + "/img/logo-horizontal.png"}}

# ---------------- posts ----------------
posts = []
for path in glob.glob(f"{ART_DIR}/*.md"):
    meta, body = parse(path)
    body, faq_items = split_faq(body)
    md = markdown.Markdown(extensions=["toc"], extension_configs={"toc": {"toc_depth": "2"}})
    html_body = md.convert(body)
    toc = [(t["id"], t["name"]) for t in md.toc_tokens]

    short_answer = ""
    m = re.search(r"<p><strong>The short answer:</strong>(.*?)</p>", html_body, re.S)
    if m:
        short_answer = plain(m.group(1))
        lede_end = m.end()
        toc_html = ""
        if len(toc) >= 3:
            toc_html = '<nav class="article-toc" aria-label="In this article"><span class="eyebrow">In this article</span><ol>' + \
                "".join(f'<li><a href="#{i}">{n}</a></li>' for i, n in toc) + "</ol></nav>\n"
        html_body = html_body[:lede_end] + "\n" + toc_html + html_body[lede_end:]
        html_body = html_body.replace("<p><strong>The short answer:</strong>",
                                      '<p class="lede" id="short-answer"><strong>The short answer:</strong>', 1)
    html_body = link_ctas(html_body)
    words = len(re.findall(r"\w+", plain(html_body)))
    meta.update(short_answer=short_answer, words=words, faq=faq_items, toc=toc)
    posts.append((meta, html_body))

posts.sort(key=lambda p: (p[0]["date"], p[0]["title"]), reverse=True)

for idx, (meta, html_body) in enumerate(posts):
    slug, url = meta["slug"], post_url(meta["slug"])
    keywords = [k.strip() for k in meta.get("keywords", "").split(",") if k.strip()] or [meta["category"]]
    posting = {
        "@type": "BlogPosting", "@id": url + "#article", "headline": meta["title"],
        "description": meta["description"], "abstract": meta["short_answer"] or meta["description"],
        "author": AUTHOR, "publisher": PUBLISHER, "isPartOf": {"@id": BLOG_ID},
        "datePublished": meta["date"], "dateModified": meta["updated"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "url": url,
        "image": SITE + "/img/hero-founder-composite.jpg", "articleSection": meta["category"],
        "keywords": keywords, "wordCount": meta["words"], "inLanguage": "en-US",
        "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["h1", "#short-answer"]},
    }
    graph = [posting, {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": meta["title"], "item": url}]}]
    jsonld = [json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1)]
    faq_block = ""
    if meta["faq"]:
        jsonld.append(faq_jsonld(meta["faq"]))
        faq_block = f'''
<section class="on-paper-dim tight">
  <div class="wrap" style="max-width:760px;">
    <div class="section-head reveal"><span class="eyebrow">FAQ</span><h2 id="faq">Frequently Asked Questions</h2></div>
    {faq(meta["faq"])}
  </div>
</section>'''

    updated_line = f'<span>Updated {nice_date(meta["updated"])}</span>' if meta["updated"] != meta["date"] else ""
    extra = (f'<meta property="article:published_time" content="{meta["date"]}">\n'
             f'<meta property="article:modified_time" content="{meta["updated"]}">\n'
             f'<meta property="article:author" content="John M Pogue">\n'
             f'<meta property="article:section" content="{meta["category"]}">\n'
             f'<meta name="author" content="John M Pogue">\n')

    # one related post: the next one in the list, wrapping around
    rel = posts[(idx + 1) % len(posts)][0] if len(posts) > 1 else None
    related = f'''
<section class="tight">
  <div class="wrap" style="max-width:900px;">
    <div class="section-head reveal"><span class="eyebrow">Keep Reading</span></div>
    <div class="article-list reveal">
<a class="article-row" href="blog/{rel["slug"]}.html">
  <div><span class="card-eyebrow">{rel["category"]} &middot; {rel["reading_time"]}</span><h3>{rel["title"]}</h3><p>{rel["description"]}</p></div>
  <span class="go">READ &rarr;</span>
</a>
    </div>
  </div>
</section>''' if rel else ""

    page = head(f'{meta["title"]} | Pogue Digital Solutions Blog', meta["description"], f"blog/{slug}.html",
                jsonld=jsonld, og_type="article", extra_meta=extra) + header("blog/index.html") + f'''
<section class="on-ink tight" style="padding-top:56px; padding-bottom:64px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:820px;">
    <nav aria-label="Breadcrumb" class="crumbs"><a href="index.html">Home</a> / <a href="blog/index.html">Blog</a></nav>
    <span class="eyebrow" style="display:block; margin-top:22px;">{meta["category"]}</span>
    <h1 style="font-size:clamp(32px,4.6vw,54px); color:#fff; margin-top:14px;">{meta["title"]}</h1>
    <p style="font-size:17px; margin-top:18px; max-width:680px;">{meta["description"]}</p>
    <div class="article-meta" style="margin-top:28px;">
      <span class="article-byline"><img src="{PORTRAIT}" alt=""><strong>John M Pogue</strong></span>
      <span>Published <time datetime="{meta["date"]}">{nice_date(meta["date"])}</time></span>
      {updated_line}
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
{faq_block}
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
{related}
{cta_band("Put This to Work", "Find out where your business stands with a free assessment, or talk it through with John.", primary=("Take an Assessment", "assessments.html"))}
''' + footer()
    open(f"blog/{slug}.html", "w").write(page)
    print("blog/" + slug, len(page))


def row(meta):
    return f'''<a class="article-row" href="blog/{meta["slug"]}.html">
  <div><span class="card-eyebrow">{meta["category"]} &middot; {nice_date(meta["date"])} &middot; {meta["reading_time"]}</span><h3>{meta["title"]}</h3><p>{meta["description"]}</p></div>
  <span class="go">READ &rarr;</span>
</a>
'''

rows = "".join(row(m) for m, _ in posts)

# ---------------- blog/index.html ----------------
BLOG_LD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "Blog", "@id": BLOG_ID, "name": "Pogue Digital Solutions Blog", "url": SITE + "/blog/",
     "description": "Articles by John M Pogue on brand voice, AI adoption, automation, and capturing founder knowledge for small businesses.",
     "publisher": {"@id": ORG_ID}, "author": {"@id": PERSON_ID}, "inLanguage": "en-US",
     "blogPost": [{"@type": "BlogPosting", "@id": post_url(m["slug"]) + "#article", "headline": m["title"],
                   "url": post_url(m["slug"]), "datePublished": m["date"], "dateModified": m["updated"],
                   "author": {"@id": PERSON_ID}} for m, _ in posts]},
    json.loads(breadcrumb("Blog", "blog/"))]}, indent=1)

cats = sorted({m["category"] for m, _ in posts})
page = head("Blog | Brand Voice, AI, and Business Systems for Small Business",
            "The Pogue Digital Solutions blog. Plain answers from John M Pogue on brand voice, what to automate first, and getting a founder's knowledge into a system.",
            "blog/index.html", jsonld=[BLOG_LD]) + header("blog/index.html") + f'''
<section class="on-ink tight" style="padding-top:56px; padding-bottom:64px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:760px;">
    <span class="eyebrow">Blog</span>
    <h1 style="font-size:clamp(34px,5vw,60px); color:#fff; margin-top:16px;">Brand Voice, AI, and Business Systems for Small Business</h1>
    <p style="font-size:17px; max-width:620px; margin-top:18px;">Each article answers one question founders ask before they hire anyone. The answer comes first, then the reasoning and the examples behind it.</p>
    <p style="margin-top:22px; font-family:var(--font-mono); font-size:11.5px; letter-spacing:0.1em; text-transform:uppercase; color:rgba(255,255,255,0.6);">Topics: {" &middot; ".join(cats)}</p>
  </div>
</section>

<section>
  <div class="wrap" style="max-width:900px;">
    <div class="section-head reveal"><span class="eyebrow">Latest Articles</span><h2>Start with the question you have.</h2></div>
    <div class="article-list reveal">
{rows}    </div>
    <p class="reveal" style="margin-top:28px; font-size:14px;">Follow along with the <a href="blog/feed.xml" style="color:var(--gold-dim);">RSS feed</a>, or connect with John on <a href="{LINKEDIN}" target="_blank" rel="noopener" style="color:var(--gold-dim);">LinkedIn</a>.</p>
  </div>
</section>

{cta_band("Not Sure Where to Start?", "Take a free assessment and the result will point you to the right article, tool, or conversation.", primary=("Take an Assessment", "assessments.html"))}
''' + footer()
open("blog/index.html", "w").write(page)
print("blog/index.html", len(page))

# ---------------- blog/feed.xml ----------------
def rfc822(d):
    return format_datetime(datetime.strptime(d, "%Y-%m-%d").replace(hour=12, tzinfo=timezone.utc))

items = "".join(f'''  <item>
    <title>{htmlmod.escape(m["title"])}</title>
    <link>{post_url(m["slug"])}</link>
    <guid isPermaLink="true">{post_url(m["slug"])}</guid>
    <pubDate>{rfc822(m["date"])}</pubDate>
    <category>{htmlmod.escape(m["category"])}</category>
    <dc:creator>John M Pogue</dc:creator>
    <description>{htmlmod.escape(m["description"])}</description>
  </item>
''' for m, _ in posts)
feed = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
  <title>Pogue Digital Solutions Blog</title>
  <link>{SITE}/blog/</link>
  <atom:link href="{SITE}/blog/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Articles by John M Pogue on brand voice, AI adoption, automation, and capturing founder knowledge.</description>
  <language>en-us</language>
  <lastBuildDate>{rfc822(max(m["updated"] for m, _ in posts))}</lastBuildDate>
{items}</channel>
</rss>
'''
open("blog/feed.xml", "w").write(feed)
print("blog/feed.xml", len(feed))

# ---------------- resources.html ----------------
RES_LD = json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "CollectionPage", "name": "Resources", "url": SITE + "/resources",
     "description": "Articles and tools from Pogue Digital Solutions on brand voice, AI adoption, automation, and capturing founder knowledge.",
     "hasPart": [{"@id": post_url(m["slug"]) + "#article"} for m, _ in posts]},
    json.loads(breadcrumb("Resources", "resources"))]}, indent=1)

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
    <div class="section-head reveal"><span class="eyebrow">From the Blog</span><h2>Start here.</h2></div>
    <div class="article-list reveal">
{rows}    </div>
    <div class="reveal" style="margin-top:28px;"><a href="blog/index.html" class="btn btn-outline-navy">See all articles on the blog <span class="btn-arrow">&rarr;</span></a></div>
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
open("resources.html", "w").write(page)
print("resources.html", len(page))

# metadata for build_all.py (sitemap, llms.txt)
json.dump([{k: m[k] for k in ("title", "slug", "description", "category", "date", "updated", "short_answer")} for m, _ in posts],
          open(os.path.join(os.path.dirname(__file__), ".posts.json"), "w"), indent=1)
