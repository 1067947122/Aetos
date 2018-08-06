#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from lib.com_class import Login
import sys,os
class MarketPrice(Login):
    def test_standard_view_select_price(self):
        """标准视图查看产品价格"""
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/rb_currency").click() #切换到外汇
        #滚动查看产品
        for a in range(6):
            driver.swipe(330,670,330,265,1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "standard_view_forex_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_metal").click()  #切换到金属
        for a in range(6):
            driver.swipe(330,670,330,265,1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "standard_view_metal_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_energy").click()  #切换到能源
        for a in range(6):
            driver.swipe(330,670,330,265,1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "standard_view_energy_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_stock").click()   #切换到股指
        for a in range(6):
            driver.swipe(330,670,330,265,1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "standard_view_stock_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

    def test_advance_view_select_price(self):
        """高级视图查看产品价格"""
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/symbol_tv_show_type").click()  #切换高级视图
        driver.tap([(400,620)],1000)
        driver.find_element_by_id("com.aetos:id/pop_type_complete").click()    #确认切换

        driver.find_element_by_id("com.aetos:id/rb_currency").click()  # 切换到外汇
        for a in range(6):
            driver.swipe(330,670,330,265,1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "advance_view_forex_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_metal").click()  # 切换到金属
        for a in range(6):
            driver.swipe(330, 670, 330, 265, 1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "advance_view_metal_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_energy").click()  # 切换到能源
        for a in range(6):
            driver.swipe(330, 670, 330, 265, 1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "advance_view_energy_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_stock").click()  # 切换到股指
        for a in range(6):
            driver.swipe(330, 670, 330, 265, 1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "advance_view_stock_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

    def test_tradition_view_select_price(self):
        """传统视图查看产品价格"""
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/symbol_tv_show_type").click()  #切换传统视图
        driver.tap([(280,700)], 1000)
        driver.find_element_by_id("com.aetos:id/pop_type_complete").click()   #切换完成

        driver.find_element_by_id("com.aetos:id/rb_currency").click()  # 切换到外汇
        for a in range(6):
            driver.swipe(330, 670, 330, 265, 1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "tradition_view_forex_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_metal").click()  # 切换到金属
        for a in range(6):
            driver.swipe(330, 670, 330, 265, 1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "tradition_view_metal_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_energy").click()  # 切换到能源
        for a in range(6):
            driver.swipe(330, 670, 330, 265, 1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "tradition_view_energy_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/rb_stock").click()  # 切换到股指
        for a in range(6):
            driver.swipe(330, 670, 330, 265, 1000)
            sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "tradition_view_stock_price_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
