# -*- coding: utf-8 -*-
import time, sys
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data
# sys.path.append('./test_cases')


'''参考资料：http://www.cnblogs.com/yufeihlf/p/5752146.html'''


test_dir = './test_cases'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')



if __name__ == "__main__":
    test_data.init_data()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Test Report',
                            description='Implementation  with: ')
    runner.run(discover)
    fp.close()
    #22