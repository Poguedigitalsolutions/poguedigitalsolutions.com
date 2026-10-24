import math, sys
C=400
def pt(r,a):
    t=math.radians(a); return (C+r*math.sin(t), C-r*math.cos(t))
def f(p): return f"{p[0]:.1f} {p[1]:.1f}"
G="#D4AF37"; L="#F2D680"
# ---- outer degree ring (turns)
ticks=[]
for d in range(0,360,1):
    if d%5 and False: pass
    Lt=18 if d%30==0 else (11 if d%10==0 else (8 if d%5==0 else 4))
    a,b=pt(352,d),pt(352-Lt,d)
    sw=' stroke-width="1.6"' if d%30==0 else ''
    ticks.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}"{sw}/>')
nums=[]
for d in range(0,360,10):
    p=pt(316,d); big=d%30==0
    fs=16 if big else 11; op=0.75 if big else 0.45
    nums.append(f'<text x="{p[0]:.1f}" y="{p[1]+fs*0.35:.1f}" font-size="{fs}" fill-opacity="{op}" transform="rotate({d} {p[0]:.1f} {p[1]:.1f})">{d}</text>')
outer=f'''<g class="ring-outer" fill="none" stroke="{G}" stroke-opacity="0.45" stroke-width="0.8">
    <circle cx="400" cy="400" r="362" stroke-width="1.4"/><circle cx="400" cy="400" r="356"/><circle cx="400" cy="400" r="352"/><circle cx="400" cy="400" r="300"/>
    <g>{''.join(ticks)}</g>
    <g stroke="none" fill="{L}" font-family="IBM Plex Mono, monospace" text-anchor="middle">{''.join(nums)}</g>
  </g>'''
# ---- ornate ring (turns the other way): scroll panels between double rings
orn=[]
for i in range(16):
    a=i*22.5
    # diamond marker
    p1,p2,p3,p4=pt(291,a),pt(284,a-1.8),pt(277,a),pt(284,a+1.8)
    orn.append(f'<path d="M{f(p1)} L{f(p2)} L{f(p3)} L{f(p4)} Z" fill="{G}" fill-opacity="0.35"/>')
    # scroll: two little S-curves either side, drawn as arcs
    for s in (1,-1):
        c0=pt(284,a+s*4); c1=pt(289,a+s*7); c2=pt(279,a+s*10); c3=pt(284,a+s*13)
        orn.append(f'<path d="M{f(c0)} Q{f(c1)} {f(pt(284,a+s*8.5))} T{f(c3)}"/>')
        q=pt(284,a+s*16); orn.append(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="1.6" fill="{G}" fill-opacity="0.5"/>')
inner=f'''<g class="ring-inner" fill="none" stroke="{G}" stroke-opacity="0.45" stroke-width="0.9">
    <circle cx="400" cy="400" r="296"/><circle cx="400" cy="400" r="292"/><circle cx="400" cy="400" r="276"/><circle cx="400" cy="400" r="272"/>
    {''.join(orn)}
    <circle cx="400" cy="400" r="258" stroke-dasharray="1 5"/>
  </g>'''
# ---- static rose: classic two-tone points (one half lightly filled)
def point(a,Lp,w,sp,op):
    tip=pt(Lp,a); b1=pt(w,a-sp); b2=pt(w,a+sp)
    return (f'<path d="M{C} {C} L{f(b1)} L{f(tip)} Z" fill="{G}" fill-opacity="{op*0.35:.2f}" stroke-opacity="{op}"/>'
            f'<path d="M{C} {C} L{f(b2)} L{f(tip)} Z" stroke-opacity="{op}"/>')
rose=[]
for i in range(32):
    a=i*11.25
    if i%8==0: continue
    if i%4==0: rose.append((205,a,42,22.5,0.65))
    elif i%2==0: rose.append((165,a,30,11.25,0.5))
    else: rose.append((215,a,18,4.5,0.4))   # long thin 32-wind needles like the reference
rose.sort(key=lambda x:x[0])
parts=[point(a,Lp,w,sp,op) for Lp,a,w,sp,op in rose]
# cardinal arms with diamond letter plates at the tips
for a in (0,90,180,270):
    parts.append(point(a,250,46,45,0.85))
    d1,d2,d3,d4=pt(294,a),pt(246,a-7.5),pt(198,a),pt(246,a+7.5)
    parts.append(f'<path d="M{f(d1)} L{f(d2)} L{f(d3)} L{f(d4)} Z" fill="#060B14" fill-opacity="0.85" stroke-opacity="0.85" stroke-width="1.3"/>')
rosesvg=f'<g class="rose" fill="none" stroke="{G}" stroke-width="1">{"".join(parts)}</g>'
# hub rings with fleur-style diamonds
hub=[]
for i in range(8):
    a=i*45+22.5; p=pt(100,a)
    hub.append(f'<path d="M{f(pt(108,a))} L{f(pt(100,a-3))} L{f(pt(92,a))} L{f(pt(100,a+3))} Z" fill="{G}" fill-opacity="0.4"/>')
hubsvg=f'''<g fill="none" stroke="{G}" stroke-opacity="0.5" stroke-width="0.9">
    <circle cx="400" cy="400" r="116"/><circle cx="400" cy="400" r="84"/>{''.join(hub)}
  </g>'''
letters=''.join(f'<text x="{pt(246,a)[0]:.1f}" y="{pt(246,a)[1]+8:.1f}">{t}</text>' for a,t in ((0,'N'),(90,'E'),(180,'S'),(270,'W')))
inter=''.join(f'<text x="{pt(232,a)[0]:.1f}" y="{pt(232,a)[1]+5:.1f}" transform="rotate({a if a<180 else a-360} {pt(232,a)[0]:.1f} {pt(232,a)[1]:.1f})">{t}</text>' for a,t in ((45,'NE'),(135,'SE'),(225,'SW'),(315,'NW')))
# anchor in a medallion
anchor=f'''<g fill="none" stroke="{L}" stroke-opacity="0.8" stroke-width="1.6" stroke-linecap="round">
    <circle cx="400" cy="400" r="26" fill="#060B14" fill-opacity="0.9" stroke="{G}" stroke-opacity="0.8"/>
    <circle cx="400" cy="400" r="21" stroke="{G}" stroke-opacity="0.5" stroke-width="0.8"/>
    <circle cx="400" cy="387" r="3"/><line x1="400" y1="390" x2="400" y2="413"/><line x1="393" y1="395" x2="407" y2="395"/>
    <path d="M389 405 Q391 414 400 414 Q409 414 411 405"/><path d="M387 407 L389 404 L392 407"/><path d="M408 407 L411 404 L413 407"/>
  </g>'''
svg=f'''<svg class="compass-bg" viewBox="0 0 800 800" aria-hidden="true" focusable="false">
  <defs>
    <radialGradient id="cg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{G}" stop-opacity="0.14"/>
      <stop offset="60%" stop-color="{G}" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="{G}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sweepg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{L}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{L}" stop-opacity="0.4"/>
    </linearGradient>
  </defs>
  <circle cx="400" cy="400" r="360" fill="url(#cg)"/>
  {outer}
  {inner}
  <g class="sweep"><path d="M400 400 L400 48 A352 352 0 0 1 571 92 Z" fill="url(#sweepg)" opacity="0.4"/></g>
  {hubsvg}
  {rosesvg}
  <g font-family="Georgia, 'Times New Roman', serif" fill="{L}" fill-opacity="0.85" text-anchor="middle" font-size="24">{letters}</g>
  <g font-family="Georgia, 'Times New Roman', serif" fill="{L}" fill-opacity="0.55" text-anchor="middle" font-size="13">{inter}</g>
  {anchor}
</svg>'''
open(sys.argv[1],'w').write(svg); print(len(svg))
