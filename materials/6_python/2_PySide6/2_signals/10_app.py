from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.counter = 0
    self.dark_theme = False
    self.init_ui()
  
  def init_ui(self):
    self.setFixedSize(420, 240)
    self.setWindowTitle("Десятое приложение")

    self.btn_add = QPushButton("Удвоить")
    self.btn_add.clicked.connect(self.counter_rise)

    self.label_counter = QLabel("Статистика")

    self.btn_clear = QPushButton("Сбросить")
    self.btn_clear.clicked.connect(self.counter_clear)

    self.main_layout = QVBoxLayout()
    self.main_layout.addWidget(self.btn_add)
    self.main_layout.addWidget(self.label_counter)
    self.main_layout.addWidget(self.btn_clear)
    
    self.main_widget = QWidget()
    self.main_widget.setLayout(self.main_layout)
    
    self.setCentralWidget(self.main_widget)

  def counter_rise(self):
    self.counter += 1
    self.label_counter.setText(f"Население города: {self.counter}")
  
  def counter_clear(self):
    self.counter = 0
    self.label_counter.setText("Население обнулено")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
