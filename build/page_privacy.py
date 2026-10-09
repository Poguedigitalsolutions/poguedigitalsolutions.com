"""Privacy Policy. Plain-language policy that describes what this static site actually does:
one blog signup form (ClickFunnels), no advertising cookies, Cloudflare hosting and cookie-free Web Analytics, Google Fonts,
outbound links to Calendly and LinkedIn, and email through Gmail. Update it when the stack changes."""
from parts import *
import json

UPDATED = "October 8, 2026"
UPDATED_ISO = "2026-10-08"

SECTIONS = [
("Who we are", f'''
<p>This website, poguedigitalsolutions.com, is run by Pogue Digital Solutions, LLC, a veteran-owned consultancy based in Conroe, Texas. John M Pogue is the founder. When this policy says "we," "us," or "our," it means Pogue Digital Solutions, LLC.</p>
<p>This policy explains what information the website collects, why, who else touches it, and what you can ask us to do with it. We wrote it in plain language on purpose.</p>
'''),
("The short version", '''
<ul>
<li>The only form on this site is the blog signup, which asks for your first name and email so we can send you new articles. There are no accounts and no comment sections.</li>
<li>We do not use advertising cookies or tracking pixels, and we do not sell or rent your information to anyone.</li>
<li>We count visits with Cloudflare Web Analytics, which does not use cookies and does not follow you across other websites.</li>
<li>If you email us or book a call, we use what you send only to reply and to do the work you asked about.</li>
</ul>
'''),
("Information you choose to give us", f'''
<p><strong>Email.</strong> Buttons on this site that say "email" open your own email program with a message addressed to {EMAIL}. Nothing is sent until you press send. When you do, we receive whatever you wrote, along with your name and email address.</p>
<p><strong>Booking a call.</strong> The "Book a Call" buttons take you to Calendly, a separate scheduling service. Calendly collects the details you enter there, such as your name, email address, and answers to any booking questions, and shares them with us so we can hold the meeting. Calendly's own privacy policy covers how Calendly handles that information.</p>
<p><strong>Blog email updates.</strong> If you subscribe to the blog, you give us your first name and email address. The signup form is run by ClickFunnels, which stores your details as a contact for us and sends the emails. We use them only to send new articles and occasional updates from Pogue Digital Solutions, LLC. Every email has an unsubscribe link, and you can also ask us by email to remove you.</p>
<p><strong>Assessments and workshop requests.</strong> These currently work by email, so the same rules as email apply.</p>
<p>We use this information to answer your questions, schedule and hold meetings, prepare proposals, and deliver services you hire us for. We keep it only as long as we need it for those purposes or as long as the law or our own records require, such as for tax and contract records.</p>
'''),
("Information collected automatically", '''
<p><strong>Visit counts.</strong> We use Cloudflare Web Analytics to see which pages people read, which sites sent them here, and general details such as country, browser, and device type. It does not set cookies, does not create a profile of you, and is not used for advertising.</p>
<p><strong>Server and security logs.</strong> Cloudflare hosts and protects this site. Like any web host, it processes technical information such as your IP address and browser details to deliver pages, block attacks, and keep the site running.</p>
<p><strong>Fonts.</strong> This site loads its typefaces from Google Fonts. When a page loads, your browser asks Google's servers for the font files, which means Google receives your IP address and basic browser information. Google says it does not use Google Fonts requests to build advertising profiles.</p>
<p><strong>Cookies.</strong> We do not set advertising cookies on this site. Cloudflare may use a strictly necessary security cookie to tell real visitors from automated attacks. The blog signup form loads a ClickFunnels script that may set its own cookies and record that the form was viewed and submitted. Calendly and LinkedIn set their own cookies once you go to their sites.</p>
'''),
("Services we rely on", '''
<p>A few outside companies handle parts of how this site and business run. Each has its own privacy policy:</p>
<ul>
<li><strong>Cloudflare</strong>: website hosting, security, email forwarding, and cookie-free visit counts.</li>
<li><strong>Google</strong>: Google Fonts on this site, and Gmail for business email.</li>
<li><strong>Calendly</strong>: scheduling calls.</li>
<li><strong>ClickFunnels</strong>: the blog signup form, the subscriber list, and blog update emails.</li>
<li><strong>LinkedIn</strong>: only if you follow a link to John M Pogue's profile.</li>
</ul>
<p>Links to other websites, including the articles cited in our blog, lead to sites we do not control. Their privacy practices are their own.</p>
'''),
("When we share information", '''
<p>We do not sell, rent, or trade personal information. We share it only:</p>
<ul>
<li>with the service providers listed above, so they can do their part;</li>
<li>with your permission, for example when you ask us to coordinate with someone on your team;</li>
<li>when the law requires it, such as a valid subpoena or court order; or</li>
<li>to protect our rights or someone's safety if there is a real threat.</li>
</ul>
'''),
("Client work and AI tools", '''
<p>Our consulting work often involves AI tools. If you become a client, our written agreement with you will spell out how we handle the business information you share for a project, which tools may process it, and how a person reviews the work. We do not put a visitor's emails or booking details into AI tools for any purpose other than replying to and serving that person.</p>
'''),
("How we protect information", '''
<p>We use reasonable administrative and technical safeguards and reputable service providers to protect the information we hold. No website or email system is perfectly secure, so please do not send passwords, full account numbers, or other highly sensitive details by email.</p>
'''),
("Your choices and requests", f'''
<p>You can ask us to tell you what personal information we have about you, correct it, or delete it. Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will respond within a reasonable time. We may need to confirm who you are first, and we may keep records the law requires us to keep.</p>
<p>You can also block or delete cookies in your browser settings. Because this site does not depend on cookies, it will work the same either way.</p>
'''),
("Children", '''
<p>This site is meant for business owners and organizations. It is not directed to children under 13, and we do not knowingly collect information from them. If you believe a child has sent us personal information, email us and we will delete it.</p>
'''),
("Changes to this policy", f'''
<p>If the way this site works changes, for example if we add a form, a newsletter, or a new analytics tool, we will update this page and the date below. The date at the top always shows the latest version.</p>
'''),
("Contact", f'''
<p>Questions about this policy or your information:</p>
<p>Pogue Digital Solutions, LLC<br>Conroe, Texas<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
'''),
]

toc = "".join(f'<li><a href="privacy.html#s{i}">{t}</a></li>' for i, (t, _) in enumerate(SECTIONS, 1))
body = "".join(f'<h2 id="s{i}">{t}</h2>\n{h.strip()}\n' for i, (t, h) in enumerate(SECTIONS, 1))

DESC = "How Pogue Digital Solutions, LLC handles information on poguedigitalsolutions.com: the blog signup, cookie-free analytics, no advertising cookies, and plain answers about email and Calendly bookings."

jsonld = [json.dumps({
    "@context": "https://schema.org", "@type": "WebPage", "name": "Privacy Policy",
    "url": f"{SITE}/privacy", "description": DESC, "dateModified": UPDATED_ISO,
    "publisher": {"@id": ORG_ID}}, indent=2),
    breadcrumb("Privacy Policy", "privacy.html")]

page = head("Privacy Policy | Pogue Digital Solutions", DESC, "privacy.html", jsonld=jsonld) + header("") + f'''
<section class="on-ink tight" style="padding-top:56px; padding-bottom:64px;">
  {compass_svg()}
  <div class="wrap reveal" style="max-width:820px;">
    <nav aria-label="Breadcrumb" class="crumbs"><a href="index.html">Home</a> / Privacy Policy</nav>
    <span class="eyebrow" style="display:block; margin-top:22px;">Legal</span>
    <h1 style="font-size:clamp(32px,4.6vw,54px); color:#fff; margin-top:14px;">Privacy Policy</h1>
    <p style="font-size:17px; margin-top:18px; max-width:680px;">What this website collects, why, and what you can ask us to do with it.</p>
    <div class="article-meta" style="margin-top:28px;"><span>Last updated <time datetime="{UPDATED_ISO}">{UPDATED}</time></span></div>
  </div>
</section>

<section>
  <div class="wrap">
    <article class="article-body reveal">
<nav class="article-toc" aria-label="On this page"><span class="eyebrow">On this page</span><ol>{toc}</ol></nav>
{body}
    </article>
  </div>
</section>
''' + footer()

open("privacy.html", "w").write(page)
print("privacy.html", len(page))
