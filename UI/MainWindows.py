# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import face_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ai.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(3.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/background/bg.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.faceView = QtWidgets.QLabel(self.centralwidget)
        self.faceView.setGeometry(QtCore.QRect(10, 110, 401, 371))
        self.faceView.setStyleSheet("background-image: url(:/imageView/ai.png);")
        self.faceView.setText("")
        self.faceView.setObjectName("faceView")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(80, 430, 261, 61))
        font = QtGui.QFont()
        font.setFamily("华文彩云")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.infoLabel.setFont(font)
        self.infoLabel.setStyleSheet("background-image: url(:/label/transparent.jpg);")
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(520, 120, 201, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.admainButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.admainButton.setFont(font)
        self.admainButton.setStyleSheet("/*登陆按钮*/\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imageView/ai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.admainButton.setIcon(icon1)
        self.admainButton.setIconSize(QtCore.QSize(32, 32))
        self.admainButton.setObjectName("admainButton")
        self.verticalLayout.addWidget(self.admainButton)
        self.cameraButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.cameraButton.setFont(font)
        self.cameraButton.setStyleSheet("/*登陆按钮*/\n"
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
        self.cameraButton.setIcon(icon)
        self.cameraButton.setIconSize(QtCore.QSize(32, 32))
        self.cameraButton.setObjectName("cameraButton")
        self.verticalLayout.addWidget(self.cameraButton)
        self.historyButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.historyButton.setFont(font)
        self.historyButton.setStyleSheet("/*登陆按钮*/\n"
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
        self.historyButton.setIcon(icon)
        self.historyButton.setIconSize(QtCore.QSize(32, 32))
        self.historyButton.setObjectName("historyButton")
        self.verticalLayout.addWidget(self.historyButton)
        self.multiImportButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.multiImportButton.setFont(font)
        self.multiImportButton.setStyleSheet("/*登陆按钮*/\n"
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
        self.multiImportButton.setIcon(icon)
        self.multiImportButton.setIconSize(QtCore.QSize(32, 32))
        self.multiImportButton.setObjectName("multiImportButton")
        self.verticalLayout.addWidget(self.multiImportButton)
        self.mulImpGuiButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(11)
        self.mulImpGuiButton.setFont(font)
        self.mulImpGuiButton.setStyleSheet("/*登陆按钮*/\n"
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
        self.mulImpGuiButton.setIcon(icon)
        self.mulImpGuiButton.setIconSize(QtCore.QSize(32, 32))
        self.mulImpGuiButton.setObjectName("mulImpGuiButton")
        self.verticalLayout.addWidget(self.mulImpGuiButton)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 560, 761, 31))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"border-radius:0;\n"
"text-align:center;\n"
"color:#fff;\n"
"background-color:transparent;\n"
"border: 2px solid #e3a21a;\n"
"border-radius:7px;\n"
"    font: 75 12pt \"Open Sans\";\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"background-color:#2d89ef;\n"
"width:20px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cameraButton.clicked.connect(MainWindow.showCamera)
        self.admainButton.clicked.connect(MainWindow.showAdmain)
        self.historyButton.clicked.connect(MainWindow.showHistory)
        self.multiImportButton.clicked.connect(MainWindow.showMultiImport)
        self.mulImpGuiButton.clicked.connect(MainWindow.showMulImpGui)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别系统"))
        self.admainButton.setText(_translate("MainWindow", "用户管理"))
        self.cameraButton.setText(_translate("MainWindow", "人脸识别"))
        self.historyButton.setText(_translate("MainWindow", "人脸识别记录"))
        self.multiImportButton.setText(_translate("MainWindow", "批量导入"))
        self.mulImpGuiButton.setText(_translate("MainWindow", "批量导入介绍"))


