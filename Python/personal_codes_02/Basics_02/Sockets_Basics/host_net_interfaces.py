import psutil
import socket  # Import socket for address family constants

def list_network_interfaces():
    # Get network interface details
    interfaces = psutil.net_if_addrs()

    # Print the list of network interfaces
    print("Network Interfaces:")
    for interface_name, interface_addresses in interfaces.items():
        print("Interface: {}".format(interface_name))
        for address in interface_addresses:
            if address.family == socket.AF_PACKET:  # Use socket.AF_PACKET for MAC addresses on Linux
                print("  MAC Address: {}".format(address.address))
            elif address.family == socket.AF_INET:  # IPv4
                print("  IP Address: {}".format(address.address))
                print("  Netmask: {}".format(address.netmask))
                print("  Broadcast IP: {}".format(address.broadcast))
            elif address.family == socket.AF_INET6:  # IPv6
                print("  IPv6 Address: {}".format(address.address))
        print()

if __name__ == "__main__":
    list_network_interfaces()
