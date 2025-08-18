import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QComboBox,
  QDial,
  QDoubleSpinBox,
  QLabel,
  QLineEdit,
  QListWidget,
  QMainWindow,
  QSlider,
  QSpinBox
)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Приложение 19")

    label = QLabel("Я Метка")
    label.setText("Да, я Метка")

    font = label.font()
    font.setPointSize(30)
    label.setFont(font)
    label.setAlignment(
      Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
    )

    self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
