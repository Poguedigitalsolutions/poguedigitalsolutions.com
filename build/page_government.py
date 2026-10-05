import json, urllib.parse
from parts import *

PHONE = "346-367-4600"
UEI = "Y6S7ZHLJH5V6"
CAGE = "219K1"

def mail(subject, body):
    return f"mailto:{EMAIL}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

CAP_MAIL = mail("Capability statement request",
  "Hi John,\n\nPlease send the Pogue Digital Solutions, LLC capability statement.\n\nAgency or prime contractor: \nOpportunity or need: \n\nName: \nTitle: \nOrganization: ")
TEAM_MAIL = mail("Teaming or subcontracting inquiry",
  "Hi John,\n\nWe are looking at a teaming or subcontracting fit.\n\nPrime contractor or agency: \nContract or opportunity: \nScope where you might fit: \n\nName: \nTitle: \nOrganization: ")

NAICS = [
 ("541613", "Marketing Consulting Services", True),
 ("541611", "Administrative Management and General Management Consulting Services", False),
 ("541511", "Custom Computer Programming Services", False),
 ("541512", "Computer Systems Design Services", False),
 ("541810", "Advertising Agencies", False),
 ("541820", "Public Relations Agencies", False),
 ("611430", "Professional and Management Development Training", False),
]
PSC = [
 ("R701", "Support, Management: Advertising"),
 ("R708", "Support, Management: Public Relations"),
 ("R799", "Support, Management: Other"),
 ("R408", "Support, Professional: Program Management and Support"),
 ("U008", "Education and Training: Training and Curriculum Development"),
 ("DA01", "IT and Telecom: Business Application and Application Development Support"),
]

FAQS = [
 ("Is Pogue Digital Solutions registered in SAM.gov?", "Yes. Pogue Digital Solutions LLC holds an active SAM.gov entity registration for all award types. The Unique Entity ID is Y6S7ZHLJH5V6 and the CAGE code is 219K1. Both are listed on this page so a contracting officer or prime can verify the record directly."),
 ("Is the company certified as a veteran-owned business?", "Pogue Digital Solutions is a veteran-owned, founder-led small business. John M Pogue served in the United States Navy as a Hospital Corpsman. The company is registered as veteran-owned in SAM.gov, and a Texas HUB certification application is in progress. Certifications will be added to this page as they are issued, and nothing is claimed here before it is confirmed."),
 ("Does Pogue Digital Solutions have federal past performance?", "Pogue Digital Solutions is a newer federal vendor and does not claim federal past performance it has not earned. The founder's experience covers customer communications and billing operations, technical support, staff training, process documentation, and AI-assisted content and workflow systems in process-heavy, customer-facing environments. Subcontracting and teaming are welcome as a first step."),
 ("What size of work fits best right now?", "Small direct contracts, micro-purchases, training and workshop engagements, and subcontracted support under a prime. Typical scopes: a training series, a communications or outreach plan, a brand voice and messaging system, workflow documentation, or a reporting process a team can run on its own."),
 ("Can you work with state, local, and Texas agencies as well as federal?", "Yes. The company is based in Conroe, Texas, in Montgomery County, and works with Texas agencies, school districts, municipalities, and community organizations in person, and with organizations nationwide virtually."),
 ("How do I get the capability statement?", "Email John with your agency or prime contractor and the opportunity you have in mind, and he will send the current one-page capability statement. Everything on it also appears on this page."),
]

LD = json.dumps({"@context": "https://schema.org", "@graph": [
 {"@type": "ProfessionalService", "@id": SITE + "/#organization", "name": "Pogue Digital Solutions, LLC",
  "legalName": "Pogue Digital Solutions LLC", "url": SITE + "/", "telephone": "+1-" + PHONE, "email": EMAIL,
  "address": {"@type": "PostalAddress", "addressLocality": "Conroe", "addressRegion": "TX", "addressCountry": "US"},
  "founder": {"@type": "Person", "name": "John M Pogue", "url": SITE + "/about.html"},
  "naics": "541613",
  "identifier": [
    {"@type": "PropertyValue", "propertyID": "UEI", "name": "SAM.gov Unique Entity ID", "value": UEI},
    {"@type": "PropertyValue", "propertyID": "CAGE", "name": "CAGE Code", "value": CAGE}],
  "knowsAbout": ["Digital outreach and communications support", "AI workflow enablement", "Training and curriculum development", "Brand voice and messaging systems", "Analytics and reporting"]},
 {"@type": "Service", "name": "Government and Organizational Services", "url": SITE + "/government.html",
  "provider": {"@id": SITE + "/#organization"},
  "serviceType": ["Digital outreach and communications support", "AI workflow enablement and process support", "Training, workshops, and curriculum development", "Content strategy, messaging, and brand voice support", "Analytics, reporting, and customer insight support"],
  "areaServed": ["United States", "Texas"],
  "audience": {"@type": "Audience", "audienceType": "Federal agencies, state and local government, prime contractors, education and training organizations, veteran-serving nonprofits, healthcare organizations"}},
 json.loads(breadcrumb("Government and Organizational Services", "government.html"))]}, indent=1)

def cap(num, title, body, items, codes):
    lis = "".join(f"<li>{i}</li>" for i in items)
    code_html = " ".join(f'<span class="code-tag">{c}</span>' for c in codes)
    return f'''<div class="card-glass reveal" style="padding:30px;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:12px;">
    <span class="card-eyebrow">{num}</span>
    <div class="code-tags">{code_html}</div>
  </div>
  <h3 style="font-size:20px; margin-bottom:10px;">{title}</h3>
  <p style="font-size:14.5px;">{body}</p>
  <ul class="feature-list cols-1" style="margin-top:14px;">{lis}</ul>
</div>'''

def spec(label, value, mono=True):
    cls = ' class="mono"' if mono else ""
    return f'<div class="spec-row"><dt>{label}</dt><dd{cls}>{value}</dd></div>'

naics_rows = "".join(
  f'<tr><td class="mono">{code}</td><td>{name}{" <span class=\"code-tag\">Primary</span>" if primary else ""}</td></tr>'
  for code, name, primary in NAICS)
psc_rows = "".join(f'<tr><td class="mono">{code}</td><td>{name}</td></tr>' for code, name in PSC)

html = head("Government and Organizational Services | Pogue Digital Solutions, LLC",
  "Veteran-owned, SAM.gov registered small business in Conroe, Texas. UEI Y6S7ZHLJH5V6, CAGE 219K1. Digital outreach, AI workflow enablement, training, messaging systems, and reporting support for agencies, primes, nonprofits, and education.",
  "government.html", jsonld=[LD, faq_jsonld(FAQS)]) + header("government.html") + f'''

<!-- HERO -->
<section class="on-ink tight" style="padding-top:56px; padding-bottom:80px;">
  {compass_svg()}
  <div class="wrap" style="display:grid; grid-template-columns:1.15fr 0.85fr; gap:56px; align-items:center; position:relative; z-index:1;">
    <div class="reveal">
      <span class="eyebrow">Government and Organizational Services</span>
      <h1 style="font-size:clamp(34px,4.6vw,56px); color:#fff; margin-top:16px;">Registered and veteran-owned. Built for teams that <em>cannot afford to stall.</em></h1>
      <p style="font-size:17.5px; max-width:580px; margin-top:22px;">Pogue Digital Solutions, LLC helps agencies, contractors, nonprofits, and education organizations keep communication, training, and reporting moving when staff are stretched thin. Practical digital strategy, AI-enabled workflows, and content systems a lean team can run on its own.</p>
      <p style="font-size:17.5px; max-width:580px;">Led by John M Pogue, a United States Navy veteran and Hospital Corpsman with a Master of Science in Digital Marketing.</p>
      <div style="display:flex; gap:16px; margin-top:32px; flex-wrap:wrap;">
        <a href="{CAP_MAIL}" class="btn btn-gold">Request the Capability Statement <span class="btn-arrow">&rarr;</span></a>
        <a href="#codes" class="btn btn-outline-gold">UEI, CAGE, NAICS, and PSC</a>
      </div>
    </div>
    <div class="card-glass reveal" style="padding:30px 32px; border-color:rgba(242,214,128,0.4);">
      <div class="bearing" style="margin-bottom:18px;"><span class="bearing-label">COMPANY SNAPSHOT</span><div class="bearing-rule"></div><span class="bearing-label">SAM.GOV</span></div>
      <dl class="spec-list">
        {spec("Legal name", "Pogue Digital Solutions LLC", mono=False)}
        {spec("UEI", UEI)}
        {spec("CAGE", CAGE)}
        {spec("SAM.gov status", "Active &middot; All awards", mono=False)}
        {spec("Business status", "Veteran-owned, founder-led small business", mono=False)}
        {spec("Primary NAICS", "541613")}
        {spec("Location", "Conroe, Texas (Montgomery County)", mono=False)}
        {spec("Contact", f'<a href="tel:+1{PHONE.replace("-", "")}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a>', mono=False)}
      </dl>
    </div>
  </div>
</section>

<!-- OVERVIEW -->
<section>
  <div class="wrap" style="max-width:800px;">
    <span class="eyebrow reveal">Company Overview</span>
    <h2 class="reveal" style="margin-top:12px;">A founder-led firm for organizations that need more than a one-time campaign.</h2>
    <p class="reveal" style="font-size:17px; margin-top:22px;">Most organizations do not need another isolated deliverable. They need repeatable systems for communication, content, staff enablement, and reporting, so the work keeps moving when time, staffing, or internal capacity runs short. That is what Pogue Digital Solutions builds.</p>
    <p class="reveal" style="font-size:17px;">The firm combines digital strategy, practical AI adoption, audience-centered messaging, and process design, and delivers them in a form that lean, nontechnical, mission-focused teams can use the next day. Every system includes documentation and training, so it outlasts the engagement.</p>
    <p class="quote-band reveal" style="margin-top:32px;">Continuity over campaigns. Systems a team can run without us.</p>
  </div>
</section>

<!-- CORE CAPABILITIES -->
<section class="on-ink" id="capabilities">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Core Capabilities</span>
      <h2 style="color:#fff;">Five lanes of support, each backed by codes already in our SAM.gov record.</h2>
    </div>
    <div class="grid-2" style="gap:22px;">
      {cap("01", "Digital Outreach and Communications Support",
        "Outreach strategy, communication calendars, campaign support, audience messaging, and stakeholder-facing content planning.",
        ["Outreach and communication plans for public, partner, and internal audiences", "Communication calendars and campaign coordination", "Stakeholder messaging and plain-language content", "Website, email, and social content planning"],
        ["541613", "541810", "R701"])}
      {cap("02", "AI Workflow Enablement and Process Support",
        "Workflow mapping, prompt libraries, standard operating procedures, AI-assisted reporting processes, and practical AI adoption for day-to-day operations.",
        ["Process and workflow mapping before any tool is chosen", "Prompt libraries and AI standard operating procedures", "Human-approval checkpoints built into every automated step", "Knowledge capture so institutional memory survives turnover"],
        ["541511", "541512", "DA01"])}
      {cap("03", "Training, Workshops, and Curriculum Development",
        "AI literacy, prompt-writing workshops, facilitator guides, onboarding materials, train-the-trainer support, and custom curriculum.",
        ["AI literacy and responsible-use training for staff", "Prompt-writing and workflow workshops", "Onboarding guides, training manuals, and facilitator decks", "Train-the-trainer sessions and custom curriculum"],
        ["611430", "U008"])}
      {cap("04", "Content Strategy, Messaging, and Brand Voice Support",
        "Brand voice guides, messaging frameworks, email sequence strategy, campaign messaging, content planning, and AI-assisted content workflows.",
        ["Voice and messaging frameworks for consistent public communication", "Audience personas and insight summaries", "Email, social, and campaign messaging", "Content calendars and AI-assisted content workflow design"],
        ["541820", "R708"])}
      {cap("05", "Analytics, Reporting, and Customer Insight Support",
        "Performance dashboards, campaign reporting summaries, KPI frameworks, audience insight summaries, journey analysis, and reporting process design.",
        ["Outreach and program performance dashboards", "KPI tracking frameworks and reporting templates", "Customer or constituent journey analysis", "Executive summaries that turn data into action steps"],
        ["541611", "R408", "R799"])}
      <div class="card-glass reveal" style="padding:30px; display:flex; flex-direction:column; justify-content:center; background:linear-gradient(160deg, rgba(242,214,128,0.12), rgba(255,255,255,0.02)); border-color:rgba(242,214,128,0.45);">
        <span class="card-eyebrow">Flagship System</span>
        <h3 style="font-size:20px; margin-bottom:10px;">Brand Voice AI for Organizations</h3>
        <p style="font-size:14.5px;">A documented communication system that captures an organization&rsquo;s mission, audiences, approved language, and review rules, then puts AI assistance behind it with a human approving every output. Built for teams where consistency and accountability matter.</p>
        <a href="solutions.html#brand-voice-ai" class="btn btn-outline-gold" style="margin-top:18px; align-self:flex-start;">See How Brand Voice AI Works <span class="btn-arrow">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>

<!-- DIFFERENTIATORS -->
<section>
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Differentiators</span><h2>Why a small firm instead of a large agency.</h2></div>
    <div class="grid-4 reveal">
      <div class="card"><span class="card-eyebrow">Continuity</span><h3 style="font-size:17px;">Systems, then campaigns</h3><p style="font-size:14px;">Every engagement leaves behind repeatable systems for outreach, content, reporting, and team workflows, with documentation the team owns.</p></div>
      <div class="card"><span class="card-eyebrow">Judgment</span><h3 style="font-size:17px;">Psychology, analytics, AI, messaging</h3><p style="font-size:14px;">Four disciplines on one desk. Communication decisions get made with data and with an understanding of the people reading it.</p></div>
      <div class="card"><span class="card-eyebrow">Translation</span><h3 style="font-size:17px;">AI nontechnical teams can use</h3><p style="font-size:14px;">Training, standard operating procedures, prompt libraries, and approval steps, so AI becomes a tool staff trust rather than a risk they avoid.</p></div>
      <div class="card"><span class="card-eyebrow">Execution</span><h3 style="font-size:17px;">Strategy that ships</h3><p style="font-size:14px;">Experience across communications, billing operations, technical support, training, and process-heavy environments. The plan and the work come from the same person.</p></div>
    </div>
  </div>
</section>

<!-- FOUNDER + WHO WE SERVE -->
<section class="on-paper-dim">
  <div class="wrap" style="display:grid; grid-template-columns:1fr 1fr; gap:48px; align-items:start;">
    <div class="reveal">
      <span class="eyebrow">Founder Experience</span>
      <h2 style="margin-top:12px;">Relevant experience, stated plainly.</h2>
      <p style="margin-top:16px;">Pogue Digital Solutions is a newer federal vendor and does not claim federal past performance it has not earned. What it brings is the founder&rsquo;s record:</p>
      <ul class="feature-list cols-1" style="margin-top:14px;">
        <li>United States Navy veteran and Hospital Corpsman. Clear communication and calm execution under pressure.</li>
        <li>Customer communications, billing, payment, and technical support operations in high-volume, customer-facing environments.</li>
        <li>Training development, staff and customer support materials, and workflow adoption support.</li>
        <li>AI-assisted content, messaging, and process systems built to improve consistency and efficiency.</li>
        <li>Master of Science in Digital Marketing, Full Sail University. Bachelor of Arts in Visual Communication.</li>
      </ul>
      <a href="about.html" class="btn btn-outline-navy" style="margin-top:22px;">About John M Pogue <span class="btn-arrow">&rarr;</span></a>
    </div>
    <div class="reveal">
      <span class="eyebrow">Who We Support</span>
      <h2 style="margin-top:12px;">Mission-driven teams at every level.</h2>
      <div class="grid-2" style="gap:14px; margin-top:22px;">
        <div class="card" style="padding:20px;"><h3 style="font-size:15.5px;">Federal agencies and offices</h3><p style="font-size:13.5px;">Communications, outreach, training, and reporting support.</p></div>
        <div class="card" style="padding:20px;"><h3 style="font-size:15.5px;">State, county, and municipal</h3><p style="font-size:13.5px;">Texas agencies, Montgomery County, and Greater Houston communities.</p></div>
        <div class="card" style="padding:20px;"><h3 style="font-size:15.5px;">Prime contractors</h3><p style="font-size:13.5px;">Subcontracted outreach, training, content, and AI workflow support.</p></div>
        <div class="card" style="padding:20px;"><h3 style="font-size:15.5px;">Education and training organizations</h3><p style="font-size:13.5px;">Curriculum, facilitator guides, and staff enablement.</p></div>
        <div class="card" style="padding:20px;"><h3 style="font-size:15.5px;">Veteran-serving nonprofits</h3><p style="font-size:13.5px;">Messaging, outreach systems, and AI training for small staffs.</p></div>
        <div class="card" style="padding:20px;"><h3 style="font-size:15.5px;">Healthcare organizations</h3><p style="font-size:13.5px;">Patient and staff communication, documentation, and training.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- WAYS TO WORK TOGETHER -->
<section>
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Ways to Engage</span><h2>Three practical entry points.</h2></div>
    <div class="grid-3 reveal">
      <div class="card"><span class="card-eyebrow">Direct</span><h3 style="font-size:18px;">Small contracts and micro-purchases</h3><p style="font-size:14.5px;">Scoped work a program office can buy directly: a training series, a communications plan, a messaging system, or a reporting process.</p></div>
      <div class="card"><span class="card-eyebrow">Teaming</span><h3 style="font-size:18px;">Subcontract under a prime</h3><p style="font-size:14.5px;">Overflow or specialty support on outreach, training, content, and AI workflow tasks where a veteran-owned small business adds value to the team.</p><a href="{TEAM_MAIL}" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;">Start a Teaming Conversation</a></div>
      <div class="card"><span class="card-eyebrow">Training</span><h3 style="font-size:18px;">Workshops and staff enablement</h3><p style="font-size:14.5px;">AI literacy, prompt-writing, brand voice, and process workshops for a department, a cohort, or a whole organization, in person in Texas or virtually.</p><a href="contact.html#workshop" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;">Request a Workshop</a></div>
    </div>
  </div>
</section>

<!-- CODES AND REGISTRATIONS -->
<section class="on-ink" id="codes">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Codes and Registrations</span>
      <h2 style="color:#fff;">Everything a contracting officer needs to verify the record.</h2>
    </div>
    <div class="grid-2 reveal" style="gap:22px; align-items:start;">
      <div class="card-glass" style="padding:30px;">
        <span class="card-eyebrow">Entity</span>
        <dl class="spec-list" style="margin-top:8px;">
          {spec("Legal name", "Pogue Digital Solutions LLC", mono=False)}
          {spec("Entity type", "Limited Liability Company, Texas", mono=False)}
          {spec("Unique Entity ID (UEI)", UEI)}
          {spec("CAGE code", CAGE)}
          {spec("SAM.gov registration", "Active &middot; Purpose: All Awards", mono=False)}
          {spec("Business status", "Veteran-owned small business", mono=False)}
          {spec("Certifications", "Texas HUB application in progress", mono=False)}
          {spec("Headquarters", "Conroe, Texas (Montgomery County)", mono=False)}
          {spec("Phone", f'<a href="tel:+1{PHONE.replace("-", "")}">{PHONE}</a>', mono=False)}
          {spec("Email", f'<a href="mailto:{EMAIL}">{EMAIL}</a>', mono=False)}
          {spec("Point of contact", "John M Pogue, Founder and Creative Strategist", mono=False)}
        </dl>
      </div>
      <div style="display:grid; gap:22px;">
        <div class="card-glass" style="padding:30px;">
          <span class="card-eyebrow">NAICS Codes</span>
          <table class="code-table"><tbody>{naics_rows}</tbody></table>
        </div>
        <div class="card-glass" style="padding:30px;">
          <span class="card-eyebrow">Product and Service Codes (PSC)</span>
          <table class="code-table"><tbody>{psc_rows}</tbody></table>
        </div>
      </div>
    </div>
    <div class="card-glass reveal cap-row" style="padding:30px; margin-top:22px;">
      <div>
        <span class="card-eyebrow">Capability Statement</span>
        <h3 style="font-size:20px; margin-bottom:6px;">One page. Ready to send.</h3>
        <p style="font-size:14.5px;">Email with your agency or prime contractor and the opportunity you have in mind. John will reply with the current capability statement PDF, and everything on it is already on this page.</p>
      </div>
      <a href="{CAP_MAIL}" class="btn btn-gold">Request the Capability Statement <span class="btn-arrow">&rarr;</span></a>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="on-paper-dim">
  <div class="wrap" style="max-width:820px;">
    <div class="section-head reveal"><span class="eyebrow">Contracting Questions</span><h2>Frequently Asked Questions</h2></div>
    {faq(FAQS)}
  </div>
</section>

{cta_band("Start the Conversation", "A thirty-minute call to find out whether there is a fit, with no proposal required first.", primary=("Request the Capability Statement", CAP_MAIL), secondary=("Schedule a Call", CALENDLY), closing="&ldquo;Don&rsquo;t tell me it can&rsquo;t be done.&rdquo;")}
''' + footer()

open("./government.html", "w").write(html)
print("government.html", len(html))
