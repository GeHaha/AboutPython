# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:25:05 2018

@author: Administrator
"""
import matplotlib.pyplot as plt
#import numpy as np
import json

filename =("test_reflector_map.json")

with open(filename) as f:
    test = json.load(f)    
    for c in test:
        id_coordinate = c['id']
        reflectors = c['reflectors']
        print(reflectors)

plt.plot(reflectors,'r-o')
plt.show()
