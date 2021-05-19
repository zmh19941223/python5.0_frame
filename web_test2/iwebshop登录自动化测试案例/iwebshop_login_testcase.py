import time
import unittest
from selenium import webdriver


class IwebshopLoginTest(unittest.TestCase):
    # 前期准备工作
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(r"http://127.0.0.1:8088/iwebshop/")
        # time.sleep(1)

    # 测试完收尾工作
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # 定位登录按钮
        self.driver.find_element_by_link_text("登录").click()
        # 定位输入框
        self.driver.find_element_by_name("login_info").send_keys("test")
        self.driver.find_element_by_name("password").send_keys("123456")
        # 定位登录提交按钮
        self.driver.find_element_by_class_name("submit_login").click()
        # 保存登录后用户信息，以便断言使用
        login_info = self.driver.find_element_by_class_name("loginfo").text
        try:
            # 执行断言操作
            self.assertIn("test", login_info)
        except AssertionError as e:
            print("登录失败")
            # 如果断言失败，截图并保存
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".", "_"))
            raise

    def test_login_error(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_name("login_info").send_keys("test1")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_class_name("submit_login").click()
        login_info = self.driver.find_element_by_class_name("loginfo").text
        try:
            self.assertIn("test1", login_info)
        except AssertionError as e:
            print("登录失败")
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".", "_"))
            raise
