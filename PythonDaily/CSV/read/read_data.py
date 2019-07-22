# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:58:05 2019

@author: Gehaha
"""

import csv

filename = open('public.test.csv',encoding='UTF-8')

with filename as f:
     #创建cvs文件读取器
     reader = csv.reader(f)
     
     #读取第一行，这行是表头数据
     header_row = next(reader)
     
     print(header_row)
     
     #读取第二行
     first_row = next(reader)
     print(first_row)
     
     