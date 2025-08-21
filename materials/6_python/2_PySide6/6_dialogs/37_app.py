import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 37")

    button = QPushButton("Нажми меня для диалога!")
    button.clicked.connect(self.button_clicked)
    self.setCentralWidget(button)

  def button_clicked(self, s):
    print("Клац!", s)

    dlg = QDialog(self)
    dlg.setWindowTitle("Привет!")
    dlg.exec()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
