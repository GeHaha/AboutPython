# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:29:37 2018

@author: Gehaha
"""
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
import logging
# 引入logging模块用于输出日志信息
import time
# 引入时间模块


class PooledObject:
    "池对象，也称池化对象"
    def __init__(self,obj):
        self.__obj = obj
        self.__busy = False
        
    def getObject(self):
        return self.__obj
    
    def setObject(self):
        return self.__obj
    
    def isBusy(self):
        return self.__busy
    
    def setBusy(self,busy):
        self.__busy = busy
        
class ObjectPool(metaclass = ABCMeta):
    "对象池"
    "对象池初始化大小"
    InitialNumOfObject = 10
    "对象池最大的大小"
    MaxNumOfObjects = 50
    
    
    def __init__(self):
        self.__pools = []
        for i in range(0,ObjectPool.InitialNumOfObject):
            obj = self.createPooledObject()
            self.__pools.append(obj)
    @abstractmethod
    def createPooledObject(self):
        "子类提供创建对象的方法"
        pass
    
    def borrowObject(self):
        #"如果找到空闲对象，直接返回"
        obj = self.__findFreeObject()
        if (obj is not None):
            logging.info("%s对象已被借用, time:%d", id(obj), time.time())
            return obj
        #如果对象池未满，则添加新的对象
        if(len(self.__pools) < ObjectPool.MaxNumOfObjects):
            pooledObj = self.addObject()
            if (pooledObj is not None):
                pooledObj.setBust(True)
                logging.info("%s对象已被借用, time:%d", id(obj), time.time())
                return obj
        #如果对象池未满，则添加新的对象
        if(len(self.__pools) < ObjectPool.MaxNumOfObjects):
            pooledObj = self.addObject()
            if (pooledObj is not None):
                pooledObj.setBusy(True)
                logging.info("%s对象已被借用, time:%d", id(pooledObj.getObject()), time.time())
                return pooledObj.getObject()
        #对象池已满且没有空闲对象，则返回None
        return None
    def returnObject(self,obj):
        for pooledObj in self.__pools:
            if(pooledObj.getObject() == obj):
                pooledObj.setBusy(False)
                logging.info("%s对象已归还, time:%d", id(pooledObj.getObject()), time.time())
    
            break
    
    def addObjec(self):
        obj = None
        if(len(self.__pools) < ObjectPool.MaxNumOfObjects):
            obj = self.createPooledObject()
            self.__pools.append(obj)
            logging.info("添加新对象%s, time:%d", id(obj), time.time())
        return obj

    def clear(self):
        self.__pools.clear()
        
    def __findFreeObject(self):
        "查找空闲的对象"
        obj = None
        for pooledObj in self.__pools:
            if (not pooledObj.isBusy()):
                obj = pooledObj.getObject()
                pooledObj.setBusy(True)
                break
        return obj
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    