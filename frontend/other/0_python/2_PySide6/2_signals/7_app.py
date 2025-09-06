from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setup_ui()
  
  def setup_ui(self):
    self.setFixedSize(400, 200)
    self.setWindowTitle("Седьмое приложение")

    self.add_btn = QPushButton("Добавить счётчик")
    self.add_btn.clicked.connect(self.add_counter)

    self.list_layout = QVBoxLayout()

    self.list_container = QWidget()
    self.list_container.setLayout(self.list_layout)

    self.main_layout = QVBoxLayout()
    self.main_layout.addWidget(self.add_btn)
    self.main_layout.addWidget(self.list_container)

    self.container = QWidget()
    self.container.setLayout(self.main_layout)

    self.setCentralWidget(self.container)
  
  def add_counter(self):
    new_label = CounterLabel("Счётчик: 0")
    self.list_layout.addWidget(new_label)

class CounterLabel(QLabel):
  def __init__(self, text = ""):
    super().__init__(text)
    self.count = 0
  
  def mouseDoubleClickEvent(self, event):
    self.count += 1
    self.setText(f"Счётчик: {self.count}")
    if self.count >= 5:
      self.setStyleSheet("background-color: lightgreen;")

app = QApplication()
window = MainWindow()
window.show()
app.exec()
