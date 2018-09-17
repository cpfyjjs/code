#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: client.py
@time: 18-9-17 下午8:58
@desc:
'''

from socket import *
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8070))

while True:
    msg=input('>>: ')
    if not msg:continue
    c.send(msg.encode('utf-8'))
    data=c.recv(1024)
    print(data.decode('utf-8'))