from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

count = 0

def my_print(checked):
  global count
  count += 1
  print("Hello World!!!", checked, count)

app = QApplication()

window = QMainWindow()
window.setWindowTitle("Good test app")
window.setFixedSize(400, 200)

btn = QPushButton("Hit me!")
btn.setCheckable(True)
btn.clicked.connect(my_print)

window.setCentralWidget(btn)
window.show()

app.exec()
