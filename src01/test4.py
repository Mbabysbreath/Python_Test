# tab和 enter--键盘事件--要先引入Keys包
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:88/biz/user-login-L2Jpei8=.html")
driver.maximize_window()
driver.find_element_by_id("account").clear()
time.sleep(5)
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)
driver.find_element_by_name("password").send_keys("419423ZZmm")
time.sleep(3)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
