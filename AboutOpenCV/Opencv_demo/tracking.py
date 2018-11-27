# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 19:13:28 2018

@author: Gehaha
"""
"""
1.Take each frame of the video
2.convert from BGR to HSV color-space
3.we threshold the HSV image for a range of blue color
4.Now extract the blue object alone,we can do whatever on that image we want

"""
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    _, frame = cap.read()
    # 将BGR转换为HSV
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    #在HSV中定义蓝色范围
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    # 阈值HSV图像只能得到蓝色
    mask = cv.inRange(hsv,lower_blue,upper_blue)
    #反转数组的每一位，函数cv::bitwise_not计算输入数组的每个元素逐位逆序:
    res = cv.bitwise_and(frame,frame,mask = mask)
    
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
