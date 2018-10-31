#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
from xml.etree import ElementTree as ET
import HTMLTestReportCN
import pymysql
import client

if __name__ == '__main__':

    et = ET.parse('./config.xml')
    li = et.findall('./cases/*')
    data_configs = et.findall('./database/*')
    database = {}
    for d in data_configs:
        database[d.tag] = d.text

    else:
        print database
        client.Client.DB = pymysql.connect(host=database.get('host'),
                                           user=database.get('user'),
                                           password=database.get('password'),
                                           db=database.get('db'))
        suite = unittest.TestSuite()
        for i in li:
            class_name = i.tag.split('-')[0]
            method_name = i.tag.split('-')[1]
            exec('import %s' %  class_name)
            exec("suite.addTest(%s.%s('test_%s'))" % (class_name,class_name,method_name))
            unittest.TextTestRunner().run(suite)
        HTMLTestReportCN.HTMLTestRunner(stream=open('./report.html', 'wb')).run(suite)
    if client.Client.DB:
        client.Client.DB.close()




