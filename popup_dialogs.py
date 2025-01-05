from PyQt6.QtGui import QPixmap, QFont
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt
from page_type_popup import Ui_Form as choose_page


def choose_page_popup():
    page_type_popup = QDialog()
    page_type_ui = choose_page()
    page_type_ui.setupUi(page_type_popup)

    page_type_ui.ok.clicked.connect(page_type_popup.accept)
    page_type_ui.cancel.clicked.connect(page_type_popup.reject)

    result = page_type_popup.exec()
    if result == QDialog.DialogCode.Accepted:  # Compare with DialogCode.Accepted
        if page_type_ui.radioSimple.isChecked():
            return 1
        elif page_type_ui.radioComplex.isChecked():
            return 2
        elif page_type_ui.radioMid.isChecked():
            return 3
        else:
            return 0
    else:
        return 0


from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class PlanSelectionDialog(QDialog):
    def __init__(self, plans, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select a Plan")
        self.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.resize(500, 600)

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        # Search input
        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Type to search for a plan...")
        self.searchBox.textChanged.connect(self.filter_plans)
        self.searchBox.setStyleSheet("color: white; background-color: rgb(50, 50, 50);")
        self.searchBox.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.searchBox)

        # Plan list
        self.listWidget = QListWidget()
        self.listWidget.setStyleSheet("color: white;")
        self.listWidget.setSpacing(5)
        font = QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.layout.addWidget(self.listWidget)

        # Add plans to the list
        self.plans = plans
        self.filtered_plans = plans  # Keep track of the filtered list
        self.populate_list(self.plans)

        # Confirm button
        self.confirmButton = QPushButton("Confirm Selection")
        self.confirmButton.clicked.connect(self.confirm_selection)
        self.confirmButton.setStyleSheet("background-color: rgb(70, 70, 70); color: white;")
        self.confirmButton.setCursor(Qt.CursorShape.PointingHandCursor)  # Set pointing hand cursor
        self.layout.addWidget(self.confirmButton)

        self.setLayout(self.layout)

    def populate_list(self, plans):
        """Populate the list widget with the given plans."""
        self.listWidget.clear()
        for plan in plans:
            item = QListWidgetItem(plan)
            item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
            self.listWidget.addItem(item)

    def filter_plans(self, text):
        """Filter the list based on the search text."""
        self.filtered_plans = [plan for plan in self.plans if text.lower() in plan.lower()]
        self.populate_list(self.filtered_plans)

    def confirm_selection(self):
        """Handle the confirmation of the selected plan."""
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select a plan before confirming.")
            return

        self.selected_plan = selected_items[0].text()
        self.accept()

    def get_selected_plan(self):
        """Return the selected plan."""
        return getattr(self, 'selected_plan', None)

class UserDialog(QDialog):
    def __init__(self, user_ids, parent=None):
        super().__init__(parent)
        self.setWindowTitle("All Plans on Database")
        self.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)  # Set tighter margins
        self.layout.setSpacing(10)
        self.resize(500, 600)

        # Create QListWidget
        self.listWidget = QListWidget()
        for user_id in user_ids:
            item = QListWidgetItem(f"• {user_id}")
            item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.listWidget.addItem(item)

        # Set font size
        font = QFont()
        font.setPointSize(14)  # Adjust the font size as needed
        self.listWidget.setStyleSheet("color: white;")
        self.listWidget.setSpacing(5)
        self.listWidget.setFont(font)

        # Add QListWidget to layout
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)


def popup_warning(parent, username=None, message=None):
    # Create a custom dialog window
    dialog = QtWidgets.QDialog(parent)
    dialog.setWindowTitle("Warning")

    # Set a dark background color for the dialog
    dialog.setStyleSheet("background-color: rgb(60, 20, 20);")  # Dark background

    # Set dialog layout
    layout = QtWidgets.QVBoxLayout(dialog)
    layout.setContentsMargins(20, 20, 20, 20)  # Set margins around the layout

    # Create and set the warning label
    if username:
        label = QtWidgets.QLabel(f"The username '{username}' already exists. Please choose another.")
    else:
        label = QtWidgets.QLabel(message)
    font = QtGui.QFont()
    font.setPointSize(16)  # Set a larger font size
    label.setFont(font)
    label.setStyleSheet("color: white;")
    label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Center align the label

    # Add the label to the layout
    layout.addWidget(label)

    # Add a button for "OK"
    button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok)
    button_box.setFont(font)

    # Style the button
    for button in button_box.buttons():
        button.setMinimumHeight(30)  # Increase button height
        button.setMinimumWidth(100)  # Increase button width
        button.setStyleSheet("color: white;")

    button_box.layout().setSpacing(20)

    # Center the button box
    button_layout = QtWidgets.QHBoxLayout()
    button_layout.addStretch(1)
    button_layout.addWidget(button_box)
    button_layout.addStretch(1)
    layout.addLayout(button_layout)

    # Connect the button
    button_box.accepted.connect(dialog.accept)

    # Resize the dialog
    dialog.resize(200, 140)  # Adjust the size of the dialog

    # Show the dialog and wait for user response
    dialog.exec()



def popup_load_plan_dialog(parent, title, line):
    # Create a custom dialog window
    dialog = QtWidgets.QDialog(parent)
    dialog.setWindowTitle(title)

    # Set a soft white background color for the entire dialog
    dialog.setStyleSheet("background-color:  rgb(30, 30, 30);")  # Light grey background

    # Set dialog layout
    layout = QtWidgets.QVBoxLayout(dialog)
    layout.setContentsMargins(20, 20, 20, 20)  # Set margins around the layout

    # Create and set the label
    label = QtWidgets.QLabel(line)

    font = QtGui.QFont()
    font.setPointSize(16)  # Set a larger font size
    label.setFont(font)
    label.setStyleSheet("color: white;")
    # Align the label at the top
    # label.setAlignment(QtCore.Qt.AlignTop)

    # Add the label to the layout with stretching
    layout.addStretch(1)
    layout.addWidget(label)

    # Create and set the QLineEdit
    line_edit = QtWidgets.QLineEdit(dialog)
    font2 = QtGui.QFont()
    font2.setPointSize(12)
    line_edit.setFont(font2)
    line_edit.setMinimumHeight(20)


    # Set a darker dirty white background color for the input field
    line_edit.setStyleSheet("""
        background-color: #616161;  /* Set background color */
        border: 2px solid #ffffff;  /* Set border thickness and color */
        border-radius: 5px;         /* Make the edges rounded */
        padding: 4px;               /* Add some inner padding for better text visibility */
    """)
    layout.addWidget(line_edit)

    # Add stretching between the input field and buttons
    layout.addStretch(1)

    # Create buttons for OK and Cancel with larger sizes
    button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
    button_box.setFont(font)

    # Make buttons larger
    for button in button_box.buttons():
        # button.setCursor(QtCore.Qt.PointingHandCursor)
        button.setMinimumHeight(20)  # Increase button height
        button.setMinimumWidth(80)  # Increase button width
        button.setStyleSheet("color: white;")

    button_box.layout().setSpacing(20)

    # Center the button box
    button_layout = QtWidgets.QHBoxLayout()
    button_layout.addStretch(1)
    button_layout.addWidget(button_box)
    button_layout.addStretch(1)
    layout.addLayout(button_layout)

    # Add stretching at the bottom
    layout.addStretch(1)

    # Connect the buttons
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    # Resize the dialog
    dialog.resize(400, 250)  # Adjust the size of the dialog for better spacing

    # Show the dialog and get the result
    result = dialog.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:  # Compare with DialogCode.Accepted
        return line_edit.text()  # Return the text from the input field if OK is pressed
    else:
        return None

def popup_insert_page_dialog(parent, title, line1, line2):
    # Create a custom dialog window
    dialog = QtWidgets.QDialog(parent)
    dialog.setWindowTitle(title)

    # Set a soft white background color for the entire dialog
    dialog.setStyleSheet("background-color: rgb(30, 30, 30);")  # Dark grey background

    # Set dialog layout
    layout = QtWidgets.QVBoxLayout(dialog)
    layout.setContentsMargins(20, 20, 20, 20)  # Set margins around the layout

    # Create a grid layout for the labels and text inputs
    grid_layout = QtWidgets.QGridLayout()

    # Create and set the first label
    label1 = QtWidgets.QLabel(line1)
    font = QtGui.QFont()
    font.setPointSize(16)  # Set a larger font size
    label1.setFont(font)
    label1.setStyleSheet("color: white;")

    # Create and set the first QLineEdit
    line_edit1 = QtWidgets.QLineEdit(dialog)
    font2 = QtGui.QFont()
    font2.setPointSize(12)
    line_edit1.setFont(font2)
    line_edit1.setMinimumHeight(20)
    line_edit1.setStyleSheet("""
        background-color: #616161;  /* Set background color */
        border: 2px solid #ffffff;  /* Set border thickness and color */
        border-radius: 5px;         /* Make the edges rounded */
        padding: 4px;               /* Add some inner padding for better text visibility */
    """)

    # Add the first label and line edit to the grid layout
    grid_layout.addWidget(label1, 0, 0)
    grid_layout.addWidget(line_edit1, 0, 1)

    # Create and set the second label
    label2 = QtWidgets.QLabel(line2)
    label2.setFont(font)
    label2.setStyleSheet("color: white;")

    # Create and set the second QLineEdit
    line_edit2 = QtWidgets.QLineEdit(dialog)
    line_edit2.setFont(font2)
    line_edit2.setMinimumHeight(20)
    line_edit2.setStyleSheet("""
        background-color: #616161;  /* Set background color */
        border: 2px solid #ffffff;  /* Set border thickness and color */
        border-radius: 5px;         /* Make the edges rounded */
        padding: 4px;               /* Add some inner padding for better text visibility */
    """)

    # Add the second label and line edit to the grid layout
    grid_layout.addWidget(label2, 1, 0)
    grid_layout.addWidget(line_edit2, 1, 1)

    # Add the grid layout to the main layout
    layout.addLayout(grid_layout)

    # Add stretching between the input fields and buttons
    layout.addStretch(1)

    # Create buttons for OK and Cancel with larger sizes
    button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
    button_box.setFont(font)

    # Make buttons larger
    for button in button_box.buttons():
        button.setMinimumHeight(20)  # Increase button height
        button.setMinimumWidth(80)  # Increase button width
        button.setStyleSheet("color: white;")

    button_box.layout().setSpacing(20)

    # Center the button box
    button_layout = QtWidgets.QHBoxLayout()
    button_layout.addStretch(1)
    button_layout.addWidget(button_box)
    button_layout.addStretch(1)
    layout.addLayout(button_layout)

    # Add stretching at the bottom
    layout.addStretch(1)

    # Connect the buttons
    button_box.accepted.connect(dialog.accept)
    button_box.rejected.connect(dialog.reject)

    # Resize the dialog
    dialog.resize(400, 250)  # Adjust the size of the dialog for better spacing

    # Show the dialog and get the result
    result = dialog.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:  # Compare with DialogCode.Accepted
        return line_edit1.text(), line_edit2.text()  # Return the texts from both input fields if OK is pressed
    else:
        return None
