import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class AnotherWindow(QWidget):
    pass

class MainWindow(QMainWindow):
    pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
