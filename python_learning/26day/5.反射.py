#!/home/cpf/anaconda3/bin
# encoding: utf-8
'''
@software: pycharm
@file: 5.反射.py
@time: 18-9-7 下午3:07
@desc:
'''

# 反射

from abc import abstractmethod,ABCMeta

class Teacher:
    dic = {'查看学生信息':'show_student','查看讲师信息':'show_teacher'}

    def show_student(self):
        print('show student')

    def show_teacher(self):
        print('show teacher')

# hasattr   getattr     delattr     setattr

ret = getattr(Teacher,'dic')
print(ret)
# {'查看学生信息': '', '查看讲师信息': ''}

alex = Teacher()
fun = getattr(alex,'show_student')
fun()
# show student

if hasattr(Teacher,'show_teac'):
    print('show_teac')
else:
    alex = Teacher()
    fun = getattr(alex, 'show_teacher')
    fun()

alex = Teacher()
key = input('输入需求： ')
func = getattr(alex,Teacher.dic[key])
func()

