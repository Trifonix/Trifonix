import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
  QApplication,
  QMainWindow,
  QTabWidget
)
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 34")

    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.West)
    tabs.setMovable(True)

    for color in ["coral", "aqua", "lightblue", "brown"]:
      tabs.addTab(Color(color), color)
    
    self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
