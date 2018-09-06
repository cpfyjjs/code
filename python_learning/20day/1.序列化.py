#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 1.序列化.py
@time: 18-9-6 下午4:32
@desc:
'''

import json

# 可以序列化： 数字、字符窜、字典、元组
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}

# json dumps 序列化方法， loads 反序列化方法

# 序列化
str_dic = json.dumps(dic)
print(type(dic), dic)
print(type(str_dic), str_dic)
# <class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
# <class 'str'> {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4"}

# 反序列化
new_dic = json.loads(str_dic)
print(type(new_dic), new_dic)
# <class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}

dic = (1, 2, 3, 4)
str_dic= json.dumps(dic)
print(type(dic), dic)
print(type(str_dic), str_dic)
new_dic = json.loads(str_dic)
print(type(new_dic), new_dic)
# <class 'tuple'> (1, 2, 3, 4)
# <class 'str'> [1, 2, 3, 4]
# <class 'list'> [1, 2, 3, 4]


# json dump load 是与文件相关的
dic = {'k1': '中文', 'k2': '英文', 'k3': '日语', 'k4': '韩语'}
f = open('json','w')
json.dump(dic,f,ensure_ascii=False)
f.close()

f = open('json','r')
res = json.load(f)
print(type(res),res)
f.close()

# dump,load 只能一次性写，一次性读

# json
# dumps {} --> '{}\n'
# 一行一行的读
# ’{}\n'
# '{}' loads

l = [{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'},{'k1': '中文', 'k2': '英文'},
     {'k1': 'v1', 'k2': 'v2'}, {'k1': '中文', 'k2': '英文', 'k3': '日语', 'k4': '韩语'}]

f = open('json','w')
for line in l:
    js = json.dumps(line) + '\n'
    f.write(js)
f.close()

f = open('json','r')
ll = []
for line in f:
    dic = json.loads(line)
    ll.append(dic)
print(ll)
f.close()



# Pickle 二进制文件      可以分步的dump,load
# 文件打开形式需要加 'b'
# dumps, loads, dump, load

import shelve

# shelve








