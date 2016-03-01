#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------

__author__ = 'deangao'

dict1 = {'name': 'deangao', 'address': ['sz', 'wh'], 'sex': 'm'}

print dict1

# ---其它操作---
# 1. pop: 剔除指定key的项并返回其value
tmp = dict1.pop('name')
print tmp

# 2. clear: 清除整个字典
dict1.clear()
print dict1

dict1 = {'name': 'deangao', 'address': ['sz', 'wh'], 'sex': 'm'}
# 3. copy: 复制
dict2 = dict1.copy()
print dict2

# 4. fromkeys: 由序列元素为键来创建值为空的字典
tmp = dict1.fromkeys(['name', 'a', 'b'])
print tmp
print dict1

# 5. get: 根据键来获取值
print dict1.get('name')

# 6. items: 获取键值对-返回列表（元素为元组）
print dict1.items()

# 7. update: 添加其它的字典
dict2 = {'name1': 'age1', 'age1': 22}
print dict1
dict1.update(dict2)
print dict1

# 8. keys: 列举所有的key
print dict1.keys()

# 9. values: 列举所有的value
print dict1.values()

