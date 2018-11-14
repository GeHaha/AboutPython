# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 09:36:00 2018

@author: Administrator
"""
def collatz(number):
    if number%2 == 0:
        print(number//2)
        return(number//2)
    else:
        print(3*number+1)
        return(3*number+1)
print("entry you number :")
try:
    nu =int(input())
    while True:
        nu = collatz(nu)
        if nu == 1:           
            break
except ValueError:
    print("请输入整数!")
            
    
    
    
        