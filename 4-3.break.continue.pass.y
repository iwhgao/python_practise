#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/24
# ---------------------------

__author__ = 'deangao'

'''
break、continue和pass用于逻辑控制：
break: 意思是终止循环
continue: 用于停止当前循环不执行后面的代码直接跳到下一个循环
pass: 不做任何处理, 可以用来定义一些要实现的函数。

'''

list1 = [12, 34, 45, 56, 54, 56, 177, 435]
# 寻找list1中的第一个大于100的元素并打印出来,将在出现该元素之前的元素进行打印
# ---break---
for tmp in list1:
	if tmp > 100:
		print 'Element is {0} > 100'.format(tmp)
		break
	else:
		print 'Element is {0}'.format(tmp)

i = 0
len_list1 = len(list1)
while i <= len_list1 - 1:
	if list1[i] > 100:
		print 'Element is {0} > 100'.format(list1[i])
		break
	else:
		print 'Element is {0}'.format(list1[i])
	i += 1

# 只打印list1中小于等于100的元素
# 当遇到大于100的元素时就不执行下面的print语句了，直接跳到下一个循环再进行判断
# ---continue---
for tmp in list1:
	if tmp > 100:
		continue
	print 'Element is {0}'.format(tmp)

# ---pass---
if len(list1) < 10:
	print 'Length of list1 is less than 10'
	pass

print 'End'
