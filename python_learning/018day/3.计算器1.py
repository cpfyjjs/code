#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 3.计算器.py
@time: 18-9-5 下午4:42
@desc:
'''

'(1)-2*((60-30+(-40/5)*(9-2*3+7/8*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# 1-2*((60-30+(-40/5)*(9-2*3+7/8*99/4*2998+10*568/14))-(-4*3)/(16-3*2))

import re

cont = '(1)-2*((60-30+(-40/5)*(9-2*3+7/8*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

re_parentheses = re.compile(r'\(([^\(]*?)\)')
ret = re_parentheses.findall(cont)
print(ret)
re_digit = re.compile('(\d+)')


"""
构建一个双端队列用于存放数字
一个存放

for 循环列表
    if 如果符号队列右侧为 × \
        从数字队列右侧弹出数据
        并进行计算
        然后放回到队列左侧侧
    else
        如果为数字放在数字双端队列右侧
        如果为符号放在符号队列右侧
sum =0
while not 数字队列不为空
    弹出数字，符号，计算
    放回
"""


from collections import  deque
import numbers
from numbers import Integral
cont_list = re_digit.split(ret[0])
cont_list.remove('')

def cal_mul_div(cont_list):

    digit_deque = deque()
    symbol_deque = deque()
    digit_deque.append(0)
    symbol_deque.append('')
    for chars in cont_list:
        last_symbol = symbol_deque[-1]
        #if last_symbol == '-':
        if last_symbol  in {'*','/'}:
            symbol_deque.pop()
            if last_symbol == '*':
                left_num = float(digit_deque.pop())
                right_num = float(chars)
                num = left_num * right_num
                digit_deque.append(num)
            if last_symbol == '/':
                left_num = float(digit_deque.pop())
                right_num = float(chars)
                num = left_num / right_num
                digit_deque.append(num)
        else:
            if chars not in {'+','-','*','/'}:
                digit_deque.append(chars)
            else:
                symbol_deque.append(chars)

    symbol_deque.popleft()
    digit_deque.popleft()
    return digit_deque,symbol_deque

digit_deque,symbol_deque = cal_mul_div(cont_list)

def cal_add_sub(digit_deque,symbol_deque):
    if len(digit_deque) == len(symbol_deque):
        digit_deque.appendleft(0)
    num = digit_deque.popleft()
    while symbol_deque and digit_deque:
        last_symbol = symbol_deque.popleft()
        if last_symbol == '+':
            left_num = float(num)
            right_num = float(digit_deque.popleft())
            num =  left_num + right_num
        elif last_symbol == '-':
            left_num = float(num)
            right_num = float(digit_deque.popleft())
            num = left_num - right_num
    return num

a = cal_add_sub(digit_deque,symbol_deque)

#65334.15178571428

def merge(cont):
    cont = '(1)-2*((60-30+(-40/5)*(9-2*3+7/8*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
    re_parentheses = re.compile(r'\(([^\(]*?)\)')
    ret = re_parentheses.findall(cont)
    print(ret)
    re_digit = re.compile('(\d+)')
    L = []
    for cont_list in ret:
        cont_list = re_digit.split(cont_list)
        cont_list.remove('')
        digit_deque, symbol_deque = cal_mul_div(cont_list)
        num = cal_add_sub(digit_deque, symbol_deque)
        L.append(str(num))
    ret = re_parentheses.split(cont)
    ret[1::2] = L
    ret = ''.join(ret)



merge(cont)













