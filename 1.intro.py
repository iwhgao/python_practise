#!/usr/bin/python
# -*- coding: utf8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------


'''
Python 的基础简介就不再介绍了，这里主要介绍下理解后面一些知识所需要的先决条件：

1. 开发环境
》 简单编辑器
Editplus、 Notepad++等常用的文本编辑器都可以用来开发Python程序，但是这些编辑器一般是没有很好的工程管理、代码提示等功能，也没有很好的
与Python console进行交互。
》 Python自带GUI
这个一般的联系可以，开发大项目就不行了。
》 Vim Emacs
这些配置好了就是开发利器，配置不好的话就呵呵。
》 IDE
Python的集成开发环境(IDE: Integrated Development Environment)有很多，比如常见的Eclipse pydev插件、PyCharm以及一些其它的工具，
sublime等，我用过pydev和PyCharm，个人觉得PyCharm的比较好用，比较是要钱的。

2. 缩进与续行
Python中是通过统一缩进来区分代码块的，常见的缩进方式有：Tab键、一个空格、四个空格等。
http://c.biancheng.net/cpp/html/1815.html
比如下面的这个就是错误的方法：

i = 2
 print i #因为前面有一个空格， 与上一句不是一个代码块，所以识别不了i

Python采用 \进行续行

3. 注释
Python的单行注释符为 #，类似于Perl等语言
Python的多行注释符为 三个单引号
另外的一种方法是将不需要的代码定义为一个函数也是可以达到多行注释的效果

4. 帮助系统
Python Console是与python交互的地方，通常查看一个类或者其它资源的帮助文档时可以利用help函数来打印，
比如：
help(sys)

5. 其它教程
http://www.runoob.com/python/python-tutorial.html
http://www.pythontab.com/
http://www.yiibai.com/python/
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
http://nbviewer.jupyter.org/github/lijin-THU/python-tutorial/tree/master/
以及一些在线视频等。
'''

# ======================华丽的分割线=================================
"""
这里没有介绍Python其它的一些模块，比如多线程编程、网络编程、GUI编程、web编程等
"""
print __doc__