# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:33:46 2018

@author: Administrator
"""
"""
filename =("learning_python.txt")

with open(filename) as file_object:
    
    contents = file_object.read()
    print(contents)
    
with open(filename) as file_object:
    
    
    
with open(filename) as file_object:
    
    for line in file_object:
        print(line)
"""
"""
with open(filename,'a') as file_object:   
    
#'a'不覆盖原本txt中的内容，且添加到文件的末尾'w'覆盖了原本txt的内容 
   
    
    file_object.write("i love python\nl love programming.")
    file_object.write("hengheng")
    
"""  
"""
#提示用户输入其名字，用户作出反应后将其名字写入到文件中
filename =("guest.txt")
user_name = input("请输入用户名 ：")
user_information =("毕业于浙江科技大学，专业：建筑电气与智能化，年龄：22\n婚否：未婚，现居地址：浙江平湖市乍浦镇")

with open (filename,'a') as file_object:
    file_object.write(user_name)
    file_object.write(user_information)

"""
"""
filename =("guest_name.txt")
user_name = input("请输入用户名： ")

while user_name:
    print("欢迎" + user_name +"先生(女士)的访问我们的网站!")
    break
  
with open(filename,'a') as file_object:
    file_object.write(user_name)
"""













































































































































































































  
    
    
