# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:52:44 2018

@author: Administrator
"""

#题目：暂停一秒输出。 
#使用time模块的sleep()函数

import time

myDict = {'color':'black','age': 23,'name':'ge'}

for k, v in dict.items(myDict):
    print(k,v)
    time.sleep(10)

    