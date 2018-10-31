#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class GetImMsgTemplateInfo(unittest.TestCase):
    '''获取IM消息模板信息'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/im/getImMsgTemplateInfo.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.GET)
    def tearDown(self):
        self.client.result()
    def test_getImMsgTemplateInfo(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token})
        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),0)
        s = cl.json.get('info')
        cl.equal(s,'请求成功！')