# coding = utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# time.sleep(30)  固定等待
# implictly_wait(30) 智能等待 等待时间<=30秒，在30秒内只要等到了，就不用继续等了
# driver.find_element_by_id("kw").send_keys("赵丽颖")
# driver.find_element_by_id("su").submit()
# time.sleep(10)
# driver.implicitly_wait(10)尽量使用这个等待的方法
# driver.implicitly_wait(10)
# driver.find_element_by_link_text("赵丽颖_百度百科").click()

# 打印 title  /  url
# t = driver.title
# print(t)
# url = driver.current_url
# print(url)

# 浏览器最大化--设置浏览器的大小--最小化
# driver.maximize_window()
# time.sleep(5)
# driver.set_window_size(400, 800)
# time.sleep(5)
# driver.minimize_window()

# 设置浏览器的前进forward和后退back
# driver.maximize_window()
# driver.find_element_by_link_text("新闻").click()
# time.sleep(10)
# print(driver.title)
# driver.back()
# time.sleep(5)
# print(driver.title)
# driver.forward()
# time.sleep(4)
# print(driver.title)

# 控制浏览器的滚动条
driver.find_element_by_id("kw").send_keys("python怎样控制浏览器的滚动条向左右滑动")
driver.find_element_by_id("su").click()
driver.set_window_size(400, 800)
# 滑到最低端
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(7)
# 向顶部滑动
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(8)
driver.quit()
