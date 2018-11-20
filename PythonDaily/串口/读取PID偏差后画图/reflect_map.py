# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:05:34 2018

@author: Administrator
"""

import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle
import time
import math



#初始数据绘图
plt.xlim(-10,250)  
plt.ylim(-10,250)
plt.title("PID实时数据图像")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
print('开始仿真')

#读取文件
path = "XY数据.txt"
file = open(path,'r')

#读取文件中的内容放到列表中
X_list=[]; Y_list=[];
try:
    for line in file.readlines():
         lineArr = line.strip().split()
         X_list.append(int(lineArr[0]))
         Y_list.append(int(lineArr[1]))    

    plt.plot(X_list,Y_list,'r',label='pid')
    plt.show() 
except Exception as err:
    print(error)


