# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:27:02 2019

@author: Gehaha
"""

import sqlite3

conn = sqlite3.connect('company.db')
print('open database successfully');

c = conn.cursor();
c = conn.cursor()



print("Table created successfully");
"""

# 下面的 Python 代码显示了如何连接到一个现有的数据库。如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象。
import sqlite3

conn = sqlite3.connect('test.db')

print "Opened database successfully";


#下面的 Python 代码段将用于在先前创建的数据库中创建一个表：
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";
conn.commit()
conn.close()



#下面的 Python 程序显示了如何在上面创建的 COMPANY 表中创建记录：
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");



#下面的 Python 程序显示了如何从前面创建的 COMPANY 表中获取并显示记录：
cursor = c.execute("SELECT id,name,address,salary from COMPANY")


#下面的 Python 代码显示了如何使用 UPDATE 语句来更新任何记录，然后从 COMPANY 表中获取并显示更新的记录：
c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()

cursor = conn.execute("SELECT id ,name,address, salary from COMPANY")

for row in cursor:
    print("ID = ",row[0])
    print("NAME =",row[1])
    print("ADDRESS = ",row[2])
    print("SALARY = ",row[3]),"\n"
"""

c.execute("DELETE from COMPANY where ID = 2;")
conn.commit()

print("Total number of rows deleted :",conn.total_changes)

cursor = conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("ADDRESS = ",row[2])
    print("SALARY = ",row[3],"\n")
    

print("Operation done successfully");
conn.close()

