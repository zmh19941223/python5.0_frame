import time
# 导包
from selenium import webdriver


# 创建driver对象
driver = webdriver.Chrome()


url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"

# 打开指定的url
driver.get(url)

input04 = driver.find_elements_by_tag_name("input")
# print(type(input04))
# print(len(input04))
# print(input04)

input04[3].send_keys("123@itcast.cn")

# input04.send_keys("123@itcast.cn")
time.sleep(1)

time.sleep(3)
# 关闭浏览器
driver.quit()

