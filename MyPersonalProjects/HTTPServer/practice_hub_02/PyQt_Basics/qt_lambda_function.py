from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signals && Slots")
        self.setGeometry(0, 0, 1000, 800)
        self.setWindowIcon(QIcon("cpp-qml-1-5b-data-flow-signal-slot-1")) 

        self.label = QLabel("Click a button!")
        self.label.setFont(QFont("Arial", 30))
        self.label.setAlignment(Qt.AlignCenter)

        self.button1 = QPushButton("Say Hello")
        self.button2 = QPushButton("Say Goodbye")

        self.button1.clicked.connect(lambda: self.greet("Hello!"))
        self.button2.clicked.connect(lambda: self.greet("Goodbye!"))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def greet(self, message):
        self.label.setText(message)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
