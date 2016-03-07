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
函数可以简化代码，提高代码的复用率；
先定义后调用
'''

'''
Python中函数的基本格式

def func_name(parm1, parm2=value, *parm3, **parm4):
	<some code>

其中的parm为参数名，可以赋予缺省值，
可以传递变长列表， 也可以传递变长字典。

下面一一介绍
'''

# ---example1 空函数---
def my_print1():
	pass

# 调用该函数
my_print1()

# ---example2 无参函数---
def my_print2():
	print 'This is an empty function without parm'

# 调用该函数
my_print2()


# ---example3 有参无缺省函数---
def my_print3(toprint):
	# 此处不限制参数的数据类型
	print 'TO print:', toprint

my_print3('Hello world')
my_print3(2016)
my_print3([1, 2, 3, 4])

# ---example4 有参有缺省值函数---
def my_print4(toprint='Hello'):
	print 'TO print:', toprint

#不传参时打印缺省值
my_print4()
my_print4('Hello world')

# ---example5 变长参数函数 元组形式---
# 此处用*来标注这个形式
def my_print5(*topprint):
	for element in topprint:
		print 'To print', element

my_print5(1)
# 虽然定义时只定义了一个，但是在调用时传参的数可以是不定的
my_print5(1, 2, 3, 4, 'hello')

# ---example6 变长的字典参数---
def my_print6(**mydict):
	for key in mydict:
		print key, mydict[key]

my_print6(name='deangao', sez='m')

# --example7 综合使用---
def my_print7(one, *two, **three):
	print 'One', one

	for tmp in two:
		print 'Two', tmp

	for tmp in three:
		print 'Three', tmp

one = 'hello'
two = (1, 3, 4, 5)
three = {'name': 'deangao', 'sex': 'm'}

# 也可以种方式来调用，省去了逐个传参
my_print7(one, *two, **three)

# 再讲讲函数的返回值  return
def test1(name, sex):
	return name, sex
	# 也可以这样
	return (name, sex)

# 可以这样调用并返回结果
name, sex = test1('deangao', 'm')
print name, sex

# 也可以这样
(name, sex) = test1('deangao', 'm')
print name, sex


# =====================华丽的分割线====================
'''
函数式编程 lambda————相当于匿名函数
只是lambda一般是返回值，即不能执行一些其它操作，比如print

lambda语法格式
lambda [parm1, parm2, ...]: expression

返回的就是一个函数句柄
这里简单介绍下
'''

a = lambda x: 'Element ' + x
print a('hello world')

# ---此处还有一些其它类似于函数编程的内置函数---
'''
apply、filter、map、reduce， 其中apply将被淘汰
这些函数的调用方法都是接收一个函数名func和序列seq(比如有n个元素)，返回相应的元素
比如：filter是将func（返回真假）应用于seq的每个元素，返回其中func返回值为真的元素， 返回元素个数<=n，即原序列的子集
map是将func函数应用于seq的每个元素，返回func的返回值，返回元素个数为n
reduce是将二元（两个参数）函数应用于seq的两个元素，得到的func返回值作为下一个参数值， 最终返回一个结果， 比如对序列求和
'''


# ---比如筛选序列中已'a'为开头的元素形成行的序列---
# filter
seq = ('abc', 'bv', '12', 'aa')
find_with_a = lambda x: x.startswith('a')

print filter(find_with_a, seq)
# 输出 ('abc', 'aa')

# ---给每个元素的开头添加A---
# map
add_a = lambda x: 'A' + x

print map(add_a, seq)
# 输出 ['Aabc', 'Abv', 'A12', 'Aaa']

# ---连接序列的元素为最终的一个字符串---
# reduce
concat_str = lambda x, y: x + y
print reduce(concat_str, seq)
# 输出  abcbv12aa

# ====================华丽的分割线====================
'''
从上面的介绍可以看出函数可以简化编程，提供代码复用率，
而lambda方式可以仅用几行的代码就实现普通的循环做法，
这就是python的强大之处之一，也是pythonic的一部分。
'''
