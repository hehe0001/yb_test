#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import GetYTXAccountLoginStatus
import List
import GetConcernDoctorList
from xml.etree import ElementTree as ET
import HTMLTestReportCN
import pymysql
import client

if __name__ == '__main__':

        suite = unittest.TestSuite()
        suite.addTest(GetYTXAccountLoginStatus.GetYTXAccountLoginStatus('test_getYTXAccountLoginStatus'))
        suite.addTest(List.List('test_list'))
        suite.addTest(GetConcernDoctorList.GetConcernDoctorList('test_getConcernDoctorList'))
        unittest.TextTestRunner().run(suite)
        suite = unittest.defaultTestLoader.discover(start_dir= './')
        print suite
        runner = unittest.TextTestRunner()
        runner.run(suite)
        unittest.TextTestRunner().run(suite)



