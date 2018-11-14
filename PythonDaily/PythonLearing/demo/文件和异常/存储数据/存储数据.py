# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 15:51:14 2018

@author: Administrator
"""
"""
import json
numbers =[2,3,4,5,6,7]
filename = ("numbers.json")
with open(filename, 'w') as f_obj:
    json.dump(numbers,f_obj)
"""  
"""
import json
username = input("what is your name?")

filename = ("username.json")

with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("we'll remember you when you come back, " + username + "!")

"""
"""
import json
filename = ("username.json")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("welcome back ", username + "!")
    
"""
"""
import json
filename = ('username.json')
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
        
except FileNotFoundError:
    
    username = input("what is you name")
    with open(filename, 'w') as f_obj:
        json.dump(username,f_obj)
        print("we'll remember you when you come back," + username +'!')    
else:
    print("welcome back, " + username + "!")

"""








































   


















