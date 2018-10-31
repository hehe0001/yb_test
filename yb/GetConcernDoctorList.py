#!/user/bin/env python
#_*_ coding:utf-8 _*_

import unittest
import requests
from client import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class GetConcernDoctorList(unittest.TestCase):
    '''获取关联医生列表'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/serviceGroup/getConcernDoctorList.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url, method=Method.GET)

    def tearDown(self):
        self.client.result()

    def test_getConcernDoctorList(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                     "start":"0","size":"10"})
        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'), 0)
        s = cl.json.get('info')
        cl.is_contain(s,u"请求成功")

