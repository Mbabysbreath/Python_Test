# div对话框--出现了大问题
from selenium import webdriver
from time import sleep
import os
import selenium.webdriver.support.ui as ui
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('D:/Python_Test/html/modal.html')
driver.get(file_path)
# 打开对话框
driver.find_element_by_id("show_modal").click()
sleep(3)
# 点击对话框中的链接
link = driver.find_element_by_id('myModal').find_element_by_id('click')
link.click()
sleep(4)
# 关闭对话框
button = driver.find_element_by_class_name('modal-footer').find_element_by_tag_name('button')
button.click()
sleep(2)
driver.quit()
