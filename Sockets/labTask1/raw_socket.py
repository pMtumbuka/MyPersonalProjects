import socket

# Create a raw ICMP socket
icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Set the target IP address
target_ip = "192.168.1.100"

# Create an ICMP echo request packet
icmp_packet = b"\x08\x00\x00\x00\x00\x00\x00\x00"

# Send the ICMP echo request packet
icmp_socket.sendto(icmp_packet, (target_ip, 0))

# Receive the ICMP echo response packet
icmp_response, _ = icmp_socket.recvfrom(1024)

# Print the ICMP echo response packet
print(icmp_response)

# Close the ICMP socket
icmp_socket.close()