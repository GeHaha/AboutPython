# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:12:36 2018

@author: Administrator
"""

plt.axis([1,3,1,3])
plt.ion()

while True:
    content = subscriber.recv_multipart()
    for i in range(len(content)):
        if content[i][0]=="1":
            x=content[i][2:9]
            X1.append(x)
            y=content[i][11:18]
            Y1.append(y)
            print(x,y)
            plt.plot(X1,Y1,color='red')
            plt.pause(0.1)
            
            