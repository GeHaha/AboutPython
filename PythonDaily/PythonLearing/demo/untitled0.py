# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:29:48 2018

@author: Administrator
"""

import random
from PIL import ImageDraw,ImageFont


def randomColor():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return(red,green,blue)
    
def colorDifference(bg_color,text_color):
    d = 0
    for i in range(0,3):
        d +=(text_color[i] - bg_color[i]) ^ 2
    return(d)
    
root =(" ")
a = ord('a')
A = ord('A')
for i in range(0,26):
    root += chr(a + i)
    root += chr(A + i)
    
font = ImageFont.truetype(r'C:\Windows\Fonts\Calibri.ttf', 60)


for j in range(0,10):
    ans = ("")
    for i in range(0,4):
        ans += random.choice(root)
        bg_color = randomColor()
        bgImg = Image.new('RGB',(185,90),bg_color)#新建一个图片对象，背景颜色随机
        canvas = ImageDraw.Draw(bgImg)
        
        
        text_color = randomColor()
        while(colorDifference(bg_color, text_color) < 100):
            text_color = randomColor()
            
        canvas.text((0,0),ans, text_color, font)
        
        name = ans + '.jpg'
        bgImg.save(name,'jpeg')
        rstImg = Image.open(name)
        rstImg.show()
        
        
        inp = input('Please type in the characters in the image :')
        while inp != ans:
            inp = input('Incorrect input.Please try again :')
            
        
























