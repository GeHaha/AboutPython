# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 20:49:58 2019

@author: Gehaha
"""

import logging

# 使用logging模块的basciConfig()方法，修改一个日志输出等级为INFO:
logging.basicConfig(level = logging.INFO,filename = 'test.log')
logging.error("出现错误了")
logging.info("打印信息")
logging.warning("警告信息")