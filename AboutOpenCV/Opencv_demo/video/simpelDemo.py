# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:47:59 2018

@author: Gehaha
"""

import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print(events)
