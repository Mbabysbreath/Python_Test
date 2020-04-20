from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")

# 鼠标事件
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("Lisa")
driver.get("http://news.baidu.com")
qqq=driver.find_element_by_xpath(".//*[@id='s_btn_wr']")
time.sleep(10)
# 右键
ActionChains(driver).context_click(qqq).perform()
# 双击
ActionChains(driver).double_click(qqq).perform()
# 定位元素的原位置
element = driver.find_element_by_id("s_btn_wr")
# 定位元素要移动到的目标位置
target = driver.find_element_by_class_name("btn")
# 执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()
driver.implicitly_wait(3)
