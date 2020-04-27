# 警告框alert-出现问题-打不开文件alert.html
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('D:\\Python_Test\\html\\alert.html')
driver.get(file_path)
time.sleep(3)

# 点击链接弹出alert
driver.find_element_by_id("tooltip").click()
time.sleep(3)
# 接受alert
alert = driver.switch_to.alert
alert.accept()
# 输出alert框的内容
print("alert:"+alert.text)
# 取消对话框
alert = driver.switch_to.alert
alert.dismiss()
# 输入内容
alert = driver.switch_to.alert
alert.send_keys("hello")

time.sleep(8)
driver.quit()
