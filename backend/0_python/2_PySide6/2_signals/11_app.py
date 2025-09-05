import sys
from random import choice

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
  "My App",
  "My app",
  "Still My App",
  "Still my app",
  "What on Earth",
  "What on earth",
  "What is surp",
  "What is surprising",
  "Something went wrong"
]

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.n_times_clicked = 0
    self.setWindowTitle("My 11th app")
    self.setFixedWidth(400)

    self.button = QPushButton("Press Me!")
    self.button.clicked.connect(self.the_button_was_clicked)

    self.windowTitleChanged.connect(self.the_window_title_changed)

    self.setCentralWidget(self.button)
  
  def the_button_was_clicked(self):
    print("Clicked.")
    new_window_title = choice(window_titles)
    print("Setting title: %s" % new_window_title)
    self.setWindowTitle(new_window_title)
  
  def the_window_title_changed(self, window_title):
    print("Window title changed: %s" % window_title)

    if window_title == "Something went wrong":
      self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
