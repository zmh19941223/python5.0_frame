
import time
# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# 创建driver对象
driver = webdriver.Chrome()
# 创建action对象
action = ActionChains(driver)

# 浏览器窗口最大化
# driver.maximize_window()
# time.sleep(1)

url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\drag.html"
# 打开指定的url
driver.get(url)
time.sleep(1)

source = driver.find_element_by_id("div1")
target = driver.find_element_by_id("div2")
time.sleep(1)
action.drag_and_drop(source, target).perform()


time.sleep(2)
driver.quit()