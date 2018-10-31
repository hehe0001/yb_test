#!/user/bin/env python
#_*_ coding:utf-8 _*_
import MySQLdb
db = MySQLdb.connect('rm-bp1222991107b88x0public.mysql.rds.aliyuncs.com',
                     'yibao_test',
                     '@9aad8327f',
                     'yibao_test')
cursor = db.cursor()

cursor.execute("SELECT * FROM yb_order WHERE fpatientid IN ('2255')")