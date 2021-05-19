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
driver.get(r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html")
time.sleep(1)

driver.find_element_by_id("userA").send_keys("admin")
# 给图片命名
# img_name = time.strftime("%Y%m%d_%H%M%S")
img_name = str(time.time()).replace(".", "_")
# 截图并生成图片
driver.get_screenshot_as_file("./images/%s.png" % img_name)

time.sleep(3)
driver.quit()

