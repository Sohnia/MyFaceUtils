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
from aip import AipSpeech

def baidu_voice(voice,savename):
    """ 你的 APPID AK SK """
    APP_ID = '14436729'
    API_KEY = 'wfzH8EZNKER7oBEy9qzmf3LK'
    SECRET_KEY = 'EO4YgSANWRfHKZTsySnkQpCVP3MXOQ5w '

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(voice, 'zh', 1, {
        'vol': 8,'per':0
    })
    tmp_dir = os.path.join(os.getcwd(),'tmp','music')
    if(not os.path.exists(tmp_dir)):
        os.mkdir(tmp_dir)
    save_path = os.path.join(tmp_dir,savename)
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(save_path, 'wb') as f:
            f.write(result)
    #time.sleep(4)
    os.system(save_path)