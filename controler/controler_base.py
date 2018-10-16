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


class ctl_base():

    def __init__(self):
        pass

    def gface(self,image):
        # 模式参数
        filename = "haarcascade_frontalface_default.xml"  # 识别模式文件
        model_path = os.path.join(os.getcwd(), 'utils', filename)
        # 创建classifier
        clf = cv2.CascadeClassifier(model_path)
        # 设定灰度
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 识别面部
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # 画方框
        result = []
        for (x, y, w, h) in faces:
            # 保存识别的人脸
            result.append((x, y, x + w, y + h))
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image, result

    # 打开摄像头进行人脸检测
    def faceCapture(self,name):
        cap = cv2.VideoCapture(0)  # 从摄像头中取得视频
        dir = os.path.join(self.execution_path,'face')
        # 获取视频播放界面长宽
        # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

        # # 定义编码器 创建 VideoWriter 对象

        while (cap.isOpened()):
            # 读取帧摄像头
            ret, frame = cap.read()
            k = cv2.waitKey(1) & 0xFF
            if ret == True:
                # 输出当前帧
                faceCapture, result = self.gface(frame)
                cv2.imshow("take photo with 's' key, exit with 'q' key", faceCapture)
                if result:
                    if k == ord('s'):
                        for x1, y1, x2, y2 in result:
                            face = frame[y1:y2, x1:x2]
                        # print(name)
                        # cv2.imwrite(dir + name + '.jpg', face)
                        cv2.imencode('.jpg', face)[1].tofile(os.path.join(dir,name + '.jpg'))
                        break
                    elif k == ord('q'):
                        break
            else:
                break

        # 释放资源
        cap.release()
        cv2.destroyAllWindows()
