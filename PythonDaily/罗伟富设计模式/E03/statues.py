# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 11:43:38 2018

@author: Administrator
"""

class Water:
    "水(H2O)"

    def __init__(self, state):
        self.__temperature = 25
        self.__state = state

    def setState(self, state):
        self.__state = state

    def changeState(self, state):
        if (self.__state):
            # cout << "由" << m_pState->GetStateName() << "变为" << pState->GetStateName() << endl;
            print("由", self.__state.getStateName(), "变为", state.getStateName())
        else:
            print("初始化为", state.getStateName())
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        if (self.__temperature <= 0):
            self.changeState(SolidState("固态"))
        elif (self.__temperature <= 100):
            self.changeState(LiquidState("液态"))
        else:
            self.changeState(GaseousState("气态"))

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State:
    "状态"

    def __init__(self, name):
        self.__name = name

    def getStateName(self):
        return self.__name

    def behavior(self, water):
        pass


class SolidState(State):
    "固态"

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格高冷，当前体温", water.getTemperature(),
              "摄氏度，我坚如钢铁，仿如一冷血动物，请用我砸人，嘿嘿……")


class LiquidState(State):
    "液态"

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格温和，当前体温", water.getTemperature(),
              "摄氏度，我可滋润万物，饮用我可让你活力倍增……")


class GaseousState(State):
    "气态"

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格热烈，当前体温", water.getTemperature(),
              "摄氏度，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到无我的境界……")


"""测试代码"""
def testState():
    "状态模式的测试代码"
    water = Water(LiquidState("液态"))
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()
    water.setTemperature(60)
    water.behavior()
    water.reduceTemperature(80)
    water.behavior()