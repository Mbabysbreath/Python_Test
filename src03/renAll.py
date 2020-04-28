# 使用测试套件来执行多个测试用例--比较麻烦--批量加载测试用例1
# 可以使用makeSuite代替
import unittest , csv
import os , sys
import time
# 导入测试用例所在的类
import src03.testBaidu1
import src03.testBaidu2

# 手工添加案例到套件---比较麻烦
def creatSuite():
        suite = unittest.TestSuite()
# 将测试用例加入到测试容器（套件）中
        suite.addTest(src03.testBaidu1.Baidu1("test_baidusearch"))
        suite.addTest(src03.testBaidu1.Baidu1("test_hao"))
        suite.addTest(src03.testBaidu2.Baidu2("test_baidusearch"))
        return suite

if __name__=="__main__":
     suite = creatSuite()
     runner = unittest.TextTestRunner(verbosity=2)
     runner.run(suite)