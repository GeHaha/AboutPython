# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from copy import copy, deepcopy

class Person:
    "人"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showMyself(self):
        print("我是" + self.__name + ",年龄" + str(self.__age) + ".")

    def coding(self):
        print("我是码农，我在Coding改变世界...")

    def reading(self):
        print("阅读使我快乐！知识使我成长！如饥似渴地阅读是生活的一部分...")

    def fallInLove(self):
        print("春风吹，月亮明，花前月下好相约...")

    def clone(self):
        return copy(self)
    
    
def testProtoType():
    tony = Person("Tony",26)
    tony.showMyself()
    tony.coding()
    
    tony1 = tony.clone()
    tony1.showMyself()
    tony1.reading()
    
    tony2 = tony.clone()
    tony2.showMyself()
    tony2.reading()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    