from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

def my_print():
  print("Hello WOrld!")

app = QApplication([])

window = QMainWindow()
window.resize(400,400)

btn = QPushButton("НАЖМИ МЕНЯ")
btn.clicked.connect(my_print)

window.setCentralWidget(btn)
window.show()

app.exec()
