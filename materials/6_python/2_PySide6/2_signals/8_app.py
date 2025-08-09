from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setup_ui()
  
  def setup_ui(self):
    self.setWindowTitle("Восьмое приложение")
    self.setFixedSize(300, 400)
    
    self.create_btn()
    self.create_label()
    self.setup_layer()
    self.setup_container()
    self.setCentralWidget(self.container)

  def setup_container(self):
    self.container = QWidget()
    self.container.setLayout(self.layer)  
  
  def setup_layer(self):
    self.layer = QVBoxLayout()
    self.layer.addWidget(self.btn)
    self.layer.addWidget(self.label)

  def create_btn(self):
    self.btn = QPushButton("Нажми меня")

  def create_label(self):
    self.label = QLabel("Ожидаю нажатия...")

app = QApplication()
window = MainWindow()
window.show()
app.exec()
