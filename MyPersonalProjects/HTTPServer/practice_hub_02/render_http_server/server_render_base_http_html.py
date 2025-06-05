from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os

TEMPLATES_DIR = 'templates'
DB_FILE = 'db.txt'
ASSETS_DIR = 'assets'

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.serve_file('index.html')
        elif self.path == '/register':
            self.serve_file('register.html')
        elif self.path.startswith('/assets/'):
            self.serve_static(self.path.lstrip('/'))
        else:
            self.send_error(404, 'File Not Found')

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()
            fields = urllib.parse.parse_qs(post_data)

            username = fields.get('username', [''])[0]
            email = fields.get('email', [''])[0]

            if username and email:
                with open(DB_FILE, 'a') as f:
                    f.write(f"{username} {email}\n")

                # Redirect after POST
                self.send_response(303)
                self.send_header('Location', '/')
                self.end_headers()
            else:
                self.send_error(400, 'Bad Request')
        else:
            self.send_error(405, 'Method Not Allowed')

    def serve_file(self, filename):
        filepath = os.path.join(TEMPLATES_DIR, filename)
        try:
            with open(filepath, 'rb') as f:
                content = f.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'File Not Found')

    def serve_static(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                content = f.read()

            # Guess content type
            if filepath.endswith('.jpg') or filepath.endswith('.jpeg'):
                content_type = 'image/jpeg'
            elif filepath.endswith('.png'):
                content_type = 'image/png'
            else:
                content_type = 'application/octet-stream'

            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'File Not Found')


def run():
    server_address = ('', 8085)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server running at http://localhost:8085...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
