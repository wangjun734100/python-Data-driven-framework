# coding=utf-8
import json
import unittest

import requests
from framework import readConfigFile
from framework.logger import Logger
from common.login import *


config = readConfigFile.ReadConfig()
mylog = Logger(logger="test_login").getlog()

class MyTest(unittest.TestCase):     #封装测试环境的初始化和还原的类
    def setUp(self):

        #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！

        print("start test")
        pass
    def tearDown(self):             #与setUp()相对
        print("end test")
        pass


class test_login(MyTest):
    '''接口名称:登录'''




    def test_Login_token(self):
        """
        登录
        :return:
        """
        login=test_Login_token()
        print(login)



    def test_LoginError(self):
        """
         测试登录用户名错误
         :return:
         """
        login=test_Login_mobile_erro()
        print(login)




    def test_Login_password_erro(self):
        """
         测试登录用户名错误
         :return:
         """
        login=test_Login_password_erro()
        print(login)



mylog.info("登录，测试完成")




if __name__ == '__main__':
    token = test_login().test_Login_token()
    print(123)
    print(token)
    # unittest.main()







