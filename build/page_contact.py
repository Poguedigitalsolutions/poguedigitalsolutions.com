import json, urllib.parse
from parts import *

def mail(subject, body):
    return f"mailto:{EMAIL}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

INTENTS = [
 ("strategy", "Schedule a strategy call", "A 30-minute working conversation on Zoom about a specific problem, decision, system, or opportunity. No pitch. Bring your questions.", "Pick a time", CALENDLY, True),
 ("assessment", "Request an assessment", "Tell us which assessment you want (Brand Voice, AI Readiness, Business Systems, or Compass) and we will send it over with instructions.", "Request an assessment", mail("Assessment request", "Hi John,\n\nI would like to take the following assessment: \n\nA little about my business: \n\nName: \nBusiness: \nWebsite: "), False),
 ("brand-voice-ai", "Ask about Brand Voice AI", "Questions about the Brand Voice AI Business Operating System, what it organizes, and whether it fits a founder-led business like yours.", "Ask about Brand Voice AI", mail("Brand Voice AI question", "Hi John,\n\nMy question about Brand Voice AI: \n\nName: \nBusiness: \nWebsite: "), False),
 ("project", "Discuss a project", "A defined engagement with specific deliverables: Brand Voice AI foundations, website strategy, customer journey mapping, AI workflow planning, messaging systems, content operations, or training development.", "Start the conversation", mail("Project inquiry", "Hi John,\n\nThe project I have in mind: \n\nTimeline: \n\nName: \nBusiness: \nWebsite: "), False),
 ("advisory", "Ask about advisory support", "Ongoing strategic guidance for businesses implementing new systems, marketing plans, AI workflows, or organizational change, without hiring a full-time strategist.", "Ask about advisory", mail("Advisory support", "Hi John,\n\nWhat we are implementing and where we could use ongoing guidance: \n\nName: \nBusiness: \nWebsite: "), False),
 ("workshop", "Request a workshop or speaking engagement", "Virtual or in-person workshops, team training, conference sessions, and community education on practical AI adoption, brand voice, digital marketing, and business systems.", "Request a workshop", mail("Workshop or speaking request", "Hi John,\n\nAudience: \nTopic or focus: \nFormat (virtual / in-person): \nDate or timeframe: \n\nName: \nOrganization: "), False),
 ("government", "Discuss government contracting", "Pogue Digital Solutions, LLC is an active SAM.gov registrant (UEI Y6S7ZHLJH5V6, CAGE 219K1, primary NAICS 541613) and a Navy veteran-owned business. A capability statement is available on request.", "Contact for contracting", mail("Government contracting inquiry", "Hi John,\n\nAgency or prime contractor: \nOpportunity or need: \n\nName: \nTitle: \nOrganization: "), False),
 ("partnerships", "Explore partnerships or affiliates", "Referral partnerships, co-hosted workshops, community collaborations, and affiliate relationships with tools that fit the human-approved AI philosophy.", "Propose a partnership", mail("Partnership inquiry", "Hi John,\n\nWhat I have in mind: \n\nName: \nOrganization: \nWebsite: "), False),
 ("general", "Submit a general inquiry", "Anything that does not fit the other boxes. You will hear back from John, not an autoresponder.", "Send a note", mail("General inquiry", "Hi John,\n\n"), False),
]

CONTACT_LD = json.dumps({"@context": "https://schema.org", "@graph": [
 {"@type": "ContactPage", "name": "Contact Pogue Digital Solutions, LLC", "url": SITE + "/contact.html",
  "about": {"@type": "Organization", "name": "Pogue Digital Solutions, LLC", "url": SITE + "/", "email": EMAIL,
            "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "email": EMAIL, "areaServed": "US", "availableLanguage": "English"}],
            "address": {"@type": "PostalAddress", "addressLocality": "Conroe", "addressRegion": "TX", "addressCountry": "US"},
            "sameAs": [LINKEDIN, STARWEAVER]}},
 json.loads(breadcrumb("Contact", "contact.html"))]}, indent=1)

TOPIC_LABELS = {"strategy": "A strategy call", "assessment": "An assessment", "brand-voice-ai": "Brand Voice AI",
  "project": "A project", "advisory": "Advisory support", "workshop": "A workshop or speaking engagement",
  "government": "Government contracting", "partnerships": "Partnerships or affiliates", "general": "Something else"}
options = "".join(f'        <option value="{k}"{" selected" if k == "general" else ""}>{v}</option>\n' for k, v in TOPIC_LABELS.items())

cards = ""
for id_, title, desc, label, href, ext in INTENTS:
    attrs = ' target="_blank" rel="noopener"' if ext else ''
    cards += f'<div class="card" id="{id_}"><h3>{title}</h3><p>{desc}</p><a class="link" href="{href}"{attrs}>{label} &rarr;</a></div>\n'

html = head("Contact | Book a Strategy Call with Pogue Digital Solutions",
  "Book a strategy call, request an assessment, ask about Brand Voice AI, request a workshop, or discuss government contracting with Pogue Digital Solutions, LLC in Conroe, Texas.",
  "contact.html", jsonld=[CONTACT_LD]) + header("contact.html") + f'''

<!-- HERO -->
<section class="on-ink tight" style="padding-top:56px; padding-bottom:80px;">
  {compass_svg()}
  <div class="wrap" style="display:grid; grid-template-columns:1.15fr 0.85fr; gap:56px; align-items:center;">
    <div class="reveal">
      <span class="eyebrow">Contact</span>
      <h1 style="font-size:clamp(36px,5.4vw,64px); color:#fff; margin-top:16px;">Let&rsquo;s find out how it <em>can</em> be done.</h1>
      <p style="font-size:17px; max-width:560px; margin-top:20px;">Pick the path that matches what you need. The fastest one is a 30-minute call. You can also send a message with the form below, or use one of the paths that opens your email with the subject line already filled in.</p>
      <div style="display:flex; gap:16px; margin-top:30px; flex-wrap:wrap;">
        <a href="{CALENDLY}" class="btn btn-gold" target="_blank" rel="noopener">Book a Strategy Call <span class="btn-arrow">&rarr;</span></a>
        <a href="mailto:{EMAIL}" class="btn btn-outline-gold">{EMAIL}</a>
      </div>
      <div class="bearing" style="margin-top:44px; max-width:480px;"><span class="bearing-label">CONROE, TX</span><div class="bearing-rule"></div><span class="bearing-label">NATIONWIDE</span></div>
    </div>
    <div class="reveal">
      <div class="card-glass" style="padding:34px;">
        <span class="card-eyebrow">What to expect</span>
        <ul class="feature-list cols-1" style="margin-top:12px;">
          <li>Calls are on Zoom, scheduled through Calendly in Central Time.</li>
          <li>You talk with John, not an autoresponder or a sales team.</li>
          <li>Based in Conroe, Texas. Serving Greater Houston and clients across the United States.</li>
          <li>Navy veteran-owned. SAM.gov registered for government and organizational work.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- INTENT GRID -->
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Choose Your Path</span>
      <h2>What would you like to do?</h2>
    </div>
    <div class="intent-grid reveal">
{cards}    </div>
  </div>
</section>

<!-- MESSAGE FORM -->
<section class="on-paper-dim" id="message">
  <div class="wrap" style="max-width:820px;">
    <div class="section-head reveal">
      <span class="eyebrow">Send a Message</span>
      <h2>Prefer to write it out?</h2>
      <p>Your message goes straight to John. He replies by email.</p>
    </div>
    <form id="contact-form" class="comments-form reveal" data-turnstile="{TURNSTILE_SITE_KEY}" novalidate style="margin-top:0;">
      <div class="row-2">
        <label>Name <input name="name" type="text" maxlength="80" required autocomplete="name"></label>
        <label>Email <input name="email" type="email" maxlength="254" required autocomplete="email"></label>
      </div>
      <label>Topic <select name="topic">
{options}      </select></label>
      <label>Message <textarea name="message" maxlength="4000" required></textarea></label>
      <div class="hp" aria-hidden="true"><label>Website <input name="website" type="text" tabindex="-1" autocomplete="off"></label></div>
      <div class="cf-turnstile"></div>
      <div class="comments-foot">
        <button class="btn btn-gold" type="submit">Send Message <span class="btn-arrow">&rarr;</span></button>
        <p class="comments-note"></p>
      </div>
      <p class="comments-hint">Your name, email, and message are used only to reply to you. See the <a href="privacy.html">privacy policy</a>.</p>
    </form>
  </div>
</section>
<script src="js/contact.js?v={ASSET_VER}" defer></script>

<!-- GOVERNMENT DETAIL -->
<section>
  <div class="wrap" style="display:grid; grid-template-columns:1fr 1fr; gap:48px; align-items:center;">
    <div class="reveal">
      <span class="eyebrow">Government and Organizational Clients</span>
      <h2 style="margin-top:12px;">Registered, veteran-owned, and ready to support the mission.</h2>
      <p style="margin-top:16px;">Pogue Digital Solutions, LLC supports government agencies, contractors, educational institutions, veteran service organizations, nonprofits, and healthcare-related organizations with AI adoption planning, workforce training, communication strategy, process documentation, and knowledge organization.</p>
      <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:18px;">
        <span class="pill">SAM.gov active</span><span class="pill">UEI Y6S7ZHLJH5V6</span><span class="pill">CAGE 219K1</span><span class="pill">NAICS 541613</span><span class="pill">Navy veteran-owned</span>
      </div>
    </div>
    <div class="card reveal">
      <span class="card-eyebrow">Capability statement</span>
      <h3 style="font-size:19px;">Available on request</h3>
      <p style="font-size:14.5px;">Email with your agency or prime contractor and the opportunity you have in mind, and John will send the current capability statement. Codes, registrations, and core capabilities are on the <a href="government.html">Government Services page</a>.</p>
      <a href="{mail("Capability statement request", "Hi John,\n\nPlease send the Pogue Digital Solutions, LLC capability statement.\n\nAgency or prime contractor: \nOpportunity: \n\nName: \nTitle: ")}" class="btn btn-outline-navy" style="margin-top:14px;">Request the Capability Statement <span class="btn-arrow">&rarr;</span></a>
    </div>
  </div>
</section>

{cta_band("Prefer to Start Smaller?", "Take a free assessment first and bring the results to the call.", primary=("Take an Assessment", "assessments.html"), secondary=None)}
''' + footer()

open("./contact.html", "w").write(html)
print("contact.html", len(html))
