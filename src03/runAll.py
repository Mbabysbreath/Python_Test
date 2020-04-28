# 测试套件快速简便版--批量加载测试用例2
# 经过makeSuite（）和TestLoader（）的引入，
# 我们不用一个py文件测试类，只需要导入一次即可。
import unittest,csv
import os,sys
import time
import src03.testBaidu1
import src03.testBaidu2

# 手工添加案例到套件
def createsuite():
    suite = unittest.TestSuite()
    # 将测试用例加入到测试容器（套件）中
    suite.addTest(unittest.makeSuite(src03.testBaidu1.Baidu1))
    suite.addTest(unittest.makeSuite(src03.testBaidu2.Baidu2))
    return suite

'''批量加载测试用例3
suite1 = unittest.TestLoader().loaderTestFromTestCase(testBaidu1.Baidu1)
suite2 = unittest.TestLoader().loaderTestFromTestCase(testBaidu2.Baidu2)
suite = unittest.TestSuite([suite1,suite2])
return suite
'''
if __name__=="__main__":
    suite=createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)