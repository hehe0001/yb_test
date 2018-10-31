#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *

class GetAreaList:
    '''获取城市信息'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/fullProcess/getAreaList'
        self.token = Client.TOKEN
        self.client = Client(url=self.url)
    def tearDown(self):
        self.client.result()
    def test_getAreaList(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token})
        cl.send()
        cl.equal(cl.status_code,0)
        cl.less_than(cl.times,200)
        cl.equal(cl.json.get('info'),'获取城市列表成功！')