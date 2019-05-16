#-*-coding:utf-8 -*-

from framework.readExcel import ReadExcel
import unittest
from framework import readConfigFile
from framework.logger import Logger

from framework.testApiUpdate import testApi
from common.login import test_Login_token
config = readConfigFile.ReadConfig()
# token=config.get_http("token")
# login = test_login()
# token = login.test_Login_token()
mylog = Logger(logger="test_bank").getlog()




class test_bank(unittest.TestCase):
    '''接口名称:删除银行卡'''

    def setUp(self):

        print("测试开始")
        pass

        pass


    def test_get_bank_list(self):
        """
        删除银行卡
        :return:

        """

        token = test_Login_token()
        t = testApi()
        host = config.get_http("browserName")

        url = host + "/api/v1/user/bank_card/list"

        method = 'get'

        result = t.http_request(url=url, method=method, token=token)
        print(result)
        self.assertEqual(result["message"], '成功')
        self.assertEqual(result["success"], True)
        id_result =result['response']
        if len(id_result) == 2:
            # print(result['response'][0]['id'])
            return id_result[1]['id']

        else:
            print('无红包ID')

    mylog.info("测试完成")

    # def test_delete_bank(self):
    #     token = test_Login_token()
    #     print(token)
    #     t = testApi()
    #
    #     host = config.get_http("browserName")
    #
    #     url = host + "/api/v1/user/bank_card/unbind"
    #     id = self.test_get_bank_list()
    #
    #     method = 'post'
    #     data={"id":id,"safetyCode":"123456"}
    #
    #     result = t.http_request(url=url, method=method, token=token, ** data)
    #     print(result)
    #     self.assertEqual(result["message"], '成功')
    #     self.assertEqual(result["success"], True)
    #
    # mylog.info("测试完成")






if __name__=='__main__':
    unittest.main(verbosity=2)