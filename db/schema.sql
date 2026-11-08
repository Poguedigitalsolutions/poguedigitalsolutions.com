-- Blog comments. Apply with:
--   npx wrangler d1 execute pds-comments --remote --file db/schema.sql
CREATE TABLE IF NOT EXISTS comments (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  slug       TEXT NOT NULL,
  author     TEXT NOT NULL,
  email      TEXT,
  body       TEXT NOT NULL,
  status     TEXT NOT NULL DEFAULT 'pending',  -- pending | approved | spam
  ip_hash    TEXT,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_comments_slug_status ON comments (slug, status, created_at);
CREATE INDEX IF NOT EXISTS idx_comments_ip_time ON comments (ip_hash, created_at);

-- Amazon link clicks (cookie-free). One row per click: which page, which product, which tag, which day.
-- Nothing about the visitor is stored: no IP, no cookie, no browser details, no time of day.
CREATE TABLE IF NOT EXISTS link_clicks (
  id    INTEGER PRIMARY KEY AUTOINCREMENT,
  page  TEXT NOT NULL,                       -- path the click came from, e.g. /blog/how-to-ask-ai-the-right-question
  item  TEXT NOT NULL,                       -- Amazon ASIN, or amzn.to/<code> for short links
  tag   TEXT,                                -- Associates tracking ID in the link, e.g. blog0ce1f-20
  day   TEXT NOT NULL DEFAULT (date('now'))  -- UTC date only
);
CREATE INDEX IF NOT EXISTS idx_link_clicks_day ON link_clicks (day);
