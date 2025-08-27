import sys, os
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
from DatabaseManager import DatabaseManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Просмотрщик картинок")
        self.setGeometry(100, 100, 600, 600)

        self.db_manager = DatabaseManager()
        self.image_manager = ImageManager(self.db_manager)
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        self.next_button = QPushButton("Следующая")
        self.prev_button = QPushButton("Предыдущая")
        self.open_button = QPushButton("Открыть папку")
        self.to_best_button = QPushButton("В Избранное")
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.image_label)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.open_button)
        buttons_layout.addWidget(self.to_best_button)
        buttons_layout.addStretch()
        buttons_layout.addWidget(self.prev_button)
        buttons_layout.addWidget(self.next_button)
        
        main_layout.addLayout(buttons_layout)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        self.next_button.clicked.connect(self.show_next_image)
        self.prev_button.clicked.connect(self.show_prev_image)
        self.open_button.clicked.connect(self.open_directory)
        self.to_best_button.clicked.connect(self.put_to_best_images)
        
    def show_image(self, path):
        if not os.path.exists(path):
            print(f"Ошибка: Файл не найден по пути: {path}")
            return
            
        pixmap = QPixmap(path)
        self.image_label.setPixmap(
            pixmap.scaled(
                self.image_label.size(), 
                Qt.KeepAspectRatio, 
                Qt.SmoothTransformation
            )
        )
    
    def open_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку с картинками")
        if directory:
            self.image_manager.scan_directory(directory)
            current_path = self.image_manager.get_current_image()
            if current_path:
                self.show_image(current_path)

    def show_next_image(self):
        self.image_manager.next_image()
        current_path = self.image_manager.get_current_image()
        if current_path:
            self.show_image(current_path)
    
    def show_prev_image(self):
        self.image_manager.prev_image()
        current_path = self.image_manager.get_current_image()
        if current_path:
            self.show_image(current_path)
    
    def put_to_best_images(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
