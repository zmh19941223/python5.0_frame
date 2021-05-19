
import time
# 导包
from selenium import webdriver


# 创建driver对象
driver = webdriver.Chrome()


url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"

# 打开指定的url
driver.get(url)


# link1 = driver.find_element_by_link_text("AA 百度 网站")
link1 = driver.find_element_by_partial_link_text("AA")
link1.click()

time.sleep(3)
# 关闭浏览器
driver.quit()
