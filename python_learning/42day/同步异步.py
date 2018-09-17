#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 同步异步.py
@time: 18-9-17 下午10:01
@desc:
'''

from gevent import spawn,joinall,monkey;monkey.patch_all()

import time
def task(pid):
    """
    Some non-deterministic task
    """
    time.sleep(0.5)
    print('Task %s done' % pid)


def synchronous():  # 同步
    for i in range(10):
        task(i)

def asynchronous(): # 异步
    g_l=[spawn(task,i) for i in range(10)]
    joinall(g_l)
    print('DONE')

print("异步")
asynchronous()
print("同步")
synchronous()