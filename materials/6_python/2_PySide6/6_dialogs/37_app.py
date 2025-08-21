import sys

from PySide6.QtWidgets import (
  QApplication, 
  QMainWindow, 
  QPushButton, 
  QDialog,
  QDialogButtonBox,
  QVBoxLayout,
  QLabel
)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 37")

    button = QPushButton("Нажми меня для диалога!")
    button.clicked.connect(self.button_clicked)
    self.setCentralWidget(button)

  def button_clicked(self, s):
    print("Клац!", s)

    dlg = CustomDialog()
    if dlg.exec():
      print("Принято!")
    else:
      print("Отмена!")

class CustomDialog(QDialog):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Привет!")

    QBtn = (
      QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    )

    self.buttonBox = QDialogButtonBox(QBtn)
    self.buttonBox.accepted.connect(self.accept)
    self.buttonBox.rejected.connect(self.reject)

    layout = QVBoxLayout()
    message = QLabel("Что-то произошло, это ОК?")
    layout.addWidget(message)
    layout.addWidget(self.buttonBox)
    self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
