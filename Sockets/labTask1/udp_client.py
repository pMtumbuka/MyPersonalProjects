import socket

HOST = input("Enter The IP Address Of The Server Here: ")

PORT = int(input("Enter The Port Number On Which The Server Is Running: "))

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = (HOST, PORT)

# Send data to the server
message = input("What Message Would You Like To Send To The Server? ")
client_socket.sendto(message.encode(), server_address)
# Receive response from the server
data, server = client_socket.recvfrom(4096)
print(f"Received response from server: {data.decode()}")

# Close the socket
client_socket.close()