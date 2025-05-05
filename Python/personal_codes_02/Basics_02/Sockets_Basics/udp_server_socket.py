import socket

def start_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a address and port
    server_socket.bind(('localhost', 12345))

    print("Server listening on port 12345...")

    while True:
        # Receive data from the client
        data, address = server_socket.recvfrom(1024)
        print(f"Received data from {address}: {data.decode()}")

        # Send response back to the client
        response = "Hello from server!"
        server_socket.sendto(response.encode(), address)

if __name__ == "__main__":
    start_server()