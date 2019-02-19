# -*- coding: utf-8 -*-
import unittest
import requests


class Test(unittest.TestCase):
    def setUp(self):
        self.base_url="http://alpha-api.szy.com/commentserver/view/list/v1"
        pass



    def test_viewlist(self):
        payload={'contentId':'599374','count':25,'page':0,'contentType':8}
        r=requests.get(self.base_url,params=payload)
        self.result=r.json()
        ''' https://blog.csdn.net/u013383813/article/details/76736720/
            除此之外，requests中也带有带有一个内置的json解码器，将返回的内容转换为dict

            import requests
            r.requests.get(url)
            print (r.json())
            print (type(r.json()))

            -----结果-----
            ......
            <class ‘dict‘>
            那么通过json解码器转为dict后，想要查看到返回内容中某个具体参数的值，就比较方便啦!'''

        #self.assertEqual(self.result['data'][0]['address'], u'北京会展中心')
        self.assertEqual(self.result['body']['list'][0]['userName'],u'静测0219伯母')
        # self.assertEqual(self.result['message'],'success')

    # def test_block_id(self):
    #     # payload={'id':'38383'}
    #     r=requests.get(self.base_url)
    #     self.result=r.json()
    #     #self.assertEqual(self.result['data'][0]['address'], u'北京会展中心')
    #     self.assertEqual(self.result['data']['block'][0]['id'],60)


    # def test_case2(self):
    #     # payload={'id':'38383'}
    #     r=requests.get(self.base_url)
    #     self.result=r.json()
    #     self.assertEqual(self.result['message'],'OKK')

    def tearDown(self):
        pass

if '__name__' == '__main':
    unittest.main()