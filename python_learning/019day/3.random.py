#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 3.random.py
@time: 18-9-6 上午11:57
@desc:
'''

import random

random.random()

random.uniform(1,3)

random.randint(1,5)

random.randrange(1,10,2)    #大于等于1,且小于10的奇数

random.choice([1,2,3,4,5,6])

random.sample([1,2,3,4,5,6],2)

item = [1,2,3,4,5,6]
random.shuffle(item)

