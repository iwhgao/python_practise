#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------


import numpy as np
import pprint as pp

"""
关于Numpy的介绍网上有很多，教程也有很多，简单的说Numpy就是Python中一个用于数值计算的模块。
百度百科： http://baike.baidu.com/link?url=XmczaCwwZzdeh6rKZXs1v_2fCo8DsnQR2-YrT99CDwymgA48zSSY2j2fsaeVuI5w3g8fcDr6HD3F3oKpoXpOD_
文档教程：http://www.tuicool.com/articles/r2yyei
视频教程：http://www.jikexueyuan.com/course/1537.html
IPython Notebook教程：http://nbviewer.jupyter.org/github/lijin-THU/python-tutorial/tree/master/03.%20numpy/
"""

# 此处使用import中的as 为numpy取别名 np

# 查看Numpy模块的说明文档
print np.__doc__

# 查看Numpy的属性和方法
pp.pprint(dir(np))

# ==============数组及其操作============
# 创建数组（一维 多维）
a1 = np.array([1, 2, 3, 4])

# 产生一维数组的元素为0的数组, 维度由元组指定
a2 = np.zeros((4,))

# 产生二维元素为1的数组
a3 = np.ones((4,3))

# 产生随机数组
a4 = np.random.rand(12, 4)

print a1, type(a1)
pp.pprint(dir(a1))

# 大小(元素个数)
print a1.size
print a2.size
print a3.size
print a4.size

# 数组维数
print a1.shape
print a2.shape
print a3.shape
print a3.shape

# max 参数有axis 即0为按列， 1为按行
# 这个参数在后面的其它大部分函数中适用
print a4.max()
print a4.max(0)
print a4.max(1)

print a4.min()
print a4.min(0)
print a4.min(1)

print a4.mean()
print a4.mean(0)
print a4.mean(1)

print a4.sum()
print a4.sum(0)
print a4.sum(1)

# 标准差 std 方差var
print a4.std()
print a4.std(0)
print a4.std(1)

# T 转置
print a4
print a4.T

# 填充替换
# a4.fill(0.2)
# print a4

# 切片操作， 即通过下标来取值
# 小标从0开始
print a4

# 部分元素
print a4[1:3, 2:4]

# 第2行
print a4[1, :]

# 第2列
print a4[:, 1]


# where all any 操作
# where 返回满足条件的元素的下表， 以元组返回下标
isBiggerThen055 = a4 > 0.5
print isBiggerThen055

print '更新bool下标取值', a4[isBiggerThen055]

rowindex, colindex = np.where(a4 > 0.5)
print rowindex
print colindex
print a4[rowindex, colindex]

# all 所有的元素满足条件才返回True 此处对应的是all函数, 一维数组
print all(a1 > 0.6)
print all(a1 < 1)

# 在Numpy中 数组的方法all 是比较给定元素是否为真, 可以指定维度axis
print (a1 == a1).all()
print a4.all()
print (a4 > 0.5).all()
print (a4 > 0.5).all(0)
print (a4 > 0.5).all(1)

# any 有一个元素满足条件则返回True， 一维数组
print any(a1 > 2)

# Numpy 中的any方法， 可以指定维度axis
print (a4 > 0.5).any()
print (a4 > 0.5).any(0)
print (a4 > 0.5).any(1)

# 计算
# 加减乘除
print a1
print a1 + 3
print a1 - 2
print a1 + a1
print a1 * 3
print a1 ** 3
print a1 * a1
print a1 / 3.0

# 分割
print np.vsplit(a4, 4)
print np.hsplit(a4, 2)

a1_copy = a1
# 浅拷贝， 内存地址一样， 避免大数组在内存上的开销
print id(a1)
print id(a1_copy)

print a1
print a1_copy
a1_copy[0] = 122

print a1
print a1_copy # 改变a1_copy, 但a1被修改了

a2_copy = np.copy(a1)
print id(a1)
print id(a2_copy)

a2_copy[0] = 233

print a1 # a1 不被修改
print a2_copy


# ================汇总==================
"""
创建数组

arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r , zeros, zeros_like
转化

astype, atleast 1d, atleast 2d, atleast 3d, mat
操作

array split, column stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
询问

all, any, nonzero, where
排序

argmax, argmin, argsort, max, min, ptp, searchsorted, sort
运算

choose, compress, cumprod, cumsum, inner, fill, imag, prod, put, putmask, real, sum
基本统计

cov, mean, std, var
基本线性代数

cross, dot, outer, svd, vdot
"""