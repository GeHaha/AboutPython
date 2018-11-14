# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:21:45 2018

@author: ASUS
"""
from copy import copy,deepcopy

class Person:
    "人"
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.__petList = []
        
    def showMyself(self):
        print("我是" + str.__name + ",年龄" + str(self.__age)+ ". 我养了这些宠物：")
        for pet in self.__petList:
            print(pet + "\t",end = "")
        print()
        
    def addPet(self,pet):
        self.__petList.append(pet)
        
    def clone(self):
        return copy(self)
    
    def deepClone(self):
        return deepcopy(self)
    

def testProtoType2():
    tony = Person("Tony", 26)
    tony.addPet("小狗Coco")
    print("父本tony：", end="")
    tony.showMyself()

    tony1 = tony.deepClone()
    tony1.addPet("小猫Amy")
    print("副本tony1：", end="")
    tony1.showMyself()
    print("父本tony：", end="")
    tony.showMyself()

    tony2 = tony.clone()
    tony2.addPet("小兔Ricky")
    print("副本tony2：", end="")
    tony2.showMyself()
    print("父本tony：", end="")
    tony.showMyself()           