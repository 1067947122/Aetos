#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
from utils.read_ini import ReadIni
from utils.write_txt import WriteTxt
from base.base_driver import Driver
from page.register_demo_page import RegisterPage
from handle.register_demo_handle import RegisterHandle
from business.register_demo_business import RegisterBusiness
from handle.fill_data_handle import FillDataHandle

class FillDataBusiness:
    def __init__(self,driver):
        self.register_handle = RegisterHandle(driver)
        self.driver = driver
        self.ini = ReadIni()
        self.txt = WriteTxt()
        self.register = RegisterBusiness(self.driver)
        self.register_page = RegisterPage(driver)
        self.fill_data_handle = FillDataHandle(driver)
        self.driver.implicitly_wait(20)

    def fill_data_pass(self):
        '''
        成功完善用户注册资料
        '''
        self.register.register_demo_pass()
        self.register_handle.click_fill_data_btn()
        time.sleep(20)
        self.fill_data_handle.select_account_type() #选择账户类型
        self.fill_data_handle.click_page1_next_step()
        self.fill_data_handle.select_call() #选择称呼
        self.fill_data_handle.send_name()
        self.fill_data_handle.send_surename()
        self.fill_data_handle.send_chinese_name()
        self.fill_data_handle.click_card_type()
        self.fill_data_handle.send_card_no()
        self.fill_data_handle.send_birth_date()
        self.fill_data_handle.send_city()
        self.fill_data_handle.send_live_address()
        self.fill_data_handle.send_live_date()
        self.fill_data_handle.send_home_phone()
        self.fill_data_handle.click_page2_next_step()
        self.fill_data_handle.select_for_exp()
        self.fill_data_handle.select_investFreq()
        self.fill_data_handle.select_otherExp()
        self.fill_data_handle.click_isPolitic()
        self.fill_data_handle.click_isTax()
        self.fill_data_handle.click_isUsa()
        self.fill_data_handle.click_isForUsa()
        self.fill_data_handle.click_isEarnUsa()
        self.fill_data_handle.click_page3_next_step()
        self.fill_data_handle.select_business()
        self.fill_data_handle.send_position()
        self.fill_data_handle.send_employerName()
        self.fill_data_handle.click_accept_term()
        self.fill_data_handle.click_accept_data()
        self.fill_data_handle.click_accept_Disclaimer()
        self.fill_data_handle.click_accept_Disclosure_Statement()
        self.fill_data_handle.click_accept_Financial_Services_Guide()
        self.fill_data_handle.click_accept_open_form()
        self.fill_data_handle.click_accept_person_data()
        self.fill_data_handle.click_accept_Policy()
        self.fill_data_handle.click_accept_Risk_Warning()
        self.fill_data_handle.click_understand_lever()
        self.fill_data_handle.click_understand_market()
        self.fill_data_handle.click_understand_risk()
        self.fill_data_handle.click_understand_trade()
        self.fill_data_handle.click_fill_complete()
        time.sleep(15)