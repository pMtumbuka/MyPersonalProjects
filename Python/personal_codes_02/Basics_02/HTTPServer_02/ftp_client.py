from ftplib import FTP

def connect_ftp(host="127.0.0.1", port=2121, user="user", passwd="12345"):
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(user, passwd)
    print("Connected to FTP server")
    return ftp

def list_files(ftp):
    print("Listing files:")
    ftp.retrlines("LIST")

def download_file(ftp, filename, dest_path):
    with open(dest_path, "wb") as f:
        ftp.retrbinary(f"RETR {filename}", f.write)
    print(f"Downloaded: {filename} to {dest_path}")

def upload_file(ftp, local_path, remote_filename=None):
    if not remote_filename:
        remote_filename = local_path.split("/")[-1]
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_filename}", f)
    print(f"Uploaded: {local_path} as {remote_filename}")

def main():
    ftp = connect_ftp()

    list_files(ftp)

    # Example GET (download)
    try:
        download_file(ftp, "server_file.txt", "client_download.txt")
    except Exception as e:
        print(f"GET failed: {e}")

    # Example PUT (upload)
    try:
        upload_file(ftp, "client_upload.txt")
    except Exception as e:
        print(f"PUT failed: {e}")

    ftp.quit()

if __name__ == "__main__":
    main()
