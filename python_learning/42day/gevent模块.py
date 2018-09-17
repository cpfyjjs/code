#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: gevent模块.py
@time: 18-9-17 下午9:55
@desc:
'''

from gevent import monkey;monkey.patch_all()
import gevent

def eat(name):
    print('%s eat 1' %name)
    gevent.sleep(2)
    print('%s eat 2' %name)

def play(name):
    print('%s play 1' %name)
    gevent.sleep(1)
    print('%s play 2' %name)

g1 = gevent.spawn(eat,'bob')
g2 = gevent.spawn(play,'jack')

g1.join()
g2.join()
print('主线程')