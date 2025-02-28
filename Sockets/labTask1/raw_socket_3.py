import socket

# Create a sequenced packet socket
seqpacket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a address
seqpacket_socket.bind(("localhost", 8080))

# Listen for incoming connections
seqpacket_socket.listen(1)

print("Sequenced packet socket listening...")

while True:
    # Accept incoming connections
    connection, address = seqpacket_socket.accept()
    print("Connection from:", address)

    # Receive data from the client
    data = connection.recv(1024)
    print("Received data:", data)

    # Send data back to the client
    connection.sendall(b"Hello, client!")

    # Close the connection
    connection.close()
    
    
    '''
    
    import socket

# Create a sequenced packet socket
seqpacket_socket = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)

# Bind the socket to a address
seqpacket_socket.bind("/tmp/seqpacket_socket")

# Listen for incoming connections
seqpacket_socket.listen(1)

print("Sequenced packet socket listening...")

while True:
    # Accept incoming connections
    connection, address = seqpacket_socket.accept()
    print("Connection from:", address)

    # Receive data from the client
    data = connection.recv(1024)
    print("Received data:", data)

    # Send data back to the client
    connection.sendall(b"Hello, client!")

    # Close the connection
    connection.close()
    
    '''