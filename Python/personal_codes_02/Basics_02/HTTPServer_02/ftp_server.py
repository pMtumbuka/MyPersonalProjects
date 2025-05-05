from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

class CustomFTPHandler(FTPHandler):
    def on_file_sent(self, file):
        print(f"GET command executed: Sent file {file}")

    def on_file_received(self, file):
        print(f"PUT command executed: Received file {file}")

    def on_list(self, path):
        print(f"LIST command executed: Listing {path}")

# Setup user authentication
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", ".", perm="elradfmwMT")  # full permissions
authorizer.add_anonymous(".")

# Setup custom handler
handler = CustomFTPHandler
handler.authorizer = authorizer

# Start the server
server = FTPServer(("127.0.0.1", 2121), handler)
print("FTP server running on port 2121")
server.serve_forever()
