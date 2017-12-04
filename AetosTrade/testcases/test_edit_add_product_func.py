#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os,sys,time
from time import sleep
from lib.common_class import Login
class Edit(Login):
    def test_edit_add_customize_product(self):
        """全选产品添加到自选中，需要各功能中无产品显示在页面"""
        driver = self.driver
        driver.implicitly_wait(15)
        driver.find_element_by_id("com.aetos:id/bar_edit").click()   #点击编辑
        driver.find_element_by_id("com.aetos:id/symbol_edit_tv_select").click()   #点击全选
        driver.find_element_by_id("com.aetos:id/symbol_edit_complete").click()   #点击完成，添加到了自选产品
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "edit_add_customize_product_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

    def test_edit_add_forex_product(self):
        """全选产品添加到外汇中，需要各功能中无产品显示在页面"""
        driver = self.driver
        driver.implicitly_wait(15)
        driver.find_element_by_id("com.aetos:id/bar_edit").click()  #点击编辑
        driver.find_element_by_id("com.aetos:id/rb_currency").click()  #点击外汇
        driver.find_element_by_id("com.aetos:id/symbol_edit_tv_select").click()  # 点击全选
        driver.find_element_by_id("com.aetos:id/symbol_edit_complete").click()  # 点击完成
        driver.find_element_by_id("com.aetos:id/rb_currency").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "edit_add_forex_product_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

    def test_edit_add_metal_product(self):
        """全选产品添加到金属中，需要各功能中无产品显示在页面"""
        driver = self.driver
        driver.implicitly_wait(15)
        driver.find_element_by_id("com.aetos:id/bar_edit").click()  # 点击编辑
        driver.find_element_by_id("com.aetos:id/rb_metal").click()
        driver.find_element_by_id("com.aetos:id/symbol_edit_tv_select").click()  # 点击全选
        driver.find_element_by_id("com.aetos:id/symbol_edit_complete").click()  # 点击完成
        driver.find_element_by_id("com.aetos:id/rb_metal").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "edit_add_metal_product_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))

    def test_edit_add_energy_product(self):
        """全选产品添加到能源中，需要各功能中无产品显示在页面"""
        driver = self.driver
        driver.implicitly_wait(15)
        driver.find_element_by_id("com.aetos:id/bar_edit").click()  # 点击编辑
        driver.find_element_by_id("com.aetos:id/rb_energy").click()
        driver.find_element_by_id("com.aetos:id/symbol_edit_tv_select").click()  # 点击全选
        driver.find_element_by_id("com.aetos:id/symbol_edit_complete").click()  # 点击完成
        driver.find_element_by_id("com.aetos:id/rb_energy").click()
        driver.get_screenshot_as_file(
            os.path.join(os.path.abspath("./screenshots"),
                         "edit_add_energy_product_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S")))