# 多层框架/窗口定位
# switch_to_frame()
# switch_to_window()
# switch_to_default_content:从frame中嵌入的页面里跳出，跳回到最外面的原始页面
# -------Start-------

from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('D:/Python_Test/html/frame.html')
driver.get(file_path)
driver.implicitly_wait(30)
# 先找到iframe1(id=f1)
driver.switch_to.frame("f1")
# 再找到其下面的ifrome2(id =f2)
driver.switch_to.frame("f2")
# 下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()
