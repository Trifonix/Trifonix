from PySide6.QtWidgets import QApplication, QMainWindow, QSlider

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 25")

    slider = QSlider()

    slider.setMinimum(-10)
    slider.setMaximum(5)

    slider.setSingleStep(3)
    slider.valueChanged.connect(self.value_changed)
    slider.sliderMoved.connect(self.slider_position)
    slider.sliderPressed.connect(self.slider_pressed)
    slider.sliderReleased.connect(self.slider_released)

    self.setCentralWidget(slider)
  
  def value_changed(self, value):
    print(value)
  
  def slider_position(self, position):
    print("Позиция", position)
  
  def slider_pressed(self):
    print("Нажали!")
  
  def slider_released(self):
    print("Отпустили")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
