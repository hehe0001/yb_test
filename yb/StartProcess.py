#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class StartProcess(unittest.TestCase):
    '''开启流程'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/shopCenter/process/startProcess.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.POST,type=Type.JSON)


    def tearDown(self):
        self.client.result()

    def test_startProcess(self):
        cl = self.client
        cl.set_header("Yb-Yh-Client", "0")
        cl.set_header("Yb-Yh-Token", self.token)
        print cl.headers

        cl.set_data({
                     "catType":cl.value("commoditySubType"),
                     "priceId":cl.value("priceId"),"patientId":1964,
                     "commodityId":cl.value("commodityId"),
                      "processDefinitionId":cl.value("processDefinitionId"),
                     "formInstance":{"templateId":cl.value("templateId"),
                                     "templateName":cl.value("templateName"),
                                    "fieldInstanceList":[{"componentId":cl.value("componentId"),
                                                        "fieldId":cl.value('fieldId'),
                                                          "fieldTypeId":cl.value('fieldTypeId'),
                                                        "fieldValueName":"必清奇朝代版福红色UI绿肥红瘦脂肪酸等分别出具",
                                                        "fieldValueId":""},
                                                        {"fieldId":cl.value('fieldId1'),
                                                         "fieldTypeId":cl.value('fieldTypeId1'),
                                                         "fieldValueName":"","fieldValueId":""}]}})

        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),0)
        s = cl.json.get('info')
        cl.is_contain(s,u"请求成功")

        cl.save("processInstanceId",cl.json.get('data')["processInstanceId"])

