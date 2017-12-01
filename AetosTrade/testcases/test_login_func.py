#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
from time import sleep
from lib.common import read_ini,is_id_exist
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import unittest,os
class LoginApp(unittest.TestCase):
    def setUp(self):
        dic = {}
        dic["platformName"] = "Android"
        dic["platformVersion"] = "5.0"
        dic["deviceName"] = "192.168.218.101:5555"
        dic["appPackage"] = "com.aetos"
        dic["appActivity"] = "com.aetos.ui.module.core.LoadingActivity"
        #dic["automationName"] = "uiautomator2"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dic)
        driver = self.driver
        driver.implicitly_wait(10)

    def tearDown(self):
        driver = self.driver
        driver.quit()
    def test_user_login_success(self):
        """用户输入正确的账户和密码登陆"""
        driver = self.driver
        driver.implicitly_wait(10)
        username = read_ini()[0]
        password = read_ini()[1]
        print username,password
        driver.find_element_by_id("login_user_et_account").clear()
        driver.find_element_by_id("login_user_et_password").clear()
        driver.find_element_by_id("login_user_et_account").send_keys(username)
        driver.find_element_by_id("login_user_et_password").send_keys(password)
        driver.find_element_by_id("login_btn").click()
        sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"), "user_success_login_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/bar_title").text
        print title
        self.assertEqual(title,u"行情") #检查点
        sleep(3)

    def test_user_login_error_pwd(self):
        """用户输入正确的账户和错误的密码登陆"""
        driver = self.driver
        username = read_ini()[0]
        error_pwd = read_ini()[3]
        print username,error_pwd
        driver.find_element_by_id("login_user_et_account").clear()
        driver.find_element_by_id("login_user_et_password").clear()
        driver.find_element_by_id("login_user_et_account").send_keys(username)
        driver.find_element_by_id("login_user_et_password").send_keys(error_pwd)
        driver.find_element_by_id("login_btn").click()
        sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "user_login_error_pwd_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/login_rb_user").text
        self.assertEqual(title,u"用户登陆")
        sleep(3)
    def test_user_login_error_username(self):
        """用户输入错误的账户和正确的密码登陆"""
        driver = self.driver
        error_username= read_ini()[2]
        pwd = read_ini()[1]
        print error_username,pwd
        driver.implicitly_wait(10)
        driver.find_element_by_id("login_user_et_account").clear()
        driver.find_element_by_id("login_user_et_password").clear()
        driver.find_element_by_id("login_user_et_account").send_keys(error_username)
        driver.find_element_by_id("login_user_et_password").send_keys(pwd)
        driver.find_element_by_id("login_btn").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "user_login_error_username_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/login_rb_user").text
        self.assertEqual(title,u"用户登陆")
        sleep(3)

    def test_MT4ID_login_success(self):
        """输入正确的mt4id和正确的密码登陆"""
        driver = self.driver
        mt4id = read_ini()[4]
        pwd = read_ini()[1]
        print mt4id,pwd
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/login_rb_mt4").click()
        driver.find_element_by_id("com.aetos:id/login_mt_et_account").clear()
        driver.find_element_by_id("com.aetos:id/login_mt_et_password").clear()
        driver.find_element_by_id("com.aetos:id/login_mt_et_account").send_keys(mt4id)
        driver.find_element_by_id("com.aetos:id/login_mt_et_password").send_keys(pwd)
        driver.find_element_by_id("com.aetos:id/login_btn").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "MT4ID_login_success_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/bar_title").text
        self.assertEqual(title,u"行情")
        sleep(3)

    def test_MT4ID_login_error_mt4id(self):
        """输入错误的mt4id和正确的密码登陆"""
        driver = self.driver
        error_mt4id = read_ini()[5]
        pwd = read_ini()[1]
        print error_mt4id,pwd
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/login_rb_mt4").click()
        driver.find_element_by_id("com.aetos:id/login_mt_et_account").clear()
        driver.find_element_by_id("com.aetos:id/login_mt_et_password").clear()
        driver.find_element_by_id("com.aetos:id/login_mt_et_account").send_keys(error_mt4id)
        driver.find_element_by_id("com.aetos:id/login_mt_et_password").send_keys(pwd)
        driver.find_element_by_id("com.aetos:id/login_btn").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "MT4ID_login_error_mt4id_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/login_mt_tv_account").text
        self.assertEqual(title,u"MT4 ID")
        sleep(3)

    def test_MT4ID_login_error_pwd(self):
        """输入正确的mt4id和错误的密码登陆"""
        driver = self.driver
        mt4id = read_ini()[4]
        error_pwd = read_ini()[3]
        print mt4id,error_pwd
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/login_rb_mt4").click()
        driver.find_element_by_id("com.aetos:id/login_mt_et_account").clear()
        driver.find_element_by_id("com.aetos:id/login_mt_et_password").clear()
        driver.find_element_by_id("com.aetos:id/login_mt_et_account").send_keys(mt4id)
        driver.find_element_by_id("com.aetos:id/login_mt_et_password").send_keys(error_pwd)
        driver.find_element_by_id("com.aetos:id/login_btn").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "MT4ID_login_error_pwd_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/login_mt_tv_account").text
        self.assertEqual(title,u"MT4 ID")
        sleep(3)


    def test_oversea_login_success(self):
        """输入正确的海外手机及正确的密码登陆"""
        driver = self.driver
        driver.implicitly_wait(10)
        area_code = read_ini()[7]
        oversea = read_ini()[6]
        pwd = read_ini()[1]
        print area_code,oversea,pwd
        driver.find_element_by_id("com.aetos:id/overseas_txt").click()
        driver.find_element_by_id("com.aetos:id/login_phone_et_code").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_account").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_password").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_code").send_keys(area_code)
        driver.find_element_by_id("com.aetos:id/login_phone_et_account").send_keys(oversea)
        driver.find_element_by_id("com.aetos:id/login_phone_et_password").send_keys(pwd)
        driver.find_element_by_id("com.aetos:id/login_btn").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "oversea_login_success_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/bar_title").text
        print title
        self.assertEqual(title,u"行情")
        sleep(3)

    def test_oversea_login_error_pwd(self):
        """输入正确的海外手机及错误的密码登陆"""
        driver = self.driver
        driver.implicitly_wait(10)
        area_code = read_ini()[7]
        oversea = read_ini()[6]
        error_pwd = read_ini()[3]
        print area_code,oversea,error_pwd
        driver.find_element_by_id("com.aetos:id/overseas_txt").click()
        driver.find_element_by_id("com.aetos:id/login_phone_et_code").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_account").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_password").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_code").send_keys(area_code)
        driver.find_element_by_id("com.aetos:id/login_phone_et_account").send_keys(oversea)
        driver.find_element_by_id("com.aetos:id/login_phone_et_password").send_keys(error_pwd)
        driver.find_element_by_id("com.aetos:id/login_btn").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "oversea_login_error_pwd_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/login_btn").text
        self.assertEqual(title,u"登   录")
        sleep(3)

    def test_oversea_login_error_oversea(self):
        """输入错误的海外手机及正确的密码登陆"""
        driver = self.driver
        driver.implicitly_wait(10)
        area_code = read_ini()[7]
        error_oversea = read_ini()[8]
        pwd = read_ini()[1]
        print area_code,error_oversea,pwd
        driver.find_element_by_id("com.aetos:id/overseas_txt").click()
        driver.find_element_by_id("com.aetos:id/login_phone_et_code").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_account").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_password").clear()
        driver.find_element_by_id("com.aetos:id/login_phone_et_code").send_keys(area_code)
        driver.find_element_by_id("com.aetos:id/login_phone_et_account").send_keys(error_oversea)
        driver.find_element_by_id("com.aetos:id/login_phone_et_password").send_keys(pwd)
        driver.find_element_by_id("com.aetos:id/login_btn").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "oversea_login_error_phone_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        title = driver.find_element_by_id("com.aetos:id/login_btn").text
        self.assertEqual(title,u"登   录")
        sleep(3)