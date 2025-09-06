from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 32")

    layout = QStackedLayout()

    layout.addWidget(Color("darkred"))
    layout.addWidget(Color("lightgreen"))
    layout.addWidget(Color("lightblue"))
    layout.addWidget(Color("yellow"))

    layout.setCurrentIndex(3)

    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
