from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Hello World - Someone accessed the server!")  # prints in terminal
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World")

HTTPServer(('localhost', 8080), Handler).serve_forever()
