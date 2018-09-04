#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@author: cpf
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: 756206487@qq.com
@software: pycharm
@file: python_gil.py
@time: 18-9-4 下午5:30
@desc:
'''

# gil global interpreter lock (cpython)

# gil 使得同一时刻只有一个线程在一个CPU上执行字节码，无法将多个线程映射到多个CPU上

# gil 会根据执行字节码的行数以及时间片释放 gil , gil 在遇到io操作的时候也会主动释放
import dis
import threading


def add(a):
    a += 1
    return a

#print(dis.dis(add))

"""
函数变成字节码的流程
 20           0 LOAD_FAST                0 (a)
              2 LOAD_CONST               1 (1)
              4 INPLACE_ADD
              6 STORE_FAST               0 (a)

 21           8 LOAD_FAST                0 (a)
             10 RETURN_VALUE
None
"""

total =0

def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -=1


thread1 = threading.Thread(target= add)
thread2 = threading.Thread(target= desc)

thread1.start()
thread2.start()

print(total)
# 116569        total 会是一个随机的数值
#TODO kaishi

