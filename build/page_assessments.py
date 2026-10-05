from parts import *

FAQS = [
 ("Are the assessments really free?", "Yes. The four self-assessments are free and come with no obligation. The Strategic Assessment is a working session with John and is scoped on a short call first."),
 ("Do I need to know which service I need before I start?", "No. The assessments exist so you do not have to. Each one ends with a plain-language read on where your business stands and one recommended next step."),
 ("What happens after I complete an assessment?", "You receive a summary of where your business is strong, where information is getting lost, and whether Brand Voice AI, AI and automation, digital strategy, training, or a conversation with John is the right next move."),
 ("Will I get a sales pitch?", "No. The result is a recommendation, which may be a free resource or a note that you are not ready yet. If a paid engagement fits, we will say so plainly and let you decide."),
 ("Can my team take an assessment together?", "Yes. The AI Readiness and Business Systems assessments work well as a team exercise, and the results often make for a useful leadership conversation."),
]

def card(id_, mins, title, desc, routes, label):
    return f'''<div class="card stack-lg" id="{id_}">
  <span class="card-eyebrow">{mins} &middot; Free</span>
  <h3>{title}</h3>
  <p>{desc}</p>
  <p style="font-family:var(--font-mono); font-size:11.5px; letter-spacing:0.08em; text-transform:uppercase; color:var(--gold-dim);">Routes to: {routes}</p>
  <a href="contact.html#assessment" class="btn btn-outline-navy" style="margin-top:12px;">{label} <span class="btn-arrow">&rarr;</span></a>
</div>'''

html = head("Free Business Assessments | Brand Voice, AI Readiness, Systems, Compass",
  "Find out where your business is actually stuck. Free brand voice, AI readiness, business systems, and Compass assessments from Pogue Digital Solutions, LLC.",
  "assessments.html", jsonld=[faq_jsonld(FAQS), breadcrumb("Assessments", "assessments.html")]) + header("assessments.html") + f'''

<!-- HERO -->
<section class="on-ink tight" style="padding-top:56px; padding-bottom:72px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:760px;">
    <span class="eyebrow">Not Sure Where to Begin?</span>
    <h1 style="font-size:clamp(36px,5.4vw,64px); color:#fff; margin-top:16px;">Start With the Right Question</h1>
    <p style="font-size:17px; max-width:600px; margin-top:18px;">You do not need to know exactly what service you need. Our assessments help identify where your business is strong, where information is getting lost, and where a clearer strategy or system could improve your work.</p>
    <div class="bearing" style="margin-top:40px; max-width:520px;"><span class="bearing-label">YOU ARE HERE</span><div class="bearing-rule"></div><span class="bearing-label">RECOMMENDED HEADING</span></div>
  </div>
</section>

<!-- ASSESSMENTS -->
<section>
  <div class="wrap">
    <div class="grid-2 reveal" style="gap:24px;">
      {card("brand-voice", "5 min", "Brand Voice Quick Check", "Discover whether your business has enough clarity and documentation to communicate consistently across people, platforms, and AI tools.", "Brand Voice AI", "Check Your Brand Voice")}
      {card("ai-readiness", "8 min", "AI Readiness Assessment", "Evaluate whether your business has the information, processes, safeguards, and team readiness needed to use AI effectively.", "AI and Automation", "Measure Your AI Readiness")}
      {card("continuity", "7 min", "Business Systems Assessment", "Identify repetitive work, undocumented processes, bottlenecks, and opportunities for better organization or automation. A gut check on what would happen to your marketing and operations if you disappeared for a month.", "Digital Strategy and Automation", "Review Your Business Systems")}
      {card("compass", "10 min", "Compass Assessment", "Explore how your purpose, skills, opportunities, service, and decisions align with the direction you want to pursue. Built on <a href=\"compass-method.html\">the Compass Method</a>: Heart at the center, with Purpose, Skill, Opportunity, and Service at the four points.", "The Compass Method", "Find Your Bearing")}
    </div>

    <div class="card-glass reveal on-ink" id="strategic" style="margin-top:24px; padding:44px; background:linear-gradient(135deg, var(--ink) 0%, var(--navy) 100%); display:flex; justify-content:space-between; align-items:center; gap:32px; flex-wrap:wrap;">
      <div style="max-width:600px;">
        <span class="card-eyebrow">30 min &middot; 1:1 with John</span>
        <h3 style="font-size:22px;">Request a Strategic Assessment</h3>
        <p>A focused review designed to identify your strongest opportunities, immediate gaps, and logical next steps. Best for businesses that know something needs to improve but are not sure where to begin.</p>
      </div>
      <a href="{CALENDLY}" class="btn btn-gold" target="_blank" rel="noopener">Request a Call <span class="btn-arrow">&rarr;</span></a>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section class="on-paper-dim">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">How It Works</span>
      <h2>Your results plot the next step.</h2>
      <p>Every assessment ends the same way: a clear read on where you are stuck, and one recommended next step. Not a hard sell.</p>
    </div>
    <div class="journey-track reveal">
      <div><div class="journey-node"></div><span class="pill">Step 1</span><h3 style="font-size:17px; margin-top:12px;">Answer honestly</h3><p style="font-size:14px; margin-top:6px;">A few minutes, no account required.</p></div>
      <div><div class="journey-node"></div><span class="pill">Step 2</span><h3 style="font-size:17px; margin-top:12px;">Get your read</h3><p style="font-size:14px; margin-top:6px;">A plain-language summary of where things stand.</p></div>
      <div><div class="journey-node"></div><span class="pill">Step 3</span><h3 style="font-size:17px; margin-top:12px;">See your next step</h3><p style="font-size:14px; margin-top:6px;">Routed toward consulting, training, or a free resource, whichever fits.</p></div>
      <div><div class="journey-node"></div><span class="pill">Step 4</span><h3 style="font-size:17px; margin-top:12px;">Decide, no pressure</h3><p style="font-size:14px; margin-top:6px;">Book a call if it fits. If it does not yet, that is a useful answer too.</p></div>
    </div>
  </div>
</section>

<!-- WHO THEY ARE FOR -->
<section class="on-ink">
  <div class="glow-blob" style="width:460px; height:460px; background:radial-gradient(circle, rgba(212,175,55,0.14), transparent 70%); top:10%; right:-140px;"></div>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Who These Are For</span>
      <h2 style="color:#fff;">Built for businesses where the founder&rsquo;s knowledge matters.</h2>
    </div>
    <div class="grid-3 reveal">
      <div class="card-glass"><h3 style="font-size:16.5px;">Founder-Led Small Businesses</h3><p style="font-size:14px;">Much of what you know still depends on your direct involvement.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Solopreneurs &amp; Consultants</h3><p style="font-size:14px;">You need systems that support growth without sounding generic.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Coaches &amp; Service Providers</h3><p style="font-size:14px;">Your methods and stories need to become a repeatable client experience.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Veteran Entrepreneurs</h3><p style="font-size:14px;">Your discipline and mission focus should show up in your systems.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Teams &amp; Organizations</h3><p style="font-size:14px;">Your people need shared standards and responsible AI guidance.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Government, Education &amp; Nonprofits</h3><p style="font-size:14px;">You need documentation, training, and systems that support accountability.</p></div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="on-paper-dim">
  <div class="wrap" style="max-width:820px;">
    <div class="section-head reveal"><span class="eyebrow">Common Questions</span><h2>Frequently Asked Questions</h2></div>
    {faq(FAQS)}
  </div>
</section>

{cta_band("Ready When You Are", "Pick the assessment that matches the question you are already asking.", primary=("Check Your Brand Voice", "#brand-voice"), closing="&ldquo;Don&rsquo;t tell me it can&rsquo;t be done. Let&rsquo;s find out how it can.&rdquo;")}
''' + footer()

open("./assessments.html", "w").write(html)
print("assessments.html", len(html))
