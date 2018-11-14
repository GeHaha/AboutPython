# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:46:42 2018

@author: Gehaha
"""

from copy import deepcopy

class Memento:
    "备忘录"

    def setAttribute(self, dict):
        "深度拷贝字典dict中的所有属性"
        self.__dict__ = deepcopy(dict)

    def getAttribute(self):
        "获取属性字典"
        return self.__dict__


class Caretaker:
    "备忘录管理类"

    def __init__(self):
        self._mementos = {}

    def addMemento(self, name, memento):
        self._mementos[name] = memento

    def getMemento(self, name):
        return self._mementos[name]

class Originator:
    "备份发起人"

    def createMemento(self):
        memento = Memento()
        memento.setAttribute(self.__dict__)
        return memento

    def restoreFromMemento(self, memento):
        self.__dict__.update(memento.getAttribute())