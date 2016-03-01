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
数组的增删改等操作
'''

array1 = [1, 2, 3, 'a']
array2 = [2, 4, 4, [1, 2, 3]]

print 'Length of array1 is {0}'.format(len(array1))
print 'Length of array2 is {0}'.format(len(array2))

print array1
print array2

# ---增加若干元素---
# ---单个单个的添加---
# print id(array1)
# 在原来的基础上进行添加， 在内存中的地址没变
array1.append(10)
# print id(array1)

print 'Length of array1 is {0}'.format(len(array1))
print array1

# ---多个添加---
# print id(array1)
# 在新的地方构建组合的数组，再赋给array1，在内存中的位置变了
array1 = array1 + array2
# print id(array1)

print 'Length of array1 is {0}'.format(len(array1))
print array1

# ---减少元素---
del array1[0]
print array1

# ---列表解析----
# ---列表解析----
# ---列表解析----

# ---重要事情说三遍---
# ---通过在列表中的单行操作 生产新的列表---
new_array1 = [str(x) + str('new') for x in array1]
print new_array1

# ---内置函数举例---
# 1. cmp 两个数组对应位置的元素进行比较
# -1 左表的小， 0 完成相等， 1 右边的小
print cmp(array1, array2)

# 2. max 最大值(都为字符串时按照ASCII码比较)
print max(array1)

# 3. min 最小值(都为字符串时按照ASCII码比较)
print min(array1)

# 4. list 元组转化为列表操作
print list((1, 2, 3))
print type(list((1, 2, 3)))

# 5. sorted 排序
print array1
array1_tmp = sorted(array1)
print array1_tmp
print array1


# ---数组自带方法举例---
# 1. 某个元素的数量
print array1
print array1.count('a')
print array1.count(1)
print array1.count([1, 2, 3])

# 2. 某个元素第一次出现的位置
# 不在列表（数组）中则报错
print array1.index(2)
print array1.index([1, 2, 3])

# 3. 在某个位置插入新元素
# 第一个参数：下标， 第二个参数元素
array1.insert(2, '1')
print array1

# 4. pop操作
# 无参数则删除最后一个并返回，有参数则删除指定位置的元素并返回
pop_tmp = array1.pop(2)
print pop_tmp
print array1

pop_tmp = array1.pop()
print pop_tmp
print array1

# 5. remove 直接删除元素
print array1
array1.remove(2)
print array1

# 6. reverse 反转
print array1
array1.reverse()
print array1

# 7. sort 排序
print array1
array1.sort()
print array1

# 总结
# 内置函数对数组（列表）的操作一般是不会改变数组（列表）本身的
# 数组（列表）的方法对其自身操作是会改变的