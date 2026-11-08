"""Amazon link click report at /clicks-admin. Not linked from the site, noindex.
Unlocks with the same ADMIN_KEY as /comments-admin (one unlock covers both in the same browser tab).
Book and product names come from the link text in build/articles/*.md, so the report reads
"Brain Rules by John Medina" instead of an Amazon product ID."""
from parts import *
import glob, html as htmlmod, json, os, re

ASIN = re.compile(r"/(?:dp|gp/product|gp/aw/d)/([A-Z0-9]{10})", re.I)
MD_LINK = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])+)\]\((https?://(?:www\.)?amazon\.com[^)\s]*)\)")
HTML_LINK = re.compile(r'<a\s[^>]*href="(https?://(?:www\.)?amazon\.com[^"]*)"[^>]*>(.*?)</a>', re.S)

def tidy(text):
    text = htmlmod.unescape(re.sub(r"<[^>]+>", "", text))
    text = text.replace("*", "").replace("_", " ").strip()
    text = re.sub(r"\s*\((?:first )?published.*$|\s*\([^)]*\d{4}\)$", "", text, flags=re.I)  # drop "(Publisher, 2023)"
    return re.sub(r"\s+", " ", text).strip()

titles, pages = {}, {}
for path in sorted(glob.glob(os.path.join("build", "articles", "*.md"))):
    src = open(path).read()
    slug = re.search(r"^slug:\s*(.+)$", src, re.M)
    title = re.search(r"^title:\s*(.+)$", src, re.M)
    if slug and title:
        pages["/blog/" + slug.group(1).strip()] = title.group(1).strip()
    found = [(t, u) for t, u in MD_LINK.findall(src)] + [(t, u) for u, t in HTML_LINK.findall(src)]
    for text, url in found:
        m = ASIN.search(url)
        name = tidy(text)
        if m and name and m.group(1).upper() not in titles:
            titles[m.group(1).upper()] = name

DATA = json.dumps({"titles": titles, "pages": pages}).replace("</", "<\\/")

body = f'''
<section class="tight" style="padding-top:56px;">
  <div class="wrap" style="max-width:960px;">
    <span class="eyebrow">Private report</span>
    <h1 style="font-size:clamp(28px,3.6vw,40px); margin-top:16px;">Amazon Link Clicks</h1>
    <p style="margin-top:10px; color:var(--charcoal);">Which books and products readers clicked on this site, and on which page. Clicks only: Amazon's own reports show what sold.</p>

    <form id="unlock" class="comments-form" style="margin-top:28px;">
      <label>Admin key <input name="key" type="password" autocomplete="current-password" required></label>
      <div class="comments-foot">
        <button class="btn btn-gold" type="submit">Unlock &rarr;</button>
        <p class="comments-note"></p>
      </div>
    </form>

    <div id="panel" hidden>
      <div class="comments-foot" style="margin-top:28px;">
        <div class="tabs" id="tabs">
          <button class="btn btn-outline-navy" data-days="7">7 days</button>
          <button class="btn btn-outline-navy" data-days="30">30 days</button>
          <button class="btn btn-outline-navy" data-days="90">90 days</button>
          <button class="btn btn-outline-navy" data-days="all">All time</button>
        </div>
        <button class="btn btn-outline-navy" id="lock" type="button">Lock</button>
      </div>
      <p id="total" class="click-total"></p>
      <h2 class="click-h">By book or product</h2>
      <div class="click-wrap"><table class="click-table" id="t-item"></table></div>
      <h2 class="click-h">By page</h2>
      <div class="click-wrap"><table class="click-table" id="t-page"></table></div>
      <h2 class="click-h">By tracking ID</h2>
      <div class="click-wrap"><table class="click-table" id="t-tag"></table></div>
    </div>
  </div>
</section>
<style>
.tabs {{ display:flex; flex-wrap:wrap; gap:10px; }}
.tabs .btn.is-active {{ background:var(--ink); color:var(--white); border-color:var(--ink); }}
.click-total {{ font-size:18px; margin-top:24px; }}
.click-h {{ font-size:20px; margin-top:32px; }}
.click-wrap {{ overflow-x:auto; margin-top:12px; }}
.click-table {{ width:100%; border-collapse:collapse; font-size:15px; }}
.click-table th, .click-table td {{ text-align:left; padding:10px 12px; border-bottom:1px solid var(--line-light); vertical-align:top; }}
.click-table th {{ font-family:var(--font-mono); font-size:11px; letter-spacing:0.06em; text-transform:uppercase; color:var(--gold-dim); }}
.click-table td.n {{ text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap; }}
.click-table th.n {{ text-align:right; }}
.click-sub {{ font-size:13px; color:var(--charcoal); }}
</style>
<script id="click-data" type="application/json">{DATA}</script>
<script>
(function(){{
  var KEY='pds_comments_admin_key', key=sessionStorage.getItem(KEY)||'', days='30';
  var META=JSON.parse(document.getElementById('click-data').textContent);
  var unlock=document.getElementById('unlock'), panel=document.getElementById('panel');
  var note=unlock.querySelector('.comments-note');
  function esc(s){{return String(s).replace(/[&<>"']/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c];}});}}
  function itemName(item){{
    if(META.titles[item]) return esc(META.titles[item]);
    return item.indexOf('/')>0 ? 'Short link '+esc(item) : 'Amazon product '+esc(item);
  }}
  function itemLink(item){{ return item.indexOf('/')>0 ? 'https://'+item : 'https://www.amazon.com/dp/'+item; }}
  function pageName(p){{ return META.pages[p] ? esc(META.pages[p]) : (p==='/'?'Home page':esc(p)); }}
  function table(el, head, rows, empty){{
    el.innerHTML = rows.length ? '<thead><tr>'+head+'</tr></thead><tbody>'+rows.join('')+'</tbody>'
                               : '<tbody><tr><td class="click-sub">'+empty+'</td></tr></tbody>';
  }}
  function api(){{
    return fetch('/api/admin/clicks?days='+days,{{headers:{{'authorization':'Bearer '+key}}}})
      .then(function(r){{ if(r.status===401) throw new Error('Wrong key.'); return r.json().catch(function(){{ throw new Error('The report could not load. Try again in a minute.'); }}); }})
      .then(function(d){{ if(d.error) throw new Error(d.error); return d; }});
  }}
  function show(){{ unlock.hidden=true; unlock.style.display='none'; panel.hidden=false; load(); }}
  function load(){{
    document.querySelectorAll('#tabs .btn').forEach(function(b){{ b.classList.toggle('is-active', b.dataset.days===days); }});
    document.getElementById('total').textContent='Loading\\u2026';
    api().then(function(d){{
      var label = days==='all' ? 'all time' : 'the last '+days+' days';
      document.getElementById('total').innerHTML='<strong>'+d.total+'</strong> Amazon link click'+(d.total===1?'':'s')+' in '+label+'.';
      table(document.getElementById('t-item'),'<th>Book or product</th><th>Page</th><th>Tracking ID</th><th class="n">Clicks</th>',
        d.byItem.map(function(r){{ return '<tr><td><a href="'+itemLink(r.item)+'" target="_blank" rel="noopener">'+itemName(r.item)+'</a></td><td><a href="'+esc(r.page)+'">'+pageName(r.page)+'</a></td><td class="click-sub">'+esc(r.tag||'(none)')+'</td><td class="n">'+r.clicks+'</td></tr>'; }}),
        'No clicks in this range yet.');
      table(document.getElementById('t-page'),'<th>Page</th><th class="n">Clicks</th>',
        d.byPage.map(function(r){{ return '<tr><td><a href="'+esc(r.page)+'">'+pageName(r.page)+'</a></td><td class="n">'+r.clicks+'</td></tr>'; }}),
        'No clicks in this range yet.');
      table(document.getElementById('t-tag'),'<th>Tracking ID</th><th class="n">Clicks</th>',
        d.byTag.map(function(r){{ return '<tr><td>'+esc(r.tag)+'</td><td class="n">'+r.clicks+'</td></tr>'; }}),
        'No clicks in this range yet.');
    }}).catch(function(e){{ document.getElementById('total').textContent=e.message; }});
  }}
  unlock.addEventListener('submit',function(ev){{
    ev.preventDefault(); key=unlock.key.value.trim(); note.textContent='Checking\\u2026';
    api().then(function(){{ sessionStorage.setItem(KEY,key); note.textContent=''; show(); }})
      .catch(function(e){{ note.textContent=e.message; }});
  }});
  document.getElementById('tabs').addEventListener('click',function(ev){{ var b=ev.target.closest('[data-days]'); if(b){{ days=b.dataset.days; load(); }} }});
  document.getElementById('lock').addEventListener('click',function(){{ sessionStorage.removeItem(KEY); key=''; location.reload(); }});
  if(key) show();
}})();
</script>
'''

page = head("Amazon Link Clicks", "Private report of Amazon link clicks on this site.", "clicks-admin.html", indexable=False) + header("") + body + footer()
open("clicks-admin.html", "w").write(page)
print("clicks-admin.html", len(page), f"({len(titles)} product names)")
