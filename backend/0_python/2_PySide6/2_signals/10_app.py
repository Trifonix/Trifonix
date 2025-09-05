from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtWidgets import QPushButton, QLabel, QCheckBox, QSlider
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.counter = 0
    self.init_ui()
  
  def init_ui(self):
    self.setFixedSize(420, 240)
    self.setWindowTitle("Десятое приложение")
    self.current_theme = "background-color: lightgreen;"
    self.current_font_size = "font-size: 14px;"
    self.setStyleSheet(f"{self.current_theme} {self.current_font_size}")

    self.theme_switcher = QCheckBox()
    self.theme_switcher.setCheckState(Qt.CheckState.Checked)
    self.theme_switcher.stateChanged.connect(self.set_theme)

    self.btn_add = QPushButton("Удвоить")
    self.btn_add.clicked.connect(self.counter_rise)
    self.btn_add.clicked.connect(lambda: self.label_operation.setText(f"Тут лямбда: {self.counter}"))

    self.label_counter = QLabel("Статистика")

    self.label_operation = QLabel("Операции")
    self.label_operation.setStyleSheet("background-color: #FFB6C1;")

    self.btn_clear = QPushButton("Сбросить")
    self.btn_clear.clicked.connect(lambda some_arg: self.counter_clear(some_arg))

    self.slider = QSlider(Qt.Orientation.Horizontal)
    self.slider.setRange(14, 22)
    self.slider.setSingleStep(2)
    self.slider.valueChanged.connect(self.value_changed)

    self.main_layout = QVBoxLayout()
    self.main_layout.addWidget(self.theme_switcher)
    self.main_layout.addWidget(self.btn_add)
    self.main_layout.addWidget(self.label_counter)
    self.main_layout.addWidget(self.btn_clear)
    self.main_layout.addWidget(self.label_operation)
    self.main_layout.addWidget(self.slider)
    
    self.main_widget = QWidget()
    self.main_widget.setLayout(self.main_layout)
    
    self.setCentralWidget(self.main_widget)

  def value_changed(self, value):
    self.current_font_size = (f"font-size: {value}px;")
    self.label_operation.setText(f"Размер шрифта: {value}")
    self.switch_theme()
  
  def set_theme(self, state):
    if state:
      self.current_theme = "background-color: lightgreen;"
    else:
      self.current_theme = "background-color: lightblue;"
    self.switch_theme()

  def switch_theme(self):
    self.setStyleSheet(f"{self.current_theme} {self.current_font_size}")

  def counter_rise(self):
    self.counter += 1
    if self.counter >= 10:
      self.btn_add.setEnabled(False)
    self.label_counter.setText(f"Население города: {self.counter}")
  
  def counter_clear(self, some_arg):
    self.counter = 0
    self.btn_add.setEnabled(True)
    self.label_operation.setText(f"Население обнулено и {some_arg}, теперь оно = {self.counter}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
