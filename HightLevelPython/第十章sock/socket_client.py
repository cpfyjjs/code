#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: socket_client.py
@time: 18-9-4 下午3:53
@desc:
'''
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8000))

try:
    while True:
        print("client : ",end = '')
        re_data = input()
        client.send(re_data.encode("utf8"))

        data = client.recv(1024)
        print("server : {}".format(data.decode("utf8")))
finally:
    client.close()
    print("88")