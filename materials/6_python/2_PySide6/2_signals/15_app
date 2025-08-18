import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.label = QLabel("Клацни в это окошко")
    self.setCentralWidget(self.label)
  
  def mousePressEvent(self, e):
    if e.button() == Qt.MouseButton.LeftButton:
      self.label.setText("Была нажата ЛЕВАЯ кнопка мыши")
    
    elif e.button() == Qt.MouseButton.MiddleButton:
      self.label.setText("Была нажата СРЕДНЯЯ кнопка мыши")

    elif e.button() == Qt.MouseButton.RightButton:
      self.label.setText("Была нажата ПРАВАЯ нопка мыши")

  def mouseReleaseEvent(self, e):
    if e.button() == Qt.MouseButton.LeftButton:
      self.label.setText("Отпустили ЛЕВУЮ кнопку мышки")
    
    elif e.button() == Qt.MouseButton.MiddleButton:
      self.label.setText("Отпустили СРЕДНЮЮ кнопку мышки")
    
    elif e.button() == Qt.MouseButton.RightButton:
      self.label.setText("Отпустили ПРАВУЮ кнопку мышки")
  
  def mouseDoubleClickEvent(self, e):
    if e.button() == Qt.MouseButton.LeftButton:
      self.label.setText("Двойной щелчок ЛЕВОЙ кнопкой мыши")
    
    elif e.button() == Qt.MouseButton.MiddleButton:
      self.label.setText("Двойной щелчок СРЕДНЕЙ кнопкой мыши")
    
    elif e.button() == Qt.MouseButton.RightButton:
      self.label.setText("Двойной щелчок ПРАВОЙ кнопкой мыши")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
