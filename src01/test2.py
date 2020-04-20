
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 测试操作对象的方法：submit \ click \clear \ text(获取文本信息)\send_keys
# driver.find_element_by_id("kw").send_keys("王一博")
# driver.find_element_by_id("su").click()
# time.sleep(5)
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("肖战")
# driver.find_element_by_id("su").submit()
# time.sleep(4)
texts = driver.find_element_by_id("s-bottom-layer-right").text
print(texts)
driver.quit()
