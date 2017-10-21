# -*- coding: utf-8 -*-
import unittest
import requests


class Test(unittest.TestCase):
    def setUp(self):
        self.base_url="http://api.sports.baofeng.com/api/v3/android/program/list"
        pass



    def test_program_title(self):
        # payload={'id':'38383'}
        r=requests.get(self.base_url)
        self.result=r.json()
        #self.assertEqual(self.result['data'][0]['address'], u'北京会展中心')
        self.assertEqual(self.result['data']['programs'][0]['title'],u'节目测试1')


    # def test_case2(self):
    #     # payload={'id':'38383'}
    #     r=requests.get(self.base_url)
    #     self.result=r.json()
    #     self.assertEqual(self.result['message'],'OKK')

    def tearDown(self):
        pass

if '__name__' == '__main':
    unittest.main()