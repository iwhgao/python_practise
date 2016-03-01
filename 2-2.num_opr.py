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
这里介绍下常见的数字操作
'''

x = 10
y = 10.3
z = 1 + 10j

# ---基本操作符---
# ---加法---
print 'x + y is', x + y
print 'x + z is', x + z
x += 2
# x = x + 2
print x

# ---减法---
print 'x - y is', x - y

# ---Python中没有++ 或者--

# ---乘法---
print 'x * y is', x * y

# ---除法---
print 'x / y is', x / y
print 'x // y is', x // y
print 'int(x / y) is', int(x / y)

try:
	x / 0
except ZeroDivisionError as e:
	print 'Error is', e.message

# ---幂---
print x ** 2, y ** 2

# ---类型转换---
print float(x), int(y), long(x), complex(y)
print float('inf'), float('-inf'), float('nan')

# ---常用数学函数---


import math

'''
 pow
fsum
cosh
ldexp
hypot
acosh
tan
asin
isnan
log
fabs
floor
atanh
modf
sqrt
frexp
degrees
lgamma
log10
asinh
fmod
atan
factorial
copysign
expm1
ceil
isinf
sinh
trunc
cos
pi 3.141592653589793
e 2.718281828459045
tanh
radians
sin
atan2
erf
erfc
exp
acos
log1p
gamma
'''

print math.pi, math.e
print max(x, y)
print min(x, y)
# --sum接收序列---
print sum((x, y))
print sum([x, y])