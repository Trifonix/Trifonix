from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QMenu
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.count = 0
    self.light_theme = True
    self.setup_ui()
  
  def setup_ui(self):
    self.setWindowTitle("Девятое приложение")
    self.setFixedSize(300, 300)

    self.btn_add = QPushButton("Увеличить")
    self.btn_add.setCheckable(True)
    self.btn_add.clicked.connect(self.up_counter_with_args)

    self.btn_clear = QPushButton("Сбросить")
    self.btn_clear.clicked.connect(lambda: self.label.setText("Ожидаю нажатия..."))
    self.btn_clear.clicked.connect(self.reset_counter)

    self.label = QLabel("Ожидаю нажатия...")
    self.label.setAlignment(Qt.AlignCenter)

    layout = QVBoxLayout()
    layout.addWidget(self.btn_add)
    layout.addWidget(self.btn_clear)
    layout.addWidget(self.label)

    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)
  
  def up_counter_with_args(self, checked: bool):
    self.count += 1
    self.label.setText(f"Нажато: {self.count} раз, checked={checked}")
    if self.count >= 5:
      self.btn_add.setEnabled(False)
  
  def reset_counter(self):
    self.count = 0
    self.label.setText("Счётчик сброшен")
    self.btn_add.setEnabled(True)
  
  def mousePressEvent(self, event):
    if event.button() == Qt.LeftButton:
      print("Левый клик по окну")
    elif event.button() == Qt.RightButton:
      print("Правый клик по окну - показываю меню")
      self.show_context_menu(event.pos())
    elif event.button() == Qt.MiddleButton:
      print("Средний клик - сбрасываю счётчик")
      self.reset_counter()
      self.label.setText("Сброшено по клику колёсиком")
  
  def show_context_menu(self, pos):
    menu = QMenu(self)
    action_reset = QAction("Сбросить счётчик", self)
    action_reset.triggered.connect(self.reset_counter)
    menu.addAction(action_reset)

    action_quit = QAction("Выйти", self)
    action_quit.triggered.connect(self.close)
    menu.addAction(action_quit)
    
    menu.exec(self.mapToGlobal(pos))

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
