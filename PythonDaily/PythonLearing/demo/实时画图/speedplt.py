# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:51:52 2018

@author: Administrator
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
 
path = "H:\PYTHON\PythonLearing\demo\实时画图\speed.txt"
file = open(path, 'r')
 
AMat = []; BMat = [];XMat = [];YMat = [];ZMat = [];
 
for line in file.readlines():
    lineArr = line.strip().split()
    AMat.append(int(lineArr[0]))
    BMat.append(int(lineArr[1]))
    XMat.append(int(lineArr[2]))
    YMat.append(int(lineArr[3]))
    ZMat.append(int(lineArr[4]))
    
fig = plt.figure()
axA = fig.add_subplot(5,1,1,xlim=(0, 0.2), ylim=(0, 40))
axB = fig.add_subplot(5,1,2,xlim=(0, 0.2), ylim=(0, 40))
axX = fig.add_subplot(5,1,3,xlim=(0, 0.2), ylim=(0, 200))
axY = fig.add_subplot(5,1,4,xlim=(0, 0.2), ylim=(0, 200))
axZ = fig.add_subplot(5,1,5,xlim=(0, 0.2), ylim=(0, 200))
 
lineA, = axA.plot([], [], lw=1)  
lineB, = axB.plot([], [], lw=1)  
lineX, = axX.plot([], [], lw=1) 
lineY, = axY.plot([], [], lw=1) 
lineZ, = axZ.plot([], [], lw=1)
 
def init():  
    lineA.set_data([], [])  
    lineB.set_data([], [])
    lineX.set_data([], [])
    lineY.set_data([], [])
    lineZ.set_data([], [])  
    return lineA,lineB,lineX,lineY,lineZ
 
def animate(i):
 
    t = np.linspace(0, 0.2, 10)   
    yA = AMat[i:10 + i]  
    lineA.set_data(t, yA)   
 
    yB = BMat[i:10 + i]
    lineB.set_data(t, yB) 
 
    yX = XMat[i:10 + i]
    lineX.set_data(t, yX) 
 
    yY = YMat[i:10 + i]
    lineY.set_data(t, yY) 
 
    yZ = ZMat[i:10 + i]
    lineZ.set_data(t, yZ) 
 
    return lineA,lineB,lineX,lineY,lineZ
 
anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=len(XMat)-10, interval=2)  
plt.show()