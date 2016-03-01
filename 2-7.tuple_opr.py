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
由于元组和数组是类似的，只是其内容不能被修改，所以其操作是有限的
'''

tuple1 = (1, 2, 3, 4)
tuple2 = (2, 3, 4)
tuple3 = (1,)
tuple4 = (1) # 这个是不对的，其不会被定义为元组而是单个数组

print type(tuple3)
print type(tuple4)

# ---取长度 len---
print 'Length of tuple1 is', len(tuple1)

# ---取最大值 max---
print 'Max if tuple1 is', max(tuple1)

# ---取最小值 min---
print 'Min if tuple1 is', min(tuple1)

# ---挨个元素比较 cmp---
print cmp(tuple1, tuple2)

# ---列表或集合转tuple---  即序列
print 'List to tuple', tuple([1, 3, 4, 5])
print 'Set to tuple', tuple(set((1, 3, 4, 5)))

# ---tuple的更新---
print 'tuple1 + tuple2 is', tuple1 + tuple2

# 非法操作
# tuple[0] = 2 不能修改

# ----也不是完全不能修改-----
tuple_tmp = (1, 2, ['a', 'b'])
print id(tuple_tmp[0])
print id(tuple_tmp[1])

print '改之前', tuple_tmp
tuple_tmp[2][0] = 'b'
print '改之后', tuple_tmp
# tuple_tmp[2] = 'a' 错误
tuple_tmp[2].append('c')
print '改之后', tuple_tmp

# ---这是为什么呢？---
'''
元组的一级元素是不能修改的， 像 1 2 ['a', 'b']就是不能修改的，
对于['a', 'b']来说这个数组你不能将它修改为数字、字符串等，但是你可以对其元素进行修改。

简单来说就是不能改变元组一级元素的地址
'''