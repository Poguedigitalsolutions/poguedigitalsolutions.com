// Pogue Digital Solutions site script.
// Mobile navigation drawer and subscribe-box sizing.
(function () {
  // ---- Mobile nav ----
  var toggle = document.querySelector('.nav-toggle');
  var drawer = document.querySelector('.nav-drawer');
  if (toggle && drawer) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      drawer.classList.toggle('open', open);
      document.body.classList.toggle('nav-locked', open);
    };
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    drawer.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setOpen(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setOpen(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080) setOpen(false);
    });
  }

  // ---- Subscribe box: size each framed signup card to its content ----
  document.querySelectorAll('iframe.sub-frame').forEach(function (f) {
    var fit = function () {
      try {
        var root = f.contentDocument && f.contentDocument.querySelector('.sub-root');
        if (root && root.offsetHeight) f.style.height = root.offsetHeight + 'px';
      } catch (e) {}
    };
    f.addEventListener('load', function () {
      fit();
      try { new ResizeObserver(fit).observe(f.contentDocument.querySelector('.sub-root')); } catch (e) {}
    });
    fit();
  });
})();

// Read & Print: remember where the reader was, so Back (button or browser arrow) returns to the same spot.
(function () {
  var key = 'pds-scroll:' + location.pathname;
  document.querySelectorAll('.print-link').forEach(function (a) {
    a.addEventListener('click', function () {
      try { sessionStorage.setItem(key, String(window.scrollY)); } catch (e) {}
    });
  });
  function restore() {
    var y = null;
    try { y = sessionStorage.getItem(key); sessionStorage.removeItem(key); } catch (e) {}
    if (y === null) return;
    var nav = (performance.getEntriesByType && performance.getEntriesByType('navigation')[0]) || {};
    if (nav.type && nav.type !== 'back_forward') return;
    window.scrollTo(0, parseInt(y, 10) || 0);
  }
  window.addEventListener('pageshow', function (e) { if (!e.persisted) restore(); });
})();

// Amazon link clicks: count which book or product was clicked, on which page. Cookie-free.
// Sends only the page path, the product ID (ASIN), and the tracking ID in the link. Report: /clicks-admin
(function () {
  if (!navigator.sendBeacon) return;
  function record(e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var url;
    try { url = new URL(a.href); } catch (err) { return; }
    var host = url.hostname.replace(/^www\./, ''), item = null;
    if (host === 'amazon.com' || host === 'smile.amazon.com') {
      var m = url.pathname.match(/\/(?:dp|gp\/product|gp\/aw\/d)\/([A-Z0-9]{10})/i);
      if (m) item = m[1].toUpperCase();
    } else if (host === 'amzn.to' || host === 'link.amazon') {
      var code = url.pathname.replace(/^\/+|\/+$/g, '');
      if (/^[A-Za-z0-9]{4,16}$/.test(code)) item = host + '/' + code;
    }
    if (!item) return;
    var body = JSON.stringify({ page: location.pathname, item: item, tag: url.searchParams.get('tag') || '' });
    try { navigator.sendBeacon('/api/click', new Blob([body], { type: 'text/plain' })); } catch (err) {}
  }
  document.addEventListener('click', record, true);
  document.addEventListener('auxclick', function (e) { if (e.button === 1) record(e); }, true);
})();
