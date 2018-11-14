# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:39:59 2018

@author: Administrator
"""

import json
filename = ("favoritenumber.json")

try:
    with open(filename) as f_obj:
        favoritenumber = json.load(f_obj)
except FileNotFoundError:
    
    favorite_number = input("请输入你最喜欢的数字：")
    with open(filename,'w') as f_obj:
        json.dump(favoritenumber,f_obj)
        print("I kown you favorite number !It's" + favorite_number +".")
else:
    print("I remember you favorite number !It's" + favorite_number +".")
    
