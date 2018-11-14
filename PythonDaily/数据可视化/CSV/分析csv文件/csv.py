# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:34:29 2018

@author: Administrator
"""

import  csv
filename =(name.csv)
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    