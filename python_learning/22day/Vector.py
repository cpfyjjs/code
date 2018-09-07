#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: Vector.py
@time: 18-9-7 下午3:36
@desc:
'''

from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools

class Vector:
    typecode = 'd'


    def __init__(self, components):
        self._conponents =array(self.typecode,components)

    def __iter__(self):
        return iter(self._conponents)

    def __repr__(self):
        components = reprlib.repr(self._conponents)
        pass

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._conponents))

    def __eq__(self, other):
        return (len(self) == len(other)) and all(a == b for a, b in zip(self,other))

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor,hashes,0)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._conponents)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item,slice):
            return cls(self._conponents[slice])
        elif isinstance(item,numbers.Integral):
            return self._conponents[item]
        else:
            msg = '{.__name__} indices must be integers'
            raise TypeError(msg.format(cls))

    shortcut_name = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_name.find(name)
            return self._conponents[pos]
        else:
            msg = '{.__name__!r} object has no attribute {!r}'
            raise AttributeError(msg.format(cls,name))

    def angle(self,n):
        pass










a = array('d',[1,2,3,4])
print(a)
print(type(a))
# array('d', [1.0, 2.0, 3.0, 4.0])
# <class 'array.array'>

a = reprlib.repr(a)
print(a)
print(type(a))
# array('d', [1.0, 2.0, 3.0, 4.0])
# <class 'str'>