# Form implementation generated from reading ui file 'ui/page3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(879, 659)
        Form.setStyleSheet("background-color: rgb(131, 131, 131);")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 842, 1012))
        self.scrollAreaWidgetContents.setStyleSheet("/*background-color: rgb(90,90,90);*/\n"
"background-color: rgb(30, 30, 30);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(30)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_9 = QtWidgets.QFrame(parent=self.frame)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 350))
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.type = QtWidgets.QLineEdit(parent=self.frame_9)
        self.type.setObjectName("type")
        self.verticalLayout_4.addWidget(self.type)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_9)
        self.comboBox.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.textEdit3 = QtWidgets.QTextEdit(parent=self.frame_9)
        self.textEdit3.setStyleSheet("background-color: rgb(110, 160, 210);")
        self.textEdit3.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.textEdit3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.textEdit3.setLineWidth(2)
        self.textEdit3.setObjectName("textEdit3")
        self.verticalLayout_4.addWidget(self.textEdit3)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_9)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_3.setStyleSheet("background-color: rgb(89, 89, 89);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(parent=self.frame_3)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setStyleSheet("background-color: rgb(210, 160, 110);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_2.setStyleSheet("background-color: rgb(210, 160, 110);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_4.setStyleSheet("background-color: rgb(89, 89, 89);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.frame_4)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_3.setStyleSheet("background-color: rgb(210, 160, 110);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_4.setStyleSheet("background-color: rgb(210, 160, 110);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_8)
        self.frame_6.setStyleSheet("background-color: rgb(89, 89, 89);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.frame_6)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_3.addWidget(self.radioButton_3)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_3.setMinimumSize(QtCore.QSize(50, 50))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_5.setStyleSheet("background-color: rgb(210, 160, 110);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_6.setStyleSheet("background-color: rgb(210, 160, 110);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.verticalLayout_14.addWidget(self.frame_9)
        self.frame_18 = QtWidgets.QFrame(parent=self.frame)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.frame_18)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_10.addWidget(self.comboBox_2)
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.frame_18)
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_10.addWidget(self.textEdit_3)
        self.frame_19 = QtWidgets.QFrame(parent=self.frame_18)
        self.frame_19.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_20 = QtWidgets.QFrame(parent=self.frame_19)
        self.frame_20.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_20)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_21 = QtWidgets.QFrame(parent=self.frame_20)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.frame_21)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_10.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.frame_21)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_10.addWidget(self.pushButton_14)
        self.verticalLayout_11.addWidget(self.frame_21)
        self.horizontalLayout_9.addWidget(self.frame_20)
        self.frame_22 = QtWidgets.QFrame(parent=self.frame_19)
        self.frame_22.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_22)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_12.addWidget(self.label_8, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_23 = QtWidgets.QFrame(parent=self.frame_22)
        self.frame_23.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.frame_23)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_11.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.frame_23)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_11.addWidget(self.pushButton_16)
        self.verticalLayout_12.addWidget(self.frame_23)
        self.horizontalLayout_9.addWidget(self.frame_22)
        self.frame_24 = QtWidgets.QFrame(parent=self.frame_19)
        self.frame_24.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_24)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_25 = QtWidgets.QFrame(parent=self.frame_24)
        self.frame_25.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.frame_25)
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_12.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.frame_25)
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_12.addWidget(self.pushButton_18)
        self.verticalLayout_13.addWidget(self.frame_25)
        self.horizontalLayout_9.addWidget(self.frame_24)
        self.verticalLayout_10.addWidget(self.frame_19)
        self.verticalLayout_14.addWidget(self.frame_18)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.frame_10)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_5.addWidget(self.comboBox_3)
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.frame_10)
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_5.addWidget(self.textEdit_2)
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_12 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_13 = QtWidgets.QFrame(parent=self.frame_12)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_13)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_13)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_6.addWidget(self.pushButton_8)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.horizontalLayout_5.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_15 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_15)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_7.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_15)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.horizontalLayout_5.addWidget(self.frame_14)
        self.frame_16 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_16)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.frame_17 = QtWidgets.QFrame(parent=self.frame_16)
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame_17)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_8.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.frame_17)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_8.addWidget(self.pushButton_12)
        self.verticalLayout_8.addWidget(self.frame_17)
        self.horizontalLayout_5.addWidget(self.frame_16)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.verticalLayout_14.addWidget(self.frame_10)
        self.verticalLayout_9.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_21.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.type.setText(_translate("Form", "3"))
        self.comboBox.setItemText(0, _translate("Form", "opçao 1"))
        self.comboBox.setItemText(1, _translate("Form", "opçao 2"))
        self.radioButton.setText(_translate("Form", " + \"/\""))
        self.label.setText(_translate("Form", "img"))
        self.pushButton.setText(_translate("Form", "+"))
        self.pushButton_2.setText(_translate("Form", "-"))
        self.radioButton_2.setText(_translate("Form", "+ \"/\""))
        self.label_2.setText(_translate("Form", "img"))
        self.pushButton_3.setText(_translate("Form", "+"))
        self.pushButton_4.setText(_translate("Form", "-"))
        self.radioButton_3.setText(_translate("Form", "+ \"/\""))
        self.label_3.setText(_translate("Form", "img"))
        self.pushButton_5.setText(_translate("Form", "+"))
        self.pushButton_6.setText(_translate("Form", "-"))
        self.label_7.setText(_translate("Form", "img"))
        self.pushButton_13.setText(_translate("Form", "+"))
        self.pushButton_14.setText(_translate("Form", "-"))
        self.label_8.setText(_translate("Form", "img"))
        self.pushButton_15.setText(_translate("Form", "+"))
        self.pushButton_16.setText(_translate("Form", "-"))
        self.label_9.setText(_translate("Form", "img"))
        self.pushButton_17.setText(_translate("Form", "+"))
        self.pushButton_18.setText(_translate("Form", "-"))
        self.label_4.setText(_translate("Form", "img"))
        self.pushButton_7.setText(_translate("Form", "+"))
        self.pushButton_8.setText(_translate("Form", "-"))
        self.label_5.setText(_translate("Form", "img"))
        self.pushButton_9.setText(_translate("Form", "+"))
        self.pushButton_10.setText(_translate("Form", "-"))
        self.label_6.setText(_translate("Form", "img"))
        self.pushButton_11.setText(_translate("Form", "+"))
        self.pushButton_12.setText(_translate("Form", "-"))
