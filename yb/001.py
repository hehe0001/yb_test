#!/user/bin/env python
#_*_ coding:utf-8 _*_

import unittest
import requests
import json
from client import *
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'https://tyh.120yibao.com/yb/itemGroup/list.do'
data = {"Yb-Yh-Client":"0","Yb-Yh-Token":"c187181d37defebf921f1c37597b2177"}
res = requests.get(url=url,params=data)
print res.text

url1 = 'https://tyh.120yibao.com/yb/im/getHistoryMsgByMsgTime.do'
data1 = {"Yb-Yh-Client":"0","Yb-Yh-Token":"c187181d37defebf921f1c37597b2177","num":"20",
         "voip":"80002500000131","msgTime":"-1","patientId":"1964"}
data2 = {"Yb-Yh-Client":"0","Yb-Yh-Token":"c187181d37defebf921f1c37597b2177","num":"20",
         "voip":"80002500000131","msgTime":"-1","patientId":"1964"}
re = requests.get(url=url1,params=data1)
print re.text

url2 = 'https://tyh.120yibao.com/yb/shopCenter/process/startProcess.do'
header = {"Content-Type":"application/json","Yb-Yh-Client":"0",
          "Yb-Yh-Token":"c187181d37defebf921f1c37597b2177"
          }
data2 = {
         "catType":9,"priceId":3889,"patientId":964,"commodityId":11065,"processDefinitionId":11811,
         "formInstance":{"templateId":659,"templateName":"基础服务在线咨询预约信息单",
                         "fieldInstanceList":[{"componentId":17,"fieldId":7540,"fieldTypeId":3,
                                               "fieldValueName":"v发热三个人他干活色弱攻守道的人发个人",
                                               "fieldValueId":""},
                                              {"fieldId":7541,"fieldTypeId":9,"fieldValueName":"","fieldValueId":""}]}}
r = requests.post(url=url2,headers =header,data=json.dumps(data2))
print r.text