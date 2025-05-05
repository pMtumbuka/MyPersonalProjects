import socket

def start_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send data to the server
    data = "Hello from client!"
    client_socket.sendto(data.encode(), ('localhost', 12345))

    # Receive response from the server
    response, address = client_socket.recvfrom(1024)
    print(f"Received response from {address}: {response.decode()}")

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()