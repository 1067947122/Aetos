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
from appium.webdriver.common.touch_action import TouchAction
from lib.common_class import Login
class Menu(Login):
    def test_left_menu_success(self):
        """左菜单点击能够正确跳转到相关页面"""
        driver = self.driver
        driver.implicitly_wait(10)
        driver.find_element_by_id("com.aetos:id/bar_user_open").click()
        sleep(3)
        driver.find_elements_by_class_name("android.widget.TextView")[0].click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").index(1).text(\"行情\")").click()
        sleep(3)
        driver.find_element_by_id("com.aetos:id/bar_user_open").click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").index(2).text(\"订单\")").click()
        sleep(3)
        driver.find_element_by_id("com.aetos:id/bar_user_open").click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").index(3).text(\"交易\")").click()
        driver.find_element_by_id("com.aetos:id/symbol_trade_back").click()
        driver.find_element_by_id("com.aetos:id/bar_user_open").click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").index(4).text(\"新闻\")").click()
        sleep(3)
        driver.find_element_by_id("com.aetos:id/bar_user_open").click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").index(5).text(\"设置\")").click()
        sleep(3)
        driver.find_element_by_id("com.aetos:id/bar_user_open").click()
        driver.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.TextView\").index(6).text(\"退出账户\")").click()
        sleep(3)