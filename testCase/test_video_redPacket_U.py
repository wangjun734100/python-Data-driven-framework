#-*-coding:utf-8 -*-

from framework.readExcel import ReadExcel
import unittest
from framework import readConfigFile
from framework.logger import Logger
# from testCase.test_login_A import test_login
from framework.testApiUpdate import testApi
from common.login import test_Login_token
config = readConfigFile.ReadConfig()
token=config.get_http("token")
# login = test_login()
# token = login.test_Login_token()
mylog = Logger(logger="test_video_RedPacket").getlog()




class test_video_RedPacket(unittest.TestCase):
    '''接口名称:视频红包'''

    def setUp(self):
        print("测试开始")
        pass


    def test_videoRedPacket(self):
        """
        视频红包
        :return:

        """
        token = test_Login_token()
        print(token)
        excel = ReadExcel("视频红包")


        data = excel.getData
        state_code = excel.getStatusCode




        url = excel.getUrl
        print(url)
        method = excel.getMethod

        row = excel.getRows
        buer=excel.getEncryption
        status=excel.getStatus
        t = testApi()

        # data={"addReqDtoList":[{"optionsList":[{"isAnswer":1,"optionName":"A","optionValue":"刚刚","sequence":0},{"isAnswer":0,"optionName":"B","optionValue":"方法","sequence":1}],"sequence":1,"surveyId":0,"title":"馆VB","type":0}],"areaType":2,"channelCode":"android","content":"我是个好人","coverUrl":"http://sz-gcyh.oss-cn-shenzhen.aliyuncs.com/default/ee24cabe3afe4da99b1ae80b4cc6896c.png","isPublicPassword":1,"isSaveTemplate":0,"kilometer":0,"microblog":"","money":100.0,"payType":10001,"quantity":1,"redPacketLatitude":"22.63085","redPacketLongitude":"113.844275","redPacketType":"video","safetyCode":"123456","surveyType":0,"urlName":"","userLatitude":"22.63085","userLongitude":"113.844275","videoUrl":"http://sz-gcyh.oss-cn-shenzhen.aliyuncs.com/video/712_1555914254726.mp4","wechat":""}
        # url="http://test_gateway.guochuangyuanhe.com/api/v1/redpacket/person_red_packet/add_video"
        # response=t.http_request(url=url,method="post",token=token,encryption=0,**data)
        # print(response)
        for i in range(0, row - 1):
            if status[i]=='执行':
                dict_data = eval(data[i])
                buer_i = int(buer[i])
                result = t.http_request(url=url[i], method=method[i], token=token, encryption=buer_i, **dict_data)
                print(result)
                # print(type(result))
                # if i ==0:
                #     print(result['response']['redPacketUuid'])
                # else:
                #     print("空值")
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