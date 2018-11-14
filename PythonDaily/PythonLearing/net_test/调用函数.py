# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:29:15 2018

@author: Administrator
"""

def hello_world():
    print('hello world')

def three_hellos():
    for i in range(3):
        hello_world()
        
if __name__ == '__main__':
    three_hellos()
    