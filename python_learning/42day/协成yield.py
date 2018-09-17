#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 协成yield.py
@time: 18-9-17 下午9:42
@desc:
'''

import time
def cunsumer(res):
    """
    任务1：接受数据，处理数据
    :param res:
    :return:
    """
    pass


def producer():
    """
    任务2：生产数据
    :return:
    """
    return [i for i in range(10000000)]

start = time.time()
cunsumer(producer())
print(time.time() - start)
# .32406232357025146
# 基于协成实现生产者消费者模型



def cunsumer():
    while True:
        x = yield


def producer():
    g = cunsumer()
    next(g)
    for i in range(10000000):
        g.send(i)

start = time.time()
producer()
print(time.time() - start)
# .73731772899627686