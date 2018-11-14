# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:11:49 2018

@author: Administrator
"""

import wx
import telnetlib
from  time import sleep
import _thread as thread

class LogibFrame(wx.Frame):
    """登陆窗口"""
    def __init__(self, parent, id, title,size):
        #初始化，添加控件并绑定事件
        wx.Frame.__init__(self,parent,id,title)
        self.SetSize(size)
        self.Center()
        self.serverAddressLabel = wx.StaticText(self,label="Server Address", pos=(10,50),size=(120,25))
        self.userNameLabel=wx.StaticText(self,label="UserName"，pos=(40, 100), size=(120,25))
        self.serverAddress = wx.TextCtrl(self,pos=(120,47),size=(150,25))
        self.userName = wx.TextCtrl(self,pos=(120,97),size=(150,25))
        self.loginButton = wx.Button(self,label='Login'，pos=(80,145),size=(130,30))
        #绑定登陆方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        self.Show()
        
    def login(self,event):
        #登陆处理
        try:
            serverAddress = self.serverAddress.GetLineText(0).split(':')
            con.open(serverAddress[0],port=int(serverAddress[1],timeout=10))
            response = con.read_some()
            if response !=b'Connect Success':
                self.showDialog('Error','Connect Fail!',(200,100))
                return
            con.write('login' +str(self.userName.GetLineText(0) +'\n').encode("utf-8"))
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        