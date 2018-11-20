# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:14:25 2018

@author: Gehaha
"""
path = "test.txt"
file = open(path,'r')
distance = []; intensity = [];
   
try:
   for line in file.readlines():
      lineArr = line.strip().split()  # 去除空格符
      distance.append(lineArr[0][9:]) # 第三列是distance的数据  
      intensity.append(lineArr[2][10:])
   print(distance)
   print(intensity)
except Exception as err:
    pass
