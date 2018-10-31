#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class Get(unittest.TestCase):
    '''get'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/cache/get.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.GET)
    def tearDown(self):
        self.client.result()
    def test_get(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                     "processDefinitionId":cl.value("processDefinitionId"),
                     "key":"mall_service_apply_form"})
        cl.send()
        cl.equal(cl.status_code, 200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),0)
        s = cl.json.get('info')
        cl.is_contain(s,u"请求成功")
