#!/usr/bin/env python
#-*- coding:utf-8 -*-
from lib.com_class import Login
import os,time
from time import sleep
class MarketChart(Login):
    def test_select_market_chart(self):
        """查看产品的行情走势图"""
        driver = self.driver
        driver.implicitly_wait(15)
        driver.find_element_by_id("com.aetos:id/symbol_chart_btn_search").click()  #点击查看
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "M1_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        sleep(3)
        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[1].click()  #M5
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "M5_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[2].click()  #M15
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "M15_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[3].click()  #M30
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "M30_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[4].click()   #H1
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "H1_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[5].click()   #H4
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "H4_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[6].click()   #D1
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "D1_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[7].click()   #W1
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "W1_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/chart_cur_date").click()
        driver.find_elements_by_id("com.aetos:id/chart_period")[8].click()   #MN1
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "MN1_chart_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

        driver.find_element_by_id("com.aetos:id/hide_tv_symbol_info").click()   #点击资讯
        sleep(3)

        driver.find_elements_by_class_name("android.widget.LinearLayout")[0].click()  #查看资讯信息
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "product_information_num1_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.LinearLayout\").index(0)").click()
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()
        driver.find_elements_by_class_name("android.widget.LinearLayout")[2].click()
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()
        driver.find_elements_by_class_name("android.widget.LinearLayout")[3].click()
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()
        driver.find_element_by_id("com.aetos:id/back_bar_back").click()
        driver.find_element_by_id("com.aetos:id/hide_tv_symbol_detail").click()  #查看该产品的产品详情
        sleep(3)
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "product_details_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))