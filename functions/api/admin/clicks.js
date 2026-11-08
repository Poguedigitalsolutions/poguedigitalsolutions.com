// Amazon link click report. Every request must carry the admin key:
//   Authorization: Bearer <ADMIN_KEY>
//
//   GET /api/admin/clicks?days=30   -> click counts by product, by page, and by tracking ID
//   days: 7 | 30 | 90 | 365 | all   (default 30)

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });

function authorized(request, env) {
  const h = request.headers.get("authorization") || "";
  const key = h.startsWith("Bearer ") ? h.slice(7) : "";
  return Boolean(env.ADMIN_KEY) && key.length > 0 && timingSafeEqual(key, env.ADMIN_KEY);
}

function timingSafeEqual(a, b) {
  if (a.length !== b.length) return false;
  let out = 0;
  for (let i = 0; i < a.length; i++) out |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return out === 0;
}

const RANGES = { "7": 7, "30": 30, "90": 90, "365": 365, all: null };

export async function onRequestGet({ request, env }) {
  if (!authorized(request, env)) return json({ error: "Unauthorized" }, 401);
  const days = new URL(request.url).searchParams.get("days") || "30";
  if (!(days in RANGES)) return json({ error: "Bad range" }, 400);

  const where = RANGES[days] ? "WHERE day >= date('now', ?)" : "";
  const binds = RANGES[days] ? [`-${RANGES[days] - 1} days`] : [];
  const q = (sql) => env.COMMENTS_DB.prepare(sql).bind(...binds).all().then((r) => r.results);

  let byItem, byPage, byTag, byDay;
  try {
    [byItem, byPage, byTag, byDay] = await Promise.all([
    q(`SELECT item, page, tag, COUNT(*) AS clicks, MAX(day) AS last_day FROM link_clicks ${where} GROUP BY item, page, tag ORDER BY clicks DESC, last_day DESC LIMIT 500`),
    q(`SELECT page, COUNT(*) AS clicks FROM link_clicks ${where} GROUP BY page ORDER BY clicks DESC LIMIT 200`),
    q(`SELECT COALESCE(tag, '(none)') AS tag, COUNT(*) AS clicks FROM link_clicks ${where} GROUP BY tag ORDER BY clicks DESC`),
    q(`SELECT day, COUNT(*) AS clicks FROM link_clicks ${where} GROUP BY day ORDER BY day DESC LIMIT 400`),
  ]);
  } catch (err) {
    return json({ error: "The click table is not set up yet. Run the link_clicks setup from db/schema.sql in the D1 console for pds-comments." }, 503);
  }
  const total = byPage.reduce((n, r) => n + r.clicks, 0);
  return json({ days, total, byItem, byPage, byTag, byDay });
}
