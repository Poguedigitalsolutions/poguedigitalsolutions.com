"""The branded 404 page. Cloudflare Pages serves 404.html for any missing route,
including nested ones like /blog/missing, so every link on it is root-relative after build_all."""
from parts import *

BODY = r'''<section class="on-ink" style="min-height:70vh; display:flex; align-items:center;">
  <svg class="compass-bg" viewBox="0 0 800 800" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="cg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#D4AF37" stop-opacity="0.18"/>
      <stop offset="60%" stop-color="#D4AF37" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="#D4AF37" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sweepg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#F2D680" stop-opacity="0"/>
      <stop offset="100%" stop-color="#F2D680" stop-opacity="0.55"/>
    </linearGradient>
  </defs>
  <circle cx="400" cy="400" r="360" fill="url(#cg)"/>
  <g class="ring-outer" fill="none" stroke="#D4AF37" stroke-opacity="0.45" stroke-width="1">
    <circle cx="400" cy="400" r="330"/>
    <circle cx="400" cy="400" r="318" stroke-dasharray="2 10"/>
    <g stroke-width="1.2"><line x1="400" y1="70" x2="400" y2="84" transform="rotate(0 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(5 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(10 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(15 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(20 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(25 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(30 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(35 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(40 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(45 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(50 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(55 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(60 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(65 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(70 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(75 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(80 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(85 400 400)"/><line x1="400" y1="70" x2="400" y2="84" transform="rotate(90 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(95 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(100 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(105 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(110 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(115 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(120 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(125 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(130 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(135 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(140 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(145 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(150 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(155 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(160 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(165 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(170 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(175 400 400)"/><line x1="400" y1="70" x2="400" y2="84" transform="rotate(180 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(185 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(190 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(195 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(200 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(205 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(210 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(215 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(220 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(225 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(230 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(235 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(240 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(245 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(250 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(255 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(260 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(265 400 400)"/><line x1="400" y1="70" x2="400" y2="84" transform="rotate(270 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(275 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(280 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(285 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(290 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(295 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(300 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(305 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(310 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(315 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(320 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(325 400 400)"/><line x1="400" y1="70" x2="400" y2="79" transform="rotate(330 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(335 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(340 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(345 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(350 400 400)"/><line x1="400" y1="70" x2="400" y2="75" transform="rotate(355 400 400)"/></g>
  </g>
  <g class="ring-inner" fill="none" stroke="#D4AF37" stroke-opacity="0.3" stroke-width="1">
    <circle cx="400" cy="400" r="230"/>
    <circle cx="400" cy="400" r="150" stroke-dasharray="1 6"/>
    <path d="M400 170 L412 388 L400 400 L388 388 Z M400 630 L412 412 L400 400 L388 412 Z M170 400 L388 388 L400 400 L388 412 Z M630 400 L412 388 L400 400 L412 412 Z" fill="#D4AF37" fill-opacity="0.12" stroke-opacity="0.5"/>
  </g>
  <g class="sweep">
    <path d="M400 400 L400 70 A330 330 0 0 1 560 110 Z" fill="url(#sweepg)" opacity="0.5"/>
  </g>
  <g font-family="IBM Plex Mono, monospace" font-size="18" fill="#F2D680" fill-opacity="0.7" text-anchor="middle">
    <text x="400" y="52">N</text><text x="754" y="407">E</text><text x="400" y="760">S</text><text x="46" y="407">W</text>
  </g>
  <circle cx="400" cy="400" r="5" fill="#F2D680"/>
</svg>
  <div class="wrap reveal" style="max-width:640px; text-align:center;">
    <span class="eyebrow">404</span>
    <h1 style="font-size:clamp(34px,5vw,58px); color:#fff; margin-top:16px;">That page is not on the chart.</h1>
    <p style="font-size:17px; margin-top:18px;">The link may be out of date, or the page has moved. Pick a heading below.</p>
    <div style="display:flex; gap:14px; justify-content:center; margin-top:30px; flex-wrap:wrap;">
      <a href="index.html" class="btn btn-gold">Back to Home <span class="btn-arrow">&rarr;</span></a>
      <a href="solutions.html" class="btn btn-outline-gold">See Solutions</a>
      <a href="https://calendly.com/poguedigitalsolutions/30min" class="btn btn-outline-gold" target="_blank" rel="noopener">Book a Call</a>
    </div>
  </div>
</section>
'''

page = head("Page Not Found | Pogue Digital Solutions", "The page you were looking for has moved or does not exist.", "404.html", indexable=False) + header("") + BODY + footer()
open("404.html", "w").write(page)
print("404.html", len(page))
