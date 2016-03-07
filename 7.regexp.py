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
这里提前介绍下Python中很有用的正则表达式。
正则表达式在很多语言里是通用的:
正则表达式有匹配、锚定、替换等操作。
正则表达式中的基础知识这里就不介绍了，
可以看看 http://baike.baidu.com/link?url=Yi67fLrjVajdoAv1Chk5T_72UzBNq140ogls6oujrNVUW3bqv5vuaip0wfk5DY-rPJBgpE_4mmLmkVIzpyi9SK
主要介绍下re这个python中内置的正则表达式模块。
'''

import re

string = '''13345679010
This is a good idea!
'''

# 下列函数中有一个缺省参数为flag表示以何种方式来进行匹配（默认是不打开这些标记的）
# 比如 re.M 多行匹配， re.I表示忽略大小写


# 正则表达式中模式的表达方式有两种：
# 一种是直接使用字符串的形式来表达模式  比如 'abc'
# 另外一致是正则表达式中一些特殊字符与系统字符产生歧义时需要特别标注， 比如\b在系统中表示退格符，而在re中表示字符边界
# 所以要以\b的形式在re中使用的话就需要用r''的形式， 比如 r'\b' ， 否则需要用'\\b'来转义\，
# 所以这里推荐后面习惯性的使用r

# 匹配 matchh
'''
从字符串的头部开始搜索，匹配到了就返回一个re对象，否则返回None
'''
# r'\s+' 表示匹配多个空格
# '\s'
res = re.match('133', string)
if res is not None:
	# 通过group函数返回匹配的结果
	print res.group()
else:
	print 'Not match'

res = re.match('33', string)
if res is not None:
	# 通过group函数返回匹配的结果
	print res.group()
else:
	print 'Not match'

# 搜索(第一次出现) search
'''
全文搜搜匹配到第一次匹配成功的模式
'''

res = re.search('good', string)
if res is not None:
	# 通过group函数返回匹配的结果
	print res.group()
else:
	print 'Not match'

# 搜索（所有出现） findall
res = re.findall('s', string)
if res is not None:
	# 此处res为list而非re对象
	print res
else:
	print 'Not match'

# 分割 split
res = re.split(' ', string)
if res is not None:
	# 此处res为list而非re对象
	print res
else:
	print 'Not match'

# 替换 sub subn
'''
sub(pattern, replace_str, raw_string)
subn参数一致， 至少会多返回一个替换的次数
'''

print 'Before:', string
string = re.sub('s', 'S', string)
print 'End:', string

print 'Before:', string
string, num = re.subn('S', 's', string)
print 'End:', string, 'Replaced', num

# 匹配引用
'''
将匹配到的内容作为变量引用应用在后面的正则表达式操作
\数字来引用
'''
res = re.findall(r'(the)\s+\1', 'the the world')
# 此处的\1就表示前面锚定的the
print res


# ================华丽的分割线===============
'''
常见实用正则表达式举例(有的并没有做严格的校验仅从字面来匹配，比如身份证号码等)：
1. 大陆身份证号码：
re.findall(r'\D([123456789]\d{5}((19)|(20))\d{2}((0[123456789])|(1[012]))((0[123456789])|([12][0-9])|(3[01]))\d{3}[Xx0-9])\D', str1)

2. 手机号：
re.findall(r'\D(1[3578]\d{9})\D', str1)

3. 邮箱地址：
re.findall(r'(([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})+)', str1)

4. 银行卡号：
re.findall(r'(([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+(\.[a-zA-Z]{2,3})+)', str1)

'''