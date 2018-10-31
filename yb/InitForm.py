#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class InitForm(unittest.TestCase):
    '''初始化表单'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/shopCenter/process/initForm.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.GET)
    def tearDown(self):
        self.client.result()
    def test_initForm(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                     "processDefinitionId":cl.value("processDefinitionId")})
        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),0)
        s = cl.json.get('info')
        cl.is_contain(s,u"请求成功")
        cl.save("templateId", cl.json.get("data")['formTemplate']['id'])
        cl.save("templateName", cl.json.get("data")['formTemplate']['name'])
        cl.save("componentId", cl.json.get("data")['formTemplate']['formFieldList'][0]['componentId'])
        cl.save("fieldId", cl.json.get("data")['formTemplate']['formFieldList'][0]['id'])
        cl.save("fieldTypeId", cl.json.get("data")['formTemplate']['formFieldList'][0]['fieldTypeId'])
        cl.save("fieldId1", cl.json.get("data")['formTemplate']['formFieldList'][1]['id'])
        cl.save("fieldTypeId1", cl.json.get("data")['formTemplate']['formFieldList'][1]['fieldTypeId'])



