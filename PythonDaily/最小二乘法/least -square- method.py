# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:38:08 2019

@author: Gehaha
"""

import numpy as np 
from matplotlib import pyplot as plt
 
A = np.array([[3],[1]])
C = np.array([[1],[3]])
 
#x'=(A.TA)^(-1)A.TC
B = A.T.dot(C)
AA = np.linalg.inv(A.T.dot(A))#求A.T.dot(A)的逆
l=AA.dot(B)
#P=Ax'
P=A.dot(l)
 
x=np.linspace(-2,2,10)#x.shape=(10,)
x.shape=(1,10)
#画出直线y=ax
xx=A.dot(x)
fig = plt.figure() #figsize=(10,6)
ax= fig.add_subplot(111)
ax.plot(xx[0,:],xx[1,:])
#画出A点
ax.plot(A[0],A[1],'ko')
#画出C点，P点
ax.plot([C[0],P[0]],[C[1],P[1]],'r-o')
#画出OC线
ax.plot([0,C[0]],[0,C[1]],'m-o')
 
#画出坐标轴x=0,y=0
ax.axvline(x=0,color='black')
ax.axhline(y=0,color='black')
 
#标写每个点的字母
margin=0.1
ax.text(A[0]+margin, A[1]+margin, r"A",fontsize=20)
ax.text(C[0]+margin, C[1]+margin, r"C",fontsize=20)
ax.text(P[0]+margin, P[1]+margin, r"P",fontsize=20)
ax.text(0+margin,0+margin,r"O",fontsize=20)
ax.text(0+margin,4+margin, r"y",fontsize=20)
ax.text(4+margin,0+margin, r"x",fontsize=20)
plt.xticks(np.arange(-2,3))
plt.yticks(np.arange(-2,3))
 
ax.axis('equal')
plt.show()