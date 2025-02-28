import socket

HOST = 'localhost'

PORT = 12345

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address
server_address = (HOST, PORT)

# Connect to the server
client_socket.connect(server_address)

try:
    # Send data to the server
    message = "Hello, TCP Server!"
    client_socket.sendall(message.encode())

    # Receive response from the server
    data = client_socket.recv(4096)
    print(f"Received response from server: {data.decode()}")
finally:
    # Close the socket
    client_socket.close()