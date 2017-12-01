#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os,sys
from common import *
class Login(unittest.TestCase):
    def setUp(self):
        dic = {}
        dic["platformName"] = "Android"
        dic["platformVersion"] = "5.0"
        dic["deviceName"] = "192.168.218.101:5555"
        dic["appPackage"] = "com.aetos"
        dic["appActivity"] = "com.aetos.ui.module.core.LoadingActivity"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dic)
        driver = self.driver
        login(driver)
    def tearDown(self):
        driver = self.driver
        driver.quit()