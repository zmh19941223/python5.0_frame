import unittest

from iwebshop_login_testcase import IwebshopLoginTest
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(IwebshopLoginTest))

with open("./reports/iwebshop_login_test_report.html", "wb") as f:
    h = HTMLTestRunner(stream=f, title="iwebshop登录模块自动化测试报告", description="windows10 chrome")
    h.run(suite)
