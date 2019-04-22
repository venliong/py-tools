#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

# 连接数据库
db = pymysql.connect(host='IP', port=6033, user='root', passwd='password', db='db')
cur = db.cursor(cursor=pymysql.cursors.DictCursor)

# query
def query():
    sql = "select * from USER"
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    cur.close()
    db.close()

query()