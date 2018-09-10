#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: client.py
@time: 18-9-10 下午8:38
@desc:
'''

import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1',8060))



cmd = sk.recv(1024).decode('utf8')
print(cmd)
res = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE)

std_out = res.stdout.read()
std_err = res.stderr.read()

std = std_out + std_err
print(std)
size = str(len(std)).encode('utf8')

sk.send(size)
sk.recv(1024)
num = 0
while num < int(size):
    sk.send(std[num:num+128])
    num +=128

sk.close()
