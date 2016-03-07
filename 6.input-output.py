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
输入输出在每个编程语言都有介绍的，这里介绍下python中的基本输入输出场景。
1. input是Python中定义如何从标准输入（键盘等）接收“表达式”的函数
2. raw_input是Python中定义从标注输入（键盘等）接收数据的函数
3. print是常见的打印函数-一般打印至标注输出（屏幕等）
'''

# ---比较input和raw_input---
# a = input('Please input something using input func:')
# print a

# b = raw_input('Please input something using raw_input func:')
# print type(b)

'''
Please input something using input func:'abc'
abc
Please input something using raw_input func:dsd
<type 'str'>
'''

'''
这里input要输入在Python脚本中同样的表达式,
raw_input中没有这样的要求， 一般raw_input用的多。
'''

# ---print---
'''
在之前的章节中都有用到print函数，都是一些常用的方法，这里不再做过多的介绍，
后面结合文件的输入输出（读写）讲解下print的另外一种用法
'''

# ===================华丽的分割线=================
'''
文件的读写操作， 也是Python的输入和输出
'''

# 1. 读文件
'''
python中可以用open和file两个函数来以指定方式打开一个文件，对应读文件中常用的模式是r
open 和 file函数的参数为：文件名，打开模式； 返回的是文件句柄
'''

# >打开
f = open('./README.md', 'r')
print f

# >读取
'''
有多种读取模式，对应函数如下：
read(size)	读取多少字节
readline()	读取一行
readlines()	读取多行返回一个列表
'''

# seek函数为调整文件句柄的游标 0，0表移至文件起始位置
print f.read()
f.seek(0,0)

print f.read(100)
f.seek(0,0)

print f.readline()
f.seek(0,0)

print f.readlines()
f.seek(0, 0)

# 常用的循环读取---推荐用第一种做法
# 迭代读取
for line in f:
	print line,

f.seek(0, 0)
for line in f.readlines():
	print line,

# >关闭文件
f.close()


# 2. 写文件

# > 打开
# 覆盖的方式进行写
# f = open('./README.md', 'w')

# 追加的方式进行写
f = open('./README.md', 'a')

# > 写入 需要自己添加换行符
f.write('\n--\n')
f.writelines('\n'.join(['---', '----', '-----']) + '\n')

# > 关闭
f.close()

# 3. print 写入文件
f = open('./README.md', 'a')
print >> f, '------'
f.close()

# 4. 强烈推荐大家使用的一种方式----使用with语法来实现文件的读写操作
'''
with open(file, 'r') as f:
	for line in f:
		<do something>

with 语法在文件读写操作中可以不用自己去关闭文件因为with会做，
而且当代码块的任何一部分发生错误时 都会得到处理。
'''
