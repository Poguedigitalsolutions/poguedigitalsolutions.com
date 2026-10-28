// Contact form: posts to /api/contact, which stores the message for John at /comments-admin.
(function () {
  var form = document.getElementById("contact-form");
  if (!form) return;
  var siteKey = form.getAttribute("data-turnstile");
  var note = form.querySelector(".comments-note");
  var submit = form.querySelector("button[type=submit]");
  var turnstileBox = form.querySelector(".cf-turnstile");
  var widgetId = null;

  function setNote(msg, kind) {
    note.textContent = msg || "";
    note.className = "comments-note" + (kind ? " is-" + kind : "");
  }

  // Preselect the topic when arriving from a link like contact#message?topic=workshop
  var m = location.search.match(/[?&]topic=([a-z-]+)/);
  if (m && form.topic.querySelector('option[value="' + m[1] + '"]')) form.topic.value = m[1];

  // Load Turnstile only when the form scrolls into view.
  function mountTurnstile() {
    if (widgetId !== null || !siteKey) return;
    function render() {
      widgetId = window.turnstile.render(turnstileBox, { sitekey: siteKey, theme: "light" });
    }
    if (window.turnstile) return render();
    var s = document.createElement("script");
    s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
    s.async = true;
    s.onload = render;
    document.head.appendChild(s);
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries.some(function (e) { return e.isIntersecting; })) { mountTurnstile(); io.disconnect(); }
    }, { rootMargin: "200px" });
    io.observe(form);
  } else {
    mountTurnstile();
  }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var token = window.turnstile && widgetId !== null ? window.turnstile.getResponse(widgetId) : "";
    if (!token) { setNote("Please wait for the verification check to finish.", "error"); return; }
    var payload = {
      name: form.name.value,
      email: form.email.value,
      topic: form.topic.value,
      message: form.message.value,
      website: form.website.value,
      token: token
    };
    submit.disabled = true;
    setNote("Sending...");
    fetch("/api/contact", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload)
    })
      .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, data: d }; }); })
      .then(function (res) {
        if (!res.ok) throw new Error(res.data.error || "Something went wrong.");
        form.reset();
        setNote("Thanks. Your message is in, and John will reply by email.", "ok");
      })
      .catch(function (err) { setNote(err.message, "error"); })
      .then(function () {
        submit.disabled = false;
        if (window.turnstile && widgetId !== null) window.turnstile.reset(widgetId);
      });
  });
})();
