# hello, world!
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
  def __init__(self):
    super(Window, self).__init__()

    self.setWindowTitle("Простая программа")
    self.setGeometry(300, 250, 350, 200)

    self.main_text = QtWidgets.QLabel(self)
    self.main_text.setText("Это базовая надпись")
    self.main_text.move(100, 100)
    self.main_text.adjustSize()

    self.btn = QtWidgets.QPushButton(self)
    self.btn.move(70, 150)
    self.btn.setText("Нажми на меня")
    self.btn.setFixedWidth(200)
    self.btn.clicked.connect(self.add_label)

  def add_label(self):
    print("123")

def application():
  app = QApplication(sys.argv)
  window = Window()

  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  application()
