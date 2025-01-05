from PyQt6.QtCore import Qt
from page_manager import PageManager
from main_window import Ui_MainWindow
from widgets_names import WidgetsNames
from PyQt6.QtWidgets import QMainWindow
from database import (save_plan_data, load_plan_data, show_user_ids, insert_new_id, new_plan_from_copy,
                      erase_app_entries, delete_plan)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.page_type = 0
        self.setWindowFlags(Qt.WindowType.Window)
        self.resize(1200, 849)  # Set desired initial size
        self.setMinimumSize(400, 300)

        self.current_user_id = None
        self.user_label = self.ui.current_id
        self.showMaximized()

        # Set variables
        self.top_bar_layout = self.ui.horizontalLayout_34
        self.page_buttons_list = []
        widgets_list = WidgetsNames().get_widgets_general()
        # Hide Sidebar
        self.ui.sidebar_expanded.hide()

        self.page_manager = PageManager(self)

        # Sidebar actions
        self.ui.push_ext_save.clicked.connect(lambda: save_plan_data(self, self.ui, WidgetsNames().get_widgets_general()))
        self.ui.push_ext_load.clicked.connect(lambda: load_plan_data(self, self.ui, WidgetsNames().get_widgets_general()))
        self.ui.push_ext_all.clicked.connect(lambda: show_user_ids(self))
        self.ui.push_ext_newplan.clicked.connect(lambda: insert_new_id(self, self.ui, WidgetsNames().get_widgets_general()))
        self.ui.push_ext_new_copy.clicked.connect(lambda: new_plan_from_copy(self, self.ui))
        self.ui.push_ext_erase.clicked.connect(lambda: erase_app_entries(self, self.ui, widgets_list, self.current_user_id))
        self.ui.push_ext_delete.clicked.connect(lambda: delete_plan(self, self.ui))

        # Pages actions
        self.ui.page_home.clicked.connect(lambda: self.page_manager.switch_to_page(self.ui.stacked_home))
        self.ui.page_general.clicked.connect(lambda: self.page_manager.switch_to_page(self.ui.stacked_general))
        self.ui.page_add.clicked.connect(self.page_manager.add_new_page)
        self.ui.page_add_where.clicked.connect(lambda: self.page_manager.add_new_page(True))


