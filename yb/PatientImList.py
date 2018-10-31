#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *

class GetpatientImList:
    '''获取患者列表'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/customer/doctor/patientImList'
        self.token = Client.TOKEN
        self.client = Client(url=self.url)
    def tearDown(self):
        self.client.result()
    def test_patientImList(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,"doctorUserId":"141273"})
        cl.send()
        cl.equal(cl.status_code,0)
        cl.less_than(cl.times,200)
        cl.equal(cl.json.get('info'),'请求成功')
