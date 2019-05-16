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
mylog = Logger(logger="test_delete_redPackets").getlog()




class test_delete_redPackets(unittest.TestCase):
    '''接口名称:删除视频红包模板'''

    def setUp(self):
        print("随机")
        pass


    def test_get_redPacket_list(self):
        """
        获取红包列表
        :return:

        """
        token = test_Login_token()
        print(token)
        t = testApi()
        host = config.get_http("browserName")

        url = host + "/api/v1/redpacket/red_packet_survey_template/get"

        method = 'get'
        data = {"redPacketType":"video"}
        result = t.http_request(url=url, method=method, token=token,encryption=1, **data)
        print(result)
        self.assertEqual(result["message"], '成功')
        self.assertEqual(result["success"], True)
        if result['response'][0]['templateId'] != None:
            print(result['response'][0]['templateId'])

        else:
            print('无红包ID')


    def test_delete_redPacket_demo(self):
        """
        删除红包
        :return:

        """
        t = testApi()
        host = config.get_http("browserName")
        token = test_Login_token()
        print(token)

        url = host + "/api/v1/redpacket/red_packet_survey_template/delete"

        method = 'post'
        id = self.test_get_redPacket_list()
        data = {"templateId":id}
        result = t.http_request(url=url, method=method, token=token,encryption=1, **data)
        print(result)
        self.assertEqual(result["message"], '成功')
        self.assertEqual(result["success"], True)







        mylog.info("测试完成")

if __name__=='__main__':
    unittest.main(verbosity=2)