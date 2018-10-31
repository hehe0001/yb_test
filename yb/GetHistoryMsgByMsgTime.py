#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class GetHistoryMsgByMsgTime(unittest.TestCase):
    '''获取历史会话'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/im/getHistoryMsgByMsgTime.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.GET)
    def tearDown(self):
        self.client.result()
    def test_getHistoryMsgByMsgTime(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,"num":"20",
         "voip":"80002500000131","msgTime":"-1","patientId":"1964"})
        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),0)
        s = cl.json.get('info')
        cl.equal(s,u'请求成功！')