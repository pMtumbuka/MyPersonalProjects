import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QLineEdit, QFileDialog, QLabel, QMessageBox
)
from ftplib import FTP, error_perm
from PyQt5.QtGui import QIcon

class FTPClientApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ftp = None
        self.init_ui()
        self.resize(800, 600)
        
        self.setWindowIcon(QIcon("Quick-‘n-Easy-FTP-Server-Logo-1.png"))  

        # Or get the current size
        width = self.width()
        height = self.height()
        print("Window size: {} x {}".format(width, height))


    def init_ui(self):
        self.setWindowTitle("FTP Client - PyQt5")

        layout = QVBoxLayout()

        self.status_label = QLabel("Status: Disconnected")
        layout.addWidget(self.status_label)

        self.connect_button = QPushButton("Connect to FTP Server")
        self.connect_button.clicked.connect(self.connect_to_ftp)
        layout.addWidget(self.connect_button)

        self.list_button = QPushButton("List Files")
        self.list_button.clicked.connect(self.list_files)
        self.list_button.setEnabled(False)
        layout.addWidget(self.list_button)

        self.upload_button = QPushButton("Upload File")
        self.upload_button.clicked.connect(self.upload_file)
        self.upload_button.setEnabled(False)
        layout.addWidget(self.upload_button)

        self.download_line_edit = QLineEdit()
        self.download_line_edit.setPlaceholderText("Enter filename to download")
        layout.addWidget(self.download_line_edit)

        self.download_button = QPushButton("Download File")
        self.download_button.clicked.connect(self.download_file)
        self.download_button.setEnabled(False)
        layout.addWidget(self.download_button)
        
        self.disconnect_button = QPushButton("Disconnect from FTP Server")
        self.disconnect_button.clicked.connect(self.disconnect_from_ftp)
        self.disconnect_button.setEnabled(False)
        layout.addWidget(self.disconnect_button)


        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def connect_to_ftp(self):
        try:
            self.ftp = FTP()
            self.ftp.connect("127.0.0.1", 9999)
            self.ftp.login("PMM_Coyote", "Coyote3456")
            self.status_label.setText("Status: Connected to FTP Server")
            self.output.append("Connected to FTP server at 127.0.0.1:9999")
            self.list_button.setEnabled(True)
            self.upload_button.setEnabled(True)
            self.download_button.setEnabled(True)
            self.disconnect_button.setEnabled(True)

        except Exception as e:
            QMessageBox.critical(self, "Connection Error", str(e))

    def list_files(self):
        try:
            self.output.append("Listing files...")
            files = self.ftp.nlst()
            self.output.append("\n".join(files))
        except error_perm as e:
            self.output.append("Permission Error: {}".format(e))
        except Exception as e:
            self.output.append("Error: {}".format(e))

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File to Upload")
        if file_path:
            try:
                with open(file_path, "rb") as f:
                    filename = file_path.split("/")[-1]
                    self.ftp.storbinary("STOR {}".format(filename), f)
                    self.output.append("Uploaded: {}".format(filename))
            except Exception as e:
                self.output.append("Upload Error: {}".format(e))

    def download_file(self):
        filename = self.download_line_edit.text()
        if filename:
            save_path, _ = QFileDialog.getSaveFileName(self, "Save Downloaded File As", filename)
            if save_path:
                try:
                    with open(save_path, "wb") as f:
                        self.ftp.retrbinary("RETR {}".format(filename), f.write)
                        self.output.append("Downloaded: {}".format(filename))
                except Exception as e:
                    self.output.append("Download Error: {}".format(e))
                    
    def disconnect_from_ftp(self):
        if self.ftp:
            try:
                self.ftp.quit()
                self.output.append("Disconnected from FTP server.")
            except Exception as e:
                self.output.append("Error during disconnect: {}".format(e))
            finally:
                self.ftp = None
                self.status_label.setText("Status: Disconnected")
                self.list_button.setEnabled(False)
                self.upload_button.setEnabled(False)
                self.download_button.setEnabled(False)
                self.disconnect_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FTPClientApp()
    window.show()
    sys.exit(app.exec_())
