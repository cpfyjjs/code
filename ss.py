#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: ss.py
@time: 18-9-23 下午4:21
@desc:
'''

import pymysql



conn = pymysql.connect('localhost','root','cui1993,','mytest')
cursor = conn.cursor()
print(cursor)

cursor.close()
conn.close()