# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 21:29:20 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk
#创建一个RamdomWalk实例，并将其包含的点都绘制出来
#只要程序处于活动状态，就不断的模拟随机漫步
while True:
    
    rw = RandomWalk(50000)
    rw.fill_walk()

    
   
    plt.scatter(rw.x_values, rw.y_values, s= 1)
    
    plt.show()
    
    keep_running = input("Make another walk?(y/n): ")
    if keep_running =='n':
        break
    