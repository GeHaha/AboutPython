# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:36:03 2018

@author: Administrator
"""
"""
filename = ('filtered_words.txt')
contens =  input("请输入内容：")

for filter_word in open(filename):
     
    if filter_word.rstrip() in contens:#使用rstrip()去掉右边的跨行符
        filter_words.append(filter_word.rstrip())   
        print(filter_words)  
    
        #filter_word.replace(, '*')
        #print(contens)
        
      #  break
#else:
 #   print("Human Rights")
   
"""

"""
user_input = input("请输入内容 ：")
print(user_input)
for filter_word in open('filtered_words.txt'):
    
    if filter_word.rstrip() in user_input:
    
        user_input.replace()
        print('Freedom')
        break
else:
    print('Human Rights')
    
"""

"""
filtered = []

def get_filtered_words():
     f = open()

"""



user_input = input("请输入内容：")
for filter_word in open('filtered_words.txt'):
    fw = filter_word.rstrip()
    if fw in user_input:
        fw_len = len(fw)
        user_input= user_input.replace(fw,'*'*fw_len)
        print(user_input)
        
           

            





























