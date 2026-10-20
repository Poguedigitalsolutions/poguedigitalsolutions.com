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
