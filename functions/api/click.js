// Records one click on an Amazon link (cookie-free). Called by js/site.js with navigator.sendBeacon.
//   POST /api/click  {page, item, tag}  -> 204
// Stores only the page path, the product (ASIN or amzn.to code), the tracking ID, and the date.
// Nothing about the visitor is kept.

const PAGE = /^\/[a-z0-9/_-]{0,160}$/;
const ITEM = /^([A-Z0-9]{10}|amzn\.to\/[A-Za-z0-9]{4,16})$/;
const TAG = /^[a-z0-9-]{1,40}$/;

const done = (status = 204) => new Response(null, { status, headers: { "cache-control": "no-store" } });

export async function onRequestPost({ request, env }) {
  // Only accept clicks sent from this site's own pages.
  const origin = request.headers.get("origin");
  if (origin && new URL(origin).host !== new URL(request.url).host) return done(403);

  let data;
  try {
    data = JSON.parse(await request.text());
  } catch {
    return done(400);
  }
  const page = String(data.page || "").toLowerCase().replace(/\/+$/, "") || "/";
  const item = String(data.item || "");
  const tag = data.tag ? String(data.tag).toLowerCase() : null;
  if (!PAGE.test(page) || !ITEM.test(item) || (tag && !TAG.test(tag))) return done(400);

  await env.COMMENTS_DB.prepare("INSERT INTO link_clicks (page, item, tag) VALUES (?, ?, ?)")
    .bind(page, item, tag).run();
  return done();
}
