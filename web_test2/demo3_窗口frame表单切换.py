
import time
# 导入webdriver包
from selenium import webdriver

# 创建driver对象
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
# 设置隐式等待时间
driver.implicitly_wait(30)
# 打开指定url
driver.get(r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册实例.html")
time.sleep(1)

# 跳转到指定frame表单
driver.switch_to.frame("myframe1")
driver.find_element_by_id("fwA").click()

print("打开新窗口后:", driver.window_handles)

# 跳转到新窗口
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)

# 跳转回老窗口
driver.switch_to.window(driver.window_handles[0])

# 回到老窗口后, 焦点默认在住页面
driver.switch_to.frame("myframe1")
driver.find_element_by_id("userA").send_keys("admin")

time.sleep(3)
driver.quit()

