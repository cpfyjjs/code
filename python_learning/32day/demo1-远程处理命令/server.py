#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: server.py
@time: 18-9-10 下午8:38
@desc:
'''

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8060))

sk.listen()
conn, addr = sk.accept()




cmd = input('远程命令 ： ').encode('utf8')
conn.send(cmd)
size = conn.recv(1024).decode('utf8')
print('size :{0}'.format(size))

conn.send('ok'.encode('utf8'))
num = 0
while num < int(size):
    info = conn.recv(128).decode('utf8')
    print(info)
    num += 128

conn.close()
sk.close()
