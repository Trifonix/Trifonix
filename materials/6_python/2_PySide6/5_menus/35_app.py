from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QLabel,
  QMainWindow,
  QStatusBar,
  QToolBar
)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Приложение 35")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
