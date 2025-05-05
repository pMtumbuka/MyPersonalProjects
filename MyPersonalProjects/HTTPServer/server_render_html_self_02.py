from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import urllib.request

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        form_data = urllib.parse.parse_qs(post_data)

        first_name = form_data.get('first_name', [''])[0]
        last_name = form_data.get('last_name', [''])[0]

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = f'Hello, {first_name} {last_name}'
        self.wfile.write(message.encode())

if __name__ == "__main__":

    try:

        httpd = HTTPServer(('', 8090), SimpleHTTPRequestHandler)
        print("The Server Is Running On Port: 8090")
        httpd.serve_forever()
        
    except Exception as an_error_occurred:
        
        print("An ERROR Occurred While Trying To Run The Server!")