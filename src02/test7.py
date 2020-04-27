# 警告框输入值
from selenium import webdriver
from time import sleep
import os
driver = webdriver.Chrome()
driver.implicitly_wait(30)
file_path = 'file:///' + os.path.abspath('D://Python_Test/html/send.html')
driver.get(file_path)
# 定位按钮
driver.find_element_by_xpath('/html/body/input').click()
# 输入内容
alert = driver.switch_to.alert
alert.send_keys('webdriver')
sleep(2)
alert.accept()
sleep(5)
driver.quit()

