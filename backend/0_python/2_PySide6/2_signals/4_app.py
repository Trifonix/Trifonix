from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
 
    self.count = 0
    self.setWindowTitle("New good app")
    self.setFixedSize(400, 400)

    self.btn = QPushButton("Push me plz")
    self.btn.setCheckable(True)
    self.btn.clicked.connect(self.my_print)

    self.setCentralWidget(self.btn)

  def my_print(self, checked):
    self.count += 1
    print("Hello World", checked, self.count)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
