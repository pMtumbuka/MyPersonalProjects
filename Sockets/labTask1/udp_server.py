import socket

HOST = "192.168.43.58"

PORT = 0

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_address = (HOST, PORT)
server_socket.bind(server_address)

print(server_socket)

print("UDP Server is listening on {}:{}".format(HOST, PORT))

# print("UDP Server is listening on {}:{}".format(HOST, server_socket.getsockname()[1]))

while True:
    # Receive data from client
    data, client_address = server_socket.recvfrom(4096)
    print("Received message from {}: {}".format(client_address, data.decode()))

    # Send a response back to the client
    response = "Server received: {}".format(data.decode())
    server_socket.sendto(response.encode(), client_address)
    
server_socket.close()