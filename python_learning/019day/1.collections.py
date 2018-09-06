#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 1.collections.py
@time: 18-9-5 下午4:42
@desc:
'''

from collections import namedtuple

Person = namedtuple('person',['name','age','sex'])

bob = Person('bob',12,'man')
print(bob.name)
print(bob)
print(type(bob))
# bob
# person(name='bob', age=12, sex='man')
# <class '__main__.person'>

Point = namedtuple('point', ('X', 'Y'))
point = Point(12, 34)
print(point.X)
print(point.Y)
print(point)
# 12
# 34
# point(X=12, Y=34)


# 牌
# 花色和数字
Card = namedtuple('card',['suits','number'])
c1 = Card('红桃',12)
print(c1)
# card(suits='红桃', number=12)

from collections import deque
q = deque([1,2,3,4])
q.pop()
print(q)
q.clear()
print(q)

import queue
q = queue.Queue()
q.put(1)
q.put(3)
q.put(8)
print(q)            # <queue.Queue object at 0x7fc278682e48>
print(q.get())      # 1
print(q.get())      # 1
print(q.get())      # 1
#print(q.get())      阻塞


from queue import PriorityQueue
from collections import OrderedDict

od = OrderedDict([('a',1), ('b',2), ('c',3)])
print(od)

for k in od:
    print (k)
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# a
# b
# c

dit = {'k1': None, 'k2': None}

from collections import defaultdict

values = [1,2,3,4,5,612,34,45,5634,234,234]

dedict = defaultdict(list)
for i in values:
    if i < 60:
        dedict['k1'].append(i)
    else:
        dedict['k2'].append(i)

print(dedict['k1'])
# [1, 2, 3, 4, 5, 34, 45]

d =defaultdict(lambda :5)
print(d['a'])
# 5

from collections import Counter
c = ['a', 'a', 'a', 'b', 'b']
con = Counter(c)
print(con)
# Counter({'a': 3, 'b': 2})