#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/3/16
# ---------------------------

__author__ = 'deangao'


def printHtmlHead(title):
	print '''<html>
	<head>
	<title>${0}</title>
	</head>	'''.format(title)


def printHtmlBody(para):
	print '''<body>
	<p>${0}</p>'''.format(para)

def printHtmlTail(para):
	print '''<p>${0}</p>
	</body>
	</html>'''.format(para)