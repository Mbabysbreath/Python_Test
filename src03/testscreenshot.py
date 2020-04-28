# 异常捕捉与错误截图
#哔哩哔哩 (゜-゜)つロ 干杯~-bilibili

from selenium import webdriver
import time, unittest
import os

class Baidu1(unittest.TestCase):
# 初始化环境
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.base_url = " https://www.bilibili.com/"
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert = True # 是否继续接受下一个警告#
# 测试用例
    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        try:
            self.assertEqual(u'哩哔哩 (゜-゜)つロ 干杯~-bilibili', driver.title)
        except:
            self.saveScreenshot(driver, 'bili.png')
# 清除环境
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def saveScreenshot(self, driver, file_name):
        if not os.path.exists('./image'):
            os.makedirs('./image')
        now = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
        # 截图保存
        driver.get_screenshot_as_file('./image/'+now+'-'+file_name)
        time.sleep(1)
if __name__=="__main__":
    unittest.main()
