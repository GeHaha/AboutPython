# -*- coding: utf-8 -*-
"""
Created on Thu May 23 17:04:32 2019

@author: Gehaha
"""

import paho.mqtt.client as mqtt
HOST = "dolphkon.com"
PORT = 1833

def testPub():
    client = mqtt.Client()
    client.connect(HOST,PORT,60)
    print("连接成功！")
    client.publish("许嵩","雅俗共赏",2)
    client.loop_forever()
    
if __name__ == '__main__':
    testPub()
    