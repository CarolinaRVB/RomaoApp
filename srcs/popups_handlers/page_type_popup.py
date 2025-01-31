# Form implementation generated from reading ui file 'ui/page_type_popup.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 250)
        Form.setMaximumSize(QtCore.QSize(400, 250))
        Form.setStyleSheet("background-color:  rgb(30, 30, 30)")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(parent=Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 15)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioSimple = QtWidgets.QRadioButton(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioSimple.setFont(font)
        self.radioSimple.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioSimple.setObjectName("radioSimple")
        self.horizontalLayout_2.addWidget(self.radioSimple, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.radioComplex = QtWidgets.QRadioButton(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioComplex.setFont(font)
        self.radioComplex.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioComplex.setObjectName("radioComplex")
        self.horizontalLayout_2.addWidget(self.radioComplex, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.radioMid = QtWidgets.QRadioButton(parent=self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioMid.setFont(font)
        self.radioMid.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioMid.setObjectName("radioMid")
        self.horizontalLayout_2.addWidget(self.radioMid, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok = QtWidgets.QPushButton(parent=self.frame)
        self.ok.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ok.setFont(font)
        self.ok.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ok.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 53, 53);")
        self.ok.setObjectName("ok")
        self.horizontalLayout.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(parent=self.frame)
        self.cancel.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(53, 53, 53);")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_3.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Please choose page type:"))
        self.radioSimple.setText(_translate("Form", "Simple"))
        self.radioComplex.setText(_translate("Form", "Complex"))
        self.radioMid.setText(_translate("Form", "Mid"))
        self.ok.setText(_translate("Form", "OK"))
        self.cancel.setText(_translate("Form", "Cancel"))
