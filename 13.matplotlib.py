#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/3/16
# ---------------------------


import numpy as np
import pprint as pp
import matplotlib.pyplot as plt

"""
matplotlib是Python中一个基础的绘图模块，是其它高级绘图模块的基础。
matplotlib 官方网站上面有很多实例：
http://matplotlib.org/gallery.html

首先我们可以先了解下一个标准图表的基本组成，
一个普通的图表组件通常包括：
x轴、y轴、x轴刻度、y轴刻度、x轴标题、y轴标题
图例、图表标题等。
而各组件的属性有：颜色、宽度、透明度等。


图表的类型有：
散点图、折线图、气泡图、雷达图、柱状图、箱线图、直方图、饼图
热图、密度图等等。
"""

# 下面选取几个进行简单的介绍
# pp.pprint(plt.style.available)
# plt可用的风格或者主题， 比如使用R中的ggplot

plt.style.use('ggplot')


# ======================散点图=======================
x = np.random.rand(100)
y = np.random.rand(100)
"""
plot方法的参数:
plot(x, y)        # 默认的为折线图
plot(x, y, 'bo')  # 使用蓝色的圆圈标记
plot(y)           # x轴为0-N-1， y轴为y
plot(y, 'r+')     # y轴为y，x轴为0-N-1， 但是点已+号表示
"""

p1 = plt.subplot(2, 2, 1)
p1.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')

p2 = plt.subplot(2, 2, 2)
p2.plot(x, y, 'bo')

p3 = plt.subplot(2, 2, 3)
p3.plot(y)

p4 = plt.subplot(2, 2, 4)
p4.plot(y, 'r+')

plt.show()

# ======================极坐标图======================
plt.figure(2)
N = 150
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 200 * r**2 * np.random.rand(N)
colors = theta

ax = plt.subplot(111, projection='polar')
c = plt.scatter(theta, r, c=colors, s=area, cmap=plt.cm.hsv)
c.set_alpha(0.75)

plt.show()

# =======================填充图=======================
plt.figure(3)
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(3 * x)
plt.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)
plt.show()
