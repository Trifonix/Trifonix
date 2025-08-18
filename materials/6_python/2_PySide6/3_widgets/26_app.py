from PySide6.QtWidgets import QApplication, QMainWindow, QDial

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 26")

    dial = QDial()
    dial.setRange(-10, 100)
    dial.setSingleStep(1)

    dial.valueChanged.connect(self.value_changed)
    dial.sliderMoved.connect(self.dial_position)
    dial.sliderPressed.connect(self.dial_pressed)
    dial.sliderReleased.connect(self.dial_released)

    self.setCentralWidget(dial)
  
  def value_changed(self, value):
    print(value)
  
  def dial_position(self, position):
    print("Позиция", position)

  def dial_pressed(self):
    print("Нажали!")
  
  def dial_released(self):
    print("Отпустили!")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
