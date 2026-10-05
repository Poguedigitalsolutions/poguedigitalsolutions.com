"""One command rebuilds the whole site:  python3 build/build_all.py  (run from the repo root)

1. Runs every page_*.py script.
2. Rewrites internal links to root-relative clean URLs (/about, /blog/slug) so pages work
   from any folder depth and never link through a Cloudflare .html redirect.
3. Writes sitemap.xml, robots.txt, llms.txt, and llms-full.txt from what was built.
"""
import glob, json, os, re, subprocess, sys, time, html as htmlmod

ROOT = os.getcwd()
BUILD = os.path.join(ROOT, "build")
sys.path.insert(0, BUILD)
from parts import SITE, CALENDLY, EMAIL, LINKEDIN, clean_path

TODAY = time.strftime("%Y-%m-%d")

# ---- 1. build pages ----
for script in sorted(glob.glob(os.path.join(BUILD, "page_*.py"))):
    subprocess.run([sys.executable, script], check=True, cwd=ROOT)

# ---- 2. link rewrite ----
SKIP = re.compile(r"^(https?:|mailto:|tel:|#|data:|//|javascript:)")

def clean_ref(ref):
    if SKIP.match(ref):
        return ref
    path, rest = re.match(r"([^#?]*)(.*)", ref).groups()
    path = path.lstrip("/")
    path = clean_path(path) if (path.endswith(".html") or path == "") else "/" + path
    return path + rest

def rewrite(html):
    html = re.sub(r'(\b(?:href|src)=")([^"]*)(")', lambda m: m.group(1) + clean_ref(m.group(2)) + m.group(3), html)
    # absolute URLs in canonical, og:url, and JSON-LD
    html = re.sub(re.escape(SITE) + r"/([\w/-]*?)index\.html", lambda m: SITE + "/" + m.group(1), html)
    html = re.sub(re.escape(SITE) + r"/([\w/-]+)\.html", lambda m: SITE + "/" + m.group(1), html)
    return html

pages = sorted(glob.glob("*.html") + glob.glob("blog/*.html"))
for p in pages:
    src = open(p).read()
    open(p, "w").write(rewrite(src))

# ---- collect page metadata ----
def meta_of(p):
    s = open(p).read()
    title = re.search(r"<title>(.*?)</title>", s).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', s).group(1)
    return htmlmod.unescape(title), htmlmod.unescape(desc), "noindex" not in s

posts = json.load(open(os.path.join(BUILD, ".posts.json")))
post_dates = {f"blog/{p['slug']}.html": p["updated"] for p in posts}

# ---- 3a. sitemap.xml ----
PRIORITY = {"index.html": "1.0", "blog/index.html": "0.9", "solutions.html": "0.9", "assessments.html": "0.9",
            "compass-method.html": "0.9", "government.html": "0.9", "resources.html": "0.7"}
urls = ""
for p in pages:
    title, desc, indexable = meta_of(p)
    if not indexable:
        continue
    urls += (f'  <url><loc>{SITE}{clean_path(p)}</loc><lastmod>{post_dates.get(p, TODAY)}</lastmod>'
             f'<priority>{PRIORITY.get(p, "0.8")}</priority></url>\n')
open("sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

# ---- 3b. robots.txt ----
# Oct 5, 2026: John wants every AI engine to read the site, so training crawlers (GPTBot, ClaudeBot,
# Google-Extended, etc.) are allowed alongside the search/answer crawlers. Nothing is blocked.
AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
           "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "Meta-ExternalAgent",
           "Amazonbot", "MistralAI-User", "DuckAssistBot", "CCBot", "cohere-ai"]
SEARCH_BOTS = ["Googlebot", "Bingbot", "Applebot", "DuckDuckBot"]
robots = "# Pogue Digital Solutions, LLC\n# Search engines and AI engines are welcome to read, cite, and learn from this site.\n# Summary for language models: /llms.txt (full text: /llms-full.txt)\n\n"
robots += "User-agent: *\nAllow: /\n\n"
robots += "".join(f"User-agent: {b}\n" for b in SEARCH_BOTS + AI_BOTS) + "Allow: /\n\n"
robots += f"Sitemap: {SITE}/sitemap.xml\n"
open("robots.txt", "w").write(robots)

# ---- 3c. llms.txt and llms-full.txt ----
def line(p):
    title, desc, _ = meta_of(p)
    name = title.split(" | ")[0]
    return f"- [{name}]({SITE}{clean_path(p)}): {desc}\n"

FACTS = f"""## Key facts

- Legal name: Pogue Digital Solutions, LLC
- Founder: John M Pogue, Founder and Creative Strategist. Navy veteran and former Hospital Corpsman. M.S. in Digital Marketing, Full Sail University. B.A. in Visual Communication.
- Location: Conroe, Texas. Serves Greater Houston and clients nationwide.
- Status: Veteran-owned, founder-led small business
- Core offers: Brand Voice AI (an AI-assisted business operating system that captures a company's knowledge, voice, and standards), AI and automation, digital strategy, training and workshops, government and organizational services
- Method: The Compass Method (Purpose, Skill, Opportunity, Service, with Heart at the center)
- Government: SAM.gov registered. UEI Y6S7ZHLJH5V6, CAGE 219K1. Primary NAICS 541613.
- Book a call: {CALENDLY}
- Email: {EMAIL}
- LinkedIn: {LINKEDIN}
"""

core = ["index.html", "solutions.html", "assessments.html", "compass-method.html", "government.html", "about.html", "contact.html"]
llms = f"""# Pogue Digital Solutions, LLC

> Pogue Digital Solutions is a veteran-owned digital strategy and AI systems consultancy in Conroe, Texas, founded by John M Pogue. It helps founder-led businesses and organizations organize their knowledge, clarify their brand voice, and build practical AI-assisted marketing and business systems, with a human approving the work.

{FACTS}
## Main pages

{"".join(line(p) for p in core if os.path.exists(p))}
## Blog

Each article opens with a short, direct answer to the question in its title.

{"".join(f"- [{p['title']}]({SITE}/blog/{p['slug']}): {p['short_answer'] or p['description']}" + chr(10) for p in posts)}
## Optional

- [Blog index]({SITE}/blog/)
- [Resources]({SITE}/resources)
- [Full text of every article]({SITE}/llms-full.txt)
"""
open("llms.txt", "w").write(llms)

full = f"# Pogue Digital Solutions, LLC: full article text\n\nSource: {SITE}. Author of all articles: John M Pogue.\n\n{FACTS}\n"
for p in posts:
    raw = open(os.path.join(BUILD, "articles", p["slug"] + ".md")).read().split("---", 2)[2].strip()
    raw = re.sub(r"^# .*\n", "", raw, count=1).strip()
    full += f"\n---\n\n# {p['title']}\n\nURL: {SITE}/blog/{p['slug']}\nPublished: {p['date']}  Updated: {p['updated']}  Topic: {p['category']}\n\n{raw}\n"
open("llms-full.txt", "w").write(full)

print(f"built {len(pages)} pages, sitemap, robots.txt, llms.txt ({len(llms)} chars), llms-full.txt ({len(full)} chars)")
