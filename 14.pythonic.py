#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/1
# ---------------------------

import time

__author__ = 'deangao'


# 1.
# pythonic
a = 2
b = 3
a, b = b, a

print a, b

# non-pythonic
print a, b
temp = a
a = b
b = temp

print a, b

# 2.
# pythonic
print 1 <= b <= a < 10

# non-pythonic
print 1 <= b and b <= a and a < 10

# 3.
# pythonic
'''
True			False
任意非空字符串	空的字符串 ''
任意非0数字		数字0
任意非空容器		空的容器 [] () {} set()
其他任意非False	None
'''

name = 'Tim'
langs = ['AS3', 'Lua', 'C']
info = {'name': 'Tim', 'sex': 'Male', 'age': 23}

if name and langs and info:
	print "All true"

# nonn-pythonic
if name != '' and len(langs) > 0 and info != {}:
	print "All true"

if name != '' and langs != [] and info != {}:
	print "All true"


# 4.
# pythonic

def reverse_str(s):
	return s[::-1]


# non-pythonic
def reverse_str1(s):
	output = ''
	for t in range(len(s) - 1, -1, -1):
		output = output + s[t]
	return output


print reverse_str('abccaa')
print reverse_str1('abccaa')

print 'aabbaa' == reverse_str('aabbaa')


# 5.
# pythonic

arr = ['a', 'b', 'c']
print '\t'.join(arr)

# non-pythonic
arr_combined = ''
for tmp in arr:
	arr_combined = arr_combined + tmp + '\t'
print arr_combined.strip('\t')

'''
# 6.
# pythonic
print(max(arr))
print(sum(map(lambda x: ord(x), arr)))

# arr = [1, 2, 3, 4]
arr = range(1, 100000000)

print "Start at " + str(time.time())
print max(arr), min(arr), sum(arr)
print "End at " + str(time.time())

# non-pythonic
max_of_arr = -float('inf')
min_of_arr = float('inf')
sum_of_arr = 0

print "Start at " + str(time.time())
for tmp in arr:
	if tmp > max_of_arr:
		max_of_arr = tmp

	if tmp < min_of_arr:
		min_of_arr = tmp

	sum_of_arr += tmp

print max_of_arr, min_of_arr, sum_of_arr
print "End at " + str(time.time())

'''

# 7.
# pythonic
arr = range(1, 10000000)
print "Start at " + str(time.time())
var = [x * x for x in arr if x % 2 == 0]
print "End at " + str(time.time())

# non-pythonic

print "Start at " + str(time.time())
res = []
for x in arr:
	if x % 2 == 0:
		res.append(x * x)
print "End at " + str(time.time())


# 8.
# pythonic
a = 3
b = a if a > 3 else 1
print b

# non-pythonic

b = 0
if a > 3:
	b = a
else:
	b = 1
print b

# 9.
# pythonic
arr = [1, 3, 4, 5]
for i, v in enumerate(arr):
	print i, v

# non-pythonic

for x in range(0, len(arr)):
	print x, arr[x]


# 10.
# pythonic
keys = ['a', 'b', 'c']
values = [1, 2, 3]
mydict1 = dict(zip(keys, values))
print(mydict1)

# non-pythonic
mydict2 = {}
for x in range(0, len(keys)):
	mydict2[keys[x]] = values[x]
print(mydict2)
