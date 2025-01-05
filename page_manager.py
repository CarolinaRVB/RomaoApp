import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from image_bank_dialog import ImageBankDialog
from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QTabWidget, QCheckBox, QStackedWidget, QFrame, QPushButton, QHBoxLayout
from main_window import Ui_MainWindow
from page1 import Ui_Form as page1
from page2 import Ui_Form as page2
from page3 import Ui_Form as page3

from popup_dialogs import choose_page_popup, popup_load_plan_dialog, popup_warning, popup_insert_page_dialog
from database import (save_plan_data, load_plan_data, show_user_ids, insert_new_id, new_plan_from_copy,
                      delete_page_from_plan, update_pages_list, erase_app_entries, delete_plan, stop_auto_save,
                      start_auto_save)
from widgets_names import WidgetsNames

class PageManager():
    def __init__(self, main_window):
        self.ui = main_window.ui
        self.top_bar_layout = main_window.top_bar_layout
        self.main_window = main_window
        self.page_type = 0

    def add_new_page(self, insert=False):
        self.page_type = choose_page_popup()
        if self.page_type == 0:
            return
        if insert:
            result = popup_insert_page_dialog(self.main_window, "New Page", "Enter Page name:", "After:")
        else:
            result = popup_load_plan_dialog(self.main_window, "New Page", "Enter Page name:")
        if not result:
            return
        self.page_name, self.position = self.handle_result(result, insert)
        if self.page_name == None:
            return

        for i in range(self.top_bar_layout.count() - 3):
            button = self.top_bar_layout.itemAt(i).widget()
            if (button and isinstance(button, QPushButton) and button.text() == self.page_name):
                popup_warning(self.main_window, None, f"Error: Page with '{self.page_name}' already exists.")
                return

        new_page = QWidget()
        if self.page_type == 1:
            ui = page1()
        elif self.page_type == 2:
            ui = page2()
        else:
            ui = page3()
        ui.setupUi(new_page)

        self.create_new_page(new_page, insert)
        update_pages_list(self.main_window)
        self.handle_page_widgets(ui)
        self.main_window.ui.stackedWidget.setCurrentWidget(new_page)

    def handle_result(self, result, insert):
        if not insert:
            return result, None

        page_name, position = result
        if position == "HOME":
            popup_warning(self.main_window, None, f"Error: Can't add page after '{position}'.")
            return None, None
        for i in range(self.top_bar_layout.count()):
            button = self.top_bar_layout.itemAt(i).widget()
            if (button and isinstance(button, QPushButton) and button.text() == position):
                break
        else:
            popup_warning(self.main_window, None, f"Error: Page '{position}' doesn't exist.")
            return None, None
        return page_name, position

    def create_new_page(self, new_page, insert):
        page_button = QPushButton(f"{self.page_name}", self.main_window.ui.top_bar)
        page_button_remove = QPushButton("-", self.main_window.ui.top_bar)
        self.style_new_page_button(page_button, page_button_remove)
        page_num = self.top_bar_layout.count() - 4
        stacked = 1
        if insert:
            for i in range(2, self.top_bar_layout.count() - 3):
                button = self.top_bar_layout.itemAt(i).widget()
                if (button and isinstance(button,
                                          QPushButton) and button.text() != self.position and button.text() != "-"):
                    stacked += 1
                elif (button and isinstance(button,
                                            QPushButton) and button.text() == self.position) and button.text() != "-":
                    stacked += 1
                    self.main_window.ui.stackedWidget.insertWidget(stacked, new_page)
                    if (self.position != "General"):
                        self.top_bar_layout.insertWidget(i + 2, page_button)
                        self.top_bar_layout.insertWidget(i + 3, page_button_remove)
                        break
                    else:
                        self.top_bar_layout.insertWidget(i + 1, page_button)
                        self.top_bar_layout.insertWidget(i + 2, page_button_remove)
                        break
        else:
            self.top_bar_layout.insertWidget(page_num + 1, page_button)
            self.top_bar_layout.insertWidget(page_num + 2, page_button_remove)
            max = self.main_window.ui.stackedWidget.count()
            self.main_window.ui.stackedWidget.insertWidget(max, new_page)

        page_button.clicked.connect(lambda: self.switch_to_page(new_page))
        page_button_remove.clicked.connect(
            lambda: delete_page_from_plan(self.main_window, self.ui, page_button, page_button_remove, new_page))

    def handle_page_widgets(self, ui):
        if self.page_type == 1:
            self.handle_page1_widgets(ui)
        elif self.page_type == 2:
            self.handle_page2_widgets(ui)
        elif self.page_type == 3:
            self.handle_page3_widgets(ui)

    def handle_page1_widgets(self, ui):
        self.connect_combo_box_to_text_edit(ui.comboBox, ui.textEdit)
        add_buttons = {"pushButton": "label", "pushButton_3": "label_2"}
        remove_buttons = {"pushButton_2": "label", "pushButton_4": "label_2"}
        img_labels = ["label", "label_2"]

        for button_name, label_name in add_buttons.items():
            button = getattr(ui, button_name)
            label = getattr(ui, label_name)
            button.clicked.connect(lambda _, lbl=label: self.open_image_bank(lbl))
        for btn_name, lbl_name in remove_buttons.items():
            button = getattr(ui, btn_name)
            label = getattr(ui, lbl_name)
            print(f"clicked on {lbl_name} and {label}")
            button.clicked.connect(lambda _, lbl=label: self.remove_img(lbl))

    def remove_img(self, label):
        label.clear()
        label.setToolTip('')
        label.setText("img")

    def open_image_bank(self, label, width=50, height=50, scaled=False):
        image_folder = 'romao_images'
        os.makedirs(image_folder, exist_ok=True)
        dialog = ImageBankDialog(image_folder, self.main_window)
        if dialog.exec():
            self.ui.image_path = dialog.selected_image_path
            pixmap = QPixmap(self.ui.image_path)
            # print(f"Label: {label}, image_path {self.ui.image_path}, pixmap {pixmap}")
            scaled_pixmap = pixmap.scaled(width, height, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(scaled_pixmap)
            label.setScaledContents(scaled)
            label.setToolTip(self.ui.image_path)

    def handle_page2_widgets(self, ui):
        self.connect_combo_box_to_text_edit(ui.comboBox, ui.textEdit2)

    def handle_page3_widgets(self, ui):
        self.connect_combo_box_to_text_edit(ui.comboBox, ui.textEdit3)

    def connect_combo_box_to_text_edit(self, combo_box, text_edit):
        text_edit.setText(combo_box.currentText())
        combo_box.currentIndexChanged.connect(lambda: self.update_text_edit(combo_box, text_edit))

    def update_text_edit(self, combo_box, text_edit):
        text = combo_box.currentText()
        text_edit.setText(text)

    def switch_to_page(self, page):
        page_index = self.ui.stackedWidget.indexOf(page)
        if page_index != -1:
            self.ui.stackedWidget.setCurrentIndex(page_index)

    def style_new_page_button(self, page_button, page_remove_button=None):
        page_button.setStyleSheet(
            "background-color: rgb(0, 0, 0); color: white; font: 11pt; text-align: right; padding-left: 5px;;")
        page_button.setCursor(Qt.CursorShape.PointingHandCursor)
        page_button.setMinimumSize(60, 40)
        # page_button.setMaximumSize(100, 40)
        page_button.setFlat(True)

        if page_remove_button:
            page_remove_button.setStyleSheet(
                "background-color: rgb(0, 0, 0); color: white; font: 11pt; text-align: center")
            page_remove_button.setCursor(Qt.CursorShape.PointingHandCursor)
            page_remove_button.setMinimumSize(50, 40)
            page_remove_button.setMaximumSize(50, 40)
            page_remove_button.setFlat(True)
