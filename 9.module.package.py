#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------

import utility

# 导入同级目录的utility模块（文件), 文件名既是模块名
# 注文件名不应含有.，否则会被认为是包结构
# 或者通过 from unility import printHtmlHead  来指明导入模块中的部分元素
# 这样的导入方式就不需要在printHtmlHead前面添加命名空间utility了

"""
Python中的模块是一个有组织的代码文件，相当于C、C++中的头文件
"""

__author__ = 'deangao'

# 通过模块名调用模块中定义的函数
utility.printHtmlHead('这是一个标题')
utility.printHtmlBody('段落')
utility.printHtmlTail('尾部')


"""
Python中的包可以理解为多层文件夹的模块，即将模块通过文件夹的形式进行了归类
各级目录下需要有一个__init__.py的文件，即使它是空的
"""

from People.Student import Student

# 导入People包下面的Student包下面的Student模块
stu1 = Student.Student('dg', 'm', '26') # 调用该模块中的Student类

stu1.printStudent()
