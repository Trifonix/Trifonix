from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 29")

    layout = QHBoxLayout()

    layout.addWidget(Color("red"))
    layout.addWidget(Color("lightcoral"))
    layout.addWidget(Color("darkred"))

    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
