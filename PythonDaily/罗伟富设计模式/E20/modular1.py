# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:47:50 2018

@author: Gehaha
"""
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Template(metaclass = ABCMeta):
    "模板类（抽象类）"
    @abstractmethod    
    def stepOne(self):
        pass
    
    @abstractmethod    
    def stepTwo(self):
        pass
    
    @abstractmethod
    def stepThree(self):
        pass
    
    def templateMethold(self):
        "模板方法"
        self.stepOne()
        self.stepTwo()
        self.stepThree()
        
class TemplateImplA(Template):
    "模板实现类B"
    def stepOne(self):
        print("Step one")
    
    def stepTwo(self):
        print("Step two")
        
    def stepThree(self):
        print("Step three")
        
        
    