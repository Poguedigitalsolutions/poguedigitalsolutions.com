// Public: how many comments are waiting for moderation, and how many contact form messages
// are unread. Returns numbers only, never content.
// Used by the hourly scheduled check that pushes a notification to John.
export async function onRequestGet({ env }) {
  const row = await env.COMMENTS_DB.prepare(
    "SELECT COUNT(*) AS n FROM comments WHERE status = 'pending'"
  ).first();
  let messages = 0;
  try {
    const m = await env.COMMENTS_DB.prepare("SELECT COUNT(*) AS n FROM messages WHERE status = 'new'").first();
    messages = m ? m.n : 0;
  } catch {
    // the messages table is created by the first contact form submission
  }
  return new Response(JSON.stringify({ pending: row ? row.n : 0, messages }), {
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" },
  });
}
