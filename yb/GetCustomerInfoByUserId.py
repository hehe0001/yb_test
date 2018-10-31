#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *

class GetCustomerInfoByUserId:
    '''获取用户个人资料'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/customerInfo/getCustomerInfoByUserId.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url)
    def tearDown(self):
        self.client.result()
    def test_getCustomerInfoByUserId(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token})
        cl.send()
        cl.equal(cl.status_code,100)
        cl.less_than(cl.times,200)
        cl.equal(cl.json.get('info'),'获得用户个人资料成功')