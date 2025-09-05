import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 27")

    widget = Color("lightgreen")
    self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
