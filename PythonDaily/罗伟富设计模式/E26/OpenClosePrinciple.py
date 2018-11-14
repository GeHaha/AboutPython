# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:29:16 2018

@author: Gehaha
"""

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    """动物"""

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def moving(self):
        pass

class TerrestrialAnimal(Animal):
    """陆生生物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在陆上跑...")

    def checkFood(self, food):
        food.category() == ""


class AquaticAnimal(Animal):
    """水生生物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在水里游...")

class BirdAnimal(Animal):
    """鸟类动物"""

    def __init__(self, name):
        super().__init__(name)

    def moving(self):
        print(self._name + "在天空飞...")


class Monkey(TerrestrialAnimal):
    """猴子"""

    def __init__(self, name):
        super().__init__(name)

    def climbing(self):
        print(self._name + "在爬树，动作灵活轻盈...")


class Zoo:
    """动物园"""

    def __init__(self):
        self.__animals =[]

    def addAnimal(self, animal):
        self.__animals.append(animal)

    def displayActivity(self):
        print("观察每一种动物的活动方式：")
        for animal in self.__animals:
            animal.moving()

测试代码：

def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrialAnimal("狗"))
    zoo.addAnimal(AquaticAnimal("鱼"))
    zoo.addAnimal(BirdAnimal("鸟"))
    zoo.displayActivity()

结果：

观察每一种动物的活动方式：
狗在陆上跑...
鱼在水里游...
鸟在天空飞...
