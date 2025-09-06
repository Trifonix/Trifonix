from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QLabel,
  QMainWindow,
  QStatusBar,
  QToolBar
)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Приложение 35")

    label = QLabel("Это метка")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)

    toolbar = QToolBar("Моё основное меню")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)

    button_action = QAction(
      QIcon("materials//6_python//2_PySide6//5_menus//bug.png"), 
      "Ваша кнопка", 
      self
    )
    button_action.setStatusTip("Это - Ваша кнопка")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)

    toolbar.addSeparator()

    button_action2 = QAction(QIcon("materials//6_python//2_PySide6//5_menus//bug.png"), "Ваша кнопка 2", self)
    button_action2.setStatusTip("Это - Ваша кнопка 2")
    button_action2.triggered.connect(self.toolbar_button_clicked)
    button_action2.setCheckable(True)
    toolbar.addAction(button_action2)

    toolbar.addSeparator()

    toolbar.addWidget(QLabel("Справа - чекбокс "))
    toolbar.addWidget(QCheckBox())

    self.setStatusBar(QStatusBar(self))

  def toolbar_button_clicked(self, s):
    print("Клик", s)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
