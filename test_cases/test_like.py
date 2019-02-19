# -*- coding: utf-8 -*-
import unittest
import requests


class Test(unittest.TestCase):
    def setUp(self):
        self.base_url="http://alpha-api.szy.com/commentserver/content/like/v2"
        pass



    def test_program_title(self):
        data={
        "contentId": "599374",
        "contentType": 8,
        "contentUserId": "7dbd4357b6f720c729ce",
        "contentUserType": 4,
        "like": 0,
        "userId": "9eb20f48ee8be34b0f1a",
        "userName": "蒋金谷园长",
        "userPic": "",
        "userType": 5
         }
        r=requests.post(self.base_url,json=data)
        self.result=r.json()
        self.assertEqual(self.result['code'],10000)

        #self.assertEqual(self.result['data'][0]['address'], u'北京会展中心')
        # self.assertEqual(self.result['data']['programs'][0]['title'],u'节目测试1')


    # def test_case2(self):
    #     # payload={'id':'38383'}
    #     r=requests.get(self.base_url)
    #     self.result=r.json()
    #     self.assertEqual(self.result['message'],'OKK')

    def tearDown(self):
        pass

if '__name__' == '__main':
    unittest.main()