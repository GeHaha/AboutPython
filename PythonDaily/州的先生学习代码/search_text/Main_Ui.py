# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:09:24 2019

@author: Gehaha
"""
from PyQt5 import QtWidgets,QtCore,QtGui
import sys
import os

from Text_Read import TextRead


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("本地文件搜索")
        self.main_widget= QtWidgets.QWidget()
        self.main_widget_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_widget_layout)
        
        
        self.search_input = QtWidgets.QLineEdit()
        self.search_btn = QtWidgets.QPushButton("搜索")
        self.search_result = QtWidgets.QListWidget()

        self.main_widget_layout.addWidget(self.search_input,0,0,1,2)
        self.main_widget_layout.addWidget(self.search_btn, 0, 2, 1, 1)
        self.main_widget_layout.addWidget(self.search_result, 1, 0, 3, 3)

        self.setCentralWidget(self.main_widget)
        
        self.search_btn.clicked.connect(self.search_slot)
        self.search_result.itemDoubleClicked.connect(self.view_item_slot)
        
        
        
    def search_slot(self):
        kw = self.search_input.text() #获取收缩词
        self.search_result.clear() #清空搜索结果列表
        for root,dirs,files in os.walk("."):
            print(root,dirs)
            for file in files:
            
                if os.path.splitext(file)[1] == '.txt': #匹配txt格式的文件
                    with open(file,encoding = 'utf-8') as files:
                        content = files.read()
                    if kw in content:
                        a = "{0}/{1}".format(root,file)#获取文件的路劲
                        f = QtWidgets.QListWidgetItem(a) # 创建一个搜索结果项
                        self.search_result.addItem(f) #将搜索结果添加到搜索部件中
                    
    def view_item_slot(self,event):
        file_name = event.text()
        content = TextRead(file = file_name)
        content.show()
        content.exec_()
        
                
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()