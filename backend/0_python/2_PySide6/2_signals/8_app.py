from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setup_ui()
    self.count = 0
    
    self.light_theme = True
    self.basic_font_size = "font-size: 24px;"
    self.basic_elements_border = "border: 1px solid #8C6BB1;"
    self.setStyleSheet(f"{self.basic_font_size} {self.basic_elements_border}")
    self.dark_color = f"background-color: #1E1E2E; color: #F5E0DC; border: 1px solid #FAB387; {self.basic_font_size}"
    self.light_color = f"background-color: #C6D0F5; color: #1E1E2E; border: 1px solid #8C6BB1; {self.basic_font_size}"

  def mousePressEvent(self, event):
    self.setStyleSheet(self.dark_color if self.light_theme else self.light_color)
    self.light_theme = not(self.light_theme)
    print(f"Активирована {'светлая' if self.light_theme else 'тёмная'} тема")

  def setup_ui(self):
    self.setWindowTitle("Восьмое приложение")
    self.setFixedSize(300, 400)
    
    self.create_btn_for_add()
    self.create_btn_for_clear()
    self.create_label()
    self.setup_layer()
    self.setup_container()
    self.setCentralWidget(self.container)

  def setup_container(self):
    self.container = QWidget()
    self.container.setLayout(self.layer)  
  
  def setup_layer(self):
    self.layer = QVBoxLayout()
    self.layer.addWidget(self.btn_add)
    self.layer.addWidget(self.btn_clear)
    self.layer.addWidget(self.label)

  def create_btn_for_add(self):
    self.btn_add = QPushButton("Увеличить")
    self.btn_add.clicked.connect(self.up_counter)
  
  def create_btn_for_clear(self):
    self.btn_clear = QPushButton("Сбросить")
    self.btn_clear.clicked.connect(self.clear_label_text)

  def create_label(self):
    self.label = QLabel("Ожидаю нажатия...")

  def up_counter(self):
    self.count += 1
    print(f"Счётчик увеличен на 1 и сейчас он равен {self.count}")
    self.change_label_text()

  def change_label_text(self):
    self.label.setText(f'Нажато {self.count} раз')
    if self.count >= 5:
      self.btn_add.setEnabled(False)
      print("Кнопка увеличения заблокирована")

  def clear_label_text(self):
    self.count = 0
    self.label.setText("Ожидаю нажатия...")
    self.btn_add.setEnabled(True)
    print("Счётчик обнулён")

app = QApplication()
window = MainWindow()
window.show()
app.exec()
