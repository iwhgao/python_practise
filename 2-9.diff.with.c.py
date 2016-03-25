#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/24
# ---------------------------

__author__ = 'deangao'


'''
Python和C在变量的操作上有些不同，即在内存管理上的差别：
http://www.cnblogs.com/CBDoctor/p/3781078.html
http://www.cnblogs.com/vamei/p/3232088.html
'''

# ---id---
'''
id函数返回Python对象在内存中的“地址”(即对象的标识)
'''

# ---Python---
a = 1
print 'a is', a, id(a)

a = 2
print 'a is', a, id(a)

# 此处b并不是一个“新变量”，而是指向a的一个引用
b = 2
print 'b is', b, id(b)

b = a
print 'b is', b, id(b)

b = 3
print 'a is', a
print 'b is', b, id(b)

# ---Python的输出----
'''
a is 1 34228768
a is 2 34228756
b is 2 34228756
b is 2 34228756
a is 2
b is 3 34228744
'''

# ---C---
'''
#include <stdlib.h>
#include <stdio.h>

int main(void){
	int a = 12;
	int b = 12;
	printf("int a = 12; int b = 12; a is %d, addr of a is %x\n", a, &a);
	printf("int a = 12; int b = 12; b is %d, addr of b is %x\n", b, &b);

	b = a;
	printf("b = a; b is %d, addr of b is %x\n", b, &b);
}
'''

# ---C的输出---
'''
int a = 12; int b = 12; a is 12, addr of a is 559e423c
int a = 12; int b = 12; b is 12, addr of b is 559e4238
b = a; b is 12, addr of b is 559e4238
'''

# ---总结---
# 1. 与C、C++相比， Python的变量不用事先声明其类型，而是在运行时才确定的，即动态特性。
# 2. Python不用像C、C++那样去手动回收内存，它有自己的垃圾回收机制。

"""
http://www.jb51.net/article/61902.htm
1. 赋值是将一个对象的地址赋值给一个变量，让变量指向该地址（ 旧瓶装旧酒 ）。
2. 浅拷贝是在另一块地址中创建一个新的变量或容器，但是容器内的元素的地址均是源对象的元素的地址的拷贝。也就是说新的容器中指向了旧的元素（ 新瓶装旧酒 ）。
3. 深拷贝是在另一块地址中创建一个新的变量或容器，同时容器内的元素的地址也是新开辟的，仅仅是值相同而已，是完全的副本。也就是说（ 新瓶装新酒 ）。
"""
