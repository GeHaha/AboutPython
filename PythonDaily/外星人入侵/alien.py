# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:14:03 2018

@author: Administrator
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #表示单个外星人的类
    def __init__(self,ai_settings,screen):
        #初始化外星人并设置其起始位置
        
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load("images/alien.bmp")
        
        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #储存外星人的准确位置
        self.x = float(self.rec.x)
        
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.iamge,self.rect)
        
    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right():
            return True
    def update(self):
        """向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        