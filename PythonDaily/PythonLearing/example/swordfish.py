# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:56:13 2018

@author: Administrator
"""

while True:
    print("who are you ?")
    name = input()
    if name !=("joe"):
        continue
    print("Hello ,joe,what is the paasword?(it is a fish.)")
    password = input()
    if password ==("swordfish"):
        break
print("access granted.")

