# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:41:54 2018

@author: Administrator
"""

filename_1 =("cats.txt")
filename_2 =("dogs.txt")


try:
    with open(filename_1) as f_obj_1:
        contens_1 = f_obj_1.read()
        print(contens_1)
    with open(filename_2) as f_obj_2:
        contens_2 = f_obj_2.read()
        print(contens_2)
                             
except FileNotFoundError:
    msg_1 = (" sorry ,the file " + filename_1 +" dose not exit")
    print(msg_1)
    msg_2 = ( "sorry ,the file " + filename_1 +" dose not exit")
    print(msg_2)
    
else:
    print(" there are all of my pets")
    


























        