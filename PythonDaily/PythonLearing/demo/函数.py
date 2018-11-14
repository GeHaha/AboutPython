# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:16:00 2018

@author: Administrator
"""

    
def testB():
    print("-------testB start------")
    print("这里是testB函数执行的代码")
    print('----testB end-----------')
def testA():
    print("------testA start-------")
    testB()
    print('-------testA end--------')
testA() 