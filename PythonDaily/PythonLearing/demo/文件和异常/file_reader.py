# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:24:20 2018

@author: Administrator
"""
"""
with open('123.txt') as file_object:
    contents = file_object.read()
    print(contents)
   
 """   
"""
filename = ("123.txt")

with open(filename) as file_object:
    for line in file_object:
        print(line)
"""
"""
filename = ("123.txt")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
"""

























