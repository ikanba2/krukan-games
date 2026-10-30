import http.server, time
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.webp'): time.sleep(4)
        return super().do_GET()
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store'); super().end_headers()
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('', 8812), H).serve_forever()
