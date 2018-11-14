# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 11:27:51 2018

@author: Administrator
"""
import string
import json
f = open("test_reflector_map.json","r")
try:
    all_the_text = f.read()
    print()
map = json.load(f)
for t in map:
    t = dic['id'],dic['reflectors']
    print(int ['id'])
    print (int ['reflectors'])
    
    
    
    