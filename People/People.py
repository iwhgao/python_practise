#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/3/15
# ---------------------------

__author__ = 'deangao'


class CommPeople(object):
	"""
	人的一个基类
	"""

	def __init__(self, name, sex):
		self.name = name
		self.sex = sex

	def print_people(self):
		print 'Name is:', self.name
		print 'Sex is:', self.sex
