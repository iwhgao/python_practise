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
这里介绍下字符串的基本操作：
连接、截取、替换等
'''

str1 = 'hello '
str2 = 'word\n'

print str1
print str2

# ---连接---
print str1 + str2

# ---截取---
# 从0开始计数， 截取start到end-1部分的字符
print str1[1:3]
print str1[2]

# ---替换---
print str1.replace('ell', 'ELL')
print str1
# 这里str1的内容并没有改变

# ---转变大小写---
print str1.upper(), str2.lower()

# ---除去前后多余字符---
# strip 默认是替换\s \r \n， 可以指定
# str1.lstrip(), str1.rstrip()

print str1 + 'word'
print str1.strip(' ') + 'word'

# ---其它常见操作---
# ---取长度、字符数组连接---
print len(str1)
print ';;'.join((str1, str2))

# ---字符串比较---
print str1 == str2
print str1 != str2
print str1 > str2
print str1 <= str2
print cmp(str1, str2)

print 'h' in str1
print str1 in str2
print 'c' not in str2

# ---数字、字符串转换---
num = 1
print str(num), float('-12.0')

# ---字符串格式化 % 方法---
# 字符串 % 需要格式化的列表
print '%2d\t%s' % (num, str1)

# ---字符串格式化 format 方法---
# 引自 http://my.oschina.net/dillan/blog/133877

'''
可以指定所需长度的字符串的对齐方式:
< （默认）左对齐
> 右对齐
^ 中间对齐
= （只用于数字）在小数点后进行补齐
'''

print '1:\t|{0:>10},'.format('wangyu')
print '2:\t|{0:4.2f}'.format(1.1415926)
print '3:\t|', format(1.1415926, '<10.2f')
print '4:\t|{0:<10},{1:<15}'.format('wangyu',1.1415926)
print '5:\t|User ID: {uid} Last seen: {last_login}'.format(uid='root',last_login = '5 Mar 2008 07:20')

'''格式化指示符可以包含一个展示类型来控制格式。
例如，浮点数可以被格式化为一般格式或用幂来表示。
'b' - 二进制。将数字以2为基数进行输出。
'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
'd' - 十进制整数。将数字以10为基数进行输出。
'o' - 八进制。将数字以8为基数进行输出。
'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。
'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。
'''

print '6:\t|{0:b}'.format(3)
print '7:\t|{0:c}'.format(3)
print '8:\t|{0:d}'.format(3)
print '9:\t|{0:o}'.format(3)
print '10:\t|{0:x}'.format(3)
print '11:\t|{0:e}'.format(3.75)
print '12:\t|{0:g}'.format(3.75)
print '13:\t|{0:n}'.format(3.75) #浮点数
print '14:\t|{0:n}'.format(3)    #整数
print '15:\t|{0:%}'.format(3.75)

# 输入形式的控制format
# a = int(raw_input('a:'))
a = 6
# b = int(raw_input('b:'))
b = 2
print '16:\t|%*.*f' % (a, b, 1.1415926)

print '17:\t|{array[2]}'.format(array=range(10))
print '18:\t|{attr.__class__}'.format(attr=0)
print '19:\t|{digit:*^ 10.5f}'.format(digit=1.0/3)
print '20:\t|{0:,}'.format(1223432434)