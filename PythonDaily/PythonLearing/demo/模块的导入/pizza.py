# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:41:21 2018

@author: Administrator
"""

def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
    
    for topping in toppings:
        print("- " + topping )