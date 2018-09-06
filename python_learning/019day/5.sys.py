#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 5.sys.py
@time: 18-9-6 下午2:48
@desc:
'''

import sys

print(sys.platform)
# linux

print(sys.path)
# ['/home/cpf/code/python_learning/019day', '/home/cpf/code', '/home/cpf/anaconda3/lib/python36.zip', '/home/cpf/anaconda3/lib/python3.6', '/home/cpf/anaconda3/lib/python3.6/lib-dynload', '/home/cpf/anaconda3/lib/python3.6/site-packages', '/snap/pycharm-professional/83/helpers/pycharm_matplotlib_backend']

print(sys.version)
# 3.6.5 |Anaconda, Inc.| (default, Apr 29 2018, 16:14:56)
# [GCC 7.2.0]

# sys.exit(0)       正确退出
# sys.exit(1)       错误退出

print(sys.argv)


ret = sys.argv
name = ret[1]
pwd = ret[2]


# python 5.sys.py alex alex3714
if name == 'alex' and pwd == 'alex3714':
    print("登陆成功")

else:
    print("用户名密码错误")
    sys.exit()

print("你可以使用计算器了")