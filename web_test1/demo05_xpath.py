import time
# 导包
from selenium import webdriver


# 创建driver对象
driver = webdriver.Chrome()


url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"

# 打开指定的url
driver.get(url)

# input01 = driver.find_element_by_xpath("//input[@id='userA']")

input01 = driver.find_element_by_css_selector("#userA")
input01.send_keys("123@itcast.cn")


time.sleep(3)
# 关闭浏览器
driver.quit()
