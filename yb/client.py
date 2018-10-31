#!/user/bin/env python
#_*_ coding:utf-8 _*_
#!/user/bin/env python
#_*_ coding:utf-8 _*_
import requests
import unittest
import pymysql
import json

class Client(unittest.TestCase):
    DATA = {}
    DB = None
    TOKEN = 'c187181d37defebf921f1c37597b2177'

    def __init__(self,url,method,type = 0):
        self.url = url
        self.method = method
        self.type = type
        self.headers = {}
        self.res = None
        self.flag = 0
        self._type_equality_funcs = {}
        self.data = {}
        # self.db = pymysql.connect(host="139.199.132.220", user="root", password="123456", db="event")

    @property
    def status_code(self):
        return self.res.status_code
    # @property
    # def status(self):
    #     return self.res.status
    @property
    def text(self):
        return self.res.text
    @property
    def json(self):
        return self.res.json()
    @property
    def times(self):
        return (int(round(self.res.elapsed.total_seconds()*1000)))

    def set_header(self,key,value):
        self.headers[key]=value

    def set_data(self, dic):
        # self.data = dic
        if isinstance(dic, dict):
            self.data = dic
        else:
            raise Exception("请求的参数请以字典格式传递")
    def send(self):
        if self.method == "GET":
            self.res = requests.get(url = self.url,headers = self.headers, params = self.data)
        elif self.method == "POST":
            if self.type == 1:
                self.res = requests.post(url=self.url, headers = self.headers, data = self.data)
            elif self.type == 5:
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 2:
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, cookies=self.headers, data=self.data)
            elif self.type == 3:
                self.set_header= ('Content-Type', 'text/xml')
                xml = self.data.get('xml')
                if xml:
                    self.res = requests.post(url=self.url, headers=self.headers, data=xml)
                else:
                    raise Exception('xml正文，入参格式：{"xml":"xxx"}')
            elif self.type == 4:
                self.set_header('Content-Type','application/json')
                # self.data = json.dumps(self.data)
                self.res = requests.post(url=self.url, headers=self.headers, json =self.data)
            elif self.type == 0:
                self.res = requests.post(url=self.url, headers=self.headers)
            else:
                raise Exception("正文格式不支持")
        else:
            raise Exception("请求的方法类型不支持")

    # 传值
    def save(self, name, value):
        Client.DATA[name] = value

    # 取值
    def value(self, name):
        return Client.DATA.get(name)

    def equal(self,first,second):
        try:
            self.assertEqual(first,second)
            print("检查点成功，实际结果[{first}]，预期结果[{second}]".format(first=first,second=second))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[{second}]".format(first=first, second=second))
            self.flag =+ 1
    def less_than(self,first,second):
        try:
            self.assertLess(first,second)
            print("检查点成功，实际结果[{first}]，预期结果[<{second}]".format(first=first, second=second))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[<{second}]".format(first=first, second=second))
            self.flag = + 1
    def db_execute(self,sql):
        cursor = Client.DB.cursor()
        cursor.execute(sql)
        Client.DB.commit()

    def db_equal(self,first,sql):
        cursor = Client.DB.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()[0]
        try:
            self.assertEqual(first,result)
            print("检查点成功，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
            self.flag = + 1

    def db_equals(self,first,sql):
        cursor = Client.DB.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        try:
            self.assertEqual(first,result)
            print("检查点成功，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
        except:
            '''此处不写信息，默认捕获所有'''
            print("检查点失败，实际结果[{first}]，预期结果[{sql}]".format(first=first, sql=result))
            self.flag = + 1
    def result(self):
        '''检查结果确认'''
        # Client.DB.close()
        if self.flag > 0:
            # self.assertTrue(False)
            self.assertTrue(False,'断言出现错误')
            # raise Exception('断言出现错误')

    def is_contain(self,str_one,str_two):
        '''
        判断一个字符串是否在另一个字符串中
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:
        '''
        flag = None
        #if isinstance(str_one,unicode):
            #str_one = str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
            print("检查点成功，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))
        else:
            flag = False
            print("检查点失败，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))
        # return flag

    def is_contain_result(self,str_one,str_two):
        '''包含结果判断'''
        cli = Client(self,str_one,str_two)
        result = cli.is_contain(str_one,str_two)
        if result:
            try:
                cli.is_contain(str_one, str_two)
                print("检查点成功，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))
            except:
                '''此处不写信息，默认捕获所有'''
                print("检查点失败，实际结果[{str_one}]，预期结果[{str_two}]".format(str_one=str_one, str_two=str_two))


class Method:
    GET = 'GET'
    POST = 'POST'

class Type:
    FORM = 1
    URL_ENCODE = 2
    XML = 3
    JSON = 4
    FILE = 5



# url = 'https://tyh.120yibao.com/yb/shopCenter/process/startProcess.do'
# client = Client(url=url,method=Method.POST,type=Type.JSON)
# client.set_header("Yb-Yh-Client", "0")
# client.set_header("Yb-Yh-Token", "c187181d37defebf921f1c37597b2177")
# client.set_header("Content-Type","application/json")
# client.set_data({"catType":9,"priceId":3889,"patientId":964,"commodityId":11065,"processDefinitionId":11811,
#                  "formInstance":{"templateId":659,"templateName":"基础服务在线咨询预约信息单",
#                                  "fieldInstanceList":[{"componentId":17,"fieldId":7540,"fieldTypeId":3,
#                                                        "fieldValueName":"v发热三个人他干活色弱攻守道的人发个人",
#                                                        "fieldValueId":""},
#                                                       {"fieldId":7541,"fieldTypeId":9,"fieldValueName":"","fieldValueId":""}]}})
#
# data = {"catType":9,"priceId":3889,"patientId":964,"commodityId":11065,"processDefinitionId":11811,
#                  "formInstance":{"templateId":659,"templateName":"基础服务在线咨询预约信息单",
#                                  "fieldInstanceList":[{"componentId":17,"fieldId":7540,"fieldTypeId":3,
#                                                        "fieldValueName":"v发热三个人他干活色弱攻守道的人发个人",
#                                                        "fieldValueId":""},
#                                                       {"fieldId":7541,"fieldTypeId":9,"fieldValueName":"","fieldValueId":""}]}}
# print type(data)
# dat = json.dumps(data)
# print type(dat)
# print client.headers
# re = requests.post(url=url, headers=client.headers, data=json.dumps(data))
# print re.text
# r = requests.post(url=url, headers=client.headers, data= dat)
# print r.text
# # client.send()
# # print client.text








