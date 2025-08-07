from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.count = 0

    self.setWindowTitle("Приложение 6")
    self.setFixedSize(260, 140)

    self.btn = QPushButton("Клацни!")
    self.btn.clicked.connect(self.press_btn)
    self.label = QLabel("I'm Label")
    self.label.setAlignment(Qt.AlignCenter)
    
    self.layout = QVBoxLayout()
    self.layout.addWidget(self.btn)
    self.layout.addWidget(self.label)

    self.container = QWidget()
    self.container.setLayout(self.layout)

    self.setCentralWidget(self.container)

  def press_btn(self):
    if (self.count < 5):
      self.count += 1
      self.label.setText(f"Нажали раз: {self.count}")
    else:
      self.btn.setEnabled(False)
      self.btn.setText("Хватит это терпеть!")
      self.label.setText("Хватит клацать!!! 👀")

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
