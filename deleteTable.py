#coding=utf-8
'''
Created on 2018年3月14日

@author: ChenJunhan
'''

import pymysql

db = pymysql.connect("localhost", "root", "123456", "test")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (40)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
