# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:05:52 2019

@author: Gehaha
"""

import h5pyd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.spatial import cKDTree

f = h5pyd.File("/nrel/nsrdb/nsrdb_2012.h5",'r')
list(f.attrs)
