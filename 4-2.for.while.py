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
循环可用于重复操作的控制，列表及字典等的遍历。
Python提供常见的两种循环语句，for及while。
'''

# ---for---
'''
for iter in <seq>:
	<some code>
'''

list1 = [1, 3, 4, 5]
# 只遍历值
for tmp in list1:
	print tmp

# 遍历下标和值 以序列（元组或者列表）的形式返回
for [ind, val] in enumerate(list1):
	print 'Data at {0} is {1}'.format(ind, val)

print '-------------------'
for (ind, val) in enumerate(list1):
	print 'Data at {0} is {1}'.format(ind, val)

print '-------------------'
# range(start, end, step) 函数, 一个参数时表示0至参数-1的列表
print range(1, 10, 1)
print range(len(list1))

for i in range(len(list1)):
	print 'Data at {0} is {1}'.format(i, list1[i])

# ---计算整个班级分数在[80, 90]间的平均分---
score = [56, 66, 78, 89, 43, 55, 67, 85, 94, 23, 45]

avg_score = 0
sum_score = 0
cnt = 0

for s in score:
	# 此处可以有简单的写法，或者说更加pythonic的写法 80 <= s <= 90
	if s >= 80 and s <= 90:
		sum_score += s
		cnt += 1
	else:
		print 'Score {0} is not in [80, 90]'.format(s)

print 'avg score is {0}'.format(float(sum_score)/cnt)


# ---while---
'''
while 是另一种循环，更多的是根据逻辑判断的变化来进行循环，
而不像for那样是有具体的对象可以枚举，所以while可用于更加复杂的逻辑。
'''

# while 格式
'''
while <逻辑判断为真>:
	<some code>

当逻辑判断为真时就继续下一步循环
'''

# ---求和---
i = 0
sum_score = 0
while i < len(score):
	sum_score += score[i]
	i += 1

print sum_score

# ---无限循环---
'''
while True:
	print 'Something'
'''
