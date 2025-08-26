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
    """
    Это "окно" - это виджет. Если он без родителя,
    он будет появляться, как свободно-плавающее окно,
    как мы и хотим.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Иное Окно")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Кликни для Окна")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
        self.w = None

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
