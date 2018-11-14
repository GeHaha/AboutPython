# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:06:37 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 1])
plt.ion()

for i in range(100):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.1)
plt.show()