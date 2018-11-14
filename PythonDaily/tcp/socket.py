# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:46:22 2018

@author: Administrator
"""

#导入socket库
import socket

#创建一个socket,AP_INET指定使用IPv4，如果要用更先进的IPV6，指定为AF_INET6
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#建立连接
s.connect(('www.sina.com.cn',80))

#发送数据
s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

#接收数据
buffer = []
while True:
    #每次最多接收1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

#关闭连接
s.close()

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

#把接收的数据写入文件
with open('sina.html','wb') as f:
    f.write(html)
    


















