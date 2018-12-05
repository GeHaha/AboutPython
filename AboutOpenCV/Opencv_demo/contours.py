# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:13:30 2018

@author: Gehaha
"""

import cv2 as cv
import numpy as np

img = cv.pyrDown(cv.imread("hammer1.jpg",cv.IMREAD_UNCHANGED)
ret,thresh = cv.threshold(cv.imread(img.copy(),cv.COLOR_BGR2GRAY),127,255,cv.THRESH_BINARY)

image,conturs,hier = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv.boundingRect(c)

    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2))
    rect = cv.minAreaRect(c)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(img,[box],0,(0,0,255),3)
    (x,y),radius = cv.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    img = cv.circle(img,center,radius,-1,(255,0,0),1)

cv.drawContours(img,contours,-1,(255,0,0),1)
cv.imshow("contours",img)
