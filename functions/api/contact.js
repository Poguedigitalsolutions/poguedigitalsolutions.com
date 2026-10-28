// Contact form API (Cloudflare Pages Function).
//   POST /api/contact  {name, email, topic, message, token, website}
// Messages are stored in D1 and read by John at /comments-admin (Messages tab).
//
// Bindings (wrangler.toml / Pages settings):
//   COMMENTS_DB       D1 database (shared with blog comments; the messages table is created on first use)
//   TURNSTILE_SECRET  Turnstile secret key (encrypted variable)

const MAX_NAME = 80;
const MAX_MESSAGE = 4000;
const SUBMITS_PER_HOUR = 5;
const TOPICS = new Set(["strategy", "assessment", "brand-voice-ai", "project", "advisory", "workshop", "government", "partnerships", "general"]);

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });

export const MESSAGES_TABLE = `CREATE TABLE IF NOT EXISTS messages (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  name       TEXT NOT NULL,
  email      TEXT NOT NULL,
  topic      TEXT NOT NULL,
  body       TEXT NOT NULL,
  status     TEXT NOT NULL DEFAULT 'new',
  ip_hash    TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
)`;

export async function onRequestPost({ request, env }) {
  let data;
  try {
    data = await request.json();
  } catch {
    return json({ error: "Bad request" }, 400);
  }

  // Honeypot: real browsers leave this empty.
  if (data.website) return json({ ok: true });

  const name = String(data.name || "").trim().slice(0, MAX_NAME);
  const email = String(data.email || "").trim().slice(0, 254);
  const topic = TOPICS.has(data.topic) ? data.topic : "general";
  const body = String(data.message || "").trim().slice(0, MAX_MESSAGE);
  const token = String(data.token || "");

  if (name.length < 2) return json({ error: "Please add your name." }, 400);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ error: "Please add an email address John can reply to." }, 400);
  if (body.length < 5) return json({ error: "Please write a short message." }, 400);

  const ip = request.headers.get("cf-connecting-ip") || "";

  // Turnstile check.
  if (!env.TURNSTILE_SECRET) return json({ error: "The form is not configured yet. Please email john@poguedigitalsolutions.com." }, 503);
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

  await env.COMMENTS_DB.prepare(MESSAGES_TABLE).run();

  // Light rate limit per IP (hashed, never stored in the clear).
  const ipHash = await sha256(ip + (env.IP_SALT || "pds"));
  const recent = await env.COMMENTS_DB.prepare(
    "SELECT COUNT(*) AS n FROM messages WHERE ip_hash = ? AND created_at > datetime('now', '-1 hour')"
  ).bind(ipHash).first();
  if (recent && recent.n >= SUBMITS_PER_HOUR) return json({ error: "Too many messages. Try again in a bit, or email john@poguedigitalsolutions.com." }, 429);

  await env.COMMENTS_DB.prepare(
    "INSERT INTO messages (name, email, topic, body, status, ip_hash) VALUES (?, ?, ?, ?, 'new', ?)"
  ).bind(name, email, topic, body, ipHash).run();

  return json({ ok: true });
}

async function sha256(s) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
