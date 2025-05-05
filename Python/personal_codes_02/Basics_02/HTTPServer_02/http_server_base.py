from http.server import BaseHTTPRequestHandler, HTTPServer

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

host = "localhost"
port = 9999
server = HTTPServer((host, port), MyHandler)
print("Custom HTTP server running on {}:{}".format(host, port))
server.serve_forever()
