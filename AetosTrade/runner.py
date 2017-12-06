#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
import time
from HTMLTestRunner import  HTMLTestRunner
from appium import webdriver
from time import sleep
import os
from lib.sendmail import *
from lib.common import zip_dir
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from testcases.test_news_func import News
if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(News))
    #test_dir = "./testcases"
    file = open("./reports/test_reports_%s.html" % time.strftime("%Y-%m-%d %H-%M-%S"),"wb")
    runner = HTMLTestRunner(stream=file,title=u"AetosTrade自动化测试报告",
                            description=u"用例执行情况:")
    #discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    runner.run(suite)
    file.close()
    zip_dir("./screenshots","screenshots.zip")
    test_report_path = os.path.join(os.getcwd(), "reports")
    new_file = new_report(test_report_path)
    newfile,reportname = new_file
    send_email(newfile,reportname)
    if os.path.isfile("./screenshots.zip"):
        os.remove("screenshots.zip")

