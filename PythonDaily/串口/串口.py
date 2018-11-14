# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:58:53 2018

@author: Administrator
"""

import sys
import serial
import serial.tools.list_ports

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class SerialDlg(QDialog):
    def __init__(self,parent = None):
        super(SerialDlg,self).__init__(parent)
        SerialCOMLable = QLabel(u'串口号')
        self.SerialCOMComboBox = QComboBox()
        self.SerialCOMComboBox.addItems(self.port_List())
        
        serialBaudRateLabel = QLabel(u'波特率')
        self.SerialBaudRateComboBox = QComboBox()
        self.SerialBaudRateComboBox.addItems(['100','300','600','1200','2400','4800','9600','14400'])
        self.SerialBaudRateComboBox.setCurrentIndex(3)
        
        
        SerialSTOPBitsLable = QLabel(u'停止位')
        self.SerialStopBitsComboBox = QComboBox()
        self.SerialStopBitsComboBox.addItems(['1','1.5','2'])
        self.SerialStopBitsComboBox.setCurentIndex(0)
        
        SerialParityLabel = QLabel(u'奇偶校验位')
        self.SerialParityComboBox.addItems(['NONE','EVEN','ODD','MARK','SPACE'])
        self.SerialParityComboBox.setCurrentIndex(0)
        
        
        self.OpenButton = QPushButton(u'打开串口')
        self.CloseButton = QPushButton(u'关闭串口')
        self.CloseButton.setDisable(True)
        
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.OpenButton)
        buttonLayout.addWidget(self.CloseButton)
        buttonLayout.addStretch()
        
        layout = QGridLayout()
        layout,addWidget(SerialCOMLabel,0,0)
        layout.addWidget(SerialCOMComboBox,0,1)
        layout.addWidget(self.SerialBaudRateLabel,1,0)
        layout.addWidget(self.SerialBaudRateComboBox,1,1)
        layout.addWidget(serialDataLabel,2,0)
        layout.addWidget(self.SerialDataComboBox,2,1)
        layout.addWidget(SerialSTOPBitsLabel,3,0)
        layout.addWidget(self.SerialStopBitsComboBox,3,1)
        layout.addWidget(SerialParityLabel,4,0)
        layout.addWidget(self.SerialParityComboBox,4,1)
        
        
        mainlayout = QVBoxLayout()
        mainlayout.addLayout(layout)
        mainlayout.addLayout(buttonLayout)
        
        self.setLayout(mainlayout)
        self.setWindowTitle(u'串口调试工具')
        
        self.connect(self.OpenButton,SIGNAL("clicked()"),self.OpenSerial)
    
        #获取COM号列表
def port_List(self):
    Com_List=[]
    port_list = list(serial.tools.list_ports.comports())
    for port in port_list:
        com_List.append(port[0])
    return Com_List
#打开串口
def OpenSerial(self):
    ser = serial.Serial()
    ser.port = self.SerialBaudRateComboBox.CurrentText()
    ser.baudrate = self.SerialBaudRateComboBox.currentText()
    ser.bytesize  = int(self.SerialDataComboBox.currentText())
    
    
    ParityValue = self.SerialParityComboBox.currentText()
    ser.parity = ParityValue[0]
    ser.stopbits =int(self.SerialStopBitsComboBox.currentText)
    ser.open()
    print(ser.isOpen)
    ser.close()
    print(ser.isOpen)


app = QApplication(sys.argv)
SerialDialog = SerialDlg()
SerialDialog.show()
app.exec()

    
             
        
        