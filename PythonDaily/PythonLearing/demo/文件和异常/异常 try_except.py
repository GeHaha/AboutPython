# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 13:13:15 2018

@author: Administrator
"""
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")
"""
"""
print("Give me two numbers,and i'll divide them .")
print("Enter ' q ' to quit.")
while True:
    
    first_number = input("\nFirst number: ")
    if first_number == ("q"):
        break
    second_number = input("second number: ")
    
    try:
         answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0")
    else:
        print(answer)
        
"""
"""

filename = ("alice.txt")

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = ("sorry,the file " + filename + " dose not exist")
    print(msg)
"""
"""
print("give me two number,I'ii add them . ")
print("Enter 'q' to quit it")

while True:
    first_name = input("\nFirst number :")
    if first_name == ('q'):
        break
    second_number = input("second number :")
    
    try:
        result = int(first_name) +int(second_number)
    except ValueError:
        print("您输入的是文本，请输入数字")
    else:
        print(result)
        
"""


































































    