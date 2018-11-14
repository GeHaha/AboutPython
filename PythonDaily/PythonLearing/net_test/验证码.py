# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 16:36:24 2018

@author: Administrator
"""

import random
import string

#生成验证码
def GenKey(length):
    chars = string.ascii_letters + string.digits  #激活码中的字符和数字
    return ''.join([random.choice(chars) for i in range(length)]) #获得四个字母和数字的随机组合

#保存验证码
def SaveKey(content):
    f = open('Result Key.txt', 'a')
    f.write(content)
    f.write('\n')
    f.close()


if __name__ == '__main__':
    for i in range(20):    #输出20个验证码
        value = GenKey(15) #，每个验证码长度是15个字符
        print (value)
        SaveKey(value)

chars = string.ascii_letters + string.digits
result = ''.join([random.choice(chars) for i in range(15)])
print (result)