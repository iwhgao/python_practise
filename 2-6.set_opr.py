#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/15
# ---------------------------

__author__ = 'deangao'

'''
集合的计算：合集、并集、差集等操作
'''

set1 = set((1, 2, 3, '1'))
set2 = set((2, 3, 4, '2', '3'))

# 单个集合操作
# 1. 添加元素
print '添加前', set1
set1.add('2')
print '添加后', set1

# 2. 删除元素
print '删除前', set1
set1.remove('2')
print '删除后', set1

# 3. 添加另一个集合到当前集合
print '合并另一个集合前', set1
set1.update(set2)
print '合并另一个集合后', set1

# 4. 清空集合
print '清理前', set1
# set1.clear()
print '清理后', set1

# 5. 其它操作
'''
union 并集
copy 复制
pop 剔除头部元素并返回
difference 计算差集但是不更新原集合
difference_update 计算差集并更新原集合
issubset 判断是否为子集
issuperset 判断是否为父集
discard 删除元素（如果其在元素中的话）
intersection 求交集
intersection_update 求交集并将结果更新到原集合
symmetric_difference 求对称差集
symmetric_difference_update  求对称差集并更新到原集合
'''

# ---------------------------------------------------------
# 两个集合的计算
# 1. 交集 &
print '交集', set1 & set2

# 2. 并集 |
print '并集', set1 | set2

# 3. 差集 -
print 'set1 - set2', set1 - set2 # 在set1中但是不在set2中
print 'set2 - set1', set2 - set1 # 在set2中但是不在set1中

# 4. 对称差集 ^
print 'set1 和 set2的对称差集', set1 ^ set2 # 在set1中或者set2中，但是不在set1和set2的交集中

# 总结
'''
集合的操作可以通过集合的方法来实现也可以通过集合运算符来实现。
'''
