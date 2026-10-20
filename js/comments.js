// Blog comments: loads approved comments and posts new ones (held for moderation).
(function () {
  var root = document.getElementById("comments");
  if (!root) return;
  var slug = root.getAttribute("data-slug");
  var siteKey = root.getAttribute("data-turnstile");
  var list = root.querySelector(".comments-list");
  var form = root.querySelector("form");
  var note = root.querySelector(".comments-note");
  var submit = form.querySelector("button[type=submit]");
  var turnstileBox = form.querySelector(".cf-turnstile");
  var widgetId = null;

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function fmtDate(iso) {
    var d = new Date(iso.replace(" ", "T") + "Z");
    return isNaN(d) ? "" : d.toLocaleDateString(undefined, { year: "numeric", month: "long", day: "numeric" });
  }
  function setNote(msg, kind) {
    note.textContent = msg || "";
    note.className = "comments-note" + (kind ? " is-" + kind : "");
  }

  function load() {
    fetch("/api/comments/" + slug)
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var items = (data && data.comments) || [];
        if (!items.length) {
          list.innerHTML = '<p class="comments-empty">No comments yet. Start the conversation.</p>';
          return;
        }
        list.innerHTML = items.map(function (c) {
          return '<div class="comment"><div class="comment-head"><strong>' + esc(c.author) +
            '</strong><time>' + esc(fmtDate(c.created_at)) + '</time></div><p>' +
            esc(c.body).replace(/\n{2,}/g, "</p><p>").replace(/\n/g, "<br>") + "</p></div>";
        }).join("");
      })
      .catch(function () { list.innerHTML = ""; });
  }

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
      author: form.author.value,
      email: form.email.value,
      body: form.body.value,
      website: form.website.value,
      token: token
    };
    submit.disabled = true;
    setNote("Sending...");
    fetch("/api/comments/" + slug, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload)
    })
      .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, data: d }; }); })
      .then(function (res) {
        if (!res.ok) throw new Error(res.data.error || "Something went wrong.");
        form.reset();
        setNote("Thanks. Your comment is in. John reads every one before it goes live.", "ok");
      })
      .catch(function (err) { setNote(err.message, "error"); })
      .then(function () {
        submit.disabled = false;
        if (window.turnstile && widgetId !== null) window.turnstile.reset(widgetId);
      });
  });

  load();
})();
