from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello! This is the root endpoint.")
        elif self.path == "/info":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Info page.")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(post_data.decode())

        print("Received POST data:", parsed_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received. Thanks!\n")
        self.wfile.write(post_data)

host = "localhost"
port = 8090
server = HTTPServer((host, port), MyHandler)
print(f"Custom HTTP server running on {host}:{port}")
server.serve_forever()
