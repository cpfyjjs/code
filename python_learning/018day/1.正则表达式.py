#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 1.正则表达式.py
@time: 18-9-5 上午9:59
@desc:
'''
"""
findall
match
"""



import re

ret = re.findall('a','asdf asdg fsdg')
print(ret)
#['a', 'a']

ret = re.findall('[a-z]+','dfadf dafa asdfaf sadf')
print(ret)
#['dfadf', 'dafa', 'asdfaf', 'sadf']

ret = re.search('[a-z]+','dfadf dafa asdfaf sadf')
print(ret)
# <_sre.SRE_Match object; span=(0, 5), match='dfadf'>

print(ret.group())
#dfadf
# 从前往后，找到一个就返回，返回的变量要调用group 才能拿到结果
# 如果没有找到，那么返回None，调用group 就会报错

ret = re.match('[a-z]+','1dfadf dafa asdfaf sadf')
print(ret)
# None

ret = re.match('[a-z]+','dfadf dafa asdfaf sadf')
print(ret)
# <_sre.SRE_Match object; span=(0, 5), match='dfadf'>

# match 是从头开始匹配，如果正则表达式从头开始匹配上，就返回结果

ret = re.split('ad','dfadf dafa asdfaf sadf')
print(ret)
# ['df', 'f dafa asdfaf s', 'f']

ret = re.split('[ad]','dfadf dafa asdfaf sadf')
# 利用a,d进行分割
print(ret)
#['', 'f', '', 'f ', '', 'f', ' ', 's', 'f', 'f s', '', 'f']


ret = re.sub('ad','','dfadf dafa asdfaf sadf')
print(ret)
# dff dafa asdfaf sf

ret = re.sub('ad','*******','dfadf dafa asdfaf sadf')
print(ret)
# df*******f dafa asdfaf s*******f

ret = re.subn('ad','*******','dfadf dafa asdfaf sadf')
print(ret)
# ('df*******f dafa asdfaf s*******f', 2)

ret = re.subn('ad','*******','dfadf dafa asdfaf sadf',1)
print(ret)
# ('df*******f dafa asdfaf sadf', 1)

obj = re.compile('\d{3}')
ret = obj.findall('adfad234afdfdf345ddsfa124')
print(ret)
# ['234', '345', '124']

ret = re.finditer('\d','asdf123adf456fdsf876')
print(ret)
print(next(ret).group())
# <callable_iterator object at 0x7fb4eb176748>
# 1

ret = re.findall('www.(baidu|oldboy).com','www.oldboy.com')
# 这里 findall 会优先把匹配结果组里内容返回。
print(ret)
# ['oldboy']

ret = re.findall('www.(?:baidu|oldboy).com','www.oldboy.com')
# ？： 取消分组优先
print(ret)
# ['www.oldboy.com']

ret = re.split('\d*','adfad234afdfdf345ddsfa124')
print(ret)
#['adfad', 'afdfdf', 'ddsfa', '']

ret = re.split('(\d*)','adfad234afdfdf345ddsfa124')
print(ret)
#['adfad', '234', 'afdfdf', '345', 'ddsfa', '124', '']





