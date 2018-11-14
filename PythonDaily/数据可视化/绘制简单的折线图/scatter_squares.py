# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:33:01 2018

@author: Administrator
"""

#绘制散点图并设置样式
import matplotlib.pyplot as plt
plt.scatter(8,10,s= 80)#scatter(x,y,s=点的尺寸)
plt.show()



#自动计算数据

import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap = plt.cm.Blues,s= 40)
#cmap使颜色渐变突出数据的规律
#c指定的是颜色，也可以设置为元组形式c=(a,b,d),其中分别表示红绿蓝，值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅
#plt.scatter(x_values,y_values,c=(0,0,0.2),s=40)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both',which ='major',labelsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,1,1100000])
plt.show()



#自动保存图表

import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap = plt.cm.Blues,s= 40)
#cmap使颜色渐变突出数据的规律
#c指定的是颜色，也可以设置为元组形式c=(a,b,d),其中分别表示红绿蓝，值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅
#plt.scatter(x_values,y_values,c=(0,0,0.2),s=40)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both',which ='major',labelsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,1,1100000])
plt.savefig("squares_plot.png",bbox_inches="tight")
#第一个实参指定要以什么样的文件名存储到scatter_squares.py所在的目录，第二个指出将图表多余的空白剪掉



















