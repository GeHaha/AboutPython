# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:34:54 2018

@author: Administrator
"""

import json
f = open(r'C:\Users\Administrator\Desktop\test_reflector_map.json','r')
test = json.load(f)
for t in test:
    print (t ['id'])  
    print(t['reflectors'])
