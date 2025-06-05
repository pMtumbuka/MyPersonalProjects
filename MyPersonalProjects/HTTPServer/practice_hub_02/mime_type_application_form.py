from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class FormHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        form_data = parse_qs(post_data)  # Parses URL-encoded data
        
        username = form_data.get('username', [''])[0]
        password = form_data.get('password', [''])[0]
        
        print(f"Username: {username}, Password: {password}")
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Form received!")

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), FormHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()