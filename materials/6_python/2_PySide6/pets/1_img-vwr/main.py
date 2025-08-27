import sys
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QPushButton, 
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QFileDialog
)
from PySide6.QtGui import QPixmap, QTransform
from PySide6.QtCore import Qt
from ImageManager import ImageManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Просмотрщик картинок")
        self.setGeometry(100, 100, 800, 600)
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        self.next_button = QPushButton("Следующая")
        self.prev_button = QPushButton("Предыдущая")
        
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.prev_button)
        buttons_layout.addWidget(self.next_button)
        
        layout.addLayout(buttons_layout)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        self.next_button.clicked.connect(self.show_next_image)
        self.prev_button.clicked.connect(self.show_prev_image)
        
    def show_image(self, path):
        pixmap = QPixmap(path)
        self.image_label.setPixmap(
            pixmap.scaled(
                self.image_label.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
        )

    def show_next_image(self):
        print("Следующая картинка")
    
    def show_prev_image(self):
        print("Предыдущая картинка")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
