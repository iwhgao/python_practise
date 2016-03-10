#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------

__author__ = 'deangao'

'''
Python中同样是支持面向对象编程的（Object Oriented Programming）。
'''


# 定义一个人物类
class People(object):
	# 此处定义的类的属性
	name = ''
	sex = ''
	age = 0
	count = 0

	def __init__(self, name, sex, age):
		# 类似this指针
		self.name, self.sex, self.age = name, sex, age
		# 此处定义实例的属性
		self.instancee_attr = 'Test'

	# 公有成员函数
	def peoplePrint(self):
		print 'Name is', name
		print 'Sex is', sex
		print 'Age is', age


name = 'who'
sex = 'm'
age = 23

# 类实例化
one_people = People(name, sex, age)

# 调用成员函数
one_people.peoplePrint()

# 实例对象调用对象的成员变量
print one_people.name
one_people.name = 'am'
print one_people.name

print People.name
print People.count

two_people = People(name, sex, age)
print People.name
print two_people.name

# print People.obj_attr

# People.peoplePrint()
