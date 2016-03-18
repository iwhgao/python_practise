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
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

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

# ==============================Series(一维)=========================================
print pd.Series([1, 2, 3, 4])
print pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='Example')

a = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='Example Series')
a.plot()

plt.show()

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

# =================================DataFrame（二维）=============================
data = {"col1": np.random.randint(0, 5, 100), "col2": np.random.randn(100), "col3": np.random.rand(100).tolist()}
print data
df = pd.DataFrame(data=data)
print df

df = pd.DataFrame(data=data, index=pd.date_range('11/1/2015', periods=100))
print df
print df.describe()

plt.figure()
df.plot()
plt.show()

print df.columns
df.columns = [1, 2, 3]
print df
print df.columns

print df.index

# 保存DataFrame为CSV
df.to_csv('./t.csv', header=False)

# 从CSV读取
print pd.read_csv('./t.csv', header=None)

# 关于DataFrame更多的方法
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

# =============================Panel（三维）============================
data = np.random.randn(2, 4, 3)

# 相对于 2层， 每层有一个4x3的矩阵
# 其中items为层
# major为DataFrame的行（index）
# minor为DataFrame的列

pn = pd.Panel(data, items=['Z1', 'Z2'], major_axis=['X1', 'X2', 'X3', 'X4'], minor_axis=['Y1', 'Y2', 'Y3'])
print pn

print pn.minor_xs('Y1')

# =========================华丽的分割线============================
# 总结
# pandas模块的东西远不止这些，例如还有groupby join concat merge等都没有讲，感兴趣的可以去官网上仔细的阅读下文档
# 在具体的业务上加以运用
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#series
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe
# http://pandas.pydata.org/pandas-docs/stable/dsintro.html#panel
# http://pandas.pydata.org/pandas-docs/stable/categorical.html
# http://pandas.pydata.org/pandas-docs/stable/io.html
# http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html
# http://pandas.pydata.org/pandas-docs/stable/visualization.html
