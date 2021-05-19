
import time
# 导包
from selenium import webdriver


# 创建driver对象
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.set_window_size(500, 600)

url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"
# 打开指定的url
driver.get(url)
time.sleep(1)

# 向下滚动1000单位
script = "window.scrollTo(0,1000)"
driver.execute_script(script)
time.sleep(2)

# 向右滚动1000单位
script = "window.scrollTo(1000,1000)"
driver.execute_script(script)

time.sleep(2)
driver.quit()