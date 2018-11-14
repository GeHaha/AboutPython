# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:03:21 2018

@author: Gehaha
"""

from abc import ABCMeta,abstractmethod

#引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class ReaderView(metaclass = ABCMeta):
    "阅读器视图"
    
    def __init__(self):
        self.__curPageNum = 1
        
    def getPage(self,pageNum):
        self.__curPageNum = pageNum
        return "第" + str(pageNum)+ "的内容"
    
    def prePage(self):
        content = self.prePage(self.__curPageNum - 1)
        self.displayPage(content)
        
    def nextPage(self):
        content = self.getPage(self.__curPageNum + 1)
        self.displayPage(content)
    
    @abstractmethod
    def displayPage(seld,content):
        "翻页效果"
        pass

class SmoothView(ReaderView):
    "左右平滑的视图"
    def displayPage(self,content):
        print("左右平滑：" + content)
    
class SimulationView(ReaderView):
    "仿真翻页的视图"
    def displayPage(self,content):
        print("仿真翻页：" + content)
        