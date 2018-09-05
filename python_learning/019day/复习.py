#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 复习.py
@time: 18-9-5 下午4:12
@desc:
'''

"""
元字符
\w \d \s
\W \D \S
. 除换行符以外的任意字符
\n \t
\b 
^ $ 匹配字符串开始和结束
（） 分组       是对多个字符组整体量词约束的时候用的
              分组是优先的
              findall
              split

| 两着取一个，从左到右匹配，只要匹配上了，就不继续匹配了。所以应该把长的放前面‘
[^] 除了字符组内的其他都匹配

量词
×
+
？
{n}
{n,}
{n,m}  if only n < m

"""

import re
ret = re.findall(r'\\w',r'\wwww')
print(ret)
# ['\\w']

ret = re.findall(r'\w',r'\wwww')
print(ret)
# ['w', 'w', 'w', 'w']

ret = re.findall('\\w',r'\wwww')
print(ret)
# ['w', 'w', 'w', 'w']

# 多行匹配
# 量词后面加问号
# 。×？abc 一直取直到遇到abc

# findall match sub split
# compile

# match 从头匹配
# search 任意位置匹配
# finditer  返回迭代器
# compile 编译
ret = re.search('\d+(?P<name>[a-z]+)','asdfa23edfas23fdasdf')
print(ret.group('name'))
# edfas












