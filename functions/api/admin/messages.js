// Contact form inbox. Every request must carry the admin key:
//   Authorization: Bearer <ADMIN_KEY>
//
//   GET    /api/admin/messages?status=new   -> list messages by status (new|read)
//   PATCH  /api/admin/messages  {id, status} -> mark read / new
//   DELETE /api/admin/messages  {id}         -> delete permanently

import { MESSAGES_TABLE } from "../contact.js";

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });

const STATUSES = new Set(["new", "read"]);

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

export async function onRequest({ request, env }) {
  if (!authorized(request, env)) return json({ error: "Unauthorized" }, 401);
  await env.COMMENTS_DB.prepare(MESSAGES_TABLE).run();

  if (request.method === "GET") {
    const url = new URL(request.url);
    const status = url.searchParams.get("status") || "new";
    if (!STATUSES.has(status)) return json({ error: "Bad status" }, 400);
    const { results } = await env.COMMENTS_DB.prepare(
      "SELECT id, name, email, topic, body, status, created_at FROM messages WHERE status = ? ORDER BY created_at DESC LIMIT 200"
    ).bind(status).all();
    const counts = await env.COMMENTS_DB.prepare(
      "SELECT status, COUNT(*) AS n FROM messages GROUP BY status"
    ).all();
    return json({ messages: results, counts: Object.fromEntries(counts.results.map((r) => [r.status, r.n])) });
  }

  let data;
  try {
    data = await request.json();
  } catch {
    return json({ error: "Bad request" }, 400);
  }
  const id = Number(data.id);
  if (!Number.isInteger(id) || id <= 0) return json({ error: "Bad id" }, 400);

  if (request.method === "PATCH") {
    if (!STATUSES.has(data.status)) return json({ error: "Bad status" }, 400);
    await env.COMMENTS_DB.prepare("UPDATE messages SET status = ? WHERE id = ?").bind(data.status, id).run();
    return json({ ok: true });
  }
  if (request.method === "DELETE") {
    await env.COMMENTS_DB.prepare("DELETE FROM messages WHERE id = ?").bind(id).run();
    return json({ ok: true });
  }
  return json({ error: "Method not allowed" }, 405);
}
