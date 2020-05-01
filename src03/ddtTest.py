# 数据驱动--。txt文件只能出来一个
# 有毒吧，已经注释掉skip了，还是执行不了
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import os, sys, csv
from ddt import ddt, data, unpack, file_data
# 解析txt文件
def getCsv(file_name):
    rows = []
    path = sys.path[0].replace('\test', '')
    print(path)
    with open(path + '/data/' + file_name, 'rt', encoding='utf-8') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows = []
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows


# 引入ddt
@ddt
class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1.增加ddt数据
    @unittest.skip("skipping")
    @data("王一博", "肖战", "赵敏")
    def test_hao(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        print(value)
        # self.assertEqual(expected_value, driver.title)
        # print(expected_value)
        print(driver.title)

    # 2.使用txt文件
    # @unittest.skip("skipping")
    @data(*getCsv('test_baidu_data.txt'))
    @unpack
    def test_hao1(self, value, expected_value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        print(value)
        self.assertEqual(expected_value, driver.title)
        print(expected_value)
        print(driver.title)

     # 3.直接输入数据
    @unittest.skip("skipping")
    @data(["Lsia", u"Lsia_百度搜索"], [u"双笙", u"双笙_百度搜索"],["999",u"999_百度搜索"])
    @unpack
    def test_hao2(self,value,expected_value):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        self.assertEqual(expected_value,driver.title)
        print(driver.title)

        # 4.读取json
    @unittest.skip("skipping")
    @file_data("data/test_baidu_data.json")
    def test_hao3(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        print(value)
        print(driver.title)


if __name__ == "__main__":
        unittest.main()
