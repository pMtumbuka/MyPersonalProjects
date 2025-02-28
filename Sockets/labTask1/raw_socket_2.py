import socket

# Create a raw IP socket
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

# Set the IP header
ip_header = b"\x45\x00\x00\x3c\x12\x34\x00\x00\x40\x06\x00\x00\xc0\xa8\x01\x01\xc0\xa8\x01\x02"
raw_socket.sendto(ip_header + b"Hello, World!", ("192.168.1.2", 0))

# Close the raw socket
raw_socket.close()