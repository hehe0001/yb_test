#!/user/bin/env python
#_*_ coding:utf-8 _*_
import unittest
import requests
from client import *
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class GetOnLineCommodityDetail(unittest.TestCase):
    '''获取医生在线咨询服务'''
    def setUp(self):
        self.url = 'https://tyh.120yibao.com/yb/shopCenter/getOnLineCommodityDetail'
        self.token = Client.TOKEN
        self.client = Client(url=self.url,method=Method.GET)

    def tearDown(self):
        self.client.result()

    def test_getOnLineCommodityDetail(self):
        cl = self.client
        cl.set_data({"Yb-Yh-Client":"0","Yb-Yh-Token":self.token,
                     "doctorUserId":"141273","serviceType":"2"})
        cl.send()
        cl.equal(cl.status_code,200)
        cl.less_than(cl.times,1000)
        cl.equal(cl.json.get('status'),0)
        s = cl.json.get('info')
        cl.is_contain(s,u"请求成功")
        # r = cl.json.get('data')
        # # print r
        # te = r['onlineCommodityList']
        # print te
        # print type(te)
        # we = te[0]['hasPriceFavorable']
        # print we
        cl.save("commoditySubType",cl.json.get("data")['onlineCommodityList'][1]['commoditySubType'])
        cl.save("processDefinitionId",cl.json.get("data")['onlineCommodityList'][1]['processDefinitionId'])
        cl.save("priceId",cl.json.get("data")['onlineCommodityList'][1]['priceId'])
        cl.save("commodityId",cl.json.get("data")['onlineCommodityList'][1]['commodityId'])
        cl.save("hasPriceFavorable",cl.json.get("data")['onlineCommodityList'][1]['hasPriceFavorable'])
        cl.save("isApplyForRefund", cl.json.get("data")['onlineCommodityList'][1]['isApplyForRefund'])
        cl.save("isFreeconsult", cl.json.get("data")['onlineCommodityList'][1]['isFreeconsult'])
        cl.save("doctorUserId",cl.json.get("data")['doctorInfo']['doctorUserId'])
        cl.save("doctorName", cl.json.get("data")['doctorInfo']['doctorName'])
        cl.save("imageHeadUrl", cl.json.get("data")['doctorInfo']['imageHeadUrl'])
        cl.save("itemName", cl.json.get("data")['doctorInfo']['itemName'])
        cl.save("titleName", cl.json.get("data")['doctorInfo']['titleName'])
        cl.save("hospitalName", cl.json.get("data")['doctorInfo']['hospitalName'])

        print cl.DATA
        print type(cl.DATA)
        print cl.value('hospitalName')
