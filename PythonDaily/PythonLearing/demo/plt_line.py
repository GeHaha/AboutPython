# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:09:38 2018

@author: Gehaha
"""
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['Simhei']  #显示中文字体
plt.rcParams['axes.unicode_minus']=False    #显示负数
plt.xlim(-10,250)  
plt.ylim(-10,250)
plt.title("数据图像")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

#读取文件
path = "H:\Python\XY数据.txt"
file = open(path,'r')

#读取文件中的内容放到列表中
X_list=[]; Y_list=[];
try:
    for line in file.readlines():
        lineArr = line.strip().split()
        X_list.append(int(lineArr[0]))  #
        Y_list.append(int(lineArr[1]))    

        plt.plot(X_list,Y_list,'r',label='pid')
        plt.show() 
except Exception as error:
    print(error)
