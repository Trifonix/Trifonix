from PySide6.QtWidgets import (
  QApplication,
  QMainWindow,
  QLabel,
  QToolBar,
  QCheckBox,
  QStatusBar,
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Приложение 36")

    label = QLabel("Привет!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)

    toolbar = QToolBar("Мой главный тулбар")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)

    btn_action = QAction(QIcon("materials//6_python//2_PySide6//5_menus//bug.png"), "&Ваша кнопка", self)
    btn_action.setStatusTip("Это Ваша кнопка")
    btn_action.triggered.connect(self.tb_btn_clicked)
    btn_action.setCheckable(True)
    toolbar.addAction(btn_action)

    toolbar.addSeparator()

    btn_action2 = QAction(QIcon("materials//6_python//2_PySide6//5_menus//bug.png"), "Ваша &кнопка 2", self)
    btn_action2.setStatusTip("Это Ваша кнопка 2")
    btn_action2.triggered.connect(self.tb_btn_clicked)
    btn_action2.setCheckable(True)
    toolbar.addAction(btn_action2)

    toolbar.addWidget(QLabel("Чекбокс"))
    toolbar.addSeparator()
    toolbar.addWidget(QCheckBox())

    self.setStatusBar(QStatusBar(self))

    menu = self.menuBar()

    file_menu = menu.addMenu("&File")
    file_menu.addAction(btn_action)
    file_menu.addSeparator()

    file_submenu = file_menu.addMenu("Подменю")
    file_submenu.addAction(btn_action2)

  def tb_btn_clicked(self, s):
    print("Нажали", s)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
