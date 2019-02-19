# -*- coding: utf-8 -*-
import time, sys
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data
# sys.path.append('./test_cases')
import os


'''参考资料：http://www.cnblogs.com/yufeihlf/p/5752146.html
https://www.cnblogs.com/puresoul/p/7490881.html'''

# 用例路径
test_dir = './test_cases'

print (test_dir)
print ('os.getcwd()=',os.getcwd())

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')



if __name__ == "__main__":
    test_data.init_data()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告存放路径
    filename = './report/' + now + '_result.html'
    # 打开一个文件，将result写入此file中
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Test Report',
                            description='Implementation  with: ')
    runner.run(discover)
    fp.close()


