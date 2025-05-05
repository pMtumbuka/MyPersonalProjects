from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class HandleClients(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"In the /root page")
        elif self.path == "/information":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"In the /root/information page")
        elif self.path == "/information/help":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"In the /root/information/help page")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 ERROR: The Page Was Not Found!")

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        data_to_be_posted = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(data_to_be_posted.decode())

        print("Received POST data! ", parsed_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data Has Been Received!")
        self.wfile.write(data_to_be_posted)

    def do_HEAD(self):
        if self.path in ["/", "/information", "/information/help"]:
            self.send_response(200)
        else:
            self.send_response(404)
        self.end_headers()

    def do_PUT(self):
        content_length2 = int(self.headers.get("Content-Length", 0))
        data_to_be_put = self.rfile.read(content_length2).decode()

        print("Received PUT Data! ", data_to_be_put)

        self.send_response(200)
        self.end_headers()
        response = "PUT Data Received at {}: \n {}".format(self.path, data_to_be_put)
        self.wfile.write(response.encode())

host_addr = "localhost"
port_number = 8090

base_http_server = HTTPServer((host_addr, port_number), HandleClients)

print("HTTP Server Running On {}:{}".format(host_addr, port_number))

base_http_server.serve_forever()
