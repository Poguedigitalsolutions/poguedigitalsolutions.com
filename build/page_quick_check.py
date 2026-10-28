"""Builds brand-voice-quick-check.html (/brand-voice-quick-check) and its thanks step
(/brand-voice-quick-check/thanks).

The quiz itself runs in js/quick-check.js. The score shows on the page right away. The optional
"email my results" form uses the ClickFunnels SDK like /subscribe: every quiz field rides along as a
hidden custom-attribute input, the SDK saves the contact, and ClickFunnels sends the visitor to the
next funnel step (the thanks page). The form only renders once CF_TOKEN_QUIZ is set in parts.py.
"""
import os
from parts import *

os.makedirs("brand-voice-quick-check", exist_ok=True)
LIVE = bool(CF_TOKEN_QUIZ)

FIELDS = (["quiz_score", "quiz_tier", "quiz_tier_summary", "quiz_next_step", "quiz_weakest_layer",
           "quiz_foundation", "quiz_playbooks", "quiz_execution"]
          + [f"q{i}_{k}" for i in range(1, 13) for k in ("answer", "note")])

STYLE = """<style>
.qc-wrap { max-width: 760px; margin: 0 auto; }
.qc-wrap [hidden] { display: none !important; }
.qc-card { background: var(--white); border: 1px solid var(--line-light); border-radius: var(--radius); padding: clamp(22px, 5vw, 44px); display: flex; flex-direction: column; gap: 20px; box-shadow: 0 24px 60px -32px rgba(6, 11, 20, 0.35); scroll-margin-top: 96px; }
.qc-card h2 { font-size: clamp(22px, 3.4vw, 30px); line-height: 1.25; }
.qc-card h3 { font-size: 19px; }
.qc-card p { margin: 0; }
.qc-meta { display: flex; flex-wrap: wrap; gap: 8px; }
.qc-chip { font-family: var(--font-mono); font-size: 11.5px; letter-spacing: 0.06em; text-transform: uppercase; padding: 5px 12px; border-radius: var(--radius-pill); background: var(--paper-dim); color: var(--ink); }
.qc-layers { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.qc-layer { border-top: 2px solid var(--gold); padding-top: 10px; }
.qc-layer b { display: block; font-family: var(--font-display); font-size: 17px; color: var(--ink); }
.qc-layer span { font-size: 14px; color: var(--charcoal-soft); }
.qc-actions { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }
.qc-small { font-size: 14px; color: var(--charcoal-soft); }
.qc-progress-top { display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 12px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--charcoal-soft); margin-bottom: 8px; }
.qc-bar { height: 6px; background: var(--paper-dim); border-radius: 99px; overflow: hidden; }
.qc-bar i { display: block; height: 100%; width: 0; background: var(--gold); transition: width .25s ease; }
.qc-options { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; }
.qc-opt { font: inherit; font-size: 14px; line-height: 1.25; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center; padding: 14px 6px; border-radius: var(--radius-sm); border: 1px solid var(--line-light); background: var(--white); color: var(--ink); }
.qc-opt:hover { border-color: var(--gold); }
.qc-opt[aria-pressed="true"] { border-color: var(--gold); background: rgba(212, 175, 55, 0.14); box-shadow: inset 0 -3px 0 var(--gold); }
.qc-num { font-family: var(--font-mono); font-size: 18px; }
.qc-nav { display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
.qc-btn { font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.06em; text-transform: uppercase; cursor: pointer; border-radius: var(--radius-pill); padding: 13px 24px; border: 1px solid var(--ink); background: transparent; color: var(--ink); }
.qc-btn:hover { background: var(--ink); color: var(--white); }
.qc-btn-primary { background: var(--ink); color: var(--white); }
.qc-btn-primary:hover { background: var(--navy); }
.qc-btn:disabled { opacity: .4; cursor: not-allowed; }
.qc-link { font: inherit; font-size: 14px; background: none; border: 0; padding: 4px 0; color: var(--charcoal-soft); text-decoration: underline; text-underline-offset: 3px; cursor: pointer; }
.qc-card button:focus-visible, .qc-card a:focus-visible, .qc-card input:focus-visible { outline: 3px solid var(--gold); outline-offset: 2px; }
.qc-head { display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 26px; align-items: center; }
.qc-gauge { width: 200px; max-width: 100%; }
.qc-score { font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.06em; text-transform: uppercase; color: var(--gold-dim); }
.qc-rows { display: flex; flex-direction: column; gap: 12px; }
.qc-row { display: grid; grid-template-columns: 110px minmax(0, 1fr) 54px; gap: 12px; align-items: center; font-size: 15px; }
.qc-row .qc-bar { height: 8px; }
.qc-n { font-family: var(--font-mono); text-align: right; color: var(--charcoal-soft); }
.qc-weak { background: var(--paper-dim); border-radius: var(--radius-sm); padding: 16px 18px; display: flex; flex-direction: column; gap: 6px; }
.qc-next { border-left: 3px solid var(--gold); padding-left: 16px; display: flex; flex-direction: column; gap: 10px; }
.qc-steps { margin: 0; padding-left: 22px; display: flex; flex-direction: column; gap: 8px; }
.qc-form { display: flex; flex-direction: column; gap: 12px; border-top: 1px solid var(--line-light); padding-top: 22px; }
.qc-fields { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.qc-form label { display: flex; flex-direction: column; gap: 4px; font-size: 14px; font-weight: 600; color: var(--ink); }
.qc-form input { font: inherit; font-weight: 400; padding: 11px 13px; border-radius: 10px; border: 1px solid var(--line-light); background: var(--paper); min-width: 0; }
@media (max-width: 640px) {
  .qc-layers, .qc-fields { grid-template-columns: 1fr; }
  .qc-options { grid-template-columns: 1fr; }
  .qc-opt { flex-direction: row; justify-content: flex-start; text-align: left; gap: 14px; padding: 12px 14px; font-size: 16px; }
  .qc-head { grid-template-columns: 1fr; justify-items: start; }
  .qc-row { grid-template-columns: 92px minmax(0, 1fr) 46px; }
}
@media (prefers-reduced-motion: reduce) { .qc-bar i, #qc-needle { transition: none !important; } }
</style>
"""

if LIVE:
    hidden = "\n".join(f'      <input type="hidden" name="{f}" data-qc-field="{f}" data-cf-element="custom-attribute:{f}">' for f in FIELDS)
    FORM = f'''<form class="qc-form" target="_top">
      <h3>Want a copy of your results?</h3>
      <p class="qc-small">Optional. Your score is already on this page. Leave your email and you&rsquo;ll get your full results, with a review of each answer and ideas to raise your score. No spam, and you can unsubscribe anytime. See the <a href="privacy.html#s3">Privacy Policy</a>.</p>
      <div class="qc-fields">
        <label>First name<input type="text" name="first_name" data-cf-element="first-name" autocomplete="given-name" required></label>
        <label>Email<input type="email" name="email" data-cf-element="email" autocomplete="email" required></label>
      </div>
{hidden}
      <div class="qc-actions"><button type="submit" class="btn btn-gold">Send my results <span class="btn-arrow">&rarr;</span></button></div>
    </form>'''
    COPY_STEP = "<li>Want the full picture? Get a copy of your results below. The email goes through each of your 12 answers with a short note on what it means and how to raise that score.</li>"
else:
    FORM = ""
    COPY_STEP = ""

QUIZ = f'''<div class="qc-wrap" id="qc">
  <div role="region" class="qc-card" id="qc-intro" aria-label="About the Quick Check">
    <span class="eyebrow">Free Assessment &middot; Brand Voice AI</span>
    <h2>Does your business sound like the same business everywhere it shows up?</h2>
    <p>This check looks at how much of what makes you <em>you</em> is written down, how your team uses it, and whether your AI tools can work from it.</p>
    <div class="qc-meta">
      <span class="qc-chip">12 statements</span>
      <span class="qc-chip">About 5 minutes</span>
      <span class="qc-chip">Free, no account</span>
      <span class="qc-chip">Score shown right away</span>
    </div>
    <div class="qc-layers" aria-label="What the check covers">
      <div class="qc-layer"><b>Foundation</b><span>Who you are, who you serve, and how you sound</span></div>
      <div class="qc-layer"><b>Playbooks</b><span>How that knowledge turns into everyday work</span></div>
      <div class="qc-layer"><b>Execution</b><span>How your team and AI tools put it to use</span></div>
    </div>
    <div class="qc-actions"><button class="btn btn-gold" id="qc-start" type="button">Start the Quick Check <span class="btn-arrow">&rarr;</span></button></div>
    <p class="qc-small">Rate each statement from 1 (Strongly disagree) to 5 (Strongly agree). Answer for how things are today, not how you want them to be.</p>
  </div>

  <div role="region" class="qc-card" id="qc-q" hidden aria-label="Quick Check statement">
    <div>
      <div class="qc-progress-top"><span id="qc-q-layer"></span><span id="qc-q-count"></span></div>
      <div class="qc-bar"><i id="qc-q-bar"></i></div>
    </div>
    <h2 id="qc-q-text"></h2>
    <p class="qc-small" id="qc-q-hint" hidden></p>
    <div class="qc-options" id="qc-q-options" role="group" aria-labelledby="qc-q-text"></div>
    <div class="qc-nav">
      <button class="qc-btn" id="qc-back" type="button">Back</button>
      <button class="qc-btn qc-btn-primary" id="qc-next" type="button" disabled>Next</button>
    </div>
  </div>

  <div role="region" class="qc-card" id="qc-result" hidden aria-label="Your Quick Check result">
    <span class="eyebrow">Your Result</span>
    <div class="qc-head">
      <svg class="qc-gauge" viewBox="0 0 200 124" role="img" aria-label="Score gauge from 12 to 60">
        <path d="M 20 104 A 80 80 0 0 1 180 104" fill="none" stroke="#F1ECDF" stroke-width="14" stroke-linecap="round"/>
        <path id="qc-arc" d="M 20 104 A 80 80 0 0 1 180 104" fill="none" stroke="#D4AF37" stroke-width="14" stroke-linecap="round" pathLength="100" stroke-dasharray="0 100"/>
        <g id="qc-needle" style="transform-origin:100px 104px; transition: transform .6s ease;"><polygon points="100,34 95,104 105,104" fill="#060B14"/></g>
        <circle cx="100" cy="104" r="8" fill="#D4AF37"/>
        <text x="20" y="122" font-size="11" text-anchor="middle" fill="#58564D" font-family="IBM Plex Mono, monospace">12</text>
        <text x="180" y="122" font-size="11" text-anchor="middle" fill="#58564D" font-family="IBM Plex Mono, monospace">60</text>
      </svg>
      <div style="display:flex; flex-direction:column; gap:8px; min-width:0;">
        <span class="qc-score" id="qc-r-score"></span>
        <h2 id="qc-r-title"></h2>
        <p id="qc-r-diag"></p>
      </div>
    </div>
    <div class="qc-rows" aria-label="Score by layer"><h3>By layer</h3><div class="qc-rows" id="qc-r-rows"></div></div>
    <div class="qc-weak" id="qc-r-weak"></div>
    <div class="qc-next">
      <h3>Your next step</h3>
      <p id="qc-r-next"></p>
      <div class="qc-actions">
        <a class="btn btn-gold" href="{CALENDLY}" target="_blank" rel="noopener">Book a Strategy Call <span class="btn-arrow">&rarr;</span></a>
        <a class="btn btn-outline-navy" href="solutions.html#brand-voice-ai" id="qc-r-cta2">See how Brand Voice AI works</a>
      </div>
    </div>
    <div class="qc-next">
      <h3>Follow-up and next steps</h3>
      <ol class="qc-steps">
        <li>Pick one tip from this page and try it this week. Small changes add up faster than a big rewrite.</li>
        {COPY_STEP}
        <li>Book a Strategy Call with John M Pogue to walk through your score and decide what to fix first.</li>
        <li>Take the Quick Check again in 90 days to see how far you&rsquo;ve come.</li>
      </ol>
    </div>
    {FORM}
    <div class="qc-actions"><button class="qc-link" id="qc-retake" type="button">Retake the Quick Check</button></div>
  </div>
</div>'''

DESC = "Take the free Brand Voice Quick Check: 12 statements, about 5 minutes, and a score out of 60 that shows whether your business sounds the same across people, platforms, and AI tools."
page = head("Brand Voice Quick Check | Free 5-Minute Assessment", DESC, "brand-voice-quick-check.html",
            jsonld=[breadcrumb("Brand Voice Quick Check", "brand-voice-quick-check.html")],
            extra_meta=STYLE + cf_meta(CF_TOKEN_QUIZ)) + header("assessments.html") + f'''
<section class="on-ink tight" style="padding-top:56px; padding-bottom:64px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:760px;">
    <nav aria-label="Breadcrumb" class="crumbs"><a href="index.html">Home</a> / <a href="assessments.html">Assessments</a></nav>
    <span class="eyebrow" style="display:block; margin-top:22px;">5 min &middot; Free</span>
    <h1 style="font-size:clamp(34px,5vw,56px); color:#fff; margin-top:14px;">Brand Voice Quick Check</h1>
    <p style="font-size:17px; max-width:620px; margin-top:18px;">Find out whether your business has enough clarity and documentation to communicate consistently across people, platforms, and AI tools.</p>
  </div>
</section>

<section class="on-paper-dim" style="padding-top:56px; padding-bottom:88px;">
  <div class="wrap">
{QUIZ}
  </div>
</section>
''' + footer().replace("</body>", f'<script src="js/quick-check.js?v={ASSET_VER}"></script>\n' + cf_script(CF_TOKEN_QUIZ) + "</body>")
open("brand-voice-quick-check.html", "w").write(page)
print("brand-voice-quick-check.html", len(page))

# ---------------- thanks ----------------
THANKS = f'''<div class="qc-wrap"><div class="qc-card">
  <span class="eyebrow">Results on the way</span>
  <h2>Thanks. Check your inbox for your full results.</h2>
  <p>Your email goes through each of your 12 answers, with a short note on what it means and one idea to raise that score. If you don&rsquo;t see it in a few minutes, check your promotions or spam folder and mark it as safe.</p>
  <div class="qc-actions">
    <a href="{CALENDLY}" class="btn btn-gold" target="_blank" rel="noopener">Book a Strategy Call <span class="btn-arrow">&rarr;</span></a>
    <a href="assessments.html" class="btn btn-outline-navy">See all assessments</a>
  </div>
</div></div>'''

page = head("Your Quick Check Results Are on the Way | Pogue Digital Solutions", "Your Brand Voice Quick Check results are on the way to your inbox.",
            "brand-voice-quick-check/thanks.html", extra_meta=STYLE + cf_meta(CF_TOKEN_QUIZ_THANKS), indexable=False) + header("assessments.html") + f'''
<section class="on-paper-dim" style="padding-top:72px; padding-bottom:96px;">
  <div class="wrap">
{THANKS}
  </div>
</section>
''' + footer().replace("</body>", cf_script(CF_TOKEN_QUIZ_THANKS) + "</body>")
open("brand-voice-quick-check/thanks.html", "w").write(page)
print("brand-voice-quick-check/thanks.html", len(page))
