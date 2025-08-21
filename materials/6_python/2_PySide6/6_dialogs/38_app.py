import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 38")

    button = QPushButton("Клацни и вызови диалог")
    button.clicked.connect(self.button_clicked)
    self.setCentralWidget(button)
  
  """
  def button_clicked(self, s):
    dlg = QMessageBox(self)
    dlg.setWindowTitle("У меня вопрос")
    dlg.setText("Это диалог с вопросом")
    dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dlg.setIcon(QMessageBox.Question)
    button = dlg.exec()

    if button == QMessageBox.Yes:
      print("ДА!")
    else:
      print("НЕТ!")
  """

  """
  def button_clicked(self, s):
    button = QMessageBox.question(
      self,
      "Диалог-вопрос",
      "Длинное сообщение"
    )
    if button == QMessageBox.Yes:
      print("АГА!")
    else:
      print("НЕА!")
  """

  def button_clicked(self, s):
    button = QMessageBox.critical(
      self,
      "О, дорогой!",
      "Что-то пошло не так.",
      buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
      defaultButton=QMessageBox.Discard
    )

    if button == QMessageBox.Discard:
      print("Отмена")
    elif button == QMessageBox.NoToAll:
      print("Всем - нет")
    else:
      print("Игнорируем")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
