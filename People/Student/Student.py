#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/3/15
# ---------------------------

# 从People包下面的People模块导入其中的CommPeople类
from People.People import CommPeople

__author__ = 'deangao'

class Student(CommPeople):
	"""
	Student类
	"""

	def __init__(self, name, sex, age):
		self.__name = name
		self.__sex = sex
		self.__age = age
		self.__occupation = 'Student'

	def printStudent(self):
		print 'Name is:', self.__name
		print 'Age is:', self.__name
		print 'Sex is:', self.__sex
		print 'Occupation is:', self.__occupation

