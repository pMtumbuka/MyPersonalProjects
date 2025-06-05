from ftplib import FTP

server_addr1 = "127.0.0.1"

server_port1 = 9999

# Connect to the local server
ftp = FTP()
ftp.connect(host=server_addr1, port=server_port1)
ftp.login(user="PMM_Coyote", passwd="#Coyote#3456%#")

# List files
ftp.retrlines("LIST")

# Try downloading a file that exists
remote_filename = "getting_started_with_ftp.txt"
local_filename = "downloaded.txt"

# Download a file
with open("downloaded.txt", "wb") as downloaded_file:
    ftp.retrbinary("RETR {}".format(remote_filename), downloaded_file.write)
    
print("\nDownloaded {} as {}".format(remote_filename, local_filename))

# Upload a file
with open("upload.txt", "rb") as upload_file:
    ftp.storbinary("STOR upload.txt", upload_file)

ftp.quit()


"""

from ftplib import FTP

# Connect to FTP server
ftp = FTP()
ftp.connect("127.0.0.1", 9999)
ftp.login(user="user", passwd="12345")

# List files
print("Files on server:")
ftp.retrlines("LIST")

# Try downloading a file that exists
remote_filename = "getting_started_with_ftp.txt"
local_filename = "downloaded.txt"

with open(local_filename, "wb") as downloaded_file:
    ftp.retrbinary(f"RETR {remote_filename}", downloaded_file.write)

print(f"\nDownloaded {remote_filename} as {local_filename}")

# Quit FTP session
ftp.quit()


"""