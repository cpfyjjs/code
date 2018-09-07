#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 2.logging.py
@time: 18-9-7 下午5:05
@desc:
'''

import logging

loger = logging.getLogger()
# 创建一个handler ,用于写入日志文件
fh = logging.FileHandler('test.log',encoding='utf8')

# 再创建一个handler ,用于控制输出控制台
ch = logging.StreamHandler()

# 定义输出格式
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] - %(levelname)s -- %(message)s')

# 设置输出等级
fh.setLevel(logging.DEBUG)

# 设置文件格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)
loger.addHandler(fh)
loger.addHandler(ch)

loger.debug('debug message')              # 排错信息
loger.info('info message')                # 正常警告
loger.warning('warning message')          # 警告信息
loger.error('error message')              # 错误信息
loger.critical('critical message')        # 严重警告信息


# longing
"""
有5种级别的日志记录模式：
    
    
"""

