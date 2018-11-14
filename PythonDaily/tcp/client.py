# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:40:47 2018

@author: Administrator
"""
import socket

listA= ['Michael','Tracy','Sarah']

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#建立连接
s.connect(('127.0.0.1',9999))
#接收欢迎消息
print(s.recv(1024).decode('utf-8'))

for data in listA:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
    
s.send(b'exit')

s.close()
