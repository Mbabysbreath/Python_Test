from selenium import webdriver
import time

driver = webdriver.Chrome()
# 打开驱动指向的浏览器
driver.get("https://www.baidu.com/")
# 用id查询
# driver.find_element_by_id("kw").send_keys("大虞海棠")
# # time.sleep(6)
# driver.find_element_by_id("su").click()

# 用name查询
# driver.find_element_by_name("wd").send_keys("王一博")
# time.sleep(3)
# driver.find_element_by_id("su").click()
# time.sleep(6)

# 用class查询class="s_ipt nobg_s_fm_hover"
# driver.find_element_by_class_name("s_ipt nobg_s_fm_hover").send_keys("王一博")
# time.sleep(3)
# driver.find_element_by_class_name("btn self-btn bg s_btn btn_h btnhover").click()
# time.sleep(4)

# 用文字链接查询
# driver.find_element_by_link_text("抗击肺炎").click()
# driver.find_element_by_partial_link_text("抗击肺炎").click()

# 用Partial link text定位--部分链接
# driver.find_element_by_partial_link_text("hao").click()

# xpath查询
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("Lisa")
# driver.find_element_by_xpath("//*[@id='su']").click()

# css样式查找 class用.s_ipt(用.)  id用（#su）
driver.find_element_by_css_selector(".s_ipt").send_keys("肖战")
driver.find_element_by_css_selector("#su").click()
time.sleep(3)
# 后退
driver.back()
time.sleep(5)
# 前进
driver.forward()
time.sleep(3)
driver.quit()
