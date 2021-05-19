import time
# 导包
from selenium import webdriver


# 创建driver对象
driver = webdriver.Chrome()
url = r"C:\Users\DOU\Desktop\day05-web自动化测试\02-资料\素材\注册A.html"
# 打开指定的url
driver.get(url)
# 设置要输入内容的列表
text_list = ['admin', '123456', '18611111111', '123@qq.com']
# 获取前四个input标签
inputs = driver.find_elements_by_css_selector("p>input")
# print(inputs)
for i in range(4):
    inputs[i].send_keys(text_list[i])
    time.sleep(1)

inputs[3].clear()

# 获取id为AAA的标签
a = driver.find_element_by_css_selector("#AAA")
# 点击
a.click()

time.sleep(3)
# 关闭浏览器
driver.quit()
