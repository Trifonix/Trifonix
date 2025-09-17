from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 23")

    self.lineedit = QLineEdit()
    self.lineedit.setMaxLength(10)
    self.lineedit.setPlaceholderText("Введите текст")

    self.lineedit.returnPressed.connect(self.return_pressed)
    self.lineedit.selectionChanged.connect(self.selection_changed)
    self.lineedit.textChanged.connect(self.text_changed)
    self.lineedit.textEdited.connect(self.text_edited)

    self.setCentralWidget(self.lineedit)
  
  def return_pressed(self):
    print("Нажали Энтер!")
    self.lineedit.setText("БУМ!")
  
  def selection_changed(self):
    print("Поменяли выбор")
    print(self.lineedit.selectedText())
  
  def text_changed(self, text):
    print("Изменили текст...")
    print(text)
  
  def text_edited(self, text):
    print("Отредактировали текст...")
    print(text)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
