
import time
# 导包
from selenium import webdriver


# 创建driver对象
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"
# 打开指定的url
driver.get(url)
time.sleep(1)

# 常见select对象
select = Select(driver.find_element_by_id("selectA"))

# # 通过索引选择 索引从0开始
# select.select_by_index(1)
# time.sleep(2)
#
# # 通过属性value的值选择
# select.select_by_value("gz")
# time.sleep(2)
#
# # 通过html显示内容选择
# select.select_by_visible_text("A重庆")

# print(select.options)
# print(len(select.options))

# 所有option标签对象都存在select.options里, 是个列表
for option in select.options:
    option.click()
    time.sleep(2)

time.sleep(2)
driver.quit()
