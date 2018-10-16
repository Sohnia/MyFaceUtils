# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddUserWindows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import face_rc
class Ui_admainDialog(object):
    def setupUi(self, admainDialog):
        admainDialog.setObjectName("admainDialog")
        admainDialog.resize(541, 354)
        self.label_3 = QtWidgets.QLabel(admainDialog)
        self.label_3.setGeometry(QtCore.QRect(170, 80, 71, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nameEdit = QtWidgets.QLineEdit(admainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(250, 80, 113, 20))
        self.nameEdit.setStyleSheet("QLineEdit\n"
"{\n"
"    background:white;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:3px;\n"
"    border-bottom-right-radius:3px;\n"
"    border: 1px solid rgb(209 , 209 , 209);\n"
"    border-top:transparent;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    padding-top:0px ;\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"")
        self.nameEdit.setObjectName("nameEdit")
        self.label_4 = QtWidgets.QLabel(admainDialog)
        self.label_4.setGeometry(QtCore.QRect(170, 130, 71, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.classEdit = QtWidgets.QLineEdit(admainDialog)
        self.classEdit.setGeometry(QtCore.QRect(250, 130, 113, 20))
        self.classEdit.setStyleSheet("QLineEdit\n"
"{\n"
"    background:white;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:3px;\n"
"    border-bottom-right-radius:3px;\n"
"    border: 1px solid rgb(209 , 209 , 209);\n"
"    border-top:transparent;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    padding-top:0px ;\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"")
        self.classEdit.setObjectName("classEdit")
        self.label_5 = QtWidgets.QLabel(admainDialog)
        self.label_5.setGeometry(QtCore.QRect(140, 180, 101, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.photoButton = QtWidgets.QPushButton(admainDialog)
        self.photoButton.setGeometry(QtCore.QRect(380, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.photoButton.setFont(font)
        self.photoButton.setStyleSheet("/*登陆按钮*/\n"
"QPushButton\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.photoButton.setObjectName("photoButton")
        self.addButton = QtWidgets.QPushButton(admainDialog)
        self.addButton.setGeometry(QtCore.QRect(260, 240, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setAutoFillBackground(False)
        self.addButton.setStyleSheet("/*登陆按钮*/\n"
"QPushButton\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 150 , 254);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(44 , 137 , 255);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    color:white;\n"
"    background-color:rgb(14 , 135 , 228);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"}\n"
"")
        self.addButton.setObjectName("addButton")
        self.imgEdit = QtWidgets.QLineEdit(admainDialog)
        self.imgEdit.setGeometry(QtCore.QRect(250, 180, 113, 20))
        self.imgEdit.setStyleSheet("QLineEdit\n"
"{\n"
"    background:white;\n"
"    padding-left:5px ;\n"
"    padding-top:1px ;\n"
"    border-bottom-left-radius:3px;\n"
"    border-bottom-right-radius:3px;\n"
"    border: 1px solid rgb(209 , 209 , 209);\n"
"    border-top:transparent;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"    padding-top:0px ;\n"
"    border: 1px solid rgb(21 , 131 , 221);\n"
"}\n"
"")
        self.imgEdit.setObjectName("imgEdit")

        self.retranslateUi(admainDialog)
        self.photoButton.clicked.connect(admainDialog.takePhoto)
        self.addButton.clicked.connect(admainDialog.addUser)
        QtCore.QMetaObject.connectSlotsByName(admainDialog)

    def retranslateUi(self, admainDialog):
        _translate = QtCore.QCoreApplication.translate
        admainDialog.setWindowTitle(_translate("admainDialog", "管理员"))
        self.label_3.setText(_translate("admainDialog", "用户姓名："))
        self.label_4.setText(_translate("admainDialog", "用户班级："))
        self.label_5.setText(_translate("admainDialog", "添加个人照片："))
        self.photoButton.setText(_translate("admainDialog", "拍照"))
        self.addButton.setText(_translate("admainDialog", "添加"))

