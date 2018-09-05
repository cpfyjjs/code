#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: sock_server.py
@time: 18-9-4 下午4:11
@desc:
'''

import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()
sock, addr = server.accept()

#获取从客户端获取的数据
try:
    while True:
        data = sock.recv(1024)
        print("client : {}".format(data.decode("utf8")))

        print("server :",end = '')
        re_data = input()
        sock.send(re_data.encode('utf8'))
finally:
    server.close()
    sock.close()
    print("88")