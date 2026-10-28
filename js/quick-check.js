// Brand Voice Quick Check (/brand-voice-quick-check).
// 12 statements rated 1 to 5, four per layer, so each layer scores 4 to 20 and the total 12 to 60.
// Statements, tiers and answer notes match John's approved results email; edit both together.
// When the page has a ClickFunnels page token, the results form carries every field below as a
// custom contact attribute (data-cf-element="custom-attribute:<name>") for the results email.
(function () {
  var LAYERS = ["Foundation", "Playbooks", "Execution"];
  var SCALE = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"];
  var QUESTIONS = [
    { layer: 0, s: "Our mission, values, and story are written down in one place anyone on my team can find.",
      tips: [
        "Your mission and values live mostly in your head, so everyone else has to guess. Try this: write one page that answers why you started, who you serve, and what you won't compromise on. Then put it where your whole team can find it.",
        "Some of it is written, but it's spread out or hard to find. Try this: pull what you have into one document and share the link with everyone who writes for your business.",
        "Your foundation is written and easy to find. To keep it that way: reread it once a quarter and update anything that changed along with your offers."] },
    { layer: 0, s: "I have a current, written description of my ideal customer, including their problems and the words they use.",
      tips: [
        "Without a written picture of your best customer, your marketing ends up talking to everyone. Try this: think of your three favorite clients and write down what they had in common, what problem brought them to you, and the exact words they used to describe it.",
        "You know your customer, but the description is general or out of date. Try this: add the questions they ask on sales calls and the words they use, so your copy sounds like them.",
        "You have a clear, current customer profile. To keep it that way: add new phrases you hear from customers as they come up."] },
    { layer: 0, s: "We have written rules for how our business sounds: words we use, words we avoid, and how formal we are.",
      tips: [
        "Without written voice rules, your business sounds different depending on who writes or which AI tool they use. Try this: list five words you like, five you never use, and save two pieces of writing that sound most like you.",
        "You have some tone guidance, but not enough for someone else to match you. Try this: add do and don't examples, like a sentence that sounds like you next to one that doesn't.",
        "Your voice rules are clear. To keep it that way: share them with every person and tool that writes for you, and add good examples as you find them."] },
    { layer: 0, s: "My best stories and client examples are collected in one place and easy to find.",
      tips: [
        "Your best stories only come out when you happen to remember them. Try this: start a simple story list and add one each time you tell a story in a meeting or on a call.",
        "Some stories are saved, but they're hard to find when you need one. Try this: label each story by the topic or the customer worry it answers.",
        "Your stories are organized and ready to use. To keep it that way: note which ones land best with customers and reach for those first."] },
    { layer: 1, s: "When customers ask common questions, everyone on our side gives the same answer.",
      tips: [
        "Customers may hear different answers depending on who they ask. Try this: write down the ten questions you hear most and your best answer to each.",
        "Your answers are mostly consistent, but they aren't all written down. Try this: turn the answers you give most often into saved replies everyone can use.",
        "Your team gives consistent answers. To keep it that way: review the list each quarter and add new questions as they come up."] },
    { layer: 1, s: "If I stepped away for two weeks, someone else could keep our marketing going in our voice.",
      tips: [
        "Right now your marketing depends on you being there. Try this: write down the steps for one weekly task, like a social post or newsletter, so someone else could do it.",
        "Someone could keep things going, but they'd need a lot of help from you. Try this: record a short video of how you do one task and save it with your written notes.",
        "Your marketing can run without you in the room. To keep it that way: have someone else run one week while you only review, and fix any gaps you find."] },
    { layer: 1, s: "We have a written process for how content gets planned, written, and approved.",
      tips: [
        "Content goes out when you find time, which makes it hard to stay consistent. Try this: pick one day a week for planning and write down the three steps every piece goes through.",
        "You have a rough process, but it isn't followed every time. Try this: write down each step, who owns it, and when it's due.",
        "You have a clear content process. To keep it that way: look for one step a helper or AI tool could prepare for your approval."] },
    { layer: 1, s: "We follow up with new leads using a written sequence that sounds like us.",
      tips: [
        "Leads can go cold when follow-up depends on memory. Try this: write a simple three-message follow-up you can send to every new lead.",
        "You follow up, but you write it fresh each time. Try this: save your best follow-up messages as templates and decide when each one goes out.",
        "Your follow-up is written and consistent. To keep it that way: check which message gets the most replies and model the others after it."] },
    { layer: 2, s: "When I use AI to help me write, it sounds like me with only light edits.",
      hint: "If you don't use AI yet, choose Strongly disagree.",
      tips: [
        "AI can't sound like you yet because it has nothing of yours to learn from. Try this: before you ask AI to write, give it your voice rules and one or two pieces you wrote yourself.",
        "AI gets partway there, but you still rewrite a lot. Try this: save one set of instructions with your voice rules and business details, and use it every time.",
        "Your AI tools work from your written voice. To keep it that way: update those instructions when your offers or voice rules change, and keep a person approving important work."] },
    { layer: 2, s: "Our website, social profiles, and emails all sound like the same business.",
      tips: [
        "Your channels sound like different businesses. Try this: read your website, your main social profile, and your last email side by side, then rewrite the one that sounds least like you.",
        "Most of your channels match, with a few that don't. Try this: list the old pages or profiles that sound off and update one each week.",
        "Your channels sound like one business. To keep it that way: check them against your voice rules whenever you change an offer."] },
    { layer: 2, s: "Before anything goes out in our name, it passes a clear review step anyone on the team can follow.",
      tips: [
        "Things go out without a clear check, so mistakes and off-brand messages can slip through. Try this: write a short checklist (facts, tone, links, next step for the reader) and use it before anything goes out.",
        "There's a review, but it depends on your time or slows you down. Try this: turn what you look for into a checklist so someone else can do the first pass and you give the final OK.",
        "You have a clear review step. To keep it that way: add any mistake that slips through to the checklist."] },
    { layer: 2, s: "Most of how my business runs is written down well enough to hand to someone else tomorrow.",
      tips: [
        "Right now you are the business, which makes it hard to grow, take time off, or sell one day. Try this: pick the task you do most often and write down how you do it, one step at a time.",
        "Some of how you run things is written down, but key parts still live with you. Try this: list the decisions only you make today and write down how you make one of them.",
        "Most of your business is written down and others use it. To keep it that way: review your documents once a year and remove anything out of date."] }
  ];
  var TIERS = [
    { min: 12, max: 28, title: "Your voice lives in your head",
      diag: "Most of what makes your business sound like you isn't written down yet. That's common for founders who built the business themselves. It also means your team, your AI tools, and any future buyer are guessing.",
      next: "Start with the Foundation layer. Brand Voice AI pulls what you know out of your head and onto paper, one conversation at a time, so you don't have to sit down and write it all yourself.",
      cta2: "See how Brand Voice AI works" },
    { min: 29, max: 41, title: "The pieces are on the table",
      diag: "You've written some of it down, but it's spread across files, folders, and old posts. People and AI tools can't use what they can't find, so your voice still changes depending on who's writing.",
      next: "Pull what you already have into one organized source, then fill the gaps. That's the Foundation work in Brand Voice AI, and it goes faster because you're not starting from zero.",
      cta2: "See how Brand Voice AI works" },
    { min: 42, max: 51, title: "Written down, not yet working for you",
      diag: "Your foundation is in decent shape. The gap is turning it into everyday habits: answers, follow-ups, approvals, and AI instructions your team can use without asking you first.",
      next: "Turn your foundation into playbooks and AI instructions, with a human approval step before anything important goes out. That's the Playbooks and Execution work in Brand Voice AI, with AI and Automation where it helps.",
      cta2: "See AI and Automation" },
    { min: 52, max: 60, title: "Ready to scale your voice",
      diag: "You've done work most businesses skip. Your voice is written down, your team uses it, and your tools can work from it. The risk now is drift as you grow and as your offers change.",
      next: "Keep it current and teach it. A short review each quarter keeps your voice and your AI instructions up to date, and training helps new team members use the system the same way.",
      cta2: "See Training and Workshops" }
  ];
  var WEAK_TIPS = [
    "Foundation is your lowest layer. Start here, because playbooks and AI tools can only repeat what's written down. One small step this week: write the three questions customers ask you most, and how you answer them.",
    "Playbooks is your lowest layer. You know who you are, but it hasn't turned into repeatable work yet. One small step this week: write your follow-up for a new lead as a template you'd be happy to send again.",
    "Execution is your lowest layer. Your knowledge exists, but your tools and channels aren't using it. One small step this week: give your AI tool your written voice rules and one example you love, and compare the result."
  ];
  function band(v) { return v <= 2 ? 0 : (v === 3 ? 1 : 2); }

  // Where each tier's second button points.
  var TIER_LINKS = ["/solutions#brand-voice-ai", "/solutions#brand-voice-ai", "/solutions#ai-automation", "/solutions#training"];

  var root = document.getElementById("qc");
  if (!root) return;
  var answers = new Array(QUESTIONS.length).fill(null);
  var idx = 0;
  var $ = function (id) { return document.getElementById(id); };
  var screens = { intro: $("qc-intro"), q: $("qc-q"), result: $("qc-result") };

  function show(name) {
    Object.keys(screens).forEach(function (k) { screens[k].hidden = k !== name; });
    // Scroll so the card's top sits just below the fixed header.
    var head = document.querySelector("header");
    var offset = (head ? head.getBoundingClientRect().bottom : 0) + 24;
    var top = root.getBoundingClientRect().top + window.pageYOffset - offset;
    window.scrollTo({ top: Math.max(0, top), behavior: "instant" });
  }

  function renderQ() {
    var item = QUESTIONS[idx];
    $("qc-q-layer").textContent = LAYERS[item.layer];
    $("qc-q-count").textContent = "Statement " + (idx + 1) + " of " + QUESTIONS.length;
    $("qc-q-bar").style.width = (idx / QUESTIONS.length * 100) + "%";
    $("qc-q-text").textContent = item.s;
    $("qc-q-hint").hidden = !item.hint;
    $("qc-q-hint").textContent = item.hint || "";
    var box = $("qc-q-options");
    box.innerHTML = "";
    SCALE.forEach(function (label, i) {
      var v = i + 1;
      var b = document.createElement("button");
      b.type = "button"; b.className = "qc-opt";
      var n = document.createElement("span"); n.className = "qc-num"; n.textContent = v;
      var t = document.createElement("span"); t.textContent = label;
      b.appendChild(n); b.appendChild(t);
      b.setAttribute("aria-pressed", answers[idx] === v ? "true" : "false");
      b.addEventListener("click", function () {
        answers[idx] = v;
        Array.prototype.forEach.call(box.children, function (c, j) { c.setAttribute("aria-pressed", j === i ? "true" : "false"); });
        $("qc-next").disabled = false;
      });
      box.appendChild(b);
    });
    $("qc-next").disabled = answers[idx] === null;
    $("qc-next").textContent = idx === QUESTIONS.length - 1 ? "See my score" : "Next";
    $("qc-back").textContent = idx === 0 ? "Back to start" : "Back";
  }

  function score() {
    var layer = [0, 0, 0], total = 0;
    QUESTIONS.forEach(function (item, i) { var v = answers[i] || 1; layer[item.layer] += v; total += v; });
    return { total: total, layer: layer };
  }

  function renderResult() {
    var s = score();
    var ti = 0;
    TIERS.forEach(function (t, i) { if (s.total >= t.min && s.total <= t.max) ti = i; });
    var tier = TIERS[ti];
    $("qc-r-score").textContent = "Score: " + s.total + " of 60";
    $("qc-r-title").textContent = tier.title;
    $("qc-r-diag").textContent = tier.diag;
    $("qc-r-next").textContent = tier.next;
    $("qc-r-cta2").textContent = tier.cta2;
    $("qc-r-cta2").setAttribute("href", TIER_LINKS[ti]);

    var pct = (s.total - 12) / 48;
    $("qc-arc").setAttribute("stroke-dasharray", (pct * 100) + " 100");
    $("qc-needle").style.transform = "rotate(" + (-90 + pct * 180) + "deg)";

    var rows = $("qc-r-rows"); rows.innerHTML = "";
    LAYERS.forEach(function (name, i) {
      var r = document.createElement("div"); r.className = "qc-row";
      r.innerHTML = '<span></span><div class="qc-bar"><i></i></div><span class="qc-n"></span>';
      r.children[0].textContent = name;
      r.children[1].firstChild.style.width = ((s.layer[i] - 4) / 16 * 100) + "%";
      r.children[2].textContent = s.layer[i] + "/20";
      rows.appendChild(r);
    });

    var weakest = 0;
    s.layer.forEach(function (v, i) { if (v < s.layer[weakest]) weakest = i; });
    var weak = $("qc-r-weak"); weak.innerHTML = "";
    var h = document.createElement("h3"); h.textContent = "Where to start";
    var p = document.createElement("p"); p.textContent = WEAK_TIPS[weakest];
    weak.appendChild(h); weak.appendChild(p);
    weak.hidden = s.total >= 52;

    // Fields for ClickFunnels and the results email
    var payload = {
      quiz_score: s.total + " of 60",
      quiz_tier: tier.title,
      quiz_tier_summary: tier.diag,
      quiz_next_step: tier.next,
      quiz_weakest_layer: LAYERS[weakest],
      quiz_foundation: s.layer[0] + " of 20",
      quiz_playbooks: s.layer[1] + " of 20",
      quiz_execution: s.layer[2] + " of 20"
    };
    QUESTIONS.forEach(function (item, i) {
      var v = answers[i] || 1;
      payload["q" + (i + 1) + "_answer"] = v + " (" + SCALE[v - 1] + ")";
      payload["q" + (i + 1) + "_note"] = item.tips[band(v)];
    });
    Array.prototype.forEach.call(root.querySelectorAll("input[data-qc-field]"), function (el) {
      el.value = payload[el.getAttribute("data-qc-field")] || "";
    });
    window.qcLastResult = payload;

    show("result");
  }

  $("qc-start").addEventListener("click", function () { idx = 0; renderQ(); show("q"); });
  $("qc-next").addEventListener("click", function () {
    if (answers[idx] === null) return;
    if (idx < QUESTIONS.length - 1) { idx++; renderQ(); } else { renderResult(); }
  });
  $("qc-back").addEventListener("click", function () {
    if (idx === 0) { show("intro"); return; }
    idx--; renderQ();
  });
  $("qc-retake").addEventListener("click", function () {
    answers = new Array(QUESTIONS.length).fill(null); idx = 0; renderQ(); show("q");
  });
})();
