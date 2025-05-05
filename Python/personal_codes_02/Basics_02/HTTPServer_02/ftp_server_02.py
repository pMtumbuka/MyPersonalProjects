from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

class CustomFTPHandler(FTPHandler):
    def on_file_received(self, file):
        # This method is called when a file is completely received (PUT operation)
        super().on_file_received(file)
        print(f"File {file} uploaded successfully (PUT operation)")

    def on_file_sent(self, file):
        # This method is called when a file is completely sent (GET operation)
        super().on_file_sent(file)
        print(f"File {file} downloaded successfully (GET operation)")

    def ftp_LIST(self, path):
        # This method handles the LIST command
        try:
            # Call the original LIST implementation
            super().ftp_LIST(path)
            print(f"Directory listing for {path} (LIST operation)")
        except Exception as e:
            print(f"Error during LIST operation: {e}")
            raise

# Setup user authentication
authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", ".", perm="elradfmwMT")  # full permissions
authorizer.add_anonymous(".")

handler = CustomFTPHandler
handler.authorizer = authorizer

# Enable passive mode
handler.passive_ports = range(60000, 65535)

server = FTPServer(("127.0.0.1", 2121), handler)
print("FTP server running on port 2121 (supports GET, PUT, LIST)")
server.serve_forever()
