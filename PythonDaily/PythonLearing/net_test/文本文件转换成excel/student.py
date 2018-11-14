# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:06:02 2018

@author: Administrator
"""

import re   #re模块（Regular Expression 正则表达式）提供各种正则表达式的匹配操作，在文本解析、复杂字符串分析和信息提取时是一个非常有用的工具
#re的主要函数：complie、search、match、split、findall（finditer）、sub（subn）

import xlwt #打开excel文件

def readxls(x):
    
    datatable = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    newsheet = datatable.add_sheet('student', cell_overwrite_ok = True)
    num = 0
    with open(x, 'r') as f:
        text = f.read()
        infomation = re.compile(r'"(\d+)":\["(.*?)",(\d+),(\d+),(\d+)]')
        #\d表示数值，+表示前面'\d'即数字这种类型字符至少出现一次，'.'表示除换行符外的任意字符，
        #'*'表示前面'.'出现任意次数（包括0次），'?'匹配表达式0次或者1次
        for x in infomation.findall(text):
            for i in range(len(x)):
                newsheet.write(num, i, x[i])
            num += 1

        datatable.save('student.xls')
readxls('student.txt')
