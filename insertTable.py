#coding=utf-8
'''
Created on 2018年3月14日

@author: ChenJunhan
'''

import pymysql

# 创建连接
db = pymysql.connect("localhost", "root", "123456", "test")

# 创建游标
cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Su', 20, 'M', 5000)"""
   
try:
    cursor.execute(sql)   # 执行sql语句
    db.commit()           # 提交更改
except:
    db.rollback()         # 若报错则回滚


# 再插入一条数据
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Kobe', 'Bryant', 40, 'M', 8000)"""

try: 
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
print(sql)
print("Yes, Insert Successful")

db.close()   # 断开连接