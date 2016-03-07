#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/25
# ---------------------------

__author__ = 'deangao'

# TODO: try except finaly

'''
在设计程序时要考虑到可能发生的异常，并进行捕获，
正确的处理异常以避免应为异常导致程序的崩溃，提高程序的鲁棒性。
python中使用的是try except语法。
Python中定义了各种异常，比如常见的类型不匹配、键不存在等。
'''

'''
exception语法
try:
	<some code>
exception (<some exception type1>, <some exception type2>)
	<deal with exception>
else:
	<some code>
finally:
	<some code>

或者try下面带多个exception
exception <type1>, e1
这里的e为异常的实例，可以被异常处理代码使用

try:
	<some code>
exception <type1> as e1:
	<deal with type1>
exception <type2> as e2:
	<deal with type2>
'''


# ---example1---
def my_abs(num):
	try:
		num = float(num)
	except ValueError, e:
		print 'Error is', e
	return num

my_abs('sdfd')
# 此处如果没有异常处理则会直接报错退出， 代码不健壮。
# Error is could not convert string to float: sdfd

print type(my_abs(-12))
print type(my_abs('-12'))


# ---example2---
# else 表示在列举的error之外的处理
# finally 表示最终都一定会执行的代码
try:
	float('aaa')
except ValueError as e:
	print 'ValueError', e
except TypeError as e:
	print 'TypeError', e
else:
	print 'No Error detected'
finally:
	print 'Finally print'

# ---输出---
'''
ValueError could not convert string to float: aaa
Finally print
'''

# ---example3---
try:
	float('12.3')
except ValueError as e:
	print 'ValueError', e
except TypeError as e:
	print 'TypeError', e
else:
	print 'No Error detected'
finally:
	print 'Finally print'

# ---输出---
'''
No Error detected
Finally print
'''