#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: server.py
@time: 18-9-17 下午7:39
@desc:
'''

import time
import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',8070))
sk.listen(5)

sk.setblocking(False)

conn_l = []
del_l =  []

while True:
    try:
        conn, addr = sk.accept()
        conn_l.append(conn)
    except BlockingIOError:
        for conn in conn_l:
            try:
                data = conn.recv(1024)
                print(data)
                if not data:
                    del_l.append(conn)
                    continue
                conn.send(data.upper())
            except BlockingIOError:
                pass

        for conn in del_l:
            conn_l.remove(conn)
            conn.close()

        del_l = []



