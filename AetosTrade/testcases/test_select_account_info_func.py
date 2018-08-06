#!/usr/bin/env python
#-*- coding:utf-8 -*-
from lib.com_class import Login
import os,time
class AccountInfo(Login):
    def test_select_account_info(self):
        """查看用户的账户详情信息"""
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/main_rb_self").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "account_balance_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/account_info_txt").click()
        driver.find_element_by_id("com.aetos:id/real_account_txt").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "real_account_info_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        driver.find_element_by_id("com.aetos:id/mt4_account_bar_back").click()

        driver.find_element_by_id("com.aetos:id/analog_account_txt").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "demo_account_info_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        driver.find_element_by_id("com.aetos:id/mt4_account_bar_back").click()

        driver.find_element_by_id("com.aetos:id/deposit_txt").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "deposit_page_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()

        driver.find_element_by_id("com.aetos:id/withdraw_txt").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "withdraw_page_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()

        driver.find_element_by_id("com.aetos:id/upload_data_txt").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "upload_data_page_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()