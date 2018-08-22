#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from base.base_driver import Driver
from business.register_demo_business import RegisterBusiness
from page.home_page import HomePage
from utils.write_txt import WriteTxt

class TestRegisterDemo(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().android_driver(0)
        self.register = RegisterBusiness(self.driver)
        self.txt = WriteTxt()
        self.driver.implicitly_wait(20)

    def tearDown(self):
        pass
        # driver = self.driver
        # driver.quit()

    def test_register_demo_success(self):
        '''
        :condition:用户正在注册页面
        :step:用户完成注册demo用户信息填写
        :except:能够完成demo账户且生成demo账户
        '''
        self.register.register_demo_pass()

if __name__ == '__main__':
    unittest.main()
