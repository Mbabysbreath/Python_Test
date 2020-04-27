# 上传文件操作
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('D:/Python_Test/html/upload.html')
driver.get(file_path)
time.sleep(3)
driver.find_element_by_name("file").send_keys("D://Python_Test/html/send.html")
time.sleep(4)
driver.quit()
