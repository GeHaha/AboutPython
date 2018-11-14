# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:24:27 2018

@author: Gehaha
"""

import cv2
import numpy
import os
 
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)

bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png',bgrImage)