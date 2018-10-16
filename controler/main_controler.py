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

import cv2
import numpy as np
import face_recognition
from PyQt5.QtWidgets import QApplication

from utils import ft2
from model.UserManage import DBHelper
from .controler_base import ctl_base

class main_window_ctl(ctl_base):
    def __init__(self,ui_instance):
        self.ui = ui_instance
        self.execution_path = os.getcwd()

        # 从数据库中获取已注册的用户脸部图片
        self.dbHelper = DBHelper()
        sql = 'select * from users';
        all_result = self.dbHelper.fetchall(sql, None)
        # 将jpg文件加载到numpy数组中
        self.imgs = list()
        self.labels = list()
        self.known_encoding = list()
        sum = len(all_result)
        for i in range(len(all_result)):
            self.ui.progressBar.setValue(i / sum*100)
            self.labels.append(all_result[i][1])
            self.imgs.append(face_recognition.load_image_file(os.path.join(self.execution_path,'face',all_result[i][3])))
            #print("识别中...")
            # 获取每个图像文件中每个面部的面部编码
            print(i,self.imgs[i])
            encode = face_recognition.face_encodings(self.imgs[i])
            self.known_encoding.append(encode[0])

        unknown_image = face_recognition.load_image_file(os.path.join(self.execution_path,'face','None.jpg'))
        self.unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        self.ui.progressBar.setValue(100)

    def show_face(self):
        if self.ui.ImageButton.clicked:
            # os.chdir('face//')
            # face = QtGui.QPixmap('None.jpg').scaled(115, 120)
            # self.faceView.setAlignment(Qt.AlignCenter)
            # self.faceView.setPixmap(face)
            info = self.faceRecognize()
            if info != False:
                self.ui.infoLabel.setText("您好，欢迎" + info + "同学进入")

            else:
                self.ui.infoLabel.setText("识别错误，重新识别！")

    def show_camera(self):
        if self.ui.cameraButton.clicked:
            # self.faceCapture('None')
            # os.chdir(os.path.join(self.execution_path, 'face'))
            # face = QtGui.QPixmap('None.jpg').scaled(115, 120)
            # self.ui.faceView.setAlignment(Qt.AlignCenter)
            # self.ui.faceView.setPixmap(face)
            self.faceRecognize()

    def faceRecognize(self,source = 0):
        cap = cv2.VideoCapture(source)
        if source != 0:
            cap = cap.open(source)
        while (cap.isOpened()):
            # 读取帧摄像头
            ret, frame = cap.read()
            k = cv2.waitKey(1) & 0xFF
            QApplication.processEvents()
            # 改变摄像头图像的大小，图像小，所做的计算就少
            small_frame = cv2.resize(frame, (0, 0), fx=0.33, fy=0.33)
            rgb_small_frame = small_frame[:, :, ::-1]
            if ret == True:
                # 输出当前帧
                faceCapture = self.frame_draw(rgb_small_frame)
                cv2.imshow("exit with 'q' key", faceCapture)
                if k== ord('q'):
                    break
            else:
                break

        # 释放资源
        cap.release()
        cv2.destroyAllWindows()

    def frame_draw(self,frame):
        QApplication.processEvents()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        face_names = []
        # print('5 is  running')
        for face_encoding in face_encodings:
            # 默认为unknown
            matches = face_recognition.compare_faces(self.known_encoding, face_encoding, tolerance=0.42)
            # 阈值太低容易造成无法成功识别人脸，太高容易造成人脸识别混淆 默认阈值tolerance为0.6
            # print(matches)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = self.labels[first_match_index]
            face_names.append(name)

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # 由于我们检测到的帧被缩放到1/4大小，所以要缩小面位置
                top *= 3
                right *= 3
                bottom *= 3
                left *= 3
                # 矩形框
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)
                ft = ft2.put_chinese_text(os.path.join(self.execution_path,'resources','msyh.ttf'))
                # 引入ft2中的字体
                frame = ft.draw_text(frame, (left + 10, bottom), name, 25, (0, 0, 255))
            # return frame
            show_video = cv2.resize(frame, (800, 494))
            show_video = cv2.cvtColor(show_video, cv2.COLOR_BGR2RGB)
            return show_video.data

