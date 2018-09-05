#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 1.内置函数.py
@time: 18-9-4 下午7:40
@desc:
'''
"""
print()
input()
len()
type()
open()
tuple()
list()
int()
bool()
set()
dir()       查看一个变量所拥有的方法
id()
str()
dict()
enumerate()
"""
a = 1
b = 2
def fun():
    c = 1
    d = 3
    print(locals())         #返回本地作用域的所有名字
    print(globals())        #返回全局作用域中的所有名字
fun()

"""
{'d': 3, 'c': 1}
{'__name__': '__main__', '__doc__': '\n@author: cpf\n@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.\n@contact: 756206487@qq.com\n@software: pycharm\n@file: 1.内置函数.py\n@time: 18-9-4 下午7:40\n@desc:\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f56e8b9acf8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/cpf/code/python_learning/015day/1.内置函数.py', '__cached__': None, 'a': 1, 'b': 2, 'fun': <function fun at 0x7f56e8bcaea0>}
"""


print(hash('123'))
print(id('123'))

# end 结束符
print('1234',end = "#######")
print(123)          #1234#######123
# sep 分隔符
print(12,4,4,5,6,76,sep = "|")      #12|4|4|5|6|76


f = open('file','w')
print("aaaa",file = f)
f.close()

print(eval('1+2+3+4'))
print(eval('fun()'))
print(exec('1+2+3+4'))

# eval exec 都可以执行字符串代码
# eval 有返回值
# exec 没有返回值        适合于流程控制
# single 交互
# eval 只能用在你明确知道执行的代码的运行结果。

#compilel   将字符串类型的代码编译。代码对象能都通过 exec 语句执行

print(help(compile))

a = complex(12,3)
print(a)
print(a.imag)
print(a.real)

print(divmod(23,5))     #(4,3)

print('你好'.encode('utf8'))
print(b'ser34')

b_array = bytearray('你好','utf8')
print(b_array)
print(b_array[0])


memoryview()








