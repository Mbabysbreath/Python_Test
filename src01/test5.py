from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
# 键盘组合键用法：ctrl+A ctrl+V ctrl+X
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("博君一笑")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(5)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(5)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(5)
driver.quit()
