# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 10:47:50 2018

@author: Gehaha
"""

from abc import ABCMeta,abstractmethod
"引入ABCMeta和abstractmethod来定义抽象类和抽象方法"
class DesignPatternBook:
    "<从生活的角度设计模式>一书"
    def getName(self):
        return "《从生活的角度解读 设计模式》"
    
class Reader(metaclass = ABCMeta):
    "访问者，也就是读者"
    @abstractmethod
    def read(self,book):
        pass

class Engineer(Reader):
    def read(self,book):
        print("技术狗读" + book.getName() + "一书后的感受：能抓住模式的核心思想")

class ProductManager(Reader):
    "产品经理"
    def read(self,book):
        print("产品经理读" + book.getName() + "一书后的感受：配图非常有趣")
        
class otherFriend(Reader):
    "IT圈外的朋友"
    def read(self,book):
        print("IT圈外的朋友度" +book.getName() + "一书后的感受，一脸懵逼")

#测试代码
def testBook():
    book = DesignPatternBook()
    fans = [Engineer(),ProductManager(),OtherFriend()];
    for fan in fans:
        fan.read(book)
        
    