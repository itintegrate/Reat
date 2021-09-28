# -*- coding: utf-8 -*-
# @Author: jinpengwu
# @Date:   2019-10-31 21:19:13
# @Last Modified by:   jinpengwu
# @Last Modified time: 2019-10-31 23:33:26
# python 所以的类都是type生产的 同时 所以的类都继承了object 也包括type

a = 1 
b = "abc"
print(type(a))
#<class 'int'>

print(type(int))
#<class 'type'>


class Student():
  pass

stu = Student()

print(type(Student))
#<class 'type'>

print(type(stu))
#<class '__main__.Student'>

print(Student.__bases__)
#(<class 'object'>,)


class Student_extend(Student):
  pass

print(type(Student_extend))
#<class 'type'>

print(Student_extend.__bases__)
#(<class '__main__.Student'>,)

print(type(object))
#<class 'type'>

print(object.__bases__)
#()

print(type(type))
#<class 'type'>

print(type.__bases__)
#<class 'object'>,)
print()