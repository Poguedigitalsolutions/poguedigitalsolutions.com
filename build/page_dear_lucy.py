"""Dear Lucy share page: the trophy image that goes with John's YouTube Short.
Unlisted (noindex, kept out of the sitemap). Share the link /dear-lucy directly."""
from parts import *

SHORT = "https://www.youtube.com/shorts/xo-7GRiKqTs"

BODY = f'''<section class="on-ink tight" style="padding-top:56px; padding-bottom:56px;">
  <div class="wrap" style="max-width:960px;">
    <span class="eyebrow">Dear Lucy's Comedy Corner</span>
    <h1 style="font-size:clamp(30px,4.6vw,48px); margin-top:14px;">The Parenting Trophy Shelf</h1>
    <blockquote style="margin:26px 0 0; padding:18px 22px; border-left:4px solid var(--gold); background:rgba(255,255,255,0.04);">
      <p style="margin:0; font-family:var(--font-display); font-style:italic; font-size:clamp(20px,3vw,27px); line-height:1.4; color:#fff;">Dear Lucy, is it good or bad to refer to your kids as &#x1F986; trophies?</p>
    </blockquote>
  </div>
</section>
<section class="tight">
  <div class="wrap" style="max-width:960px;">
    <figure style="margin:0;">
      <img src="img/dear-lucy-trophies.jpg" width="1376" height="768" loading="eager" style="width:100%; height:auto; display:block; border-radius:6px;" alt="Two joke trophies on a shelf. The gold one reads The Ultimate Accomplishment: Proved We Can Have Kids. The silver one reads Greatest Genetic Merge Champion. A cardboard sign says Dear Lucy's Comedy Corner.">
      <figcaption style="margin-top:12px; font-size:14px;">Companion image for the YouTube Short.</figcaption>
    </figure>
    <div style="margin-top:28px;">
      <a href="{SHORT}" class="btn btn-gold" target="_blank" rel="noopener">Watch the Short on YouTube <span class="btn-arrow">&rarr;</span></a>
    </div>
  </div>
</section>
'''

page = head("Dear Lucy: The Parenting Trophy Shelf | Pogue Digital Solutions",
            "Dear Lucy, is it good or bad to refer to your kids as duck trophies? The companion image for the YouTube Short.",
            "dear-lucy.html", og_image="img/dear-lucy-trophies.jpg", indexable=False) + header("") + BODY + footer()
open("dear-lucy.html", "w").write(page)
print("dear-lucy.html", len(page))
