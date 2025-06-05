from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import logging

logging.basicConfig(level=logging.DEBUG)

# Set up the authorizer
authorizer = DummyAuthorizer()

authorizer.add_user(
    username="PMM_Coyote",
    password="Coyote3456",
    homedir=r"C:\Users\mtumb\Documents\CodingEnv\Python\MyPersonalProjects\HTTPServer\practice_hub_02\ftp_server",
    perm="elradfmwMT"
)

# Set up the FTP handler
handler = FTPHandler
handler.authorizer = authorizer

#This sets up the FTP handler. passive_ports defines the range of ports used 
#for passive mode data connections (important for FTP clients behind firewalls/NAT).
handler.passive_ports = range(60000, 65535)

host_addr = "127.0.0.1"

port_num = 9999

# Start the FTP server
ftp_server = FTPServer((host_addr, port_num), handler)

print("FTP server running on port 9999, press Ctrl+C to stop")

try:
    with ftp_server as ftp_with1:
        ftp_with1.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down FTP server... Received a KeyboardInterrupt")
    ftp_server.close_all()
