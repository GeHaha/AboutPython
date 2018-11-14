# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 17:21:21 2018

@author: Administrator
"""
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

x = [1,2,3,10]  
y = [8,5,4,12]  
    #可用字符串表示线的样式，比如"b^-"，ms是标记大小，label是图例  
    #还可以根据需求设置线的粗细等其他样式  
plt.plot(x,y,"b^-",ms="6",label="mylabel")  
    #设置横纵坐标轴的范围  
plt.xlim(-2,12)  
plt.ylim(2,14)  
    #设置横纵坐标轴标签  
plt.xlabel("x")  
plt.ylabel("y")  
    #设置标题  
plt.title("mytitle")  
plt.legend()  
    #画网格线，默认横纵坐标轴都画，grid(axis="y")表示只画y轴  
plt.grid()  
plt.show()  
