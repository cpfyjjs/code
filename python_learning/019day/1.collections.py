#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 1.collections.py
@time: 18-9-5 下午4:42
@desc:
'''

import re

cont = '(1)-2*((60-30+(-40/5)*(9-2*3+7/8*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

re_parentheses = re.compile(r'\(([^\(]*?)\)')
ret = re_parentheses.findall(cont)
c =re_parentheses.split(cont)
print(c)
re_digit = re.compile('(\d+)')
for txt in ret:
    c = re_digit.split(txt)
    print (c)