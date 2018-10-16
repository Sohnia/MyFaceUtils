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
import pymysql

import config


class DBHelper:
    def __init__(self, host=config.host, user=config.user,
                 pwd=config.pwd, db='face'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None

    # 连接数据库
    def connect(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.pwd, self.db, charset='utf8')
        except:
            print("connect error...")
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 插入操作,执行数据库语句
    def execute(self, sql, params=None):
        # 连接数据库
        if not self.connect() :
            return False
        try:
            if self.conn and self.cur:
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            print("insert error...")
            self.close()
            return False
        return True

    # 查询表数据
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.fetchall()
