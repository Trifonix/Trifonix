from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 21")

    combobox = QComboBox()
    combobox.addItems(["Один", "Два", "Три"])
    combobox.setEditable(True)

    combobox.currentIndexChanged.connect(self.index_changed)

    combobox.currentTextChanged.connect(self.text_changed)

    self.setCentralWidget(combobox)
  
  def index_changed(self, index):
    print(index)
  
  def text_changed(self, text):
    print(text)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
