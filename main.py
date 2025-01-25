from PyQt6.QtWidgets import QApplication
#from app_window import MainWindow
from srcs.window_handler.app_window import MainWindow
#from srcs.window_handler.app_window import MainWindow
from srcs.images_handlers.image_folder_watcher import (start_folder_watcher, stop_folder_watcher)
from srcs.database.database import init_db
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