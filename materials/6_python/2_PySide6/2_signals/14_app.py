from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setMouseTracking(True)
    self.label = QLabel("Кликните в это окно")
    self.label.setMouseTracking(True)
    self.setCentralWidget(self.label)

  def mouseMoveEvent(self, e):
    self.label.setText("Мышкой ведут")
  
  def mousePressEvent(self, e):
    self.label.setText("Сюда кликнули")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
