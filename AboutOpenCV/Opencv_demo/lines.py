# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:06:56 2018

@author: Gehaha
"""

import cv2
import numpy as np
img = cv2.imread('lines.ipg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,120)
minLineLength = 20
maxLineGap = 5
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)


for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("edges",edges)
cv2.imshow("lines",img)
cv2.waitKey()
