#-*-coding:utf-8 -*-
# from framework.testApiWay import *
from framework.readExcel import ReadExcel
import unittest
from framework import readConfigFile
from framework.logger import Logger
from common.login import test_Login_token
from framework.testApiUpdate import testApi
# from framework.testApiWay import testApi
# from common.login import test_Login_token
config = readConfigFile.ReadConfig()
# token=config.get_http("token")
# login = test_login()
# token = login.test_Login_token()
mylog = Logger(logger="test_KSB_detail").getlog()




class test_KSB_detail(unittest.TestCase):
    '''接口名称:KSB明细'''

    def setUp(self):
        print("测试开始")
        pass


    def test_ksb_detail(self):
        """
        KSB明细
        :return:

        """
        token = test_Login_token()
        print(token)
        excel = ReadExcel("KSB明细")


        data = excel.getData
        state_code = excel.getStatusCode




        url = excel.getUrl
        print(url)
        method = excel.getMethod

        row = excel.getRows
        buer=excel.getEncryption
        status=excel.getStatus
        t = testApi()


        for i in range(0, row - 1):
            if status[i]=='执行':
                dict_data = eval(data[i])
                buer_i = int(buer[i])
                result = t.http_request(url=url[i], method=method[i], token=token, encryption=buer_i, **dict_data)
                print(result)
                self.assertEqual(result['message'], state_code[i])

                # print(type(result))

                if result['message'] == state_code[i]:
                    RESULT = 'PASS'
                else:
                    RESULT = 'FAIL'

                excel.result_write(str(RESULT))
            else:
                print('你规定不执行')



        mylog.info("测试完成")
















if __name__=='__main__':
    unittest.main(verbosity=2)