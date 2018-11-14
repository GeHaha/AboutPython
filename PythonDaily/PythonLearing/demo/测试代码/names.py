# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 20:24:44 2018

@author: Administrator
"""

from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first ==("q"):
        break
    last = input("Pleas give me a last name: ")
    if last == ("q"):
        break
    formatted_name = get_formatted_name(first,last)
    print("\nNeatly formatted name : " + formatted_name + ".")
    