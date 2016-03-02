#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/15
# ---------------------------

__author__ = 'deangao'


'''
条件判断是很基础的。
'''

# ---if格式---
'''
1. 单个if判断，为真则执行<some code>
if <逻辑判断是否为真>:
	<some code>

2. if else对， 为真则执行code1，否则执行code2
if <逻辑判断是否为真>:
	<some code1>
else:
	<some code2>

3. if elif else 多个条件依次判断，符合在执行相应的代码并退出后续判断
if <逻辑判断1是否为真>:
	<some code1>
elif <逻辑判断2是否为真>:
	<some code2>
elif <逻辑判断3是否为真>:
	<some code3>
else:
	<other code>

4. 单行条件判断 即三目操作
z = x if <条件判断为真> else y
为真则将x赋给z，否则将y赋给z

'''

# ---example1---
a = 3
if a > 2:
	print 'a > 2'

# ---example2---
if a > 5:
	print 'a > 5'
else:
	print 'a <= 5'

# ---example3---
score = 77
if score <= 60:
	print '不及格'
elif score <= 80:
	print '良好'
elif score <= 90:
	print '优先'
elif score == 100:
	print '满分'
else:
	print '分数大于100'

# ---example4---
x = 12
y = 23
z = x if x > y else y
print 'max of x and y is', z
