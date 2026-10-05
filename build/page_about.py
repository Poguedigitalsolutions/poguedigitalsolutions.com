import json
from parts import *

PERSON = json.dumps({"@context": "https://schema.org", "@graph": [
 {"@type": "Person", "name": "John M Pogue", "url": SITE + "/about.html", "jobTitle": "Founder & Creative Strategist",
  "worksFor": {"@type": "Organization", "name": "Pogue Digital Solutions, LLC", "url": SITE + "/"},
  "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Full Sail University"}],
  "sameAs": [LINKEDIN], "email": EMAIL,
  "description": "John M Pogue is the Founder and Creative Strategist of Pogue Digital Solutions, LLC. He is a Navy veteran and former Hospital Corpsman who holds a Master of Science in Digital Marketing from Full Sail University and a bachelor's degree in Visual Communication. His work focuses on AI-assisted business systems, brand voice, digital strategy, customer communication, training, and practical technology adoption.",
  "knowsAbout": ["AI-assisted business systems", "Brand voice strategy", "Digital marketing strategy", "Customer journey mapping", "Visual communication", "Veteran entrepreneurship", "The Compass Method"]},
 json.loads(breadcrumb("About John M Pogue", "about.html"))]}, indent=1)

html = head("About John M Pogue | Navy Veteran, Founder, Creative Strategist",
  "John M Pogue is the Founder and Creative Strategist of Pogue Digital Solutions, LLC: a Navy veteran and former Hospital Corpsman with an M.S. in Digital Marketing from Full Sail University.",
  "about.html", jsonld=[PERSON]) + header("about.html") + f'''

<!-- HERO -->
<section class="on-ink tight" style="padding-top:56px; padding-bottom:88px;">
  {compass_svg()}
  <div class="glow-blob" style="width:420px; height:420px; background:radial-gradient(circle, rgba(15,37,68,0.7), transparent 70%); bottom:-160px; left:-120px;"></div>
  <div class="wrap" style="display:grid; grid-template-columns:1.2fr 0.8fr; gap:56px; align-items:center;">
    <div class="reveal">
      <span class="eyebrow">About John M Pogue</span>
      <h1 style="font-size:clamp(36px,5.6vw,66px); margin-top:18px; color:#fff;">Diagnose first.<br>Then treat what&rsquo;s <em>actually</em> wrong.</h1>
      <p style="font-size:17px; max-width:520px; margin-top:22px;">That is what the Navy taught me. It turns out it is also the only way to fix a business.</p>
      <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:28px;">
        <span class="pill">U.S. Navy &middot; Hospital Corpsman</span>
        <span class="pill">M.S. Digital Marketing, Full Sail University</span>
        <span class="pill">B.A. Visual Communication</span>
        <span class="pill">Founder &amp; Creative Strategist</span>
        <span class="pill">Veteran-Owned Business</span>
      </div>
      <div style="display:flex; gap:16px; margin-top:32px; flex-wrap:wrap;">
        <a href="{CALENDLY}" class="btn btn-gold" target="_blank" rel="noopener">Book a Strategy Call <span class="btn-arrow">&rarr;</span></a>
        <a href="assessments.html" class="btn btn-outline-gold">Take an Assessment</a>
      </div>
      <div class="bearing" style="margin-top:48px; max-width:460px;">
        <span class="bearing-label">U.S. NAVY</span><div class="bearing-rule"></div><span class="bearing-label">FOUNDER &amp; STRATEGIST</span>
      </div>
    </div>
    {hero_portrait("Navy Veteran &middot; Hospital Corpsman")}
  </div>
</section>

<!-- STORY -->
<section>
  <div class="wrap" style="max-width:760px;">
    <p class="reveal" style="font-family:var(--font-display); font-style:italic; font-size:clamp(22px,2.6vw,30px); color:var(--ink); line-height:1.3; margin-bottom:32px;">Before John M Pogue built businesses, he kept people alive.</p>
    <div class="reveal stack-lg" style="font-size:17px; line-height:1.75;">
      <p>He spent his early career as a U.S. Navy Hospital Corpsman, trained to stay level-headed under pressure, diagnose accurately before treating, and act the moment it mattered. Those instincts did not fade when he left the service. They became the lens for everything he has built since.</p>
      <p>After the Navy, John earned a bachelor&rsquo;s degree in Visual Communication and later a Master of Science in Digital Marketing from Full Sail University, pairing that same diagnose-first instinct with a formal grounding in visual storytelling, customer psychology, and the emerging role of AI in how businesses operate. He founded Pogue Digital Solutions, LLC to bring it all together: the discipline of a corpsman and the creativity of a strategist.</p>
      <p>His work today focuses on AI-assisted business systems, brand voice, digital strategy, customer communication, training, and practical technology adoption. He believes the most valuable knowledge inside a business often lives in the experiences, stories, and judgment of the people doing the work, and his mission is to capture that knowledge and turn it into systems that create greater clarity, confidence, consistency, and freedom.</p>
      <p>It is why <strong>Clarify</strong> comes before <strong>Diagnose</strong>, and <strong>Diagnose</strong> comes before <strong>Build</strong>, in every engagement Pogue Digital Solutions takes on. You do not treat what you have not looked at first.</p>
    </div>
  </div>
</section>

<!-- PULL QUOTE -->
<section class="on-paper-dim tight">
  <div class="wrap reveal center" style="max-width:720px; text-align:center;">
    <p style="font-family:var(--font-display); font-style:italic; font-size:clamp(22px,3vw,34px); color:var(--ink); line-height:1.3;">&ldquo;Helping people understand themselves and the systems around them so they can live and work with greater freedom, confidence, purpose, and humanity.&rdquo;</p>
  </div>
</section>

<!-- EXPERTISE -->
<section class="on-ink">
  <div class="glow-blob" style="width:460px; height:460px; background:radial-gradient(circle, rgba(212,175,55,0.14), transparent 70%); top:20%; right:-140px;"></div>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Experience and Frameworks</span>
      <h2 style="color:#fff;">What John brings to the table.</h2>
    </div>
    <div class="bento reveal">
      <div class="card-glass span-2"><span class="card-eyebrow">Service background</span><h3 style="font-size:18px;">U.S. Navy Hospital Corpsman</h3><p style="font-size:14.5px;">Clinical training in triage, assessment, and acting under pressure. The habit of diagnosing before treating runs through every engagement.</p></div>
      <div class="card-glass"><span class="card-eyebrow">Education</span><h3 style="font-size:18px;">M.S. Digital Marketing</h3><p style="font-size:14.5px;">Full Sail University, plus a bachelor&rsquo;s degree in Visual Communication.</p></div>
      <div class="card-glass"><span class="card-eyebrow">Practice</span><h3 style="font-size:18px;">AI &amp; Digital Marketing Consultant</h3><p style="font-size:14.5px;">AI-assisted business systems, brand voice, digital strategy, customer communication, and training.</p></div>
      <div class="card-glass"><span class="card-eyebrow">Original framework</span><h3 style="font-size:18px;">Brand Voice AI</h3><p style="font-size:14.5px;">An AI-assisted business operating system that captures founder knowledge and keeps human approval in the loop.</p></div>
      <div class="card-glass"><span class="card-eyebrow">Original framework</span><h3 style="font-size:18px;">The Compass Method</h3><p style="font-size:14.5px;">Heart at the center. Purpose, Skill, Opportunity, and Service at the four points. Lead with heart. Navigate with purpose.</p></div>
      <div class="card-glass span-2"><span class="card-eyebrow">Teaching</span><h3 style="font-size:18px;">Workshops, training, and community education</h3><p style="font-size:14.5px;">Practical AI adoption, brand voice, digital marketing, and business systems for entrepreneurs, teams, veteran-owned businesses, nonprofits, and organizations. See one, do one, teach one.</p></div>
    </div>
  </div>
</section>

<!-- PHILOSOPHY -->
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">What John Believes</span>
      <h2>Two ideas guide everything built here.</h2>
    </div>
    <div class="grid-2 reveal">
      <div class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--gold-dim)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.2"/><path d="M5.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="4" cy="7" r="1"/><circle cx="20" cy="7" r="1"/><circle cx="20" cy="17" r="1"/></svg></div>
        <h3>Human-Centered AI</h3>
        <p style="font-size:15px;">AI should amplify a founder&rsquo;s voice, not replace it. Every system Pogue Digital Solutions builds, from Brand Voice AI to a client&rsquo;s very first assessment, runs on one rule: a human approves the work before it goes out the door.</p>
      </div>
      <div class="card">
        <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="var(--gold-dim)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 6.5L13.6 10.4L17.5 12L13.6 13.6L12 17.5L10.4 13.6L6.5 12L10.4 10.4Z"/></svg></div>
        <h3>A Bigger Purpose</h3>
        <p style="font-size:15px;">At its core, John&rsquo;s work is about something bigger than marketing: helping people understand themselves and the systems around them well enough to lead with confidence. That same idea runs through The Compass Method, his framework for founders navigating their own direction, not just their business&rsquo;s.</p>
      </div>
    </div>
    <p class="quote-band reveal" style="margin-top:36px;">&ldquo;Curiosity is my superpower.&rdquo;</p>
  </div>
</section>

{cta_band("Let&rsquo;s Talk", "Book a strategy call with John directly.", primary=("Book a Strategy Call", CALENDLY), secondary=("Take an Assessment", "assessments.html"))}
''' + footer()

# primary external link needs target attrs; cta_band only adds them for secondary. Patch here.
html = html.replace(f'<a href="{CALENDLY}" class="btn btn-gold">Book a Strategy Call', f'<a href="{CALENDLY}" class="btn btn-gold" target="_blank" rel="noopener">Book a Strategy Call')
open("./about.html", "w").write(html)
print("about.html", len(html))
