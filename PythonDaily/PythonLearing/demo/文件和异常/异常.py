# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:13:15 2018

@author: Administrator
"""

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")
    