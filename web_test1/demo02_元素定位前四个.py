import time
# 导包
from selenium import webdriver


# 创建driver对象
driver = webdriver.Chrome()

url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"
driver.get(url)

input01 = driver.find_element_by_id("userA")
input01.send_keys("admin")
time.sleep(1)

input02 = driver.find_element_by_name("passwordA")
input02.send_keys("123456")
time.sleep(1)

input03 = driver.find_element_by_class_name("telA")
input03.send_keys("18811110000")
time.sleep(1)

driver.find_elements_by_tag_name("input")[3].send_keys("123@itcast.cn")
time.sleep(1)

time.sleep(2)
driver.quit()
