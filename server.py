from http.server import HTTPServer, SimpleHTTPRequestHandler

server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print("Serving at http://localhost:8080")
server.serve_forever()
