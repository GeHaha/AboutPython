# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:46:28 2018

@author: Gehaha
"""

import cv2
import numpy as np


img = cv2.imread('MyPic.png')
print(img.shape)
print(img.size) # 指图像像素的大小
print(img.dtype) # datatype 会得到图像的数据类型，一般为一个无符号整数类型的变量和该类型占的位数

# 返回图片的宽度，高度，和通道数，图像是单色或者灰度的，将不包含通道值(1800, 2880, 3)
# 15552000
uint8