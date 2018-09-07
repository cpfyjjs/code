#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 1.logging.py
@time: 18-9-7 下午4:19
@desc:
'''

import logging


# basicconfig 简单能做的事情相对较少
# 配置log 对象，稍微有点复杂，能做的事情相对较多

logging.basicConfig(level=logging.DEBUG,
                    format = '%(asctime)s %(filename)s[line:%(lineno)d]  %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename = 'test.log',
                    filemode = 'a'
                    )
logging.debug('debug message')              # 排错信息
logging.info('info message')                # 正常警告
logging.warning('warning message')          # 警告信息
logging.error('error message')              # 错误信息
logging.critical('critical message')        # 严重警告信息

try:
    ret = int(input('Number : '))
except ValueError:
    logging.error('值错误')