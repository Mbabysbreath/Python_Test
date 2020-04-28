# 使用discover()来执行测试用例，不用导包
# 生成测试报告
import sys
import unittest,csv
import time
import os
import HTMLTestRunner

def creatSuite():

    discover = unittest.defaultTestLoader.discover('../src03',pattern='testB*.py',top_level_dir=None)
    return discover

if __name__=="__main__":
        curpath = sys.path[0]
        print(sys.path)
        print(curpath)
        now = time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))
        if not os.path.exists(curpath+'/resultreport'):
            os.makedirs(curpath+'/resultreport')
        filename = curpath+'/resultreport/'+now+'resultreport.html'
        with open(filename, 'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况', verbosity=2)
            suite = creatSuite()
            runner.run(suite)
