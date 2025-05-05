from http.server import SimpleHTTPRequestHandler, HTTPServer

# host_addr = "localhost"

# port_number = 8090

simple_http_server = HTTPServer(("localhost", 8090), SimpleHTTPRequestHandler)

print("HTTP Server Running on {}:{}".format("localhost", 8090))

simple_http_server.serve_forever()

