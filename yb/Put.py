#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Put(unittest.TestCase):
    '''put'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/cache/put.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.POST,type=Type.URL_ENCODE)
    def tearDown(self):
        self.client.result()
    def test_put(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                     "key":"mall_service_apply_form",
                     "data":{"orderType":cl.value("commoditySubType"),
                             "priceId":cl.value("priceId"),
                             "doctor":{"name":cl.value('doctorName'),
                                       "imgPath":cl.value('imageHeadUrl'),
                                       "itemName":cl.value('itemName'),
                                       "titleName":cl.value('titleName'),
                                       "hospitalName":cl.value('hospitalName'),
                                       "userId":cl.value("doctorUserId")},
                             "hasPriceFavorable":cl.value("hasPriceFavorable"),
                             "processDefinitionId":cl.value("processDefinitionId"),
                             "prevPage":"consult_my",
                             "commodityId":cl.value("commodityId")}})
        data = {"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                "key":"mall_service_apply_form",
                "data":{"orderType":cl.value("commoditySubType"),
                        "priceId":cl.value("priceId"),
                        "doctor":{"name":cl.value('doctorName'),
                                  "imgPath":cl.value('imageHeadUrl'),
                                    "itemName":cl.value('itemName'),
                                    "titleName":cl.value('titleName'),
                                    "hospitalName":cl.value('hospitalName'),
                                    "userId":cl.value("doctorUserId")},
                             "hasPriceFavorable":cl.value("hasPriceFavorable"),
                             "processDefinitionId":cl.value("processDefinitionId"),
                             "prevPage":"consult_my",
                             "commodityId":cl.value("commodityId")}}
        print cl.DATA
        print cl.value("doctorUserId")
        print data
        cl.send()
        cl.equal(cl.status_code, 200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),0)
        s = cl.json.get('info')
        cl.is_contain(s,u"请求成功")
