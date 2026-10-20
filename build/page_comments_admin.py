"""Comment moderation page at /comments-admin. Not linked from the site, noindex.
Unlock it with the ADMIN_KEY set in the Pages project; the key is kept in this browser only."""
from parts import *

body = f'''
<section class="tight" style="padding-top:56px;">
  <div class="wrap" style="max-width:860px;">
    <span class="eyebrow">Moderation</span>
    <h1 style="font-size:clamp(28px,3.6vw,40px); margin-top:16px;">Blog Comments</h1>
    <p style="margin-top:10px; color:var(--charcoal);">Everything readers submit lands here first. Approve it to publish, mark it spam to hide it, or delete it for good.</p>

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
          <button class="btn btn-outline-navy" data-status="pending">Pending <span id="n-pending"></span></button>
          <button class="btn btn-outline-navy" data-status="approved">Approved <span id="n-approved"></span></button>
          <button class="btn btn-outline-navy" data-status="spam">Spam <span id="n-spam"></span></button>
        </div>
        <button class="btn btn-outline-navy" id="lock" type="button">Lock</button>
      </div>
      <div class="comments-list" id="mod-list" style="margin-top:22px;"></div>
    </div>
  </div>
</section>
<style>
.tabs {{ display:flex; flex-wrap:wrap; gap:10px; }}
.tabs .btn.is-active {{ background:var(--ink); color:var(--white); border-color:var(--ink); }}
.mod-actions {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:12px; }}
.mod-actions button {{ font:inherit; font-size:13px; padding:7px 14px; border-radius:var(--radius-pill); border:1px solid var(--line-light); background:var(--white); cursor:pointer; }}
.mod-actions button:hover {{ border-color:var(--gold); }}
.mod-actions .danger:hover {{ border-color:#a33; color:#a33; }}
.mod-meta {{ font-family:var(--font-mono); font-size:11px; letter-spacing:0.06em; text-transform:uppercase; color:var(--gold-dim); margin-top:6px; }}
</style>
<script>
(function(){{
  var KEY='pds_comments_admin_key', key=sessionStorage.getItem(KEY)||'', status='pending';
  var unlock=document.getElementById('unlock'), panel=document.getElementById('panel'), list=document.getElementById('mod-list');
  var note=unlock.querySelector('.comments-note');
  function esc(s){{return String(s).replace(/[&<>"']/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c];}});}}
  function api(method,qs,body){{
    return fetch('/api/admin/comments'+(qs||''),{{method:method,headers:{{'authorization':'Bearer '+key,'content-type':'application/json'}},body:body?JSON.stringify(body):undefined}})
      .then(function(r){{ if(r.status===401) throw new Error('Wrong key.'); return r.json(); }});
  }}
  function show(){{ unlock.hidden=true; unlock.style.display='none'; panel.hidden=false; load(); }}
  function load(){{
    document.querySelectorAll('#tabs .btn').forEach(function(b){{ b.classList.toggle('is-active', b.dataset.status===status); }});
    list.innerHTML='<p class="comments-empty">Loading&hellip;</p>';
    api('GET','?status='+status).then(function(d){{
      ['pending','approved','spam'].forEach(function(s){{ document.getElementById('n-'+s).textContent=d.counts[s]?'('+d.counts[s]+')':''; }});
      if(!d.comments.length){{ list.innerHTML='<p class="comments-empty">Nothing here.</p>'; return; }}
      list.innerHTML=d.comments.map(function(c){{
        var acts='';
        if(status!=='approved') acts+='<button data-act="approved" data-id="'+c.id+'">Approve</button>';
        if(status!=='pending') acts+='<button data-act="pending" data-id="'+c.id+'">Move to pending</button>';
        if(status!=='spam') acts+='<button data-act="spam" data-id="'+c.id+'">Spam</button>';
        acts+='<button class="danger" data-act="delete" data-id="'+c.id+'">Delete</button>';
        return '<div class="comment"><div class="comment-head"><strong>'+esc(c.author)+'</strong><time>'+esc(c.created_at)+' UTC</time></div>'
          +'<div class="mod-meta">On <a href="/blog/'+esc(c.slug)+'" target="_blank" rel="noopener">'+esc(c.slug)+'</a>'+(c.email?' &middot; '+esc(c.email):'')+'</div>'
          +'<p style="margin-top:10px;">'+esc(c.body).replace(/\\n/g,'<br>')+'</p><div class="mod-actions">'+acts+'</div></div>';
      }}).join('');
    }}).catch(function(e){{ list.innerHTML='<p class="comments-empty">'+esc(e.message)+'</p>'; }});
  }}
  unlock.addEventListener('submit',function(ev){{
    ev.preventDefault(); key=unlock.key.value.trim(); note.textContent='Checking\\u2026';
    api('GET','?status=pending').then(function(){{ sessionStorage.setItem(KEY,key); note.textContent=''; show(); }})
      .catch(function(e){{ note.textContent=e.message; }});
  }});
  document.getElementById('tabs').addEventListener('click',function(ev){{ var b=ev.target.closest('[data-status]'); if(b){{ status=b.dataset.status; load(); }} }});
  document.getElementById('lock').addEventListener('click',function(){{ sessionStorage.removeItem(KEY); key=''; location.reload(); }});
  list.addEventListener('click',function(ev){{
    var b=ev.target.closest('[data-act]'); if(!b) return;
    var id=Number(b.dataset.id), act=b.dataset.act;
    if(act==='delete'){{ if(!confirm('Delete this comment permanently?')) return; api('DELETE','',{{id:id}}).then(load); return; }}
    api('PATCH','',{{id:id,status:act}}).then(load);
  }});
  if(key) show();
}})();
</script>
'''

page = head("Comment Moderation", "Moderation for blog comments.", "comments-admin.html", indexable=False) + header("") + body + footer()
open("comments-admin.html", "w").write(page)
print("comments-admin.html", len(page))
