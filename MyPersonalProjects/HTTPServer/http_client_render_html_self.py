import urllib.request # a library for handling user requests

import urllib.parse # a library for handling data transimission between the server and the client

server_url = "http://localhost:8090"

data_to_be_sent = { "name": "Patrick Mtumbuka Munthali", "message": "Hello From Client To Server AND Also True In Reverse" }

encoded_data = urllib.parse.urlencode(data_to_be_sent).encode() # encode the data to be sent into from a string literal a byte literal 

client_request_to_server = urllib.request.Request(server_url, data=encoded_data, method=None) # sending the request to the server

client_request_to_server.add_header("Content-Type", "application/x-www-form-urlencoded")

try:
    
    # echo back the response from the server
    with urllib.request.urlopen(client_request_to_server) as response_from_server: 
    
        response_text_received = response_from_server.read().decode() # since data is sent in byte literals, it needs to be converted to a string literal for ease readability by the client
    
        print("The Server Has Responded: \n", response_text_received) # print the received response to the console

except Exception as error:
    
    print("An Error Occurred While Contacting The Server!")