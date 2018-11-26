# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:47:25 2018

@author: Gehaha
"""
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret ,frame = cap.read()
    if ret == True:
        frame = cv.flip(frame,0)
        
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
out.release()
cv.destroyAllWindows()

