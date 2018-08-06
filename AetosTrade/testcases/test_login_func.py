#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from base.base_driver import Driver
from business.login_business import LoginBusiness
from page.home_page import HomePage
from utils.write_txt import WriteTxt


class LoginApp(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().android_driver(0)
        self.login = LoginBusiness(self.driver)
        self.txt = WriteTxt()
        self.homepage = HomePage(self.driver)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        driver = self.driver
        driver.quit()

    def test_login_success(self):
        '''
        :condition:用户用户登陆页面
        :step:输入正确的用户名和密码登陆
        :except:用户能够登陆成功
        '''
        self.login.username_login_pass()
        market = self.homepage.get_market_tab_element().text
        print(market)
        try:
            self.assertEqual(market,'行情',msg='登陆成功')
        except:
            self.txt.write_data('fail')
            raise
        else:
            self.txt.write_data('pass')

    def test_login_username_error(self):
        '''
        :condition:用户在登陆页面
        :step:用户名输入错误，密码输入正确
        :except:用户不能够登陆成功
        '''
        self.login.username_login_username_error()
        market = self.homepage.get_market_tab_element()

        try:
            self.assertIsNone(market,msg='登陆失败')
        except:
            self.txt.write_data('fail')
            raise
        else:
            self.txt.write_data('pass')

    def test_login_password_error(self):
        '''
        :condition:用户在登陆页面
        :step:用户名输入正确，密码输入错误
        :except:用户不能够登陆成功
        '''
        self.login.username_login_password_error()
        market = self.homepage.get_market_tab_element()
        try:
            self.assertIsNone(market,msg='登陆失败')
        except:
            self.txt.write_data('fail')
            raise
        else:
            self.txt.write_data('pass')

    def test_mt4_login_pass(self):
        '''
        :condition:用户在MT4登陆页面
        :step:mt4输入正确，密码输入正确
        :except:用户能够登陆成功
        '''
        self.login.mt4_login_pass('AETOS-LIVE')
        market = self.homepage.get_market_tab_element().text
        print(market)
        try:
            self.assertEqual(market,u'行情',msg='登陆成功')
        except:
            self.txt.write_data('fail')
            raise
        else:
            self.txt.write_data('pass')

    def test_mt4_login_mt4_error(self):
        '''
        :condition:用户在MT4登陆页面
        :step:mt4输入错误，密码输入正确
        :except:用户登陆不成功
        '''
        self.login.mt4_login_mt4_error('AETOS-LIVE')
        market = self.homepage.get_market_tab_element()
        try:
            self.assertIsNone(market,msg='登陆失败')
        except:
            self.txt.write_data('fail')
            raise
        else:
            self.txt.write_data('pass')

    def test_mt4_login_pwd_error(self):
        '''
        :condition:用户在MT4登陆页面
        :step:mt4输入正确，密码输入错误
        :except:用户登陆不成功
        '''
        self.login.mt4_login_pwd_error('AETOS-LIVE')
        market = self.homepage.get_market_tab_element()
        try:
            self.assertIsNone(market,msg='登陆失败')
        except:
            self.txt.write_data('fail')
            raise
        else:
            self.txt.write_data('pass')


if __name__ == '__main__':
    unittest.main()