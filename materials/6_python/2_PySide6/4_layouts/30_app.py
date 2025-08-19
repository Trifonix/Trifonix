from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 30")

    layout1 = QHBoxLayout()
    layout2 = QVBoxLayout()
    layout3 = QVBoxLayout()

    layout1.setContentsMargins(0,0,0,0)
    layout1.setSpacing(0)

    layout2.addWidget(Color("red"))
    layout2.addWidget(Color("yellow"))
    layout2.addWidget(Color("purple"))

    layout1.addLayout(layout2)

    layout1.addWidget(Color("lightgreen"))

    layout3.addWidget(Color("blue"))
    layout3.addWidget(Color("magenta"))

    layout1.addLayout(layout3)

    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
