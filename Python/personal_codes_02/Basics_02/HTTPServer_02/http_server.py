from http.server import SimpleHTTPRequestHandler, HTTPServer

host = "localhost"
port = 9999

# Serve files from current directory
server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print("Serving HTTP on {}:{}".format(host, port))
server.serve_forever()
