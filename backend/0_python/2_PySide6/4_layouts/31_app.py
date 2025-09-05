from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
  
    self.setWindowTitle("Приложение 31")
    
    layout = QGridLayout()
    layout.addWidget(Color("red"), 0, 0)
    layout.addWidget(Color("blue"), 1, 0)
    layout.addWidget(Color("green"), 1, 1)
    layout.addWidget(Color("coral"), 2, 1)

    widget = QWidget()
    widget.setLayout(layout)

    self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
