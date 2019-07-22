# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:44:46 2019

@author: Gehaha
"""

import pymongo
#myclient = pymongo.MongoClient(host = 'localhost',port = 63342)
myclient = pymongo.MongoClient("mongodb://localhost:63342")

mydb = myclient["gehaha"]

mycol = mydb["sites"]
