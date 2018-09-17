#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: server.py
@time: 18-9-17 下午8:47
@desc:
'''

import socket
import select

sk = socket.socket()
sk.bind(('127.0.0.1',8070))
sk.listen()

sk.setblocking(False)
read_l = [sk]

while True:
    r_l , w_l , x_l = select.select(read_l, [], [])
    print(r_l)
    for ready_obj in r_l:
        if ready_obj == sk:
            conn, addr =ready_obj.accept()
            read_l.append(conn)
        else:
            try:
                data = ready_obj.recv(1024)
                if not data:
                    ready_obj.close()
                    read_l.remove(ready_obj)
                    continue
                ready_obj.send(data.upper())
            except ConnectionResetError:
                ready_obj.close()
                read_l.remove(ready_obj)
