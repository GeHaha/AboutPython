# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:06:53 2018

@author: Administrator
"""

#题目：输入三个整数x,y,z，请把这三个数由小到大输出。


l = []
for char in range(3):
    char = int(input("请输入一个整数："))
    l.append(char)
l.sort()
print(l)

    

