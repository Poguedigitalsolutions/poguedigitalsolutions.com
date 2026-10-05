import json
from parts import *

FAQS = [
 ("What is The Compass Method?", "The Compass Method is a decision-making and personal-development framework created by John M Pogue. It uses five points, Heart at the center with Purpose, Skill, Opportunity, and Service around it, to help a person see where they are and where they are headed before they make a decision."),
 ("Is The Compass Method for businesses or for people?", "Both, in that order of discovery. It was written for people first: founders, veterans in transition, anyone at a turning point. Businesses pick it up because a company cannot communicate clearly until the person running it knows what they believe and who they serve."),
 ("How does The Compass Method connect to Brand Voice AI?", "The Compass Method helps a founder uncover their direction. Brand Voice AI turns that direction into a working system. Mission, values, audience, stories, and voice come out of the Compass work and go into the Brand Voice AI foundation."),
 ("Is there a book?", "Yes, The Compass Method is in development as a book with a companion workbook. John tells his own stories against each compass point to prompt the reader's stories, with exercises along the way. He does not tell the reader what to do."),
 ("Can The Compass Method be taught to a group?", "Yes. Workshops, speaking, and veteran transition programs are part of the plan, along with a certified facilitator path. Ask about a workshop through the Contact page."),
]

LD = json.dumps({"@context": "https://schema.org", "@graph": [
 {"@type": "CreativeWork", "name": "The Compass Method", "url": SITE + "/compass-method.html",
  "author": {"@type": "Person", "name": "John M Pogue", "url": SITE + "/about.html"},
  "description": "A decision-making and personal-development framework with Heart at the center and Purpose, Skill, Opportunity, and Service at the four points. Lead with Heart. Navigate with Purpose.",
  "keywords": ["Compass Method", "personal development framework", "veteran transition", "founder clarity", "John M Pogue"]},
 json.loads(breadcrumb("The Compass Method", "compass-method.html"))]}, indent=1)

def compass_diagram():
    """Large interactive compass: five points as labeled nodes. Pure SVG, no JS needed."""
    return '''<svg viewBox="0 0 640 640" style="width:100%; max-width:560px; margin:0 auto; display:block;" role="img" aria-label="The Compass Method: Heart at the center; Purpose to the North, Skill to the East, Service to the South, Opportunity to the West">
  <defs>
    <radialGradient id="heartglow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#F2D680" stop-opacity="0.55"/><stop offset="100%" stop-color="#F2D680" stop-opacity="0"/></radialGradient>
  </defs>
  <circle cx="320" cy="320" r="290" fill="none" stroke="rgba(212,175,55,0.35)" stroke-width="1"/>
  <circle cx="320" cy="320" r="270" fill="none" stroke="rgba(212,175,55,0.18)" stroke-width="1" stroke-dasharray="2 9"/>
  <g stroke="rgba(212,175,55,0.3)" stroke-width="1"><line x1="320" y1="50" x2="320" y2="590"/><line x1="50" y1="320" x2="590" y2="320"/></g>
  <path d="M320 70 L336 304 L320 320 L304 304 Z M320 570 L336 336 L320 320 L304 336 Z M70 320 L304 304 L320 320 L304 336 Z M570 320 L336 304 L320 320 L336 336 Z" fill="#D4AF37" fill-opacity="0.16" stroke="#D4AF37" stroke-opacity="0.55" stroke-width="1"/>
  <circle cx="320" cy="320" r="120" fill="url(#heartglow)"/>
  <circle cx="320" cy="320" r="62" fill="#0B1F3A" stroke="#F2D680" stroke-width="2"/>
  <text x="320" y="312" text-anchor="middle" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="3" fill="#F2D680">CENTER</text>
  <text x="320" y="340" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-size="26" fill="#FFFFFF">Heart</text>
  <g font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="3" fill="#D4AF37" text-anchor="middle">
    <text x="320" y="40">NORTH</text><text x="320" y="622">SOUTH</text><text x="608" y="326" text-anchor="start">EAST</text><text x="32" y="326" text-anchor="end">WEST</text>
  </g>
  <g font-family="Fraunces, Georgia, serif" font-size="24" fill="#FFFFFF" text-anchor="middle">
    <text x="320" y="118">Purpose</text><text x="320" y="548">Service</text><text x="500" y="328">Skill</text><text x="140" y="328">Opportunity</text>
  </g>
  <g font-family="Inter, sans-serif" font-size="12" fill="rgba(255,255,255,0.6)" text-anchor="middle">
    <text x="320" y="140">your true north, your values</text><text x="320" y="570">community, family, giving back</text><text x="500" y="350">your natural talents</text><text x="140" y="350">what the world is offering</text>
  </g>
</svg>'''

def point(dir_, word, sub, body, story_title, story):
    return f'''<div class="card-glass reveal" style="padding:34px;">
  <span class="card-eyebrow">{dir_}</span>
  <h3 style="font-size:24px; margin-bottom:4px;">{word}</h3>
  <p style="font-family:var(--font-mono); font-size:11.5px; letter-spacing:0.08em; text-transform:uppercase; color:var(--gold-bright); margin-bottom:14px;">{sub}</p>
  <p style="font-size:15px;">{body}</p>
  <div style="margin-top:20px; padding-top:18px; border-top:1px solid rgba(212,175,55,0.2);">
    <p style="font-family:var(--font-mono); font-size:10.5px; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin-bottom:8px;">A story from John &middot; {story_title}</p>
    <p style="font-size:14.5px; font-style:italic; color:rgba(255,255,255,0.78);">{story}</p>
  </div>
</div>'''

html = head("The Compass Method | Lead with Heart. Navigate with Purpose.",
  "The Compass Method is John M Pogue's framework for finding direction: Heart at the center, with Purpose, Skill, Opportunity, and Service at the four points. For founders, veterans in transition, and anyone at a turning point.",
  "compass-method.html", jsonld=[LD, faq_jsonld(FAQS)]) + header("compass-method.html") + f'''

<!-- HERO -->
<section class="on-ink tight" style="padding-top:56px; padding-bottom:80px;">
  <div class="glow-blob" style="width:560px; height:560px; background:radial-gradient(circle, rgba(212,175,55,0.2), transparent 70%); top:-120px; right:-120px;"></div>
  <div class="wrap" style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:56px; align-items:center;">
    <div class="reveal">
      <span class="eyebrow">The Compass Method</span>
      <h1 style="font-size:clamp(38px,5.8vw,70px); color:#fff; margin-top:16px;">Lead with Heart.<br>Navigate with <em>Purpose.</em></h1>
      <p style="font-size:17.5px; max-width:560px; margin-top:22px;">Before direction comes reflection. The Compass Method is a way of seeing where you are and where you are headed, so the decisions you make are yours and not somebody else&rsquo;s marketing.</p>
      <p style="font-size:17.5px; max-width:560px;">It was built for people first. Businesses borrow it because a company cannot say clearly what it believes until the person running it can.</p>
      <div style="display:flex; gap:16px; margin-top:32px; flex-wrap:wrap;">
        <a href="assessments.html#compass" class="btn btn-gold">Take the Compass Assessment <span class="btn-arrow">&rarr;</span></a>
        <a href="#five-points" class="btn btn-outline-gold">See the Five Points</a>
      </div>
    </div>
    <div class="reveal">{compass_diagram()}</div>
  </div>
</section>

<!-- THE IDEA -->
<section>
  <div class="wrap" style="max-width:760px;">
    <span class="eyebrow reveal">The Idea</span>
    <h2 class="reveal" style="margin-top:14px;">Earned, not purchased.</h2>
    <div class="reveal stack-lg" style="font-size:17.5px; line-height:1.8; margin-top:20px;">
      <p>Most of us are navigating by somebody else&rsquo;s map. We buy the thing because the ad made us afraid of missing it. We take the job because it was offered. We describe ourselves in words we picked up from people who were trying to sell us something. Then we wonder why the life we built does not feel like ours.</p>
      <p>The Compass Method starts from a different place. It assumes you already carry the answers, and that what you lack is a way to read them. Five points, one at the center and four around it. Each one is a question you ask yourself, and each one gets easier to answer once you have told the story that goes with it.</p>
      <p>I do not tell you what to do. I tell you what happened to me at each point of the compass, and the stories shake yours loose. That is the whole method. The exercises and the workbook are there to catch what comes out.</p>
    </div>
    <p class="quote-band reveal" style="margin-top:36px;">If I can see what is on your heart, I can always find your true north.</p>
  </div>
</section>

<!-- FIVE POINTS -->
<section class="on-ink" id="five-points">
  <div class="glow-blob" style="width:520px; height:520px; background:radial-gradient(circle, rgba(212,175,55,0.14), transparent 70%); top:10%; right:-160px;"></div>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">The Five Points</span>
      <h2 style="color:#fff;">Heart at the center. Four directions around it.</h2>
      <p>Each point is a question. Each question has a story. Here are mine.</p>
    </div>

    <div class="card-glass reveal" style="padding:40px; margin-bottom:22px; border-color:rgba(242,214,128,0.5); background:linear-gradient(160deg, rgba(242,214,128,0.1), rgba(255,255,255,0.02));">
      <span class="card-eyebrow">Center</span>
      <h3 style="font-size:28px; margin-bottom:4px;">Heart</h3>
      <p style="font-family:var(--font-mono); font-size:11.5px; letter-spacing:0.08em; text-transform:uppercase; color:var(--gold-bright); margin-bottom:14px;">What do you care about when nobody is scoring you?</p>
      <p style="font-size:15.5px; max-width:720px;">Everything else on the compass is read from here. Purpose without heart is ambition. Skill without heart is a résumé. Opportunity without heart is a trap, and service without heart burns out. The center is not the softest point on the compass. It is the one that holds the needle steady.</p>
      <div class="grid-2" style="margin-top:24px; gap:20px;">
        <div style="padding-top:18px; border-top:1px solid rgba(212,175,55,0.2);">
          <p style="font-family:var(--font-mono); font-size:10.5px; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin-bottom:8px;">A story from John &middot; The 100-foot dive</p>
          <p style="font-size:14.5px; font-style:italic; color:rgba(255,255,255,0.78);">During advanced scuba certification in the Navy, our class sank to the floor at 100 feet and knelt there. I looked up at the line where the ocean met the sky and thought, this is how fish feel when they watch us go into space. When we surfaced, the instructor asked why I had barely used any air. I was relaxed. I was just breathing. Everyone else burned their tanks fighting the water. The heart is the part of you that is not fighting.</p>
        </div>
        <div style="padding-top:18px; border-top:1px solid rgba(212,175,55,0.2);">
          <p style="font-family:var(--font-mono); font-size:10.5px; letter-spacing:0.1em; text-transform:uppercase; color:var(--gold); margin-bottom:8px;">A story from John &middot; The shoebox of shells</p>
          <p style="font-size:14.5px; font-style:italic; color:rgba(255,255,255,0.78);">I have a shoebox of shells I dove for off the ocean floor in Okinawa. One day they will be set into a coffee table. It will have a story to it, not &ldquo;oh, I got these from Hobby Lobby.&rdquo; Earned versus purchased. That is the thesis of this whole method. The things you worked for are the things that tell you who you are.</p>
        </div>
      </div>
    </div>

    <div class="grid-2" style="gap:22px;">
      {point("North", "Purpose", "Your true north, your values. Where are you actually headed?",
             "Purpose is not a mission statement. It is the direction you drift toward when nobody is steering. Finding it means noticing what you keep coming back to, what you refuse to do even when it would pay, and what you would still do if the money stopped.",
             "Create more than you consume",
             "My VA benefits cover my basics and paid for my master&rsquo;s degree. I do not have to work. Because I have been given the gift of being taken care of like that, I want to bring more to the world than I take from it. Create more than you consume. I did not plan that as a purpose. I noticed I was already living by it.")}
      {point("East", "Skill", "Your natural talents. What comes easily to you that is hard for others?",
             "Skill is the sunrise point because talent shows up early, usually before you have a name for it. Most people undervalue what comes naturally and overvalue what they struggled to learn. The East asks you to look at what you do without trying.",
             "The truck conversations",
             "I let my younger son drive my truck and I keep the tank full, partly because the truck is where we are both trapped and have to talk. He cycled through military, CIA, police, and I priced each one out honestly. Then one day: &ldquo;Dad, I finally figured it out. I want to be a fireman. I&rsquo;ve got a heart to help people.&rdquo; I told him I could see that in him. I had seen it for years. The method is not about pointing someone somewhere new. It is about leading them where they are already going.")}
      {point("West", "Opportunity", "What the world is offering. What doors are open right now?",
             "Opportunity is the sunset point. It is time-bound, and it is the easiest point to fake. Every ad is an opportunity dressed up as urgency. The West asks whether a door is open because it is right for you, or because someone wants you to walk through it.",
             "The master&rsquo;s at 51",
             "After a layoff in my late forties I went back to school for a master&rsquo;s in digital marketing. The degree did not erase the earlier chapters of my life: healthcare, the Navy, customer support, design. It reorganized them. Experience that had looked scattered turned into raw material. The opportunity was not the degree. It was the chance to see my own history as an asset instead of a detour.")}
      {point("South", "Service", "Community, family, giving back. Who are you doing this for?",
             "Service grounds the compass. It is the point that keeps purpose from becoming self-importance and opportunity from becoming greed. The South asks who benefits when you get this right, and whether that answer includes anyone besides you.",
             "See one, do one, teach one",
             "In the Navy medical world, that is how you learn: watch it once, do it once, then teach it to the next person. The teaching step is not optional. You do not understand something until you can explain it to someone who has never done it. That is why I write this method as stories rather than instructions. Teaching is the service. If you lead with your heart, you will love the people you serve.")}
    </div>
  </div>
</section>

<!-- HOW IT WORKS / FOR WHOM -->
<section class="on-paper-dim">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">How It Is Used</span><h2>A book first. Then everything the book makes possible.</h2></div>
    <div class="grid-3 reveal">
      <div class="card"><span class="card-eyebrow">In progress</span><h3 style="font-size:18px;">The Book and Workbook</h3><p style="font-size:14.5px;">John&rsquo;s own stories against each compass point, with exercises and a companion workbook to catch what the stories bring up in you.</p></div>
      <div class="card"><span class="card-eyebrow">Available now</span><h3 style="font-size:18px;">The Compass Assessment</h3><p style="font-size:14.5px;">A ten-minute reflection on all five points. The result is a read on which point needs your attention first.</p><a href="assessments.html#compass" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;">Find Your Bearing</a></div>
      <div class="card"><span class="card-eyebrow">By request</span><h3 style="font-size:18px;">Workshops and Speaking</h3><p style="font-size:14.5px;">Group sessions for teams, veteran transition programs, and communities. A certified facilitator path is planned.</p><a href="contact.html#workshop" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;">Request a Session</a></div>
    </div>
    <div class="section-head reveal" style="margin-top:64px;"><span class="eyebrow">Who It Is For</span><h2>People at a turning point.</h2></div>
    <div class="grid-4 reveal">
      <div class="card"><h3 style="font-size:16.5px;">Founders</h3><p style="font-size:14px;">Who need to know what they believe before they can say it to a customer.</p></div>
      <div class="card"><h3 style="font-size:16.5px;">Veterans in Transition</h3><p style="font-size:14px;">Who have a hundred skills and no civilian words for them yet.</p></div>
      <div class="card"><h3 style="font-size:16.5px;">Career Changers</h3><p style="font-size:14px;">Who suspect their scattered history is an asset and want to prove it.</p></div>
      <div class="card"><h3 style="font-size:16.5px;">Anyone Mid-Life</h3><p style="font-size:14px;">Who was told the meaningful direction should be fixed by now, and does not believe it.</p></div>
    </div>
  </div>
</section>

<!-- BRIDGE TO BRAND VOICE AI -->
<section class="on-ink">
  <div class="wrap" style="display:grid; grid-template-columns:1fr 1fr; gap:48px; align-items:center;">
    <div class="reveal">
      <span class="eyebrow">Where It Leads</span>
      <h2 style="color:#fff; margin-top:14px;">Business direction begins with human direction.</h2>
      <p style="margin-top:16px; font-size:16px;">Before a business can train AI to communicate clearly, the person running it has to know what they believe, who they serve, and where they are going. The Compass Method uncovers that. Brand Voice AI turns it into a working system.</p>
      <p style="font-size:16px;">Mission, values, audience, stories, and voice come out of the Compass work. They go straight into the Brand Voice AI foundation.</p>
      <a href="solutions.html#brand-voice-ai" class="btn btn-outline-gold" style="margin-top:24px;">See Brand Voice AI <span class="btn-arrow">&rarr;</span></a>
    </div>
    <div class="card-glass reveal" style="padding:34px;">
      <div class="bearing" style="margin-bottom:22px;"><span class="bearing-label">COMPASS</span><div class="bearing-rule"></div><span class="bearing-label">BRAND VOICE AI</span></div>
      <ul class="feature-list cols-1">
        <li><strong style="color:#fff;">Heart</strong> becomes the values your brand will not compromise</li>
        <li><strong style="color:#fff;">Purpose</strong> becomes the mission statement that is actually true</li>
        <li><strong style="color:#fff;">Skill</strong> becomes the offer you are uniquely able to make</li>
        <li><strong style="color:#fff;">Opportunity</strong> becomes the audience you choose to serve</li>
        <li><strong style="color:#fff;">Service</strong> becomes the stories your customers remember</li>
      </ul>
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

{cta_band("Before Direction Comes Reflection", "Take ten minutes with the Compass Assessment and see which point needs your attention first.", primary=("Take the Compass Assessment", "assessments.html#compass"), closing="&ldquo;Lead with Heart. Navigate with Purpose.&rdquo;")}
''' + footer()

open("./compass-method.html", "w").write(html)
print("compass-method.html", len(html))
