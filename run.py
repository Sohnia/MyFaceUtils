#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Sohnia'
__mtime__ = '2018/10/16'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from PyQt5 import QtWidgets, QtGui
from UI.AddUserWindows import Ui_admainDialog
from UI.MainWindows import Ui_MainWindow
import sys, os
from controler import admin_window_ctl, main_window_ctl


class AdmainWindow(QtWidgets.QDialog, Ui_admainDialog):
    def __init__(self):
        super(AdmainWindow, self).__init__()
        self.setupUi(self)
        self.execution_path = os.getcwd()
        self.ctl = admin_window_ctl(self)

    def takePhoto(self):
        self.ctl.take_photo()

    def addUser(self):
        self.ctl.add_user()


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.execution_path = os.getcwd()
        self.setFixedSize(self.width(), self.height())
        self.ctl = main_window_ctl(self)

    def showCamera(self):
        self.ctl.show_camera()

    def showHistory(self):
        pass

    def showMultiImport(self):
        pass

    def showMulImpGui(self):
        pass

    def showFace(self):
        self.ctl.show_face()

    def showAdmain(self):
        if self.admainButton.clicked:
            admainDialog = AdmainWindow()
            admainDialog.show()
            admainDialog.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    app.exec_()
    sys.exit(0)
