# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:05:59 2018

@author: Administrator
"""
import matplotlib
import matplotlib.pyplot as plt
#import pprint
#分别存放所有点的横坐标和纵坐标，一一对应

import json

filename =("test_reflector_map.json")

map_dic = {}
with open(filename) as f:
    test = json.load(f)    
    for i in test:
        id_section = i['id']
        reflector = i['reflectors']
        map_dic[id_section] = reflector
        
print "map_dic:", map_dic

x_list = []
for x_coordiation in map_dic[1]:
    x_list.append(x_coordiation['x'])
print "x_list", x_list    
    
y_list = []
for y_coordiation in map_dic[1]:
    y_list.append(y_coordiation['y'])
print "y_list", y_list



"""
x_list = []
y_list = []

for i in datalist.values():
    x_list.append(i)
    x_list.append(d[i])
print(x_list)
dic = datalist
lst = [item[key] for item in dic for key in item]
print lst
"""

#设置x轴，y轴名称
#设置横纵坐标轴标签

plt.xlabel("x")  
plt.ylabel("y") 
plt.xlim(xmax = 4, xmin = 0)
plt.ylim(ymax = 4, ymin = 0)

plt.plot(x_list, y_list, "b^-", ms = "6", label = 0)  
#plt.plot(x_list,y_list,'r-o')
plt.legend()  


'''
画网格线，默认横纵坐标轴都画，grid(axis="y")表示只画y轴  
'''
plt.grid()  
plt.show()  








