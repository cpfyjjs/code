#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 2.time.py
@time: 18-9-6 上午10:36
@desc:
'''

import time

"""
%y     两位数的年份表示（00-99）
%Y     四位数的年份表示（0000-9999）
%m     月份（01-12）
%d     月中的一天（0-31）
%H     24小时制小时数（0-23）
%I     12小时制小时数（0-11）
%M     分钟数（0-55）
%S     秒（00-59）
%a     本地简化星期名称
%A     本地完整星期名称
%b     本地简化月份名称
%B     本地完整月份名称
%c     本地相应的日期表示和时间表示
%j     年内的一天（001-366）
%p     本地A.M.或P.M.的等价符
%U     一年中的星期数（00-53）星期天为星期的开始
%w     星期（0-6），星期天为星期的开始
%W     一年中的星期数（00-53）星期一为星期的开始
%x     本地相应的日期表示
%X     本地相应的时间表示
%Z     当前时区的名称
%%     %号本身


"""
time.sleep(0.001)
now = time.time()
print(now)
# 1536201459.4352944

# 格式化时间 -- 字符串时间 ： 给人看的
# 时间戳时间 -- float时间 ： 给计算机看的
# 结构化时间 -- 元祖 ： 计算用的

now = time.strftime('%Y-%m-%d %X')
print(now)
# 2018-09-06 10:46:30

# year month day HOUR MINUTE SECOND
now = time.strftime('%Y-%m-%d %H:%M:%S')
print(now)
# 2018-09-06 10:47:57

now = time.strftime('%Y-%m-%d %H:%M')
print(now)
# 2018-09-06 10:48

print(time.localtime())
#time.struct_time(tm_year=2018, tm_mon=9, tm_mday=6, tm_hour=10, tm_min=52, tm_sec=41, tm_wday=3, tm_yday=249, tm_isdst=0)

struct_time = time.localtime()
print(struct_time.tm_year)
# 2018

# 时间戳和结构化时间的转换

t = time.time()
print(t)
print(time.localtime(t))
print(time.gmtime(t))

# 1536202920.9682267
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=6, tm_hour=11, tm_min=2, tm_sec=0, tm_wday=3, tm_yday=249, tm_isdst=0)
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=6, tm_hour=3, tm_min=2, tm_sec=0, tm_wday=3, tm_yday=249, tm_isdst=0)

print(time.localtime(1500000000))
# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=10, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)

t = time.localtime(t)
print(time.mktime(t))
# 1536203129.0

# 结构化时间和字符串时间相互转换
now = time.strftime('%Y-%m-%d %H:%M:%S')
print(now)
# 2018-09-06 10:47:57
print(time.strptime(now,'%Y-%m-%d %H:%M:%S'))
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=6, tm_hour=11, tm_min=7, tm_sec=37, tm_wday=3, tm_yday=249, tm_isdst=-1)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1500000000)))
# 2017-07-14 10:40:00

print(time.asctime())
# Thu Sep  6 11:18:26 2018
print(time.asctime(time.localtime(1500000000)))
# Fri Jul 14 10:40:00 2017

print(time.ctime(1500000000))
# Fri Jul 14 10:40:00 2017