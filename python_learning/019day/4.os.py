#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 4.os.py
@time: 18-9-6 下午12:07
@desc:
'''

import os

# os 模块是与操作系统相关的模块

os.makedirs('dirname1/dirname2')
os.removedirs('dirname1/dirname2')
os.mkdir('dirname1')
os.rmdir('dirname1')
l = os.listdir('/home/cpf/code/python_learning/019day/')
print(l)
# ['3.random.py', '4.os.py', '2.time.py', '5.sys.py', '复习.py', '1.collections.py']

# os.remove()       删除一个文件
# os.rename()       重命名一个文件
stat = os.stat('4.os.py')       # 获取文件/目录信息
print(stat)
# os.stat_result(st_mode=33204, st_ino=6691934, st_dev=2050, st_nlink=1, st_uid=1000, st_gid=1000, st_size=559, st_atime=1536220608, st_mtime=1536220608, st_ctime=1536220608)

stat = os.getcwd()     # 获取当前脚本的工作目录，即当前Python脚本的工作目录
print(stat)

import os.path

"""
os.path.abspath(path)   返回path规范化的绝对路径
os.path.split(path)     将path分割成目录和文件名二元组返回 
os.path.dirname(path)   返回path的目录。其实就是os.path.split(path)的第一个元素 
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)    如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)     如果path是绝对路径，返回True
os.path.isfile(path)    如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)     如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
os.path.getsize(path)   返回path的大小

stat 结构:

st_mode: inode 保护模式
st_ino: inode 节点号。
st_dev: inode 驻留的设备。
st_nlink: inode 的链接数。
st_uid: 所有者的用户ID。
st_gid: 所有者的组ID。
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
st_atime: 上次访问的时间。
st_mtime: 最后一次修改的时间。
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
"""

