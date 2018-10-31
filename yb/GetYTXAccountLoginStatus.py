#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
'''
解决UnicodeEncodeError: 'ascii' codec can't encode characters in position问题
引入sys包
'''
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class GetYTXAccountLoginStatus(unittest.TestCase):
    '''查看登录状态'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/im/getYTXAccountLoginStatus.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.GET)
    def tearDown(self):
        self.client.result()
    def test_getYTXAccountLoginStatus(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token})
        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),100)
        # cl.equal(cl.json.get('isLogin'),1)
        print type(cl.json.get('info'))
        s = cl.json.get('info')
        cl.is_contain(s,u"请求成功！")
