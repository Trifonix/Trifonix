from PySide6.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 22")

    listwidget = QListWidget()
    listwidget.addItems(["Первый", "Второй", "Третий"])

    listwidget.currentItemChanged.connect(self.index_changed)
    listwidget.currentTextChanged.connect(self.text_changed)
    
    self.setCentralWidget(listwidget)
  
  def index_changed(self, index):
    print(index.text())
  
  def text_changed(self, text):
    print(text)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
