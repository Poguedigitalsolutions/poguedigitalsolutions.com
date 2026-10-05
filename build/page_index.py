import re, json
from parts import *

src = open("/home/claude/site-build/legacy/index.html").read()

# ---- body between old header and old footer ----
body = src.split("</header>", 1)[1].split("<footer", 1)[0]

def rep(old, new, count=1):
    global body
    assert body.count(old) >= 1, f"MISSING: {old[:80]}"
    body = body.replace(old, new, count)

# Hero: remove ghosted texture artwork, add compass backdrop + real portrait
rep("""  <div style="position:absolute; inset:0; z-index:0;">
    <img src="img/hero-bg-texture.jpg" alt="" style="width:100%; height:100%; object-fit:cover; opacity:0.6;">
    <div style="position:absolute; inset:0; background:linear-gradient(175deg, rgba(6,11,20,0.25) 0%, rgba(6,11,20,0.92) 88%);"></div>
  </div>
""", """  <div style="position:absolute; inset:0; z-index:0; background:radial-gradient(ellipse at 20% 30%, rgba(15,37,68,0.9), rgba(6,11,20,0) 60%);"></div>
""")
rep('''  <div class="glow-blob" style="width:560px; height:560px; background:radial-gradient(circle, rgba(212,175,55,0.26), transparent 70%); top:-200px; right:-140px;"></div>
  <div class="glow-blob" style="width:440px; height:440px; background:radial-gradient(circle, rgba(15,37,68,0.7), transparent 70%); bottom:-180px; left:-120px;"></div>
''', f'''  {compass_svg()}
  <div class="glow-blob" style="width:440px; height:440px; background:radial-gradient(circle, rgba(15,37,68,0.7), transparent 70%); bottom:-180px; left:-120px;"></div>
''')
start = body.index('    <div class="reveal" style="display:flex; justify-content:center;">\n      <div style="width:100%; max-width:280px;')
end = body.index('</section>', start)
body = body[:start] + "    " + hero_portrait("Navy Veteran &middot; Founder &amp; Creative Strategist") + "\n  </div>\n" + body[end:]

# Em dashes -> plain punctuation (John's standing copy rule)
rep("communication standards &mdash; giving your team and AI tools a shared foundation while keeping human approval at the center.",
    "communication standards. It gives your team and AI tools a shared foundation while keeping human approval at the center.")
rep("adopting AI and digital systems &mdash; not just a tool demo, but how to use it responsibly inside real work.",
    "adopting AI and digital systems. The goal is to show people how to use the tools responsibly inside real work.")
rep("defines your business &mdash; your mission, values, offers, audience, stories, processes, tone, customer journey, and approval standards &mdash; then uses that foundation",
    "defines your business: your mission, values, offers, audience, stories, processes, tone, customer journey, and approval standards. It then uses that foundation")
rep("to strategy, communication, and technology &mdash; and believes", "to strategy, communication, and technology. He believes")
rep("Meet John M. Pogue", "Meet John M Pogue", 2)

# Unbuilt destinations: no dead links
rep('<a href="#compass" class="btn btn-outline-navy" style="margin-top:22px;">Explore The Compass Method <span class="btn-arrow">&rarr;</span></a>',
    '<a href="assessments.html#compass" class="btn btn-outline-navy" style="margin-top:22px;">Take the Compass Assessment <span class="btn-arrow">&rarr;</span></a>')
rep('<div class="reveal" style="margin-top:28px;"><a href="#resources" class="btn btn-outline-navy">Visit the Resource Center <span class="btn-arrow">&rarr;</span></a></div>',
    '<div class="reveal" style="margin-top:28px;"><a href="resources.html" class="btn btn-outline-navy">Visit the Resource Center <span class="btn-arrow">&rarr;</span></a></div>')
rep('<div class="card"><span class="card-eyebrow">Article</span><h3 style="font-size:16.5px;">What Is Brand Voice AI?</h3>', '<a href="what-is-brand-voice-ai.html" class="card" style="text-decoration:none;"><span class="card-eyebrow">Article</span><h3 style="font-size:16.5px;">What Is Brand Voice AI?</h3>')
rep('so people and AI communicate consistently.</p></div>', 'so people and AI communicate consistently.</p></a>')
rep('<div class="card"><span class="card-eyebrow">Article</span><h3 style="font-size:16.5px;">What Should a Small Business Automate First?</h3>', '<a href="what-should-a-small-business-automate-first.html" class="card" style="text-decoration:none;"><span class="card-eyebrow">Article</span><h3 style="font-size:16.5px;">What Should a Small Business Automate First?</h3>')
rep('without buying unnecessary software.</p></div>', 'without buying unnecessary software.</p></a>')
rep('<div class="card"><span class="card-eyebrow">Article</span><h3 style="font-size:16.5px;">How Do You Capture the Knowledge Inside a Founder&rsquo;s Head?</h3>', '<a href="how-do-you-capture-the-knowledge-inside-a-founders-head.html" class="card" style="text-decoration:none;"><span class="card-eyebrow">Article</span><h3 style="font-size:16.5px;">How Do You Capture the Knowledge Inside a Founder&rsquo;s Head?</h3>')
rep('into a usable resource.</p></div>', 'into a usable resource.</p></a>')
rep('<a href="#case-studies" class="btn btn-outline-gold" style="margin-top:22px;">View Case Studies <span class="btn-arrow">&rarr;</span></a>',
    '<a href="about.html" class="btn btn-outline-gold" style="margin-top:22px;">Read the Story Behind It <span class="btn-arrow">&rarr;</span></a>')
rep('<a href="#contact" class="btn btn-outline-gold">Schedule a Strategy Conversation</a>',
    f'<a href="{CALENDLY}" class="btn btn-outline-gold" target="_blank" rel="noopener">Schedule a Strategy Conversation</a>')

# Solutions: four equal cards instead of an uneven bento
rep('<div class="bento reveal">\n      <div class="card span-2">\n        <h3>Brand Voice AI</h3>', '<div class="grid-2 reveal">\n      <div class="card">\n        <h3>Brand Voice AI</h3>')
rep('<div class="card span-2">\n        <h3>Training and Workshops</h3>', '<div class="card">\n        <h3>Training and Workshops</h3>')
rep('<a href="solutions.html" class="btn btn-outline-navy" style="margin-top:16px;">Explore AI and Automation', '<a href="solutions.html#ai-automation" class="btn btn-outline-navy" style="margin-top:16px;">Explore AI and Automation')
rep('<a href="solutions.html" class="btn btn-outline-navy" style="margin-top:16px;">Explore Digital Strategy', '<a href="solutions.html#digital-strategy" class="btn btn-outline-navy" style="margin-top:16px;">Explore Digital Strategy')
rep('<a href="solutions.html" class="btn btn-outline-navy" style="margin-top:20px;">View Training Options', '<a href="solutions.html#training" class="btn btn-outline-navy" style="margin-top:20px;">View Training Options')

# Assessment cards link to the assessment anchors
for label, anchor in [("Check Your Brand Voice","brand-voice"),("Measure Your AI Readiness","ai-readiness"),("Review Your Systems","continuity"),("Find Your Bearing","compass")]:
    rep(f'<a href="assessments.html" class="btn btn-outline-navy" style="margin-top:14px; font-size:11px; padding:10px 16px;">{label}</a>',
        f'<a href="assessments.html#{anchor}" class="btn btn-outline-navy" style="margin-top:14px; font-size:11px; padding:10px 16px;">{label}</a>')

# FAQ list -> accordion
faq_start = body.index('<div class="reveal" style="display:flex; flex-direction:column;">\n      <div style="padding:20px 0;">')
faq_end = body.index('</section>', faq_start)
faq_html = body[faq_start:faq_end]
pairs = re.findall(r'<h3[^>]*>(.*?)</h3><p[^>]*>(.*?)</p>', faq_html, re.S)
body = body[:faq_start] + faq(pairs) + "\n  </div>\n" + body[faq_end:]

# ---- JSON-LD from old head, with name fix ----
blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
blocks = [b.strip().replace("John M. Pogue", "John M Pogue") for b in blocks]
org = json.loads(blocks[0]); org["sameAs"] = [LINKEDIN]; org["email"] = EMAIL
org["founder"]["url"] = SITE + "/about.html"
blocks[0] = json.dumps(org, indent=1)

html = head("Pogue Digital Solutions | AI Strategy, Brand Voice & Business Systems",
            "Pogue Digital Solutions, LLC helps founder-led businesses organize their knowledge, clarify their brand voice, and build practical AI-assisted marketing and business systems.",
            "index.html", jsonld=blocks) + header("index.html") + body + footer()
open("./index.html", "w").write(html)
print("index.html", len(html))
