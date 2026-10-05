import json
from parts import *

FAQS = [
 ("What services does Pogue Digital Solutions provide?", "Pogue Digital Solutions, LLC provides Brand Voice AI development, AI and automation planning, digital strategy, business knowledge organization, customer journey mapping, content systems, training, workshops, and organizational consulting."),
 ("What is the difference between Brand Voice AI and regular AI content creation?", "Regular AI content creation typically begins with a prompt and produces an isolated piece of content. Brand Voice AI begins by organizing the business&rsquo;s identity, knowledge, audience, stories, messaging, processes, and approval standards. That foundation supports greater consistency across many forms of communication and work."),
 ("Can you help a business that has not used AI before?", "Yes. We can begin with an AI Readiness Assessment and help identify practical, low-risk starting points based on the business&rsquo;s goals and current processes."),
 ("Do you build automations?", "We help identify, plan, and develop practical AI-assisted workflows and automation systems. The appropriate approach depends on the tools involved, the process being improved, and the level of technical implementation required."),
 ("Can you help us choose AI tools?", "Yes, but tool selection comes after the business need is understood. We evaluate whether an existing tool can solve the problem before recommending additional software."),
 ("Do you offer one-time consulting?", "Yes. Strategy sessions, assessments, project-based consulting, workshops, and ongoing advisory arrangements are available."),
 ("Can you train our team?", "Yes. Training can be customized for leadership teams, employees, entrepreneurs, veteran-owned businesses, nonprofits, educational organizations, and professional communities."),
 ("Do you work with clients outside Texas?", "Yes. Pogue Digital Solutions is based in Conroe, Texas, and can work virtually with clients and organizations throughout the United States."),
 ("Do you work with government agencies and contractors?", "Yes. Services for government and organizational clients can include training, communication strategy, process documentation, digital outreach, knowledge organization, AI adoption planning, and curriculum development."),
 ("Where should I begin?", "Begin with an assessment when the underlying problem is unclear. Schedule a strategy conversation when you already have a specific objective or project in mind."),
]

def service(name, desc):
    return {"@type": "Service", "name": name, "serviceType": name,
            "provider": {"@type": "Organization", "name": "Pogue Digital Solutions, LLC", "url": SITE + "/"},
            "areaServed": ["Conroe, Texas", "Greater Houston", "United States"], "description": desc}

SERVICES_LD = json.dumps({"@context": "https://schema.org", "@graph": [
 service("Brand Voice AI", "An AI-assisted business operating system that captures and organizes the information that defines how a company thinks, communicates, serves customers, and makes decisions, with human approval kept in the process."),
 service("AI and Automation", "Examining repetitive work, clarifying the process behind it, and building practical AI-assisted workflows, custom AI assistants, knowledge systems, customer follow-up, and approval workflows."),
 service("Digital Strategy", "Connecting positioning, customer journey, content, website, campaigns, customer insights, analytics, and outreach into one coordinated plan."),
 service("Training and Workshops", "Practical AI adoption, brand voice, content systems, customer journey, digital marketing, process improvement, and automation training for entrepreneurs, teams, veteran-owned businesses, and organizations."),
 service("Government and Organizational Services", "AI adoption planning, workforce training, communication strategy, process documentation, knowledge organization, and curriculum development for government, education, nonprofit, and organizational clients."),
]}, indent=1)

def li(items, cols=2):
    return f'<ul class="feature-list cols-{cols}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

html = head(
  "AI Strategy, Brand Voice & Digital Solutions | Pogue Digital Solutions",
  "Explore Brand Voice AI, AI automation, digital strategy, training, and business systems from Pogue Digital Solutions, LLC in Conroe, Texas.",
  "solutions.html",
  jsonld=[SERVICES_LD, faq_jsonld(FAQS), breadcrumb("Solutions", "solutions.html")],
) + header("solutions.html") + f'''

<!-- 1. HERO -->
<section class="on-ink tight" style="padding-top:56px; padding-bottom:88px;">
  {compass_svg()}
  <div class="glow-blob" style="width:520px; height:520px; background:radial-gradient(circle, rgba(212,175,55,0.2), transparent 70%); top:-200px; left:-160px;"></div>
  <div class="wrap" style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:56px; align-items:center;">
    <div class="reveal">
      <span class="eyebrow">Strategy. Systems. Solutions.</span>
      <h1 style="font-size:clamp(36px,5.4vw,64px); margin-top:18px; color:#fff;">Turn Business Knowledge Into Workable Systems</h1>
      <p style="font-size:17px; max-width:560px; margin-top:22px;">Your business already contains valuable knowledge, experience, ideas, stories, processes, and customer insights. The problem is that much of it may be scattered across files, platforms, conversations, and the founder&rsquo;s memory.</p>
      <p style="font-size:17px; max-width:560px;">Pogue Digital Solutions, LLC helps you organize that knowledge, clarify your direction, and build practical AI-assisted systems that support better marketing, communication, customer experiences, and business operations.</p>
      <div style="display:flex; gap:16px; margin-top:30px; flex-wrap:wrap;">
        <a href="assessments.html" class="btn btn-gold">Find the Right Solution <span class="btn-arrow">&rarr;</span></a>
        <a href="{CALENDLY}" class="btn btn-outline-gold" target="_blank" rel="noopener">Schedule a Strategy Conversation</a>
      </div>
      <p class="quote-band" style="margin-top:40px; font-size:19px;">We do not begin with software. We begin with the problem your business needs to solve.</p>
    </div>
    <div class="reveal">
      <div class="photo-card tilt no-fade" style="aspect-ratio:744/458;">
        <img src="img/hero-founder-composite.jpg" alt="John M Pogue reviewing connected AI strategy, brand voice, and business systems" width="744" height="458" loading="eager">
      </div>
    </div>
  </div>
</section>

<!-- 2. OVERVIEW -->
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Solutions Overview</span>
      <h2>Practical Solutions Built Around Your Business</h2>
      <p>There is no value in adding another tool to an unclear process. We begin by understanding what you want to accomplish, what is getting in the way, and what information your people and systems need to work effectively. Your solution may involve strategy, documentation, training, AI, automation, or a combination of all five.</p>
    </div>
    <div class="grid-4 reveal">
      <a href="#brand-voice-ai" class="card" style="text-decoration:none;"><span class="card-eyebrow">01</span><h3 style="font-size:18px;">Brand Voice AI</h3><p style="font-size:14px;">Organize your company&rsquo;s identity, knowledge, messaging, stories, customer insights, and communication standards into one connected business system.</p></a>
      <a href="#ai-automation" class="card" style="text-decoration:none;"><span class="card-eyebrow">02</span><h3 style="font-size:18px;">AI and Automation</h3><p style="font-size:14px;">Identify repetitive work and create practical AI-assisted workflows that improve efficiency without removing human judgment.</p></a>
      <a href="#digital-strategy" class="card" style="text-decoration:none;"><span class="card-eyebrow">03</span><h3 style="font-size:18px;">Digital Strategy</h3><p style="font-size:14px;">Connect your business goals, audience, content, customer journey, technology, and measurement into one coordinated direction.</p></a>
      <a href="#training" class="card" style="text-decoration:none;"><span class="card-eyebrow">04</span><h3 style="font-size:18px;">Training and Workshops</h3><p style="font-size:14px;">Help entrepreneurs, teams, and organizations understand and adopt AI, marketing, and business systems through practical instruction.</p></a>
    </div>
  </div>
</section>

<!-- 3. BRAND VOICE AI -->
<section class="on-ink" id="brand-voice-ai">
  <div class="glow-blob" style="width:520px; height:520px; background:radial-gradient(circle, rgba(212,175,55,0.16), transparent 70%); top:5%; right:-160px;"></div>
  <div class="wrap">
    <div class="solution-block reveal">
      <div>
        <span class="eyebrow">Flagship Solution</span>
        <h2 style="color:#fff; margin-top:14px;">Brand Voice AI Business Operating System&trade;</h2>
        <p style="margin-top:18px; font-size:16.5px;">Most people use AI to create more content. Brand Voice AI helps businesses create greater continuity.</p>
        <p style="font-size:16.5px;">Brand Voice AI is an AI-assisted business operating system that captures and organizes the information that defines how your company thinks, communicates, serves customers, and makes decisions. Instead of asking AI to guess your voice from a short prompt, we build a structured foundation based on your actual business.</p>
      </div>
      <div class="photo-card no-fade" style="aspect-ratio:698/458;">
        <img src="img/brand-voice-ai-system.jpg" alt="Brand Voice AI organizing scattered company knowledge into connected brand identity, customer insights, messaging, processes, AI instructions, and resources" width="698" height="458" loading="lazy">
      </div>
    </div>

    <div class="grid-2 reveal" style="margin-top:56px; align-items:start;">
      <div>
        <h3 style="color:#fff; font-size:20px; margin-bottom:16px;">What Brand Voice AI Can Organize</h3>
        {li(["Mission, vision, and values","Founder knowledge and experience","Brand voice and communication standards","Products, services, and offers","Customer avatars and audience insights","Customer journeys","Stories, examples, and case studies","Content standards and campaign structures","Internal processes and playbooks","Approval requirements","AI instructions and safeguards","Frequently asked customer questions"])}
      </div>
      <div class="stack-lg">
        <div class="card-glass"><span class="card-eyebrow">Layer 1 &middot; Foundation</span><p style="font-size:14.5px;">We capture the identity and knowledge at the heart of your business: mission, values, audience, services, stories, differentiators, terminology, tone, and communication preferences.</p></div>
        <div class="card-glass"><span class="card-eyebrow">Layer 2 &middot; Playbooks</span><p style="font-size:14.5px;">We turn that foundation into usable guidance for content creation, customer communication, marketing campaigns, sales follow-up, customer journeys, approvals, and recurring business processes.</p></div>
        <div class="card-glass"><span class="card-eyebrow">Layer 3 &middot; Execution</span><p style="font-size:14.5px;">Your team and AI tools use the organized system to prepare work more efficiently and consistently. Human approval remains part of the process before important work is published, delivered, or executed.</p></div>
      </div>
    </div>

    <div class="grid-2 reveal" style="margin-top:48px; align-items:center;">
      <div>
        <h3 style="color:#fff; font-size:18px; margin-bottom:14px;">Best Fit For</h3>
        {li(["Founder-led companies","Consultants and coaches","Professional service providers","Solopreneurs preparing to grow","Businesses with inconsistent marketing","Organizations with fragmented knowledge","Teams adopting AI without clear standards","Businesses that depend heavily on founder expertise"])}
      </div>
      <div>
        <p class="quote-band">Your business knowledge becomes a working resource instead of remaining trapped in separate files, tools, and memories.</p>
        <a href="assessments.html#brand-voice" class="btn btn-gold" style="margin-top:26px;">Take the Brand Voice Quick Check <span class="btn-arrow">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>

<!-- 4. AI AND AUTOMATION -->
<section id="ai-automation">
  <div class="wrap">
    <div class="solution-block flip reveal">
      <div>
        <span class="eyebrow">Work Smarter Without Losing Control</span>
        <h2 style="margin-top:14px;">Practical AI and Automation</h2>
        <p style="margin-top:18px; font-size:16.5px;">AI should remove unnecessary friction, not introduce another layer of confusion. Pogue Digital Solutions helps businesses examine repetitive work, clarify the process behind it, and determine where AI or automation can produce meaningful improvement.</p>
        <p style="font-size:16.5px;">The goal is not to automate everything. The goal is to automate the right work while preserving human responsibility where judgment, empathy, creativity, or approval matters.</p>
        <p class="quote-band" style="margin-top:22px; font-size:19px;">Automate repetition. Support judgment. Preserve accountability.</p>
      </div>
      <div class="photo-card no-fade" style="aspect-ratio:1056/800;">
        <img src="img/ai-automation-workflow.jpg" alt="Human-approved AI workflow: a person opens big by setting intent, AI carries the middle through research, analysis, drafting, organizing, and summarizing, and a person closes big with judgment and approval" width="1056" height="800" loading="lazy">
      </div>
    </div>
    <div class="grid-3 reveal" style="margin-top:48px;">
      <div class="card"><h3 style="font-size:17px;">Knowledge Organization</h3><p style="font-size:14.5px;">Bring information from documents, notes, past content, and business records into a structure that is easier to search and use.</p></div>
      <div class="card"><h3 style="font-size:17px;">Custom AI Assistants</h3><p style="font-size:14.5px;">Create guided AI tools that support defined business activities, such as content development, customer research, email preparation, or internal knowledge access.</p></div>
      <div class="card"><h3 style="font-size:17px;">Content Workflows</h3><p style="font-size:14.5px;">Develop repeatable systems for researching, drafting, reviewing, approving, publishing, and repurposing content.</p></div>
      <div class="card"><h3 style="font-size:17px;">Customer Follow-Up</h3><p style="font-size:14.5px;">Improve how leads and customers receive information, reminders, responses, and next-step guidance.</p></div>
      <div class="card"><h3 style="font-size:17px;">Administrative Processes</h3><p style="font-size:14.5px;">Identify repetitive tasks that can be simplified, standardized, or partially automated.</p></div>
      <div class="card"><h3 style="font-size:17px;">Approval Workflows</h3><p style="font-size:14.5px;">Build checkpoints that keep people responsible for reviewing important AI-assisted work.</p></div>
    </div>
    <div class="grid-2 reveal" style="margin-top:40px; align-items:center;">
      <div>
        <h3 style="font-size:18px; margin-bottom:12px;">Tool Integration Planning</h3>
        <p style="font-size:15px;">Evaluate how your current platforms can work together before adding unnecessary software.</p>
        <h3 style="font-size:18px; margin:24px 0 12px;">Best Fit For</h3>
        {li(["Small businesses overwhelmed by repetitive work","Teams experimenting with disconnected AI tools","Businesses that rely on manual content production","Organizations with undocumented processes","Owners who want more efficiency without losing oversight","Teams that need a responsible AI adoption plan"])}
      </div>
      <div><a href="assessments.html#ai-readiness" class="btn btn-outline-navy">Take the AI Readiness Assessment <span class="btn-arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<!-- 5. DIGITAL STRATEGY -->
<section class="on-ink" id="digital-strategy">
  <div class="glow-blob" style="width:460px; height:460px; background:radial-gradient(circle, rgba(212,175,55,0.14), transparent 70%); bottom:-160px; left:-120px;"></div>
  <div class="wrap">
    <div class="solution-block reveal">
      <div>
        <span class="eyebrow">Direction Before Tactics</span>
        <h2 style="color:#fff; margin-top:14px;">Digital Strategy That Connects the Pieces</h2>
        <p style="margin-top:18px; font-size:16.5px;">Your website, social media, email, advertising, customer experience, analytics, and technology should not operate as separate islands. Digital strategy connects those elements to one business objective and one customer journey.</p>
        <p style="font-size:16.5px;">Pogue Digital Solutions helps you determine who you are trying to reach, what they need to understand, what actions they should take, and how each digital touchpoint supports that movement.</p>
        <p class="quote-band" style="margin-top:22px; font-size:19px;">Every platform should have a purpose. Every message should support the customer journey.</p>
      </div>
      <div class="photo-card no-fade" style="aspect-ratio:906/804;">
        <img src="img/digital-strategy-journey.jpg" alt="Digital strategy diagram connecting website, social media, email, content, customer service, data and analytics, and paid advertising around the customer" width="906" height="804" loading="lazy">
      </div>
    </div>
    <div class="grid-4 reveal" style="margin-top:48px;">
      <div class="card-glass"><h3 style="font-size:16px;">Positioning and Messaging</h3><p style="font-size:14px;">Clarify how your company explains what it does, who it serves, and why its approach is different.</p></div>
      <div class="card-glass"><h3 style="font-size:16px;">Customer Journey Development</h3><p style="font-size:14px;">Map how people move from first awareness to inquiry, purchase, service, retention, and referral.</p></div>
      <div class="card-glass"><h3 style="font-size:16px;">Content Strategy</h3><p style="font-size:14px;">Develop content themes, formats, channels, and publishing priorities based on business goals and customer needs.</p></div>
      <div class="card-glass"><h3 style="font-size:16px;">Website Strategy</h3><p style="font-size:14px;">Improve the structure, messaging, calls to action, and visitor journey across your website.</p></div>
      <div class="card-glass"><h3 style="font-size:16px;">Campaign Planning</h3><p style="font-size:14px;">Connect content, email, social media, landing pages, offers, and follow-up into coordinated campaigns.</p></div>
      <div class="card-glass"><h3 style="font-size:16px;">Customer Insights</h3><p style="font-size:14px;">Use interviews, research, feedback, and behavioral information to better understand the people you serve.</p></div>
      <div class="card-glass"><h3 style="font-size:16px;">Analytics and Reporting</h3><p style="font-size:14px;">Identify meaningful measurements and create reporting structures that support better decisions.</p></div>
      <div class="card-glass"><h3 style="font-size:16px;">Digital Outreach</h3><p style="font-size:14px;">Develop practical plans for reaching customers, partners, organizations, and referral sources.</p></div>
    </div>
    <div class="grid-2 reveal" style="margin-top:40px; align-items:center;">
      <div>
        <h3 style="color:#fff; font-size:18px; margin-bottom:12px;">Best Fit For</h3>
        {li(["Businesses with disconnected marketing activities","Founders who are unsure what to prioritize","Companies preparing for a website redesign","Businesses launching a new service","Organizations that need clearer messaging","Teams collecting data without using it effectively"])}
      </div>
      <div><a href="assessments.html#strategic" class="btn btn-outline-gold">Request a Strategic Assessment <span class="btn-arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<!-- 6. TRAINING -->
<section class="on-paper-dim" id="training">
  <div class="wrap">
    <div class="solution-block flip reveal">
      <div>
        <span class="eyebrow">See One. Do One. Teach One.</span>
        <h2 style="margin-top:14px;">Practical Training for Real Work</h2>
        <p style="margin-top:18px; font-size:16.5px;">Learning a tool is not the same as knowing how to apply it responsibly inside a business. Pogue Digital Solutions provides training and workshops that connect technology, strategy, communication, and human judgment.</p>
        <p style="font-size:16.5px;">Sessions can be delivered for entrepreneurs, teams, veteran-owned businesses, educational organizations, nonprofits, government-related organizations, and professional communities.</p>
        <p class="quote-band" style="margin-top:22px; font-size:19px;">The purpose of training is not to impress people with technology. It is to help them use it with clarity and confidence.</p>
      </div>
      <div class="photo-card" style="aspect-ratio:910/808;">
        <img src="img/training-workshop.jpg" alt="John M Pogue presenting a practical AI and digital strategy workshop to business owners and organizational teams" width="910" height="808" loading="lazy">
        <span class="photo-caption">Practical AI for real work</span>
      </div>
    </div>
    <div class="grid-4 reveal" style="margin-top:48px;">
      <div class="card"><h3 style="font-size:16px;">Practical AI Adoption</h3><p style="font-size:14px;">Understand what AI can do, where it can help, and where human review is still essential.</p></div>
      <div class="card"><h3 style="font-size:16px;">Brand Voice and Messaging</h3><p style="font-size:14px;">Define how an organization communicates and translate those standards into guidance people and AI can follow.</p></div>
      <div class="card"><h3 style="font-size:16px;">AI-Assisted Content Systems</h3><p style="font-size:14px;">Create structured workflows for research, drafting, approval, publication, and repurposing.</p></div>
      <div class="card"><h3 style="font-size:16px;">Customer Journey Mapping</h3><p style="font-size:14px;">Understand how people discover, evaluate, choose, experience, and recommend a business.</p></div>
      <div class="card"><h3 style="font-size:16px;">Digital Marketing Strategy</h3><p style="font-size:14px;">Connect audience, message, content, channels, offers, and measurement.</p></div>
      <div class="card"><h3 style="font-size:16px;">Business Process Improvement</h3><p style="font-size:14px;">Identify bottlenecks, repeated work, unclear responsibilities, and opportunities for better systems.</p></div>
      <div class="card"><h3 style="font-size:16px;">Automation Planning</h3><p style="font-size:14px;">Learn how to evaluate automation opportunities before selecting software.</p></div>
      <div class="card"><h3 style="font-size:16px;">Human-Centered AI</h3><p style="font-size:14px;">Explore responsible use, accountability, privacy, oversight, and the role of human experience.</p></div>
    </div>
    <div class="grid-2 reveal" style="margin-top:40px; align-items:center;">
      <div>
        <h3 style="font-size:18px; margin-bottom:12px;">Training Formats</h3>
        {li(["Virtual workshops","In-person workshops","Team training","Group presentations","Conference sessions","Community education","Customized curriculum","Small-business intensives"])}
      </div>
      <div><a href="contact.html#workshop" class="btn btn-outline-navy">View Training and Workshop Options <span class="btn-arrow">&rarr;</span></a></div>
    </div>
  </div>
</section>

<!-- 7. GOVERNMENT AND ORGANIZATIONS -->
<section class="on-ink" id="organizations">
  <div class="wrap">
    <div class="grid-2 reveal" style="align-items:start; gap:48px;">
      <div>
        <span class="eyebrow">Structured Support for Organizations</span>
        <h2 style="color:#fff; margin-top:14px;">Government, Education, Nonprofit, and Team Services</h2>
        <p style="margin-top:18px; font-size:16.5px;">Pogue Digital Solutions, LLC supports organizations that need clearer communication, practical training, documented systems, customer or stakeholder insights, and responsible AI adoption.</p>
        <p style="font-size:16.5px;">As a Navy veteran-founded company, we bring a mission-focused approach centered on preparation, accountability, adaptability, and service.</p>
        <div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:18px;">
          <span class="pill">SAM.gov registered</span><span class="pill">NAICS 541611</span><span class="pill">PSC D302</span><span class="pill">Veteran-owned</span>
        </div>
        <a href="contact.html#government" class="btn btn-outline-gold" style="margin-top:26px;">Explore Organizational Services <span class="btn-arrow">&rarr;</span></a>
      </div>
      <div class="grid-2" style="gap:18px;">
        <div class="card-glass">
          <span class="card-eyebrow">Capabilities</span>
          {li(["AI adoption planning","Workforce training","Digital communication strategy","Process documentation","Customer and stakeholder journey mapping","Content and messaging systems","Knowledge organization","Curriculum development","Digital outreach","Analytics and reporting","Human approval workflows","Small-business and veteran entrepreneurship training"], cols=1)}
        </div>
        <div class="card-glass">
          <span class="card-eyebrow">Organizations We Support</span>
          {li(["Government agencies","Government contractors","Educational institutions","Veteran service organizations","Nonprofits","Healthcare-related organizations","Chambers of commerce","Business development programs","Professional associations","Community organizations"], cols=1)}
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 8. HOW SOLUTIONS ARE DEVELOPED -->
<section>
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">How Solutions Are Developed</span>
      <h2>Clarify. Diagnose. Build. Scale.</h2>
      <p class="center">Our work follows a practical four-stage process.</p>
    </div>
    <div class="bearing reveal" style="margin-bottom:40px;"><span class="bearing-label">DEPARTURE</span><div class="bearing-rule"></div><span class="bearing-label">DESTINATION</span></div>
    <div class="journey-track reveal">
      <div><div class="journey-node"></div><h3 style="font-size:19px;">1. Clarify</h3><p style="font-size:14.5px; margin-top:8px;">We begin with your goals, customers, challenges, current systems, available information, and desired results.</p><p style="font-size:13px; margin-top:10px; color:var(--charcoal-soft);">What are you trying to accomplish? Who needs to use the system? Where is knowledge stored? What work is repeated? Where do mistakes or delays happen? What decisions still require human judgment?</p></div>
      <div><div class="journey-node"></div><h3 style="font-size:19px;">2. Diagnose</h3><p style="font-size:14.5px; margin-top:8px;">We examine the gaps between your current state and desired outcome.</p><p style="font-size:13px; margin-top:10px;">The diagnosis may reveal problems in messaging, documentation, process design, customer experience, technology, team alignment, data organization, AI readiness, or approval and accountability.</p></div>
      <div><div class="journey-node"></div><h3 style="font-size:19px;">3. Build</h3><p style="font-size:14.5px; margin-top:8px;">We develop the appropriate strategy, system, playbook, workflow, training, or AI-assisted solution.</p><p style="font-size:13px; margin-top:10px;">Knowledge organization, messaging standards, process maps, AI instructions, content systems, customer journey maps, training materials, automation plans, reporting frameworks.</p></div>
      <div><div class="journey-node"></div><h3 style="font-size:19px;">4. Scale</h3><p style="font-size:14.5px; margin-top:8px;">Once the system is in place, we help you use it consistently, evaluate its effectiveness, and adapt it as your business changes.</p></div>
    </div>
    <p class="quote-band reveal center" style="margin:44px auto 0; border-left:0; padding-left:0; text-align:center;">We build systems that can grow with your business instead of forcing your business to fit a rigid template.</p>
  </div>
</section>

<!-- 9. WAYS TO WORK TOGETHER -->
<section class="on-paper-dim">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">Ways to Work Together</span>
      <h2>Choose the Level of Support You Need</h2>
    </div>
    <div class="bento reveal">
      <div class="card"><span class="card-eyebrow">Assessment</span><h3 style="font-size:19px;">Strategic Assessment</h3><p style="font-size:14.5px;">A focused review designed to identify your strongest opportunities, immediate gaps, and logical next steps.</p><p style="font-size:13px;"><strong>Best for:</strong> businesses that know something needs to improve but are not sure where to begin.</p><a href="assessments.html#strategic" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;">Request a Strategic Assessment</a></div>
      <div class="card"><span class="card-eyebrow">Session</span><h3 style="font-size:19px;">Strategy Session</h3><p style="font-size:14.5px;">A working conversation focused on a specific problem, decision, system, campaign, or opportunity.</p><p style="font-size:13px;"><strong>Best for:</strong> founders who need clarity before committing to a larger project.</p><a href="{CALENDLY}" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;" target="_blank" rel="noopener">Schedule a Strategy Session</a></div>
      <div class="card span-2"><span class="card-eyebrow">Project</span><h3 style="font-size:19px;">Project-Based Consulting</h3><p style="font-size:14.5px;">A defined engagement with specific deliverables, milestones, and outcomes.</p>{li(["Brand Voice AI foundations","Website strategy","Customer journey mapping","AI workflow planning","Messaging systems","Content operations","Training development"], cols=2)}<a href="contact.html#project" class="btn btn-outline-navy" style="margin-top:18px; font-size:11px; padding:10px 16px;">Discuss a Project</a></div>
      <div class="card span-2"><span class="card-eyebrow">Training</span><h3 style="font-size:19px;">Workshops and Training</h3><p style="font-size:14.5px;">Customized education for teams, organizations, communities, and professional groups.</p><a href="contact.html#workshop" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;">Request a Workshop</a></div>
      <div class="card span-2"><span class="card-eyebrow">Advisory</span><h3 style="font-size:19px;">Ongoing Advisory Support</h3><p style="font-size:14.5px;">Continued strategic guidance for businesses implementing new systems, marketing plans, AI workflows, or organizational changes.</p><p style="font-size:13px;"><strong>Best for:</strong> businesses that need consistent support without hiring a full-time strategist.</p><a href="contact.html#advisory" class="btn btn-outline-navy" style="margin-top:12px; font-size:11px; padding:10px 16px;">Ask About Advisory Support</a></div>
    </div>
  </div>
</section>

<!-- 10. FIND YOUR STARTING POINT -->
<section>
  <div class="wrap" style="max-width:900px;">
    <div class="section-head reveal">
      <span class="eyebrow">Find Your Starting Point</span>
      <h2>Which Solution Does Your Business Need?</h2>
    </div>
    <div class="matcher reveal">
      <a class="row" href="#brand-voice-ai"><span class="say">&ldquo;Our marketing does not sound consistent.&rdquo;</span><span class="arrow">START WITH &rarr;</span><span class="to">Brand Voice AI</span></a>
      <a class="row" href="#ai-automation"><span class="say">&ldquo;We spend too much time repeating the same work.&rdquo;</span><span class="arrow">START WITH &rarr;</span><span class="to">AI and Automation</span></a>
      <a class="row" href="#digital-strategy"><span class="say">&ldquo;We are doing many marketing activities, but they do not feel connected.&rdquo;</span><span class="arrow">START WITH &rarr;</span><span class="to">Digital Strategy</span></a>
      <a class="row" href="#training"><span class="say">&ldquo;Our team needs to understand how to use AI responsibly.&rdquo;</span><span class="arrow">START WITH &rarr;</span><span class="to">Training and Workshops</span></a>
      <a class="row" href="assessments.html"><span class="say">&ldquo;We know something is wrong, but we cannot clearly define the problem.&rdquo;</span><span class="arrow">START WITH &rarr;</span><span class="to">An Assessment</span></a>
    </div>
    <div class="reveal" style="margin-top:28px;"><a href="assessments.html" class="btn btn-gold">Take an Assessment <span class="btn-arrow">&rarr;</span></a></div>
  </div>
</section>

<!-- 11. WHAT MAKES OUR APPROACH DIFFERENT -->
<section class="on-ink">
  <div class="glow-blob" style="width:480px; height:480px; background:radial-gradient(circle, rgba(212,175,55,0.14), transparent 70%); top:0; right:-140px;"></div>
  <div class="wrap">
    <div class="section-head reveal">
      <span class="eyebrow">What Makes Our Approach Different</span>
      <h2 style="color:#fff;">Technology With a Human Point of View</h2>
    </div>
    <div class="grid-3 reveal">
      <div class="card-glass"><h3 style="font-size:16.5px;">Strategy Comes First</h3><p style="font-size:14px;">Tools are selected after the problem, process, people, and desired outcome are understood.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Your Knowledge Matters</h3><p style="font-size:14px;">The system should reflect your experience, customers, language, stories, and way of working.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Human Approval Is Built In</h3><p style="font-size:14px;">Important communication and decisions should not be surrendered to an unsupervised tool.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Education Is Part of the Work</h3><p style="font-size:14px;">You should understand what has been created and how to use it.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Systems Should Create Freedom</h3><p style="font-size:14px;">A good system reduces unnecessary repetition and gives people more room for judgment, creativity, service, and meaningful work.</p></div>
      <div class="card-glass"><h3 style="font-size:16.5px;">Curiosity Leads the Diagnosis</h3><p style="font-size:14px;">We ask questions before making assumptions.</p></div>
    </div>
    <p class="quote-band reveal" style="margin-top:32px;">&ldquo;Curiosity is my superpower.&rdquo;</p>
  </div>
</section>

<!-- 12. FAQ -->
<section class="on-paper-dim">
  <div class="wrap" style="max-width:820px;">
    <div class="section-head reveal">
      <span class="eyebrow">Common Questions</span>
      <h2>Frequently Asked Questions</h2>
    </div>
    {faq(FAQS)}
  </div>
</section>

<!-- 13. FINAL CTA -->
{cta_band("Stop Adding Tools to an Unclear System",
  "Your business does not need more disconnected technology. It needs a clear strategy, organized knowledge, defined processes, and tools that support the way your people actually work.",
  primary=("Find Your Starting Point", "assessments.html"),
  closing="&ldquo;Don&rsquo;t tell me it can&rsquo;t be done. Let&rsquo;s define the problem and build the right solution.&rdquo;")}

''' + footer()

open("./solutions.html", "w").write(html)
print("solutions.html", len(html))
