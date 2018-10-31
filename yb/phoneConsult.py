#!/user/bin/env python
#_*_ coding:utf-8 _*
import unittest
import requests
from client import *
class PhoneConsult:
    '''电话咨询结果'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/commodity/phoneConsult'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.GET)
    def tearDown(self):
        self.client.result()
    def test_phoneConsult(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                     "doctorUserId":cl.value("doctorUserId"),"patientId":"1964"})
        cl.send()
        cl.equal(cl.status_code,0)
        cl.less_than(cl.times,200)
        cl.equal(cl.json.get('info'),'请求成功')