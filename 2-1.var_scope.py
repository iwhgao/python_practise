#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/14
# ---------------------------

__author__ = 'deangao'

num = 0


# 在函数中对变量进行赋值操作则被视为内部局部变量
# ---------------------------
def var_func1():
	num = 1
	print "num in var_func1 is %d" % num


var_func1()

print "num is %d " % num


# --------------------------
# --num 被视为var_func2的内部局部变量， 但是调用是在定义之前
def var_func2():
	print "num in var_func2 is %d" % num
	num = 1


try:
	var_func2()
except UnboundLocalError as e:
	print 'Error is:', e.message

print "num is %d " % num

# ---------------------------
li = [1, 2, 3]


def foo():
	# 此处li是对应的全局变量， 而非内部局部变量
	li.append(4)
	print li


foo()


def bar():
	# 此处li被视为是内部局部变量(因为是赋值操作)， 但是在执行li 追加的时候li并没有定义
	li += [5]
	print li


try:
	bar()
except UnboundLocalError as e:
	print 'Error is:', e.message


def bar1():
	# 已显式全局变量的形式调用li变量
	global li
	li += [5]
	print li


bar1()
