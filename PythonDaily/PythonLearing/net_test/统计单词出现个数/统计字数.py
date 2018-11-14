# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:16:20 2018

@author: Administrator
"""


filename = ('english.txt')
count={}
with open (filename) as file_object:
    for line in file_object:
        for character in line:
            count.setdefault(character,0)
            count[character] = count[character] +1
    print(count)
    
            