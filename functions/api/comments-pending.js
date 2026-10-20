// Public: how many comments are waiting for moderation. Returns a number only, never content.
// Used by the hourly scheduled check that pushes a notification to John.
export async function onRequestGet({ env }) {
  const row = await env.COMMENTS_DB.prepare(
    "SELECT COUNT(*) AS n FROM comments WHERE status = 'pending'"
  ).first();
  return new Response(JSON.stringify({ pending: row ? row.n : 0 }), {
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });
}
