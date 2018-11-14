# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:15:37 2018

@author: Administrator
"""

#导入socket库
import socket
import time
import threading



#创建一个socket,AP_INET指定使用IPv4，如果要用更先进的IPV6，指定为AF_INET6
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#监听端口
s.bind('127.0.0.1',9999)

s.listen(5)

print('Waiting for connection...')


while True:
    
    #接受一个新连接
    sock,addr = s.accept()
    
    #创建新线程来处理TCP连接
    t = threading.Thread(target = tcplink , args=(sock,addr))
    
    t.start()
    
def tcplink(sock,addr):
    print('Accept new connection from %s:&s..'%addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello. %s!'%data.decode('utf_8')).encode('utf-8'))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    