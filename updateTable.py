#coding=utf-8
'''
Created on 2018年3月14日

@author: ChenJunhan
'''

import pymysql

db = pymysql.connect("localhost", "root", "123456", "test")

cursor = db.cursor()
sql = "UPDATE EMPLOYEE SET AGE = 123 WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
