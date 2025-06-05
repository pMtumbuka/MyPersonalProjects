from http.server import SimpleHTTPRequestHandler, HTTPServer # built in python module for the http server requests

host_addr = "localhost"

port_num = 8090

if __name__ == "__main__": 
    
    try:

        with HTTPServer(server_address=(host_addr, port_num), RequestHandlerClass=SimpleHTTPRequestHandler, bind_and_activate=True) as basic_http_server:

            print("Server Running On Port {}: {}".format(host_addr, port_num))

            basic_http_server.serve_forever()

    except Exception as an_error_occurred:
        
        print("An Error Occurred While Running The Server!")