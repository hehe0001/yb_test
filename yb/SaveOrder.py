#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SaveOrder(unittest.TestCase):
    '''开启流程'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/shopCenter/saveOrder.do'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.POST,type=Type.URL_ENCODE)

    def tearDown(self):
        self.client.result()

    def test_saveOrder(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                     "isFree":cl.value("isFreeconsult"),
                     "catType":cl.value("commoditySubType"),
                     "priceId":cl.value("priceId"),
                     "refer":"1",
                     "patientId":1964,
                     "commodityId":cl.value("commodityId"),
                      "processInstanceId":cl.value("processInstanceId"),
                     "isAnonymousDisplay":cl.value('isApplyForRefund')})
        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),100)
        s = cl.json.get('info')
        cl.is_contain(s,u"保存商城订单信息成功")
        # cl.equal(cl.json.get('body')['orderSn'],'select orderSn from yb_order where FCommodityId = ')

        cl.db_execute("update yb_order "
                      "set FRefundApply = 2,FRefundStatus = 1, FrefundTime = NOW(),FRefundDetail= 'XXXX',FStatus = 0,FRefundReasonType = 2 "
                      "where FPatientId=1964")
        cl.db_execute("UPDATE yb_process_instance "
                      "SET serviceStatus = 3,status = 2, version = 4,nextProcessNodeDefinitionId= 57319 "
                      "WHERE PatientId=1964")