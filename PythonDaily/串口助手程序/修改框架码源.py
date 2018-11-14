# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 15:15:23 2018

@author: Administrator
"""

import sys
import serial
import threading
import binascii 
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 141, 311))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 41, 16))
        self.label_5.setObjectName("label_5")
        
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setGeometry(QtCore.QRect(60, 20, 71, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 50, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
  #更改波特率
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_1.setGeometry(QtCore.QRect(60, 50, 71, 22))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        
        
      
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 110, 71, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 140, 71, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        
        #打开
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 51, 23))
        self.pushButton.setObjectName("pushButton")
        
        #关闭
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 200, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        
        #打开文件
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 280, 55, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        
        #发送文件
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 280, 55, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 41, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(70, 170, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 10, 411, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 391, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 200, 261, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 241, 91))
        self.textEdit.setObjectName("textEdit")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(430, 210, 61, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(500, 210, 61, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        
        #清除
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 240, 61, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        #发送
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 280, 61, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        
        #新加pushButton_6是显示按钮，弹出实时图像
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 260, 61, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        
    
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());  
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial_gui"))
        self.groupBox.setTitle(_translate("MainWindow", "串口设置"))
        self.label.setText(_translate("MainWindow", "串 口"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.label_3.setText(_translate("MainWindow", "校验位"))
        self.label_4.setText(_translate("MainWindow", "数据位"))
        self.label_5.setText(_translate("MainWindow", "停止位"))
        
       # self.lineEdit_3.setText(_translate("MainWindow", "9600"))
       
        self.comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5"))
        
        #增加的波特率
        self.comboBox_1.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "14400"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "19200"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "38400"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "56000"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "57600"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "115200"))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "128000"))
      
    
        #校验位
        self.comboBox_2.setItemText(0, _translate("MainWindow", "N"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "E"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "O"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "M"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "S"))
        
        #停止位
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2"))
        
        #串口
        self.comboBox_4.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "COM10"))
        
        
        #按钮类
        self.pushButton.setText(_translate("MainWindow", "打开"))     
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        
        self.pushButton_3.setText(_translate("MainWindow", "检测串口"))     
        self.label_11.setText(_translate("MainWindow", "状 态："))
        self.label_12.setText(_translate("MainWindow", "串口状态"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送区"))
        
        
        self.checkBox.setText(_translate("MainWindow", "Hex显示"))
        self.checkBox_2.setText(_translate("MainWindow", "Hex发送"))
        self.pushButton_4.setText(_translate("MainWindow", "清除接收"))   
        self.pushButton_5.setText(_translate("MainWindow", "发送"))
        self.pushButton_7.setText(_translate("MainWindow", "打开文件"))   
        self.pushButton_8.setText(_translate("MainWindow", "发送文件"))
        
        #显示图像
        self.pushButton_6.setText(_translate("MainWindow", "PID图像"))
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 