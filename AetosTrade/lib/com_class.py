#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from base.base_driver import Driver
from business.login_business import LoginBusiness
from page.home_page import HomePage
from utils.write_txt import WriteTxt
from handle.login_handle import LoginHandle
class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver().android_driver(0)
        cls.login = LoginBusiness(cls.driver)
        cls.homepage = HomePage(cls.driver)
        cls.txt = WriteTxt()
        cls.driver.implicitly_wait(15)
        cls.login.username_login_pass()

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.quit()