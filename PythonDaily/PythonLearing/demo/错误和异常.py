
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:14:50 2018

@author: Administrator
"""

import random
offices =[[],[],[]]
names =['a','b','c','d','e','f','g','h']
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("-"*20)