#!/usr/bin/python
# -*- coding:utf-8 -*-

# ---------------------------
# Author: deangao
# Copyright: 2016 deangao
# Version: v1.0.0
# Created: 2016/2/3
# ---------------------------

__author__ = 'deangao'

'''
Python中同样是支持面向对象编程的（Object Oriented Programming）。
'''

'''
	1. 类的数据属性和实例的数据属性不同，即使同名；
	2. 类的实例可以在被创建后通过.的形式来新增实例数据属性；
	3. 类色数据属性通过类名来调用和修改，也可以通过实例来调用但不能修改，如果通过实例来更新则会产生一个新的仅属于该实例属性；
	4. 类有静态方法和类方法，可以通过函数修饰符来说明；
	5. Python中的类可以多继承;
	6. 默认Python中的属性和方法是公开的（Public），可以通过下面的方法来实现 私有变量和方法
		_xxx        不能用'from module import *'导入
		__xxx__ 	系统定义名字
		__xxx    	类中的私有变量名

		"单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
		"双下划线" 开始的是私有成员，意思是只在类内部能被访问，连子类对象也不能访问到这个数据。
'''


# 定义一个人物类
class People(object):
	# 此处定义的类的属性
	count = 0

	def __init__(self, name, sex, age):
		# 类似this指针
		People.count += 1
		self.name, self.sex, self.age = name, sex, age
		self.count = 10
		# 此处定义实例的属性
		self.instance_attr = 'Test'

	# 公有成员函数
	def peoplePrint(self):
		print 'Name is', name
		print 'Sex is', sex
		print 'Age is', age

	# 静态方法  此处无参数
	@staticmethod
	def static_method():
		print 'This is a static method in', People.__name__

	# 类方法 cls为类
	@classmethod
	def class_method(cls):
		print 'This is a class method', cls.__name__


name = 'who'
sex = 'm'
age = 23

# 打印类的属性
print People.__dict__

# 类实例化
one_people = People(name, sex, age)
print one_people.__dict__

# 调用成员函数
one_people.peoplePrint()

# 实例对象调用对象的成员变量
print one_people.name
one_people.name = 'am'
print one_people.name

# 调用类的属性
print People.count
People.count += 1
print People.count

print People.__dict__

# 实例化另一个对象 类的属性count自增1
two_people = People(name, sex, age)
print People.__dict__


# ============================
# 静态方法
People.static_method()

# 类方法
People.class_method()


# ============================华丽的分割线===================================
class Animal(object):
	"""
	这是一个动物的基类
	"""

	def __init__(self):
		"""
		初始化方法
		"""
		print '这是一个动物的基类'
		self.__printAnimal()
		self._printAnimal()

	def sounding(self):
		"""
		定义一个基本行为（方法）
		"""
		print '动物的发声'

	def _printAnimal(self):
		"""
		类的保护函数
		"""
		print 'Protected'

	def __printAnimal(self):
		"""
		类的私有函数，只能被在类的内部使用
		"""
		print 'Private'


class Dog(Animal):
	"""
	继承Animal基类
	"""

	def __init__(self):
		Animal.__init__(self)  # 此处需要显示的给定参数self
		print '实例化一个Dog对象'

	def sounding(self):
		"""
		重载基类的方法
		"""
		Animal.sounding(self)
		print 'Dog的发声是：汪汪'


class Cat(Animal):
	"""
	继承Animal基类
	"""

	def __init__(self):
		Animal.__init__(self)
		print '实例化一个Cat对象'

	def sounding(self):
		"""
		重载父类的sounding方法
		:return: None
		"""
		Animal.sounding(self)
		print 'Cat的发声是:喵喵'


# 实例Dog对象
dog1 = Dog()

# 调用Dog类的sounding方法
dog1.sounding()

# 调用父类的保护方法
dog1._printAnimal()

# 实例Cat对象
cat1 = Cat()

# 调用Cat类的sounding方法
cat1.sounding()

# 调用父类的保护方法
cat1._printAnimal()
# cat1.__printAnimal() 报错

