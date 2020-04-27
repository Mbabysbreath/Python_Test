#  层级定位
from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('D://Python_Test/html/level_locate.html')
driver.get(file_path)
driver.implicitly_wait(3)
# 点击Link1链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
driver.implicitly_wait(10)
# 找到id 为dropdown1的父元素--ul列表
list = driver.find_element_by_id("dropdown1").find_element_by_link_text("Action")
# list = driver.find_element_by_id("dropdown1").find_elements_by_link_text("Action")
ActionChains(driver).move_to_element(list).perform()
# ActionChains(driver).move_to_element(list[0]).perform()
time.sleep(4)
driver.quit()
