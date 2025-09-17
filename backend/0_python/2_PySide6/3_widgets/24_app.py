from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 24")

    spinbox = QSpinBox()

    spinbox.setMinimum(-10)
    spinbox.setMaximum(3)

    spinbox.setPrefix("$")
    spinbox.setSuffix("c")
    spinbox.setSingleStep(3)
    spinbox.valueChanged.connect(self.value_changed)
    spinbox.textChanged.connect(self.value_changed_str)

    self.setCentralWidget(spinbox)
  
  def value_changed(self, value):
    print(value)
  
  def value_changed_str(self, str_value):
    print(str_value)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
