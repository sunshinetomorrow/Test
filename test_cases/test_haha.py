import unittest
import requests


class Test(unittest.TestCase):
    def setUp(self):
        self.base_url="http://api.sports.baofeng.com/api/v3/android/event/match?id=38383"
        pass



    def test_case1(self):
        # payload={'id':'38383'}
        r=requests.get(self.base_url)
        self.result=r.json()
        self.assertEqual(self.result['message'],'OK')


    def test_case2(self):
        # payload={'id':'38383'}
        r=requests.get(self.base_url)
        self.result=r.json()
        self.assertEqual(self.result['message'],'OKK')

    def tearDown(self):
        pass

if '__name__' == '__main':
    unittest.main()