# 下拉框处理
from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('D://Python_Test/html/drop_down.html')
driver.get(file_path)
time.sleep(3)
# 先定位到下拉框
m = driver.find_element_by_id("ShippingMethod")
m.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()
time.sleep(3)
driver.quit()
