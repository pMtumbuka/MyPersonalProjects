from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle("MyWindow")
        self.initUI()
        
    def initUI(self):
        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("My 1st Label")
        self.label_1.move(40, 110)
        
        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setText("Click Me")
        self.button_1.move(20, 60)
        self.button_1.clicked.connect(self.once_clicked)
        
    def once_clicked(self):
        self.label_1.setText("You Clicked Me")
        self.update_label_size()
        
    def update_label_size(self):
        self.label_1.adjustSize()
        
def show_MyWindow():
    myApp = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(myApp.exec_())
        
if __name__ == "__main__":
    show_MyWindow()