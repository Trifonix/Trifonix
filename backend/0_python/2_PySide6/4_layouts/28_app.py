from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Приложение 28")

    layout = QVBoxLayout()
    layout.addWidget(Color("lightblue"))
    layout.addWidget(Color("blue"))
    layout.addWidget(Color("darkblue"))
    layout.addWidget(Color("aqua"))

    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)
  
app = QApplication([])

window = MainWindow()
window.show()

app.exec()
