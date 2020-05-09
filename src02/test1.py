# 定位一组元素
from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
# file:///+本地文件路径
file_path = 'file:///'+os.path.abspath("D:/Python_Test/html/checkbox.html")
driver.get(file_path)
# 选择页面上所有的input，然后从中过滤出所有的checkbox并勾选
# get_attribute获得属性值
inputs = driver.find_elements_by_tag_name("input")
for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()
        time.sleep(4)
driver.implicitly_wait(3)
driver.quit()
