#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: socket_http.py
@time: 18-9-4 下午5:06
@desc:
'''

import requests
import socket
from urllib.parse import urlparse

def get_url(url):
    #通过socket请求url
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    #建立socket链接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\n\Host:{}\r\nConnection:close\r\n\r\n".format(path,host).encode('utf8'))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')
    print(data)

    client.close()

if __name__ == "__main__":
    get_url("http://www.baidu.com")


