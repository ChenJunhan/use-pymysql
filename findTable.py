#coding=utf-8
'''
Created on 2018年3月14日

@author: ChenJunhan
'''

import pymysql
db = pymysql.connect("localhost", "root", "123456", "test")

cursor = db.cursor()

sql = sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %d" % (1000)
    
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[1]
        lname = row[2]
        age = row[3]
        sex = row[4]
        income = row[5]
        
        print("name = %s, age = %s, sex = %s, income = %s" % (fname, lname, age, sex, income))

except:
    # tarceback将异常打印出来
    import traceback
    traceback.print_exc()
    
    print("Error: unable to fetch data")

db.close()