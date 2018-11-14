# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 20:17:22 2018

@author: Administrator
"""

import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button
from pygame.sprite import Group
from scoreboard import Scoreboard



def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()#初始化背景设置
    ai_settings = Settings() #全局设置
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))#创建screen显示窗口
   
    pygame.display.set_caption("Alien Invasion")#标题
    #新建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用于存储游戏系统统计信息的是咧，并创建记分牌
    stats =GameStats(ai_settings) 
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建子弹编组
    bullets = Group()
    #创建一个外星人
    aliens = Group()
    #创建外星人群
    gf.creat_fleet(ai_settings,screen,ship,aliens)
      
    #开始游戏的主循环
    while True:
        #监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, stats, sb,play_button, ship, aliens, bullets)
     
        if stats.game_active:
            #移动飞船
            gf.update_ship(ship)
            #更新子弹位置
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            #更新外星人
            gf.update_screen(ai_settings,stats,screen,sb,ship,aliens,bullets)
            #更新屏幕
            gf.update_screen(ai_settings,stats,screen,sb,ship,aliens,bullets,play_button)
            
run_game()




































