# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:14:30 2018

@author: Gehaha
"""

import numpy as np
import cv2 as cv

img = cv.imread('gehaha.jpg',0)
rows,cols = img.shape

M = np.float32([1,0,100],[0,1,50])
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
