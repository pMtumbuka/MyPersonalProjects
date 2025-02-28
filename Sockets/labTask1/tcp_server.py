import socket

HOST = 'localhost'

PORT = 12345

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = (HOST, PORT)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("TCP Server is listening on {}:{}".format(HOST, PORT))

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")

        # Receive data from the client
        data = connection.recv(4096)
        print(f"Received message: {data.decode()}")

        # Send a response back to the client
        response = f"Server received: {data.decode()}"
        connection.sendall(response.encode())
    finally:
        # Clean up the connection
        connection.close()
server_socket.close()