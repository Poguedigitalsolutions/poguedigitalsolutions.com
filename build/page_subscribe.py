"""Builds subscribe.html (/subscribe) and subscribe/thanks.html (/subscribe/thanks).

/subscribe is the one page registered in ClickFunnels as an External page. It works two ways:
  - opened directly, it is a normal page with the site header and footer;
  - framed by the blog (see parts.subscribe_embed), EMBED_DETECT adds the "embedded" class and
    CSS hides everything except the signup card.
The ClickFunnels SDK finds fields by their data-cf-element attribute, intercepts the submit,
saves the contact, and sends the visitor to the next funnel step (/subscribe/thanks).
"""
import json, os
from parts import *

os.makedirs("subscribe", exist_ok=True)
posts = json.load(open(os.path.join(os.path.dirname(__file__), ".posts.json")))

LIVE = bool(CF_TOKEN_SUBSCRIBE)

if LIVE:
    form = '''<form class="sub-form" target="_top">
      <label class="sub-field"><span>First name</span>
        <input type="text" name="first_name" data-cf-element="first-name" autocomplete="given-name" required></label>
      <label class="sub-field"><span>Email</span>
        <input type="email" name="email" data-cf-element="email" autocomplete="email" required></label>
      <button type="submit" class="btn btn-gold sub-btn">Subscribe <span class="btn-arrow">&rarr;</span></button>
    </form>'''
else:
    form = '''<p class="sub-soon">Email signups open soon. Until then, follow along with the <a href="blog/feed.xml" target="_top">RSS feed</a>.</p>'''

CARD = f'''<div class="sub-card">
  <span class="eyebrow">Get New Articles</span>
  <h2 class="sub-title">New articles, sent to your inbox.</h2>
  <p class="sub-copy">When John M Pogue publishes a new piece on brand voice, AI, or business systems, you get it by email. No spam, and you can unsubscribe any time.</p>
  {form}
  <p class="sub-fine">We use your name and email only to send blog updates. See the <a href="privacy.html#s3" target="_top">Privacy Policy</a>.</p>
</div>'''

latest = "".join(f'<li><a href="blog/{p["slug"]}.html" target="_top">{p["title"]}</a></li>' for p in posts[:3])

DESC = "Subscribe to the Pogue Digital Solutions blog and get new articles from John M Pogue on brand voice, AI, and business systems by email."
page = head("Subscribe | Pogue Digital Solutions Blog", DESC, "subscribe.html",
            extra_meta=EMBED_DETECT + cf_meta(CF_TOKEN_SUBSCRIBE)) + header("blog/index.html") + f'''
<section class="on-ink tight sub-hero" style="padding-top:56px; padding-bottom:64px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:760px;">
    <nav aria-label="Breadcrumb" class="crumbs"><a href="index.html">Home</a> / <a href="blog/index.html">Blog</a></nav>
    <span class="eyebrow" style="display:block; margin-top:22px;">Subscribe</span>
    <h1 style="font-size:clamp(34px,5vw,56px); color:#fff; margin-top:14px;">Subscribe to the Pogue Digital Solutions Blog</h1>
    <p style="font-size:17px; max-width:620px; margin-top:18px;">Plain answers for founders on brand voice, what to automate first, and getting the knowledge out of your head and into a system.</p>
  </div>
</section>

<section class="sub-main">
  <div class="wrap" style="max-width:760px;">
    <div class="sub-root">
{CARD}
    </div>
    <div class="sub-latest reveal">
      <span class="eyebrow">Recent articles</span>
      <ul>{latest}</ul>
    </div>
  </div>
</section>
''' + footer().replace("</body>", cf_script(CF_TOKEN_SUBSCRIBE) + "</body>")
open("subscribe.html", "w").write(page)
print("subscribe.html", len(page))

# ---------------- thanks ----------------
THANKS = f'''<div class="sub-card">
  <span class="eyebrow">You&rsquo;re subscribed</span>
  <h2 class="sub-title">Thanks for signing up.</h2>
  <p class="sub-copy">New articles will land in your inbox when they publish. If you don&rsquo;t see the first one, check your promotions or spam folder and mark it as safe.</p>
  <a href="blog/index.html" target="_top" class="btn btn-outline-gold">Back to the blog <span class="btn-arrow">&rarr;</span></a>
</div>'''

page = head("Thanks for Subscribing | Pogue Digital Solutions", "You are subscribed to the Pogue Digital Solutions blog.",
            "subscribe/thanks.html", extra_meta=EMBED_DETECT + cf_meta(CF_TOKEN_THANKS), indexable=False) + header("blog/index.html") + f'''
<section class="sub-main" style="padding-top:72px;">
  <div class="wrap" style="max-width:760px;">
    <div class="sub-root">
{THANKS}
    </div>
  </div>
</section>
''' + footer().replace("</body>", cf_script(CF_TOKEN_THANKS) + "</body>")
open("subscribe/thanks.html", "w").write(page)
print("subscribe/thanks.html", len(page))
