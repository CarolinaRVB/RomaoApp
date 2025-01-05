import os
from PyQt6.QtGui import QPixmap, QFont, QColor
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QSize
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLineEdit, QGridLayout, QLabel, QListWidget, QListWidgetItem, QPushButton,
                              QScrollArea, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy)

class ImageLoader(QThread):
    images_loaded = pyqtSignal(list, list)

    def __init__(self, folder):
        super().__init__()
        self.folder = folder

    def run(self):
        images = []
        folders = []
        for entry in os.listdir(self.folder):
            path = os.path.join(self.folder, entry)
            if os.path.isdir(path):
                folders.append(entry)
            elif entry.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                images.append(entry)
        self.images_loaded.emit(images, folders)


class ImageBankDialog(QDialog):
    def __init__(self, image_folder, parent=None):
        super(ImageBankDialog, self).__init__(parent)
        self.image_folder = image_folder
        self.selected_image_path = None
        self.history = []

        # Window Setup
        self.setWindowTitle("Select an Image")
        self.setStyleSheet("background-color: #fafafa;")
        self.resize(900, 700)

        # Main Layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(15)

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search images...")
        self.search_bar.setStyleSheet("padding: 10px; border: 1px solid #ccc; border-radius: 5px;")
        self.search_bar.textChanged.connect(self.filter_images)
        self.layout.addWidget(self.search_bar)

        # Folder and Image Container
        self.container_layout = QHBoxLayout()
        self.layout.addLayout(self.container_layout)

        # Folder List (Sidebar)
        self.folder_list = QListWidget(self)
        self.folder_list.setFixedWidth(200)
        self.folder_list.setStyleSheet("padding: 10px; border: 1px solid #ccc; border-radius: 5px;")
        self.folder_list.itemClicked.connect(self.open_folder)
        self.container_layout.addWidget(self.folder_list)

        # Scroll Area for Images
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none;")

        # Container for Image Grid
        self.image_container = QWidget()
        self.image_grid = QGridLayout(self.image_container)
        self.image_grid.setSpacing(5)  # Reduced space between images
        self.image_grid.setContentsMargins(5, 5, 5, 5)  # Reduced margins
        self.scroll_area.setWidget(self.image_container)
        self.container_layout.addWidget(self.scroll_area)

        # Back Button
        self.navigation_layout = QHBoxLayout()
        self.back_button = QPushButton("Back", self)
        self.back_button.setFixedWidth(100)
        self.back_button.setStyleSheet("padding: 10px; border-radius: 5px; background-color: #f0ad4e; color: white;")
        self.back_button.clicked.connect(self.go_back)
        self.back_button.setEnabled(False)
        self.navigation_layout.addWidget(self.back_button)

        # Spacer to center the button
        self.navigation_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.layout.addLayout(self.navigation_layout)

        # Load initial images and folders
        self.load_images(self.image_folder)
    def load_images(self, folder):
        self.loader = ImageLoader(folder)
        self.loader.images_loaded.connect(self.on_images_loaded)
        self.loader.start()

    def on_images_loaded(self, images, folders):
        self.images = images
        self.folders = folders
        self.display_images(self.images)
        self.display_folders()  # Always display root folders in sidebar

    def display_images(self, images):
        # Clear the previous grid layout
        for i in reversed(range(self.image_grid.count())):
            widget = self.image_grid.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Display the images in a grid
        for index, image_name in enumerate(images):
            image_path = os.path.join(self.image_folder, image_name)
            pixmap = QPixmap(image_path).scaled(120, 120, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            label = QLabel(self)
            label.setPixmap(pixmap)
            label.setStyleSheet("border: 1px solid #ccc; border-radius: 5px;")  # Add border and radius
            label.mousePressEvent = self.get_image_click_handler(image_path)
            row = index // 5  # Display 5 images per row
            col = index % 5
            self.image_grid.addWidget(label, row, col)

    def display_folders(self):
        self.folder_list.clear()
        self.folder_list.setSpacing(2)

        for folder_name in self.folders:
            item = QListWidgetItem(folder_name)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center-align text
            item.setSizeHint(QSize(150, 40))  # Adjust width and height of each item

            # Apply styles to the folder item
            # item.setFont(QFont("Arial", 10, QFont.)  # Example font styling
            item.setForeground(QColor("#4a4a4a"))  # Text color
            item.setBackground(QColor("#eaeaea"))  # Background color for each folder item

            # Add styled item to the folder list
            self.folder_list.addItem(item)

    def open_folder(self, item):
        folder_name = item.text()
        new_folder = os.path.join(self.image_folder, folder_name)

        self.history.append(self.image_folder)
        self.image_folder = new_folder
        self.back_button.setEnabled(True)
        self.load_images(new_folder)

    def go_back(self):
        if self.history:
            self.image_folder = self.history.pop()
            self.load_images(self.image_folder)
            self.back_button.setEnabled(len(self.history) > 0)

    def filter_images(self, text):
        filtered_images = [img for img in self.images if text.lower() in img.lower()]
        self.display_images(filtered_images)

    def get_image_click_handler(self, image_path):
        def handler(event):
            self.selected_image_path = image_path
            self.accept()

        return handler
