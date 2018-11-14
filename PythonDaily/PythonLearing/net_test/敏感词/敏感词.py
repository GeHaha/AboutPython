# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:42:34 2018

@author: Administrator
"""

filename = ('filtered_words.txt')
contens =  input("请输入内容：")
for filter_word in open(filename):
     
    if filter_word.rstrip() in contens:#使用rstrip()去掉右边的跨行符
        
        print("Freedom")
        break
else:
    print("Human Rights")
    

       

"""
user_input = input("请输入内容 ：")
print(user_input)
for filter_word in open('filtered_words.txt'):
    
    if filter_word.rstrip() in user_input:
        print('Freedom')
        break
else:
    print('Human Rights')
    
 """   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    