# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:05:14 2018

@author: Gehaha
"""

class PowerBank:
    
    "移动电源"
    
    def __init__(self,serialNum,electricQuantity):
        self.__serialNum = serialNum
        self.__electricQuantity = electricQuantity
        self.__user = ''
    
    def getElectricQuantity(self):
        return self.__electricQuantity
    
    def setUser(self,user):
        self.__user = user
    
    def getUser(self):
        return self.__user
    
    def showInfo(self):
        print("序列号：" + str(self.__serialNum) + "电量：" + str(self.__electricQuantity)+"%  使用者:" + self.__user)
        
        
class ObjectPack:
    "对象的包装类，封装指定的对象(如充电宝)是否被使用中"
    def __init__(self,obj,inUsing = False):
        self.__obj = obj
        self.__inUsing = inUsing
        
    def inUsing(self):
        return self.__inUsing
    
    def setUsing(self,isUsing):
        self.__inUsing = isUsing
        
    def getObj(self):
        return self.__obj
    
class PowerBankBox:
    "存放移动电源的智能箱盒"
    def __init__(self):
        self.__pools = {}
        self.__pools['0001'] = ObjectPack(PowerBank('0001,100'))
        self.__pools['0002'] = ObjectPack(PowerBank('0002,100'))
        
    def borrow(self,serialNum):
        "使用移动电源"
        item = self.__pools.get(serialNum)
        result = None
        if (item is None):
            print("没有可用的电源")
        elif(not item.inUsing()):
            item.setUsing(True)
            result = item.getObj()
        else:
            print(set(serialNum) + "电源已被借用!")
        return result
     
    def giveBack(self,serialNum):
        "归还移动电源"
        item = self.__pools.get(serialNum)
        if(item is not None):
            item.setUsing(False)
            print(set(serialNum) + "电源已归还")
    
    
    
def testPowerBank():
    box = PowerBankBox()
    powerBank1 = box.borrow('0001')
    if (powerBank1 is not None):
        powerBank1.setUser('Tony')
        powerBank1.showInfo()
    powerBank2 = box.borrow('0002')
    if (powerBank2 is not None):
        powerBank2.setUser('sam')
        powerBank2.showInfo()
    powerBank3 = box.borrow('0001')
    if (powerBank3 is not None):
        powerBank3.setUser('Aimee')
        powerBank3.showInfo()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    