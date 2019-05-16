#-*-coding:GBK -*-



import unittest
import requests
# from testCase.test_login_A import test_login
import json
import time
import hashlib
import random
token = ""

salt = "*2f4961%8*5B588463bee04djDAed27"
from framework.readExcel import ReadExcel

class testApi(object):
    def math_sign(self,**kwargs):
        api_param = dict(sorted(kwargs.items()))
        param_string = ''

        for key, value in api_param.items():
            param_string = param_string + key + '=' + str(value) + '&'
        # print(param_string + "secretValue=" + salt)
        return param_string + "secretValue=" + salt

    def encode_md5(self,str_para):
        print(u"加密前的字符串：", str_para)
        m = hashlib.md5()
        m.update(str_para.encode("utf-8"))
        # print(u"加密值为：", m.hexdigest())
        return m.hexdigest()

    def get_time(self):
        request_time = int(time.time())
        return request_time

    def get_params(self, url, **kwargs):
        url = url + '?'
        for key in kwargs:
            url = url + key+'='+kwargs[key]+'&'
        return url[:-1]


    def http_request(self,url, method, token, encryption, **kwargs):
        h_nonce = random.randint(1, 10000) + self.get_time()
        headers = {
            "h-time": str(self.get_time() * 1000),
            "h-nonce": str(h_nonce),
            "h-tenant-code": 'gcyh'
        }
        if encryption:#0:不加密，1:加密
            params = dict(headers, **kwargs)


        else:
            params = dict(headers)
            headers["Content-Type"] = "application/json; charset=utf-8"


        headers["h-sign"] = self.encode_md5(self.math_sign(**params))
        headers['h-api-token'] = token
        # print(headers)
        if method.lower() == 'get':
            url = self.get_params(url, **kwargs)
            response = requests.get(url=url, data=params, headers=headers).json()
        if method.lower() == 'post' and encryption:
            response = requests.post(url=url, data=params, headers=headers).json()
        if method.lower() == 'post'and not encryption:
            response = requests.post(url=url, data=json.dumps(kwargs), headers=headers).json()

        return response



    # def http_request(self,url, method, data,token ):
    #     h_nonce = random.randint(1, 10000) + self.get_time()
    #     headers = {}
    #     params = dict(headers)
    #     headers["h-time"] = str(self.get_time() * 1000)
    #     headers["h-nonce"] = str(h_nonce)
    #     headers["h-tenant-code"] = 'gcyh'
    #     headers['h-api-token'] = token
    #     headers['Content-Type'] = 'application/json; charset=utf-8'
    #
    #     # params = dict(headers)
    #     headers["h-sign"] = self.encode_md5(self.math_sign(**params))
    #
    #     if method.lower() == 'get':
    #
    #         response = requests.get(url=url, data=data, headers=headers, verify=False)
    #     if method.lower() == 'post':
    #         response = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
    #     return response



if __name__ == '__main__':
    # unittest.main(verbosity=2)
    data = ''
    print(type(data))
    url = ''
    t=testApi()
    dict_data = eval(data)
    t.http_request(url=url, method='post', token=token, **dict_data)
