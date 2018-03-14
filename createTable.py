import pymysql

db = pymysql.connect('localhost', 'root', '123456', 'test')

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS employee')

sql = """CREATE TABLE `employee` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `first_name` char(20) NOT NULL,
  `last_name` char(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `income` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

cursor.execute(sql)

print("Created table Successful.")

db.close()