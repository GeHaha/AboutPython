# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:19:16 2018

@author: Gehaha
"""

import numpy as np
import cv2 as cv 

#首先创建了200x200的黑色空白图像，
img = np.zeros((200,200),dtype = np.uint8)
img[50:150,50:150] = 255

ret ,thresh = cv.threshold(img,127,255,0)  # 二值化

# 找轮廓，三个参数，输入图像，层次类型，轮廓逼近
image,contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# 三个返回值：修改后的图像、图像的轮廓以及它们的层次

#画轮廓
color = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
img = cv.drawContours(color,contours,-1,(0,255,0),2)

cv.imshow("contours",color)
cv.waitKey()
cv.destroyAllWindows()
