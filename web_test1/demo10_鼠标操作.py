import time
# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# 创建driver对象
driver = webdriver.Chrome()
action = ActionChains(driver)

# 浏览器窗口最大化
# driver.maximize_window()
# time.sleep(1)

url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"
# 打开指定的url
driver.get(url)
time.sleep(1)

userA = driver.find_element_by_id("userA")
userA.send_keys("admin")
# 右击
action.context_click(userA).perform()
# 双击
action.double_click(userA).perform()

time.sleep(2)
driver.quit()