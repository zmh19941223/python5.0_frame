
import time
# 导包
from selenium import webdriver


# 创建driver对象
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\css_example.html"
# 打开指定的url
driver.get(url)
time.sleep(1)

# 获取元素并点击
driver.find_element_by_xpath("/html/body/input[1]").click()
# 切换到alter弹框
alter = driver.switch_to.alert
time.sleep(1)
# 进行操作
alter.accept()

# 获取元素并点击
driver.find_element_by_xpath("/html/body/input[2]").click()
# 切换到alter弹框
alter = driver.switch_to.alert
time.sleep(1)
# 进行取消操作
print(alter.text)
alter.dismiss()

# 获取元素并点击
driver.find_element_by_xpath("/html/body/input[3]").click()
# 切换到alter弹框
alter = driver.switch_to.alert
time.sleep(1)
# alter.send_keys("哈哈")
time.sleep(2)
# 进行操作
alter.dismiss()


time.sleep(2)
driver.quit()