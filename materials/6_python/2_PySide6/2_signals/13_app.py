import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.label = QLabel("Click in this window")
    self.setCentralWidget(self.label)

  def mouseMoveEvent(self, e):
    self.label.setText("Событие мышь двигается")
  
  def mousePressEvent(self, e):
    self.label.setText("Событие мышкой нажимают")
  
  def mouseReleaseEvent(self, e):
    self.label.setText("Событие мышку отпустили")
  
  def mouseDoubleClickEvent(self, e):
    self.label.setText("Событие двойного щелчка мышкой")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
