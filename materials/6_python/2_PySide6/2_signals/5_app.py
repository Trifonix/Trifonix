from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.my_count = 1

    self.setWindowTitle("Fifth app")
    self.setFixedWidth(640)

    self.btn = QPushButton("New button")
    self.btn.clicked.connect(self.my_print)
    self.setCentralWidget(self.btn)

  def my_print(self):
    self.my_count *= 2
    self.btn.setText(f"Удвоено: {self.my_count} байт")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
