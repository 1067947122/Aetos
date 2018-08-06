#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
from time import sleep
import unittest,os,sys
from keywords.get_data import GetData
from appium import webdriver
from base.base_driver import Driver
from utils.read_ini import ReadIni
from keywords.action_method import ActionMethod


# class LoginApp(unittest.TestCase):
#     def setUp(self):
#         self.driver = Driver().android_driver(0)
#
#
#     def tearDown(self):
#         driver = self.driver
#         driver.quit()
#
#     def test_user_login_success(self):
#         """用户输入正确的账户和密码登陆"""
#
#         driver = self.driver
#         key01 = GetData().get_element_key(1)
#         key02 = GetData().get_element_key(2)
#         ActionMethod().input()
#
#
#
#         # username = ReadIni().get_value(key=key01)
#         # password = ReadIni().get_value(key=key02)
#         driver.implicitly_wait(10)
#         driver.find_element_by_id("login_user_et_account").clear()
#         driver.find_element_by_id("login_user_et_password").clear()
#         driver.find_element_by_id("login_user_et_account").send_keys(username)
#         driver.find_element_by_id("login_user_et_password").send_keys(password)
#         driver.find_element_by_id("login_btn").click()
#         sleep(3)
#         title = driver.find_element_by_id("com.aetos:id/bar_title").text
#         print(title)
#         self.assertEqual(title,u"行情") #检查点
#         sleep(3)
#
# key01 = GetData().get_element_key(1)
# key02 = GetData().get_element_key(2)
# print(type(key01))
# username = ReadIni().get_value(key01)
# print(key01,username)
from page.login_page import LoginPage
page = LoginPage(1)
print page.get_username_element()