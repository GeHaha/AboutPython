# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:56:08 2018

@author: Gehaha
"""

from abc import ABCMeta ,abstractmethod
#引入ABCMeta和abstramethod来定义抽象类和抽象方法

class Flyweight(metaclass = ABCMeta):
    "享元类"
    def operation(self,extrinsicState):
        pass
    
class FlyweightImpl(Flyweight):
    "享元类的具体实现类"
    def __init__(self,color):
        self.__color = color
        
    def operation(self,extrinsicState):
        print(extrinsicState + "取得" + self.__color + "色颜料")
        
class FlyweightFactory:
    "享元工厂"
    def __init__(self):
        self.__flyweights = {}
        
    def getFlyweight(self,key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
            
        return pigment
    
    
def testPigment2():
    factory = FlyweightFactory()
    pigmentRed = factory.getFlyweight("红")
    pigmentRed.operation("梦之队")
    
    pigmentYellow = factory.getFlyweight("黄")
    pigmentYellow.operation("梦之队")
    
    pigmentBlue1 = factory.getFlyweight("蓝")
    pigmentBlue1.operation("梦之队")
    
    pigmentBlue2= factory.getFlyweight("蓝")
    pigmentBlue2.operation("梦之队")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  