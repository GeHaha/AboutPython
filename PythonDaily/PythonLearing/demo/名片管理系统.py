# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def displayMenu():
    print("-"*40)
    print("      名片管理系统     ")
    print("1.  添加名片")
    print("2.  删除名片")
    print("3.  修改名片")
    print("4.  查询名片")
    print("6.  退出系统")
    print("-"*40)
i = 0
while i<1:
    displayMenu()
def getChoice():
    selectedKey = input("请输入选着的序号：")
    return int(selectedKey)
key= getChoice()
if key == 1:
    pass
elif key ==2:
    pass
elif key ==3:
    pass
elif key ==4:
    pass
elif key ==5:
    pass
elif key ==6:
    pass
else:
    print("输入有误，请重新输入...")
    

    