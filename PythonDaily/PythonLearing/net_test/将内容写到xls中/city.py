# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:38:32 2018

@author: Administrator
"""
import re
import xlwt
  
def readxls(x):
    
    datatable = xlwt.Workbook(encoding = 'utf-8',style_compression = 0)#创建一个工作簿
    newsheet = datatable.add_sheet('city',cell_overwrite_ok = True) #创建一个工作表
    num = 0
    with open(x,'r') as f:
        text = f.read()
        information = re.compile(r'"(\d+)" : "(.*?)"')#使用正则表达式，读取文本文件中数据的格式
        
        for x in information.findall(text):
            for i in range(len(x)):
                newsheet.write(num, i, x[i])
            num += 1      
        datatable.save('city.xls')
readxls('city.txt')
