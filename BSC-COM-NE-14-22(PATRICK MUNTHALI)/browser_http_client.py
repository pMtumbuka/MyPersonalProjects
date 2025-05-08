
"""

THE FOLLOWING CODE IS SOURCED FROM THE "dummy PyQt5 app" IN "lab_05" IN THE
"qt_chat_client.py" FILE AND THE SERVER CODE THAT IS IN "server.py" FILE

"""

import sys
import os
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout,
    QWidget, QTextBrowser, QLabel, QMessageBox
)
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap
import pathlib

ICON_PATH = pathlib.Path(__file__).parent / "vector-mozilla-firefox-logo.jpg"

LOCAL_SERVER = "http://localhost:8085"
TEMPLATES_FOLDER = "templates"  

class LocalClientWebBrowser(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Local Search Engine")
        self.setWindowIcon(QIcon(QPixmap(str(ICON_PATH))))
        self.resize(500, 500)

        # Widgets to be added onto the Qt app
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter your search query here (e.g. index or register)...")
        self.search_button = QPushButton("Go To Site")
        self.web_display = QTextBrowser()
        self.status_code_label = QLabel()

        # Layout Of The Qt App
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.search_input)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.status_code_label)
        self.layout.addWidget(self.web_display)

        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # Event_Listener For When The Search Button Is Clicked
        self.search_button.clicked.connect(self.search_from_local)

    def search_from_local(self):
        input_query = self.search_input.text().strip().lower()

        if not input_query:
            self.status_code_label.setText("Please enter a search query.")
            return

        local_url = "{}/{}".format(LOCAL_SERVER, (input_query if input_query != 'index' else ''))

        try:
            response = requests.get(local_url)
            if response.status_code == 200:
                self.status_code_label.setText("Loaded from local server: {}".format(local_url))
                self.web_display.setHtml(response.text)
            else:
                self.handle_404_not_found(input_query)
        except requests.ConnectionError:
            self.status_code_label.setText("Unable to connect to local server.")
            QMessageBox.critical(self, "Connection Error", "Failed to connect to local server at http://localhost:8085")

    def handle_404_not_found(self, error_query):
        self.status_code_label.setText("The Document you are searching for was not found on the local server.")
        self.web_display.setHtml("""
            <h2>Document not found: {0}</h2>
            <p>The page you are looking for was not found on the local server.</p>
            <p><a href="https://www.google.com/search?q={1}">Search "{2}" on Google</a></p>
        """.format(error_query, error_query, error_query))
        
def main():
    client_app = QApplication(sys.argv)
    client_app_window = LocalClientWebBrowser()
    client_app_window.show()
    sys.exit(client_app.exec_())

if __name__ == "__main__":
    main()
    