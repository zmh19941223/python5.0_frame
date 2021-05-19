import time
# 导包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# 创建driver对象
driver = webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(10)
# 窗口最大化
driver.maximize_window()


action = ActionChains(driver)

# 浏览器窗口最大化
# driver.maximize_window()
# time.sleep(1)

url = r"https://www.baidu.com"
# 打开指定的url
driver.get(url)
# 获取元素
more = driver.find_element_by_name("tj_briicon")
print(more)
time.sleep(1)
# 鼠标悬停
action.move_to_element(more).perform()


time.sleep(2)
driver.quit()

