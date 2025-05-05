import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))

    print("Connected to the server...")

    # Send data to the server
    data = "Hello from client!"
    client_socket.send(data.encode())

    # Receive response from the server
    response = client_socket.recv(1024)
    print(f"Received response: {response.decode()}")

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()