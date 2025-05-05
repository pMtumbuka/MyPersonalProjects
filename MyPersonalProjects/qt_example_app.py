from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("My First Qt App")
window.setMinimumSize(400, 300)

label = QLabel("Hello, Qt!", parent=window)
label.move(150, 140)

window.show()
app.exec()