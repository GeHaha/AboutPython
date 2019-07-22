# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:14:20 2019

@author: Gehaha
"""
import requests

r = requests.get('https://api.github.com/user',auth=('user','pass'))
print(r.status_code)
