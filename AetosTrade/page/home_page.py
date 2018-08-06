#!/usr/bin/env python
#-*- coding:utf-8 -*-
from utils.get_by_local import GetByLocal
import time
from base.base_driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    '''获取首页页面所有的页面元素信息'''
    def __init__(self,driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

    def get_market_tab_element(self):
        '''
        获取行情元素信息
        '''
        return self.get_by_local.get_element('market_tab','home_page_element')


    def get_trade_tab_element(self):
        '''
        获取订单元素信息
        '''
        return self.get_by_local.get_element('trade_tab', 'home_page_element')

    def get_news_tab_element(self):
        '''
        获取新闻元素信息
        '''
        return self.get_by_local.get_element('news_tab', 'home_page_element')

    def get_self_tab_element(self):
        '''
        获取我元素信息
        '''
        return self.get_by_local.get_element('self_tab', 'home_page_element')
