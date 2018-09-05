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

"""
输入一串字符串，根据数学运算规则进行数学运算，最后输出运算结果
这个版本有点小问题
"""

import re
from collections import  deque


cont = '(1)-2*((60-30+(-40/5)*(9-2*3+7/8*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'


def cal_mul_div(cont_list):
    """
    根据数学运算规则，有限运算乘除法
    :param cont_list: cont_list
        for example :['9', '-', '2', '*', '3', '+', '7', '/', '8', '*', '99', '/', '4', '*', '2998', '+', '10', '*', '568', '/', '14', '']
    :return: digit_deque,symbol_deque
    """
    digit_deque = deque()
    symbol_deque = deque()
    digit_deque.append(0)
    symbol_deque.append('')
    # 便利列表中的字符
    for chars in cont_list:
        last_symbol = symbol_deque[-1]
        # 判断是否有双字符
        if chars in {'+-','--','*-','/-'}:
            if chars == '+-':
                symbol_deque.append('-')
            elif chars == '--':
                symbol_deque.append('+')
            elif chars == '*-' or chars == '/-':
                last_symbol = symbol_deque.pop()
                # 更改前一个字符的
                if last_symbol == '+' and last_symbol == '':
                    symbol_deque.append('-')
                    symbol_deque.append(chars[0])
                    last_symbol = chars[0]
                elif last_symbol == '-' :
                    symbol_deque.append('+')
                    symbol_deque.append(chars[0])
                    last_symbol = chars[0]

        #运算乘除法
        elif last_symbol  in {'*','/'}:
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
        elif chars not in {'+-','--','*-','/-'}:
            if chars not in {'+','-','*','/'}:
                digit_deque.append(chars)
            else:
                symbol_deque.append(chars)

    symbol_deque.popleft()
    digit_deque.popleft()
    return digit_deque,symbol_deque



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



#65334.15178571428

def merge(cont):

    re_parentheses = re.compile(r'\(([^\(]*?)\)')
    re_digit = re.compile('(\d+\.\d+|\d+)')
    ret = re_parentheses.findall(cont)
    if ret :
        L = []

        for cont_list in ret:
            cont_list = re_digit.split(cont_list)
            cont_list.remove('')
            print(cont_list)
            digit_deque, symbol_deque = cal_mul_div(cont_list)
            num = cal_add_sub(digit_deque, symbol_deque)
            L.append(str(num))
        ret = re_parentheses.split(cont)
        ret[1::2] = L
        ret = ''.join(ret)
        return ret
    else:
        cont_list = re_digit.split(cont)
        cont_list.remove('')
        digit_deque, symbol_deque = cal_mul_div(cont_list)
        num = cal_add_sub(digit_deque, symbol_deque)
        return num

#cont = '60-30+-8.0*65334.15178571428'
#-522643.21428571426

"""
if __name__ == '__main__':
    while not issubclass(type(cont),float):
        cont = merge(cont)
        print(cont)
"""

cont = merge(cont)
print(cont)
cont = merge(cont)
print(cont)
cont = merge(cont)
print(cont)
cont = merge(cont)
print(cont)