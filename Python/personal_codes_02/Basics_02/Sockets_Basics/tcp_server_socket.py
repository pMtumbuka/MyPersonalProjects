import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a address and port
    server_socket.bind(('localhost', 12345))

    # Listen for incoming connections
    server_socket.listen(5)

    print("Server listening on port 12345...")

    while True:
        # Accept an incoming connection
        client_socket, address = server_socket.accept()

        print(f"Connection from {address} has been established.")

        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received data: {data.decode()}")

        # Send response back to the client
        response = "Hello from server!"
        client_socket.send(response.encode())

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    start_server()