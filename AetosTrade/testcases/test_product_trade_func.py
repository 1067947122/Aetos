#!/usr/bin/env python
#-*- coding:utf-8 -*-
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
import time
from time import sleep
from lib.common_class import Login
from lib.common import read_ini
import traceback
import sys,os
class ProductTrade(Login):
    def test_product_trade(self):
        """产品交易用例,需外汇页面存在产品"""
        driver = self.driver
        print driver.get_window_size()
        x = driver.get_window_size()["width"]
        y = driver.get_window_size()["height"]
        pwd = read_ini()[1]
        driver.find_element_by_id("com.aetos:id/rb_currency").click()   #点击外汇
        driver.find_elements_by_id("com.aetos:id/normal_tv_name")[0].click()   #选取外汇页面第一个产品
        driver.find_element_by_id("hide_tv_symbol_trade").click() #点击交易
        driver.find_element_by_id("com.aetos:id/trade_soon_bid").click()   #选择买入或卖出
        driver.find_element_by_id("js_xd_sub_btn").click()    #点击下单交易
        driver.find_element_by_class_name("android.widget.RelativeLayout").find_element_by_id("mt4_pwd_edt").send_keys(pwd)
        driver.find_element_by_id("pop_mt4pwd_complete").click()
        driver.find_element_by_id("com.aetos:id/trade_btn_succ").click()  #下单成功确认返回
        sleep(3)

        driver.find_element_by_id("symbol_trade_back").click()   #返回行情页面
        driver.find_elements_by_id("com.aetos:id/normal_tv_name")[1].click()  #选取外汇页面第二个产品
        driver.find_element_by_id("hide_tv_symbol_trade").click()
        driver.find_element_by_id("trade_soon_bid").click()
        driver.find_element_by_id("js_xd_sub_btn").click()
        driver.find_element_by_id("trade_btn_succ").click()
        driver.find_element_by_id("com.aetos:id/symbol_trade_back").click() #返回行情页面
        driver.find_element_by_id("com.aetos:id/main_rb_trade").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "product_order_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))  #产生的订单截图
        for a in range(2):
            #driver.swipe(749,339,370,339,1000)
            driver.find_element_by_id("com.aetos:id/order_item_close_out").click() #点击平仓
            driver.tap([(636,614)],500)
            driver.get_screenshot_as_file(
                os.path.join(os.path.abspath("./screenshots"),
                             "close_out_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
            driver.find_element_by_id("com.aetos:id/sub_btn_succ").click()
























