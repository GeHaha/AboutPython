# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:47:30 2019

@author: Gehaha
"""



import sqlite3

conn = sqlite3.connect('test1.db')
c = conn.cursor()
print('open database sucessfully');
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES(1,'Paul',32,'California',20000.00)");
          
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES(2,'Allen',25,'Texas',15000.00)");

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES(3,'Teddy',23,'Norway',20000.00)");
          
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
          VALUES(4,'Mark',25,'Rich-Mond',65000.00)");
conn.commit()
print("Records create sucessfully")
conn.close()
