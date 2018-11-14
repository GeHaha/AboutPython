# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:07:31 2018

@author: Administrator
"""
import json

filename =("test_reflector_map.json")
with open(filename) as f:
    test = json.load(f)    
    for c in test:
        id_coordinate = c['id']
        reflectors = c['reflectors']
        print(reflectors)