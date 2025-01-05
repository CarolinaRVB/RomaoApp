from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication
from main_window import Ui_MainWindow
from app_window import MainWindow
from image_folder_watcher import (start_folder_watcher, stop_folder_watcher)
from database import init_db
import os
import sys

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    os.makedirs('romao_images', exist_ok=True)
    db_folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    os.makedirs(db_folder, exist_ok=True)
    db_path = os.path.join(db_folder, 'database.db')
    # start database
    init_db()
    observer = start_folder_watcher('romao_images')
    try:
        main()
    except KeyboardInterrupt:
        stop_folder_watcher(observer)
        exit(0)