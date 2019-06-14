# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:44:01 2019

@author: Gehaha
"""
import paho.mqtt.client as mqtt
MQTTHOST = "dolphkon.com"
MQTTPORT = 1883

mqttClient = mqtt.Client()

# 连接MQTT服务器

def on_mqtt_connect():
    mqttClient.connect(MQTTHOST,MQTTPORT,60)
    mqttClient.loop_start()
    

#消息处理函数
def on_message_come(client,userdata,msg):
    print("话题:" + msg.topic + "" + "消息内容" + msg.payload.decode("utf-8"))


def on_subscribe():
    mqttClient.subscribe("Python",1)
    mqttClient.on_message = on_message_come #消息到来处理函数

def main():
    on_mqtt_connect()
    on_subscribe() 
    while True:
        pass
    
if __name__ == '__main__':
    main()
    