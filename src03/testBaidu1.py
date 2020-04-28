# unittest框架解析
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# Baidu1这个类继承自unittest.TestCase类

class Baidu1(unittest.TestCase):

# 初始化,声明变量，初始化数据库等
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

# test_开头的方法都是测试用例，按照字典序执行aA-zZ 0-9
# # 忽略测试用例的执行
#  # @unittest.skip("skipping")
    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"测试")
        driver.find_element_by_id("su").click()
# self代表的是类的实例
# 断言 assert
    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("hao123").click()
        self.assertEqual(u"hao123_上网从这里开始", driver.title,"false!!")
# how和what是参数，用的时候要传参，不用传self
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

# 判断alert是否存在，可删除
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                 alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

# test fixture，清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    if __name__ == "__main__":
        unittest.main(verbosity=2)

    '''
可以增加verbosity参数，例如unittest.main(verbosity=2)
在主函数中，直接调用main() ，在main中加入verbosity=2 ，这样测试的结果就会显示的更加详细。
这里的verbosity 是一个选项, 表示测试结果的信息复杂度，有三个值:
0 ( 静默模式): 你只能获得总的测试用例数和总的结果比如总共100个失败,20 成功80
1 ( 默认模式): 非常类似静默模式只是在每个成功的用例前面有个“ . ” 每个失败的用例前面有个“F”
2  ( 详细模式): 测试结果会显示每个测试用例的所有相关的信息
    '''
