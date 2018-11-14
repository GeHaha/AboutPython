# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:45:57 2018

@author: Gehaha
"""

#导入cv模块
import cv2 as cv
#读取图像。支持bmp，jpg，png，tiff等常用格式
img = cv.imread(r"D:\PYTHON\AboutOpenCV\Opencv_demo\first_demo\test.png")
#创建窗口并显示图像
cv.namedWindow('Image')
cv.imshow('Image',img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()
