"""Local preview server that mimics Cloudflare Pages clean URLs (/about -> about.html,
/blog/ -> blog/index.html, unknown -> 404.html). Run from the repo root: python3 build/serve.py"""
import http.server, os, sys
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
class H(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.path.split("?")[0].split("#")[0]
        fs = path.lstrip("/")
        for c in [fs, fs + ".html", os.path.join(fs, "index.html")]:
            if c and os.path.isfile(c) or (c == "" and False):
                self.path = "/" + c
                return super().send_head()
        if path == "/":
            self.path = "/index.html"; return super().send_head()
        self.send_response(404); self.send_header("Content-Type", "text/html"); self.end_headers()
        return open("404.html", "rb")
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
