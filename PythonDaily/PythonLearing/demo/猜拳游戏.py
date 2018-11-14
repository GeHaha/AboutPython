# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:02:40 2018

@author: Administrator
"""

import random
playerInput = input("请输入(0剪刀、1石头、2布:)")
player = int(playerInput)
computer = random.randint(0,2)#自动输出0、1、2

if(player == 0 and computer == 2) or (player == 1 and computer == 0)\
   or (player == 2 and computer == 1):
        
       print("电脑出的拳头是%s,恭喜，你赢了!"%computer)
     
elif (player == 0 and computer == 0) or (player == 1 and computer == 1)\
   or (player == 2 and computer == 2):
       print("电脑出的拳头是%，打成平局了!"%computer)
else:
    print("电脑出的拳头是%s你输了，再接再厉!"%computer)
  
    
        
      
   