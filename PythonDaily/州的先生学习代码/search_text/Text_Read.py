# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:09:28 2019

@author: Gehaha
"""

from PyQt5 import QtWidgets


class TextRead(QtWidgets.QDialog):
    def __init__(self,file = None):
        super().__init__()
        self.setWindowTitle("文本内容-{}".format(file))
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        
        text = QtWidgets.QTextEdit()
        text.setReadOnly(True)
        
        self.layout.addWidget(text)
        try:
            with open(file,encoding = 'utf-8') as files:
                content = files.read()
            text.setText(content)
        except Exception as e:
            print(e)
            
            