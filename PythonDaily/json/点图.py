# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:52:08 2018

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

x = [0.0,1.0,2.0,3.0]
y = [0.0,1.0,2.0,3.0]

for i in range(len(x)):
    plt.plot(x[i],y[i],color ='r')
    plt.scatter(x[i],y[i],color='b')
