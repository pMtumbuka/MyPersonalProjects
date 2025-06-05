from http.server import BaseHTTPRequestHandler, HTTPServer # built in python module for the http server requests

import urllib.request
import urllib.parse

class HandleClient(BaseHTTPRequestHandler):
    
    # The GET HTTP method requests a representation of the specified resource.("""Serve a GET request.""")
    def do_GET(self):
        
        if self.path == "/":
            self.send_response(200) # The server sends back the resource with a 200 OK status code, indicating success
            self.end_headers() # Adds a blank line (indicating the end of the HTTP headers in the response) to the headers buffer
            self.wfile.write(b"Hello This Is The Root Page!")
            
        elif self.path == "/information":
            self.send_response(200) # To Indicate That The resource has been fetched and transmitted in the message body.
            self.end_headers() # Adds a blank line (indicating the end of the HTTP headers in the response) to the headers buffer
            self.wfile.write(b"Hello This Is The Information Page!")
            
        elif self.path == "/information/help":
            self.send_response(200) # The resource has been fetched and transmitted in the message body.
            self.end_headers() # Adds a blank line (indicating the end of the HTTP headers in the response) to the headers buffer and calls flush_headers().
            self.wfile.write(b"Hello This Is The Help Page")
        
        # if the page being searched for does not exist    
        else:
            self.send_response(404) # File Not Found, The server cannot find the requested resource
            self.end_headers()
            self.wfile.write(b"404, 'File not found'")
            
    # The HEAD HTTP method requests the metadata of a resource in the form of headers that the server would have sent if the GET method was used instead
    def do_HEAD(self):
        # """Serve a HEAD request."""
        
        if self.path in [ "/", "/information", "/information/help" ]:
            self.send_response(200) # The Page Being Searched for exists in our DataBase
                                    # Representation headers are included in the response without any message body.
        else:
            self.send_response(404) # The Page Being Searched For Does Not Exist In Our DataBase
            self.end_headers()
            
    # The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.
    def do_POST(self):
        # """Serve a POST request.""" The POST HTTP method sends data to the server. The type of the body of the request is indicated by the Content-Type header.
        
        length_of_content = int(self.headers.get("Content-Length", 0))
        
        post_data = self.rfile.read(length_of_content)
        
        parsed_data = urllib.parse.parse_qs(post_data.decode())
        
        print("Received POST Data: ", parsed_data)
        
        self.send_response(200) # The resource describing the result of the action is transmitted in the message body.
        self.end_headers()
        self.wfile.write(b"The Data Has Been Received!")
        self.wfile.write(post_data)
        
    # The PUT HTTP method creates a new resource or replaces a representation of the target resource with the request content.
    def do_PUT(self):
        
        content_length = int(self.headers.get("Content-Length", 0))
        
        put_data = self.rfile.read(content_length)
        
        print("Received PUT Data: ", put_data)
        
        self.send_response(200) # The resource describing the result of the action is transmitted in the message body.
        self.end_headers()
        response = "PUT Data Received at {}: \n{}".format(self.path, put_data)
        self.wfile.write(response.encode())
        
# the definition of the address on which the server will be listening
host_addr = "localhost"
    
port_number = 8090
    
if __name__ == "__main__":    
    
    try:    
        # defining the server 
        with HTTPServer(server_address=(host_addr, port_number), RequestHandlerClass=HandleClient, bind_and_activate=True) as base_http_server:
    
            print("Server Running On {}: {}".format(host_addr, port_number))
    
            base_http_server.serve_forever()
        
    except Exception as an_error_occurred:
        
        print("An Error Occurred While Running The Server!")