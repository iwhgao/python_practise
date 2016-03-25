#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Email: gaowenhui2012@gmail.com
# Version: v1.0.0
# Created: 2016/3/25
# ---------------------------


notices = [
	"在代码中适当的添加注释",
	"适当的添加空行提高代码可读性",
	"将常量集中到一个文件中",
	"不同推荐用type进行类型检查",
	"使用enumerate获取序列的索引和值",
	"分清==和is的区别",
	"考虑字符的编码",
	"使用with",
	"连接字符串应优先使用join而非+",
	"优先用format格式而非%",
	"区别可变和非可变对象",
	"函数传参是传值还是传引用呢？都NO",
	"分清staticmethod和classmethod",
	"",
]

suggestions = zip(range(len(notices)), notices)

for k, v in suggestions:
	print k, v

