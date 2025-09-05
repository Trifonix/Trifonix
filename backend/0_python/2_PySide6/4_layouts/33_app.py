import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QPushButton,
  QStackedLayout,
  QVBoxLayout,
  QWidget
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 33")

    pagelayout = QVBoxLayout()
    button_layout = QHBoxLayout()
    self.stacklayout = QStackedLayout()

    pagelayout.addLayout(button_layout)
    pagelayout.addLayout(self.stacklayout)

    btn = QPushButton("Красный")
    btn.pressed.connect(self.activate_tab_1)
    button_layout.addWidget(btn)
    self.stacklayout.addWidget(Color("coral"))

    btn = QPushButton("Зелёный")
    btn.pressed.connect(self.activate_tab_2)
    button_layout.addWidget(btn)
    self.stacklayout.addWidget(Color("lightgreen"))

    btn = QPushButton("Голубой")
    btn.pressed.connect(self.activate_tab_3)
    button_layout.addWidget(btn)
    self.stacklayout.addWidget(Color("lightblue"))

    widget = QWidget()
    widget.setLayout(pagelayout)
    self.setCentralWidget(widget)

  def activate_tab_1(self):
    self.stacklayout.setCurrentIndex(0)

  def activate_tab_2(self):
    self.stacklayout.setCurrentIndex(1)

  def activate_tab_3(self):
    self.stacklayout.setCurrentIndex(2)  

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
