#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------



import numpy as np
import pandas as pd


"""
Pandas可以理解为更高级的数据分析包. 类似与R中的基本DataFrame 和列表等
百度百科：http://baike.baidu.com/link?url=e6AuowY8kv_0HA2-sFXEMlLolGJP91Tq-PwtTjpaP17S5urAwAXhjPCVgGn7ZN0LFCkpDDwmSQI3hRtnDNlqeK
Pandas官网：http://pandas.pydata.org/
文档教程：http://www.open-open.com/lib/view/open1402477162868.html
文档教程：http://www.cnblogs.com/chaosimple/p/4153083.html
视频教程：http://www.jikexueyuan.com/course/1739_1.html
"""

"""
Series
DataFrame
Panel
"""

# ==============================Series=========================================
print pd.Series([1, 2, 3, 4])
print pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='Example')

a = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='Example Series')

# 通过下标或者索引取值
print a[0]
print a[0:2]
print a['a']

# 基本属性
print a.name

# 基本计算 和Numpy类似
print a.sum()
print a.mean()
print a.max()
print a.all()
print a.any()
print a.abs()
print a.unique()
print a.append(pd.Series([12, 23]))
print a.tolist()

# ====================================DataFrame=============================
data = {"col1": range(0,10), "col2": range(1,11), "col3": np.random.rand(10).tolist()}
print data
df = pd.DataFrame(data=data)
print df

df = pd.DataFrame(data=data, index=range(2000, 2010))
print df

print df.columns
df.columns = [1, 2, 3]
print df
print df.columns

print df.index
