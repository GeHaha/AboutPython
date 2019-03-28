# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:14:56 2019

@author: Gehaha
"""

import sqlite3

conn = sqlite3.connect('test1.db')
c = conn.cursor()

print('open database sucessfully');
c.execute(''' CREATE TABLE COMPANY
          (ID INT PRIMARY KEY     NOT NULL,
           NAME          TEXT     NOT NULL,
           AGE           INT      NOT NULL,
           ADDRESS       CHAR(50),
           SALARY         REAL);''')
print("Table create successfully")
conn.commit()
conn.close()