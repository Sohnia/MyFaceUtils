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
import os

from PyQt5.QtWidgets import QMessageBox

from .controler_base import ctl_base
from model.UserManage import DBHelper


class admin_window_ctl(ctl_base):
    def __init__(self,ui_instance):
        self.ui = ui_instance
        self.execution_path = os.getcwd()

    def take_photo(self):
        name = self.ui.nameEdit.text()
        if name != "":
            dir = os.path.join(self.execution_path, 'face')
            if not os.path.exists(dir):
                os.mkdir(dir)
            self.faceCapture(name)
            self.ui.imgEdit.setText(name + '.jpg')
        else:
            img_box = QMessageBox.information(self.ui, "拍照", "请输入姓名")

    def add_user(self):
        dbHelper = DBHelper()
        userName = self.ui.nameEdit.text()
        userClass = self.ui.classEdit.text()
        userImg = self.ui.imgEdit.text()
        if userName == "" or userClass == "" or userImg == "":
            blank_box = QMessageBox.information(self.ui, "注册", "不能输入空值")
        else:
            print('Name:{0}, Class:{1}, Image:{2}'.format(userName, userClass, userImg))
            sql = "insert into users values (null,'{0}','{1}','{2}')".format(userName, userClass, userImg)
            result = dbHelper.execute(sql, None)
            if result:
                success_box = QMessageBox.information(self.ui, "注册", "恭喜，\n注册成功！")
            else:
                fail_box = QMessageBox.information(self.ui, "注册", "抱歉，\n注册失败！")
