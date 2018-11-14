# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 11:52:07 2018

@author: Gehaha
"""

import logging

class Pigment:
    "颜料"
    def __init__(self,color):
        self.__color = color
        self.__user = ""
        
    def getColor(self,user):
        self.__user = user
        return self.__color
    
    def setUser(self,user):
        self.__user = user
        return self
    
    def showInfo(self):
        print(self.__user + "取得" + self.__color + "色颜料")
        
class PigmengFactory:
    "资料的工厂类"
    def __init__(self):
        self.__sigmentSet = {
            "红": Pigment("红"),
            "黄": Pigment("黄"),
            "蓝": Pigment("蓝"),
            "绿": Pigment("绿"),
            "紫": Pigment("紫"),
        }
    
    def getPigment(self,color):
        pigment = self._sigmentSet.get(color)
        if pigment is None:
            logging.error("没有%s颜色的颜料！",color)
            
        return pigment
    
def testPigment():
    factory = PigmengFactory()
    pigmentRed = factory.getPigment ("红").setUser("梦之队")
    pigmentRed.showInfo()
    
    pigmentYellow = factory.getPigment ("黄").setUser("梦之队")
    pigmentYellow.showInfo()
    
    pigmentBlue1 = factory.getPigment ("蓝").setUser("梦之队")
    pigmentBlue1.showInfo()
    
    pigmentBlue2 = factory.getPigment ("").setUser("梦之队")
    pigmentBlue2.showInfo()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    