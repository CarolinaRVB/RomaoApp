import os
import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap
from page1 import Ui_Form as page1
from page2 import Ui_Form as page2
from page3 import Ui_Form as page3
from PyQt6.QtCore import QTimer, Qt
from widgets_names import WidgetsNames
from PyQt6.QtWidgets import QPushButton, QHBoxLayout
from popup_dialogs import popup_load_plan_dialog, UserDialog, popup_warning, PlanSelectionDialog

timer = None
is_saving = False

def init_image_tracker_database(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='images_paths';")
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE images_paths (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path TEXT
            )
        ''')

def init_main_database(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='User';")
    if cursor.fetchone() is None:
        columns = ",\n".join(f"{name} TEXT" for name in WidgetsNames().get_widgets_general() if name != "username")
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS User (
            userID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            {columns}
        );
        """)

def init_simple_pages_database(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='SimplePages';")
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SimplePages (
                username TEXT,
                pagePosition INTEGER,
                pageName TEXT,
                comboBox INTEGER,
                img TEXT,
                textEdit TEXT,
                PRIMARY KEY (username, pageName)
            );
        ''')

def init_complex_pages_database(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ComplexPages';")
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ComplexPages (
                username TEXT,
                pagePosition INTEGER,
                pageName TEXT,
                comboBox INTEGER,
                textEdit2 TEXT,
                PRIMARY KEY (username, pageName)
            );
        ''')

def init_mid_pages_database(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='MidPages';")
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MidPages (
                username TEXT,
                pagePosition INTEGER,
                pageName TEXT,
                comboBox INTEGER,
                textEdit3 TEXT,
                PRIMARY KEY (username, pageName)
            );
        ''')

def init_db():
    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Start Tables in database
    init_image_tracker_database(cursor)
    init_main_database(cursor)
    init_simple_pages_database(cursor)
    init_complex_pages_database(cursor)
    init_mid_pages_database(cursor)

    conn.commit()
    conn.close()

def fetch_form_data(user_id, table):
    cursor, conn = get_cursor()
    cursor.execute(f'SELECT * FROM {table} WHERE username = ?', (user_id,))
    columns = [description[0] for description in cursor.description]
    data = cursor.fetchone()
    conn.close()
    return dict(zip(columns, data)) if data else None

def load_plan_data(parent, ui, widgets_list):
    if parent.current_user_id:
        confirm = QtWidgets.QMessageBox.question(
            parent, "Warning: Plan opened",
            f"Please Confirm loading of another plan ?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if confirm == QtWidgets.QMessageBox.StandardButton.No:
            return

    # add option to confirm the loading of a new plan if there's one on the app
    user_input = popup_load_plan_dialog(parent, "Load Plan", "Plan ID: ")
    if user_input:
        data = fetch_form_data(user_input, "User")
        if data:
            stop_auto_save(parent)
            remove_all_pages(parent)
            # current_user_id = user_input
            parent.current_user_id = user_input
            parent.user_label.setText(user_input)
            for name, value in data.items():
                element = getattr(ui, name, None)
                if value and isinstance(element, QtWidgets.QLineEdit):
                    element.setText(value if value is not None else "")
                elif value and isinstance(element, QtWidgets.QPlainTextEdit):
                    element.setPlainText(value if value is not None else "")
            #     elif value and isinstance(element, QtWidgets.QLabel):
            #         set_image(element, value)
            #     elif value and isinstance(element, QtWidgets.QComboBox):
            #         set_all_pages_visible(parent, name, element, value, True)
            #     elif value and isinstance(element, QtWidgets.QCheckBox):
            #         handle_tabs(value, element)

            load_all_pages(parent, user_input)
            start_auto_save(parent, ui, widgets_list)

        else:
            QtWidgets.QMessageBox.warning(parent, "Error", "No data found for the given plan ID.")


def update_pages_list(parent):
    parent.page_buttons_list = []
    for i in range(3, parent.top_bar_layout.count() - 3):
        button = parent.top_bar_layout.itemAt(i).widget()
        if (button and isinstance(button, QPushButton) and button.text() != "-"):
            parent.page_buttons_list.append(button.text())

def delete_page_from_plan(parent, ui, page_button, page_button_remove, page_name):

    confirm = QtWidgets.QMessageBox.question(
        parent, "Warning: Page Removal",
        f"Please Confirm deletion of page: {page_button.text()}?",
        QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
    )
    if confirm == QtWidgets.QMessageBox.StandardButton.No:
        return

    if parent.current_user_id:
        page_type_line = page_name.findChild(QtWidgets.QLineEdit, "type")
        page_type = int(page_type_line.text())
        table_map = {
            1: "SimplePages",
            2: "ComplexPages",
            3: "MidPages"
        }
        table_name = table_map.get(page_type)

        folder = os.path.join(os.path.expanduser("~"), 'romao_database')
        db_path = os.path.join(folder, 'database.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Delete the page record from the database
        cursor.execute(f"""
            DELETE FROM {table_name}
            WHERE username = ? AND pageName = ?;
        """, (parent.current_user_id, page_button.text(), ))
        conn.commit()
        conn.close()

    parent.top_bar_layout.removeWidget(page_button)
    parent.top_bar_layout.removeWidget(page_button_remove)
    page_button.deleteLater()
    page_button_remove.deleteLater()
    parent.ui.stackedWidget.removeWidget(page_name)

    update_pages_list(parent)


def delete_plan(parent, ui):
    confirm = QtWidgets.QMessageBox.question(
        parent, "Warning: Plan Removal",
        f"Please Confirm plan deletion ?",
        QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
    )
    if confirm == QtWidgets.QMessageBox.StandardButton.No:
        return

    plan_id = popup_load_plan_dialog(parent, "Plan Removal", "Please indicate plan ID:")
    if not plan_id:
        return

    if plan_id == parent.current_user_id:
        erase_app_entries(parent, ui, WidgetsNames().get_widgets_general(), plan_id, True)
        parent.current_user_id = None
        parent.user_label.setText("Current Plan ID")

    tables = ["User", "SimplePages", "ComplexPages", "MidPages"]
    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for table in tables:
        cursor.execute(f"""
                        DELETE FROM {table}
                        WHERE username = ?;
                    """, (plan_id, ))
    conn.commit()
    conn.close()


def erase_app_entries(parent, ui, widgets_list, user=None, flag=False):
    if not flag:
        confirm = QtWidgets.QMessageBox.question(
            parent, "Warning: Erasing entries",
            f"Please Confirm entries deletion ?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if confirm == QtWidgets.QMessageBox.StandardButton.No:
            return
    stop_auto_save(parent)
    remove_all_pages(parent, user)
    update_pages_list(parent)
    for name in widgets_list:
        if name != "username":
            element = getattr(ui, name, None)
            if isinstance(element, QtWidgets.QLineEdit):
                element.setText("")
            elif isinstance(element, QtWidgets.QPlainTextEdit):
                element.setPlainText("")
            elif isinstance(element, QtWidgets.QLabel):
                element.setText("img")
            elif isinstance(element, QtWidgets.QComboBox):
                element.setCurrentIndex(0)
    if not flag:
        start_auto_save(parent)

def remove_all_pages(parent, user=None):
    for page_index in range(parent.ui.stackedWidget.count() - 1, 1, -1):  # Reverse loop
        page = parent.ui.stackedWidget.widget(page_index)
        if page:
            parent.ui.stackedWidget.removeWidget(page)
            page.deleteLater()  # Ensure the page is deleted

    for i in reversed(range(3, parent.top_bar_layout.count() - 3)):
        item = parent.top_bar_layout.itemAt(i)
        widget = item.widget()
        if widget and isinstance(widget, QtWidgets.QPushButton):
            parent.top_bar_layout.removeWidget(widget)
            widget.deleteLater()

    parent.ui.stackedWidget.setCurrentIndex(0)

    if user:
        parent.page_buttons_list = []
        tables = ["SimplePages", "ComplexPages", "MidPages"]
        folder = os.path.join(os.path.expanduser("~"), 'romao_database')
        db_path = os.path.join(folder, 'database.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        for table in tables:
            cursor.execute(f"""
                            DELETE FROM {table}
                            WHERE username = ?;
                        """, (user,))
        conn.commit()
        conn.close()


def load_all_pages(parent, user_input):
    page_handlers = {
        1: handle_simple_page,
        2: handle_complex_page,
        3: handle_mid_page,
    }

    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    all_pages = []
    for page_type in page_handlers.keys():
        table_name = get_table_name(page_type)
        cursor.execute(f"SELECT * FROM {table_name} WHERE username = ?", (user_input,))
        pages = cursor.fetchall()

        # Add page type to the data for later processing
        for page in pages:
            all_pages.append((page_type, page))
    conn.commit()
    conn.close()

    # Sort all pages by their page_position
    all_pages.sort(key=lambda x: x[1][1])
    # Add pages in the sorted order
    parent.page_buttons_list = []
    for page_type, page_data in all_pages:
        handler = page_handlers[page_type]
        handler(parent, page_data)

def get_table_name(page_type):
    table_names = {
        1: "SimplePages",
        2: "ComplexPages",
        3: "MidPages",
    }
    return table_names.get(page_type)

def set_image(label, image_path):
    width = 50
    height = 50
    if image_path:
        label.setToolTip(image_path)
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            if label.objectName() == "profile":
                label.setScaledContents(True)
                width = 150
                height = 150
            scaled_pixmap = pixmap.scaled(width, height, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(scaled_pixmap)

        else:
            label.setText("img")
def handle_simple_page(parent, page_data):

    _, page_position, page_name, combo_box_value, img, text_edit_value = page_data
    # Create a new page dynamically
    new_page = QtWidgets.QWidget()
    ui = page1()
    ui.setupUi(new_page)

    # Add the page to the stacked widget
    parent.ui.stackedWidget.addWidget(new_page)

    # Populate the widgets with data
    if ui.textEdit:
        ui.textEdit.setPlainText(text_edit_value if text_edit_value else "")
    if ui.comboBox:
        ui.comboBox.setCurrentIndex(combo_box_value if combo_box_value else 0)
    if ui.label:
        set_image(ui.label, img)
    # Add a button for the page in the top bar

    parent.page_manager.page_type = 1
    parent.page_manager.handle_page_widgets(ui)
    create_top_bar_button(parent, page_name, new_page)

def handle_complex_page(parent, page_data):
    _, page_position, page_name, combo_box_value, text_edit2_value = page_data

    # Create a new page dynamically
    new_page = QtWidgets.QWidget()
    ui = page2()
    ui.setupUi(new_page)

    # Add the page to the stacked widget
    parent.ui.stackedWidget.addWidget(new_page)

    # Populate the widgets with data
    if ui.textEdit2:
        ui.textEdit2.setPlainText(text_edit2_value if text_edit2_value else "")
    if ui.comboBox:
        ui.comboBox.setCurrentIndex(combo_box_value if combo_box_value else 0)

    # Add a button for the page in the top bar
    parent.page_manager.page_type = 2
    parent.page_manager.handle_page_widgets(ui)
    create_top_bar_button(parent, page_name, new_page)

def handle_mid_page(parent, page_data):
    _, page_position, page_name, combo_box_value, text_edit3_value = page_data

    # Create a new page dynamically
    new_page = QtWidgets.QWidget()
    ui = page3()
    ui.setupUi(new_page)

    # Add the page to the stacked widget
    parent.ui.stackedWidget.addWidget(new_page)

    # Populate the widgets with data
    if ui.textEdit3:
        ui.textEdit3.setPlainText(text_edit3_value if text_edit3_value else "")
    if ui.comboBox:
        ui.comboBox.setCurrentIndex(combo_box_value if combo_box_value else 0)

    # Add a button for the page in the top bar
    parent.page_manager.page_type = 3
    parent.page_manager.handle_page_widgets(ui)
    create_top_bar_button(parent, page_name, new_page)

def create_top_bar_button(parent, page_name, new_page):
    page_button = QPushButton(f"{page_name}", parent.ui.top_bar)
    page_button_remove = QPushButton("-", parent.ui.top_bar)

    parent.page_manager.style_new_page_button(page_button, page_button_remove)
    # if page_position
    total = parent.top_bar_layout.count() - 4
    parent.top_bar_layout.insertWidget(total + 1, page_button)
    parent.top_bar_layout.insertWidget(total + 2, page_button_remove)
    parent.page_buttons_list.append(page_name)
    page_button.clicked.connect(lambda: parent.page_manager.switch_to_page(new_page))
    page_button_remove.clicked.connect(lambda: delete_page_from_plan(parent, parent.ui, page_button, page_button_remove, new_page))


def update_form_data(data):
    cursor, conn = get_cursor()
    columns = ', '.join(f"{key} = ?" for key in data.keys() if key != 'username')
    cursor.execute(f'''
        UPDATE User
        SET {columns}
        WHERE username = ?
    ''', tuple(value for key, value in data.items() if key != 'username') + (data['username'],))
    conn.commit()
    conn.close()


def align_page_positions(username, page_buttons_list):
    """Update the database to align page positions with the current order."""
    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for table_name in ["SimplePages", "ComplexPages", "MidPages"]:
        for index, page_name in enumerate(page_buttons_list):
            cursor.execute(f"""
                UPDATE {table_name}
                SET pagePosition = ?
                WHERE username = ? AND pageName = ?
            """, (index, username, page_name))

    conn.commit()
    conn.close()


def save_plan_data(parent, ui, widgets_list):
    # global is_saving, current_user_id
    global is_saving

    # Check if the function is already running
    if is_saving:
        print("Save in progress. Skipping autosave trigger.")
        return

    # Set the flag to True when entering the function
    is_saving = True

    try:
        # user_input = current_user_id
        user_input = parent.current_user_id
        if not user_input:
            user_input = popup_load_plan_dialog(parent, "Save Plan", "Plan ID: ")
            if user_input:
                start_auto_save(parent, ui, widgets_list)
        if user_input:
            data = {}
            if user_id_exists(user_input) and not parent.current_user_id:
                confirm = QtWidgets.QMessageBox.question(
                    parent, "Warning: Plan already exists!",
                    f"Please confirm if you want to override plan: {user_input}?",
                    QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
                )
                if confirm == QtWidgets.QMessageBox.StandardButton.No:
                    return
            parent.current_user_id = user_input
            parent.user_label.setText(user_input)
            for name in widgets_list:
                if name != "username":
                    element = getattr(ui, name, None)
                    if isinstance(element, QtWidgets.QLineEdit):
                        data[name] = element.text()
                    elif isinstance(element, QtWidgets.QPlainTextEdit):
                        data[name] = element.toPlainText()
                    elif isinstance(element, QtWidgets.QLabel):
                        data[name] = element.toolTip()
                    elif isinstance(element, QtWidgets.QComboBox):
                        data[name] = element.currentIndex()
                    elif isinstance(element, QtWidgets.QCheckBox):
                        if element.isChecked():
                            data[name] = 2
                        else:
                            data[name] = 0
                    else:
                        data[name] = ""
            data['username'] = user_input
            if fetch_form_data(user_input, "User"):
                update_form_data(data)
            else:
                insert_form_data(data)

            index = 2
            align_page_positions(parent.current_user_id, parent.page_buttons_list)
            for page_index in range(len(parent.page_buttons_list)):
                page_button = parent.page_buttons_list[page_index]
                page = parent.ui.stackedWidget.widget(index)

                page_type_text = page.findChild(QtWidgets.QLineEdit, "type").text()
                page_type = int(page_type_text)
                if page_type == 1:
                    # collect page1 data
                    textEdit_option = page.findChild(QtWidgets.QTextEdit, "textEdit")
                    comboBox_option = page.findChild(QtWidgets.QComboBox, "comboBox")
                    img_option = page.findChild(QtWidgets.QLabel, "label")

                    data = {
                        "pageName": page_button,
                        "textEdit": textEdit_option.toPlainText(),
                        "comboBox": comboBox_option.currentIndex(),
                        "img": img_option.toolTip(),
                    }
                elif page_type == 2:
                    textEdit_option = page.findChild(QtWidgets.QTextEdit, "textEdit2")
                    comboBox_option = page.findChild(QtWidgets.QComboBox, "comboBox")
                    data = {
                        "pageName": page_button,
                        "textEdit2": textEdit_option.toPlainText(),
                        "comboBox": comboBox_option.currentIndex(),
                    }
                elif page_type == 3:
                    textEdit_option = page.findChild(QtWidgets.QTextEdit, "textEdit3")
                    comboBox_option = page.findChild(QtWidgets.QComboBox, "comboBox")
                    data = {
                        "pageName": page_button,
                        "textEdit3": textEdit_option.toPlainText(),
                        "comboBox": comboBox_option.currentIndex(),
                    }
                save_to_database(user_input, page_type, page_index, data)
                index += 1
    finally:
        is_saving = False

# def save_to_database(username, page_type, page_position, data):
#     folder = os.path.join(os.path.expanduser("~"), 'romao_database')
#     os.makedirs(folder, exist_ok=True)
#     db_path = os.path.join(folder, 'database.db')
#
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#
#     table_name = None
#     text_edit_key = None
#
#     # Determine table and text key based on page type
#     if page_type == 1:
#         table_name = "SimplePages"
#         text_edit_key = "textEdit"
#     elif page_type == 2:
#         table_name = "ComplexPages"
#         text_edit_key = "textEdit2"
#     elif page_type == 3:
#         table_name = "MidPages"
#         text_edit_key = "textEdit3"
#
#     # if table_name and text_edit_key:
#     if table_name:
#         # Check if the entry exists
#         cursor.execute(f"""
#             SELECT 1 FROM {table_name}
#             WHERE username = ? AND pageName = ?
#         """, (username, data["pageName"]))
#         result = cursor.fetchone()
#
#         if result:
#             # Update the existing entry
#             cursor.execute(f"""
#                 UPDATE {table_name}
#                 SET pagePosition = ?, {text_edit_key} = ?, comboBox = ?, img = ?
#                 WHERE username = ? AND pageName = ?
#             """, (page_position, data[text_edit_key], data["comboBox"], data["img"], username, data["pageName"]))
#         else:
#             # Insert new entry
#             cursor.execute(f"""
#                 INSERT INTO {table_name} (username, pagePosition, pageName, {text_edit_key}, comboBox, img)
#                 VALUES (?, ?, ?, ?, ?, ?)
#             """, (username, page_position, data["pageName"], data[text_edit_key], data["comboBox"], data["img"]))
#
#     conn.commit()
#     conn.close()



def save_to_database(username, page_type, page_position, data):
    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    os.makedirs(folder, exist_ok=True)
    db_path = os.path.join(folder, 'database.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # print(f"Data is {data}")
    if page_type == 1:
        cursor.execute("""
            INSERT OR REPLACE INTO SimplePages (username, pagePosition, pageName, textEdit, comboBox, img)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (username, page_position, data["pageName"], data["textEdit"], data["comboBox"], data["img"]))
    if page_type == 2:
        cursor.execute("""
            INSERT OR REPLACE INTO ComplexPages (username, pagePosition, pageName, textEdit2, comboBox)
            VALUES (?, ?, ?, ?, ?)
        """, (username, page_position, data["pageName"], data["textEdit2"], data["comboBox"]))
    if page_type == 3:
        cursor.execute("""
            INSERT OR REPLACE INTO MidPages (username, pagePosition, pageName, textEdit3, comboBox)
            VALUES (?, ?, ?, ?, ?)
        """, (username, page_position, data["pageName"], data["textEdit3"], data["comboBox"]))

    conn.commit()
    conn.close()


def user_id_exists(user_id):
    cursor, conn = get_cursor()
    cursor.execute('SELECT 1 FROM User WHERE username = ?', (user_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
def fetch_user_ids(parent):
    cursor, conn = get_cursor()
    cursor.execute('SELECT DISTINCT username FROM User')
    user_ids = cursor.fetchall()
    conn.close()

    user_ids = [user_id[0] for user_id in user_ids]
    return user_ids

def show_user_ids(parent):
    user_ids = fetch_user_ids(parent)
    dialog = UserDialog(user_ids, parent)
    dialog.exec()

def insert_form_data(data):
    cursor, conn = get_cursor()

    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))

    cursor.execute(f'''
        INSERT INTO User ({columns})
        VALUES ({placeholders})
    ''', tuple(data.values()))

    conn.commit()
    conn.close()
def new_plan_from_copy(parent, ui):
    user_ids = fetch_user_ids(parent)
    dialog = PlanSelectionDialog(user_ids, parent)
    if dialog.exec():
        username = dialog.get_selected_plan()
    else:
        return

    user_id = popup_load_plan_dialog(parent, "Plan Copy", "Insert ID for new plan:")
    if not user_id:
        return

    remove_all_pages(parent)
    data = fetch_form_data(username, "User")
    parent.current_user_id = user_id
    parent.user_label.setText(user_id)
    if data:
        for name, value in data.items():
            element = getattr(ui, name, None)
            if value and isinstance(element, QtWidgets.QLineEdit):
                element.setText(value if value is not None else "")
            elif value and isinstance(element, QtWidgets.QPlainTextEdit):
                element.setPlainText(value if value is not None else "")
        #     elif value and isinstance(element, QtWidgets.QLabel):
        #         set_image(element, value)
        #     elif value and isinstance(element, QtWidgets.QComboBox):
        #         set_all_pages_visible(parent, name, element, value, True)
        #     elif value and isinstance(element, QtWidgets.QCheckBox):
        #         handle_tabs(value, element)

        load_all_pages(parent, username)
        data["username"] = user_id
        setup_auto_save(parent, ui, WidgetsNames().get_widgets_general())

def insert_new_id(parent, ui, names_list):
    if parent.current_user_id:
        confirm = QtWidgets.QMessageBox.question(
            parent, "Warning: Plan open",
            f"Please Confirm creation of new plan ?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if confirm == QtWidgets.QMessageBox.StandardButton.No:
            return

    user_id = popup_load_plan_dialog(parent, "New Plan", "Insert New Plan ID:")
    if user_id:
        if user_id_exists(user_id):
            popup_warning(parent, user_id)
            return
        stop_auto_save(parent)
        remove_all_pages(parent)
        parent.current_user_id = user_id
        parent.user_label.setText(user_id)
        data = {name: "" for name in names_list if name != "username"}
        data["username"] = user_id
        insert_form_data(data)
        update_pages_list(parent)
        setup_auto_save(parent, ui, names_list)


def setup_auto_save(parent, ui, names_list, interval=600):
    # Store the QTimer instance as an attribute of the parent object
    parent.auto_save_timer = QTimer(parent)
    parent.auto_save_timer.timeout.connect(lambda: save_plan_data(parent, ui, names_list))
    parent.auto_save_timer.start(interval)

def stop_auto_save(parent):
    # Stop the QTimer instance stored in the parent object
    if hasattr(parent, "auto_save_timer") and parent.auto_save_timer.isActive():
        parent.auto_save_timer.stop()

def start_auto_save(parent, ui=None, names_list=None):
    # Stop the QTimer instance stored in the parent object
    if not hasattr(parent, "auto_save_timer"):
        if ui is not None and names_list is not None:
            print(f"Here in setup auto save")
            setup_auto_save(parent, ui, names_list, 600)
    elif hasattr(parent, "auto_save_timer") and not parent.auto_save_timer.isActive():
        parent.auto_save_timer.start(600)
    else:
        return

def get_cursor():
    folder = os.path.join(os.path.expanduser("~"), 'romao_database')
    os.makedirs(folder, exist_ok=True)

    db_path = os.path.join(folder, 'database.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return cursor, conn
