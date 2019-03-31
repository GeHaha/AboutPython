# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:57:40 2019

@author: Gehaha
"""

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:63342")

mydb = myclient["gehaha"]
collist = mydb.list_collection_names()
if "sites" in collist:
    print("集合已存在")