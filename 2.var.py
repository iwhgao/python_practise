#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------

__author__ = 'deangao'


# ---变量名---
# ---和其它语言的变量名命名规则类似---
# 一般是下划线或英文字符开头，且名称是大小写敏感的
A = 5
a = 4
_09 = 12

# 09A = 34  错误的变量名命名方法

print 'A is:', A
print 'a is:', a
print '_09 is:', _09

# ---常量---
# python中没有像C那样使用宏来定义常量的，通常是习惯性的用大写表示常量
PI = 3
PI = 4

print PI

# ---常见数据类型---
# ---数字---
# 整型
num1 = 12

# 浮点数
num2 = 12.0

# 长整型
num3 = 12L

# 复数
num4 = 1 + 2j

print type(num1), type(num2), type(num3), type(num4)

# ---字符串---
# --- 单引号， 双号都行， 三个单引号就是可以
str1 = 'A'
str2 = 'AA'
str3 = "A"
str4 = "AA" \
	   "A"
str5 = '''abc
	123'''

str6 = ''
print str1, str2, str3, str4, str5, str6
print 'END'

# ---布尔值---
# --- 特定的单词 True ，False， 注意大小写---
bool1 = True
bool2 = False
# bool3 = true  错误

print bool1, bool2

# ---数组（或列表）---
# [] 定义，可以表示不同类型的基础变量
array1 = [1, 3, 'a']
array2 = [1, 3, [1, 3]]
array3 = []

print array1
print array2
print array3

# ---集合---
# ---set函数接收一个数组， 数组中可以存储不同数据类型---
set1 = set([1, 2, 3, 3])
set2 = set([1, '1'])

print set1, set2

# ---元组---
# () 定义，可以表示不同类型的基础变量
tuple1 = (1, 3)
tuple2 = (1, 3, ('a', 5))
tuple3 = (1, 3, [3, 4, 5])
tuple4 = ()

print tuple1, tuple2, tuple3, tuple4

# ---字典（或hash数组或关联数组）---
# {} 定义，key-value形式来存储, value可以是不同类型的变量

dict1 = {'name': 'deangao', 'age': 27}
name = 'name'
dict2 = {name: 'deangao', 'age': 27}
dict3 = {name: 'deangao', 'address': ['sz', 'wh']}
dict4 = {}

print dict1, dict2, dict3, dict4

# ---空值---
# ---None---表示空值 好比NULL
# ---None不能理解为0 及''等， 应为0和''是有意义的
A = None

print A

# ---真假---
'''
类型		True			False
字符串	任意非空字符串	空的字符串 ''
数字		任意非0数字		数字0
容器		任意非空容器		空的容器 [] () {} set()
其它		其它任意非False	None
'''
