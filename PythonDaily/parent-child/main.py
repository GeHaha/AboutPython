# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:38:57 2019

@author: Gehaha
"""

from mainWindow import Ui_MainWindow
from qw import Ui_Form
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QWidget
import sys

class parentWindow(QMainWindow): 
    def __init__(self): 
        QMainWindow.__init__(self) 
        self.main_ui = Ui_MainWindow() 
        self.main_ui.setupUi(self)




class childWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.child=Ui_Form()
        self.child.setupUi(self)


def main():
    app=QApplication(sys.argv) 
    window=parentWindow() 
    child=childWindow() #通过toolButton将两个窗体关联 
    btn=window.main_ui.pushButton 
    btn.clicked.connect(child.show) # 显示 
    window.show() 
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()
    
