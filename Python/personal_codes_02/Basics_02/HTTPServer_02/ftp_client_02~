from ftplib import FTP
import os

class FTPClient:
    def __init__(self, host='127.0.0.1', port=2121, username='user', password='12345'):
        self.ftp = FTP()
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        """Connect to the FTP server"""
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.username, self.password)
        print(f"Connected to {self.host}:{self.port}")

    def disconnect(self):
        """Disconnect from the server"""
        self.ftp.quit()
        print("Disconnected from server")

    def list_files(self, directory='.'):
        """LIST operation - list files in directory"""
        print(f"Listing files in {directory}:")
        files = []
        self.ftp.retrlines(f'LIST {directory}', files.append)
        for file in files:
            print(file)
        return files

    def get_file(self, remote_file, local_file=None):
        """GET operation - download file from server"""
        if local_file is None:
            local_file = os.path.basename(remote_file)

        print(f"Downloading {remote_file} to {local_file}")
        with open(local_file, 'wb') as f:
            self.ftp.retrbinary(f'RETR {remote_file}', f.write)
        print("Download complete")
        return local_file

    def put_file(self, local_file, remote_file=None):
        """PUT operation - upload file to server"""
        if remote_file is None:
            remote_file = os.path.basename(local_file)

        print(f"Uploading {local_file} to {remote_file}")
        with open(local_file, 'rb') as f:
            self.ftp.storbinary(f'STOR {remote_file}', f)
        print("Upload complete")
        return remote_file

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

# Example usage
if __name__ == "__main__":
    with FTPClient() as client:
        # LIST operation
        client.list_files()

        # PUT operation (upload)
        client.put_file('example.txt')  # Uploads example.txt to server

        # GET operation (download)
        client.get_file('example.txt', 'downloaded_example.txt')  # Downloads to new filename

        # Verify upload by listing again
        client.list_files()
