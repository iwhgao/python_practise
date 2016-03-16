#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/24
# ---------------------------

__author__ = 'deangao'

"""
这里介绍下常用的几个模块：
比如：
os			与操作系统相关的，如目录等
sys			与系统相关的，如接收命令行参数等
time		Python中的时间处理方法
datetime	时间日期处理模块
pprint		对变量的结构化打印模块
json		json格式处理模块
"""

import os
import sys
import time
import datetime
import pprint
import json

# 可以 imort os,sys,json 但是不推荐这样
print dir(os)

# =================os模块常见属性和方法简介==============
# getcwd获取当前工作目录
print os.getcwd()

# system 执行外部命令
os.system('dir')

# =================sys模块常见属性和方法简介==============
print dir(sys)

# argv 获取命令行参数列表 第一个为脚本本身
print sys.argv

# 获取系统默认编码
print sys.getfilesystemencoding()

# 获取系统的信息
print sys.getwindowsversion()

# 获取系统的Python环境变量path
print sys.path

# platform 系统版本
print sys.platform

# ==================time模块常见属性和方法简介===============
print dir(time)

# 获取到小数点两位的unixtimestamp形式
t = time.time()

# 转换为细分的格式
tl = time.localtime(t)
print tl
print tl.tm_year

# 格式化输出
print time.strftime('%Y-%m-%d %H:%M:%S')

# ================datetime模块常见属性和方法简介==============
print dir(datetime)

d1 = datetime.date(year=2016, month=03, day=15)
print d1
t = datetime.time(hour=20, minute=8, second=12)
print t

d2 = datetime.date(year=2016, month=3, day=11)
print d2
print d2-d1
print d1-d2

# ================pprint模块常见属性和方法简介==============
print dir(pprint)

example = {"name": "dg",
		   "address": ["zhongguo guangdong shenzhen", "zhongguo hubei 武汉"],
		   "occup": "coding",
		   "sex": "m"}

print example

# indent 缩进
# width 一行的宽度
# depth 打印的深度， 多层嵌套的情况 超过深度的则用...表示， 默认都打印

pprint.pprint(example, indent=2)

# ================json模块常见属性和方法简介====================
print dir(json)
print example

# 字典类型转换为JSON字符串  dumps
# 常见参数：
# ensure_ascii True/False 是否已ASCII编码， False的可以显示中文
# indent JSON字符串缩进
# encoding 编码

json_str = json.dumps(example, ensure_ascii=False)
print json_str, type(json_str)

# JSON字符串转换为Python对应的数据类型  loads
# 常见参数
# encoding
# parse_float
# parse_int

dict1 = json.loads(json_str)
print dict1, type(dict1)
