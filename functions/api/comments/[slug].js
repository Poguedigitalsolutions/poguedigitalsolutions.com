// Blog comments API (Cloudflare Pages Function).
//   GET  /api/comments/<slug>  -> approved comments for that post
//   POST /api/comments/<slug>  -> submit a comment (held for moderation)
//
// Bindings (wrangler.toml / Pages settings):
//   COMMENTS_DB       D1 database
//   TURNSTILE_SECRET  Turnstile secret key (encrypted variable)

const MAX_NAME = 80;
const MAX_BODY = 2000;
const SUBMITS_PER_HOUR = 5;

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });

const SLUG = /^[a-z0-9-]{1,120}$/;

export async function onRequestGet({ params, env }) {
  const slug = params.slug;
  if (!SLUG.test(slug)) return json({ error: "Bad slug" }, 400);
  const { results } = await env.COMMENTS_DB.prepare(
    "SELECT id, author, body, created_at FROM comments WHERE slug = ? AND status = 'approved' ORDER BY created_at ASC"
  ).bind(slug).all();
  return json({ comments: results });
}

export async function onRequestPost({ request, params, env }) {
  const slug = params.slug;
  if (!SLUG.test(slug)) return json({ error: "Bad slug" }, 400);

  let data;
  try {
    data = await request.json();
  } catch {
    return json({ error: "Bad request" }, 400);
  }

  // Honeypot: real browsers leave this empty.
  if (data.website) return json({ ok: true, held: true });

  const author = String(data.author || "").trim().slice(0, MAX_NAME);
  const email = String(data.email || "").trim().slice(0, 254);
  const body = String(data.body || "").trim().slice(0, MAX_BODY);
  const token = String(data.token || "");

  if (author.length < 2) return json({ error: "Please add your name." }, 400);
  if (body.length < 3) return json({ error: "Please write a comment." }, 400);
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ error: "That email doesn't look right." }, 400);

  const ip = request.headers.get("cf-connecting-ip") || "";

  // Turnstile check.
  if (!env.TURNSTILE_SECRET) return json({ error: "Comments are not configured yet." }, 503);
  const form = new FormData();
  form.append("secret", env.TURNSTILE_SECRET);
  form.append("response", token);
  if (ip) form.append("remoteip", ip);
  let outcome;
  try {
    const verify = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", body: form });
    outcome = await verify.json();
  } catch {
    return json({ error: "Could not reach the verification service. Please try again." }, 502);
  }
  if (!outcome.success) return json({ error: "Verification failed. Please try again." }, 403);

  // Light rate limit per IP (hashed, never stored in the clear).
  const ipHash = await sha256(ip + (env.IP_SALT || "pds"));
  const recent = await env.COMMENTS_DB.prepare(
    "SELECT COUNT(*) AS n FROM comments WHERE ip_hash = ? AND created_at > datetime('now', '-1 hour')"
  ).bind(ipHash).first();
  if (recent && recent.n >= SUBMITS_PER_HOUR) return json({ error: "Too many comments. Try again in a bit." }, 429);

  await env.COMMENTS_DB.prepare(
    "INSERT INTO comments (slug, author, email, body, status, ip_hash) VALUES (?, ?, ?, ?, 'pending', ?)"
  ).bind(slug, author, email || null, body, ipHash).run();

  return json({ ok: true, held: true });
}

async function sha256(s) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
