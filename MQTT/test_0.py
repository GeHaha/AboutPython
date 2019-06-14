# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:41:36 2019

@author: Gehaha
"""

# coding=utf-8
import json
import threading

import paho.mqtt.client as mqtt

# 当连接上服务器后回调此函数
import time

from my_lib.code_handle.code_handle import auto_code
from windows_info.read_info import Win_psutil


class MqttClient:
    client = mqtt.Client('tester')

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.client.on_connect = self._on_connect  # 设置连接上服务器回调函数
        self.client.on_message = self._on_message  # 设置接收到服务器消息回调函数

    def connect(self, username='tester', password='tester'):
        self.client.username_pw_set(username, password)
        self.client.connect(self._host, self._port, 60)  # 连接服务器,端口为1883,维持心跳为60秒

    def publish(self, topic, data):
        self.client.publish(topic, data)

    def loop(self, timeout=None):
        thread = threading.Thread(target=self._loop, args=(timeout,))
        # thread.setDaemon(True)
        thread.start()

    def _loop(self, timeout=None):
        if not timeout:
            self.client.loop_forever()
        else:
            self.client.loop(timeout)

    def _on_connect(self, client, userdata, flags, rc):
        print("\nConnected with result code " + str(rc))
        client.subscribe("test-0")

    def _on_message(self, client, userdata, msg):  # 从服务器接受到消息后回调此函数
        print ("\n主题:" + auto_code(str(msg.topic)) + " 消息:" + auto_code(str(msg.payload)))

    def _is_json(self, data):
        try:
            json.loads(data)
        except ValueError:
            return False
        return True

    def publish_loop(self):
        pass


if __name__ == '__main__':
    
    host=None
    client = MqttClient(host, 1883)
    client.connect('tester','tester')
    client.publish('test-0', '我上线啦!')
    client.loop()
    wp = Win_psutil()#自己定义的一个类
    while True:
        data_json=wp.auto_json()#方法返回一个包含CPU和进程信息的JSON字符串
        client.publish('test-0',data_json)
        time.sleep(2)
