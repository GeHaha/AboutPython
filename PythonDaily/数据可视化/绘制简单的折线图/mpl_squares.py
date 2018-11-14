# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:33:49 2018

@author: Administrator
"""
#简单的折线图

import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()



#修改标签文字和线条的粗细
import matplotlib.pyplot as plt
squares = [1,4,9,16.25]
plt.plot(squares,linewidth =5)
#设置图标标题，并给坐标轴加上标签
plt.title("Squares Numners",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Squares of Value",fontsize = 14)
ck_params(axis ='both',labelsize = 14)#设置刻度的样式 ，其中指定的实参axis='both'影响全部的x轴y轴

#设置刻度标记的大小
plt.tick_params(axis ='both',labelsize = 14)#设置刻度的样式 ，其中指定的实参axis='both'影响全部的x轴y轴
plt.show()





#校正图形

import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5)

#设置图表标题并给坐标轴加上标签
plt.title("")

#设置图标标题，并给坐标轴加上标签
plt.title("Squares Numners",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Squares of Value",fontsize = 14)
plt.tick_params(axis ='both',labelsize = 14)#设置刻度的样式 ，其中指定的实参axis='both'影响全部的x轴y轴

#设置刻度标记的大小
plt.tick_params(axis ='both',labelsize = 14)#设置刻度的样式 ，其中指定的实参axis='both'影响全部的x轴y轴
plt.show()






























