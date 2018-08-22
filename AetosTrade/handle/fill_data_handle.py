#!/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from page.fill_data_page import FillDataPage

class FillDataHandle:
    def __init__(self, driver):
        self.fill_data_page = FillDataPage(driver)
        self.driver = driver


    def select_account_type(self,account_type='7'):
        '''
        在填写个人信息页面选择账户类型
        account_type:默认为7
        '''
        Select(self.fill_data_page.get_account_type_element()).select_by_value(account_type)

    def select_call(self,call='1'):
        '''
        在填写个人信息页面选择称呼
        call:默认为1,1为先生，0为女士
        '''
        Select(self.fill_data_page.get_call_element()).select_by_value(call)

    def send_name(self,name='test'):
        '''
        在填写个人信息页面输入姓
        '''
        self.fill_data_page.get_name_element().send_keys(name)

    def send_surename(self,surename='cache'):
        '''
        在填写个人信息页面输入名
        '''
        self.fill_data_page.get_surename_element().send_keys(surename)

    def send_chinese_name(self,chinese_name='数字'):
        '''
        在填写个人信息页面输入中文姓名
        '''
        self.fill_data_page.get_chinese_name_element().send_keys(chinese_name)

    def click_card_type(self):
        '''
        点击证件类型
        '''
        self.fill_data_page.get_card_type_element().click()

    def send_card_no(self,card_no='52145025201'):
        '''
        在填写个人信息页面输入证件号
        '''
        self.fill_data_page.get_card_no_element().send_keys(card_no)

    def send_birth_date(self,year='1980',month='02',day='05'):
        '''
        在填写个人信息页面输入出生日期
        '''
        self.fill_data_page.get_birth_date_element().send_keys(year)
        self.fill_data_page.get_birth_date_element().send_keys(Keys.TAB)
        self.fill_data_page.get_birth_date_element().send_keys(month)
        self.fill_data_page.get_birth_date_element().send_keys(day)

    def send_city(self,city='sz'):
        '''
        在填写个人信息页面输入城市
        '''
        self.fill_data_page.get_city_element().send_keys(city)

    def send_live_address(self,live_address='sz'):
        '''
        在填写个人信息页面输入居住地址
        '''
        self.fill_data_page.get_live_address_element().send_keys(live_address)

    def send_live_date(self,live_date='4'):
        '''
        在填写个人信息页面输入居住年限
        '''
        self.fill_data_page.get_live_date_element().send_keys(live_date)

    def send_home_phone(self,home_phone='1402503'):
        '''
        在填写个人信息页面输入家庭电话
        '''
        self.fill_data_page.get_home_phone_element().send_keys(home_phone)

    def select_for_exp(self,exp='1-3年'):
        '''
        在填写个人信息页面选择外汇经验
        exp:可选择’无‘，’1-3年‘，’3年以上‘
        '''
        Select(self.fill_data_page.get_for_exp_element()).select_by_value(exp)

    def select_investFreq(self,value='1'):
        '''
        在填写个人信息页面选择外汇投资频率
        value:可选择1--5
        '''
        Select(self.fill_data_page.get_invest_freq_element()).select_by_value(value)

    def select_otherExp(self,value='2'):
        '''
        在填写个人信息页面选择其他经验
        value:可选择1--3
        '''
        Select(self.fill_data_page.get_otherExp_element()).select_by_value(value)

    def select_business(self,bus='1'):
        '''
        在填写个人信息页面选择行业
        bus:可选择'1---13'
        '''
        Select(self.fill_data_page.get_business_element()).select_by_value(bus)

    def click_fill_complete(self):
        '''
        点击完成
        '''
        self.fill_data_page.get_fill_complete_element().click()

    def click_page1_next_step(self):
        '''
        点击page1_next_step下一步
        '''
        self.fill_data_page.get_page1_next_step_element().click()

    def click_page2_next_step(self):
        '''
        点击page2_next_step下一步
        '''
        self.fill_data_page.get_page2_next_step_element().click()

    def click_page3_next_step(self):
        '''
        点击page3_next_step下一步
        '''
        self.fill_data_page.get_page3_next_step_element().click()

    def click_isPolitic(self):
        '''
        点击isPolitic
        '''
        self.fill_data_page.get_isPolitic_element().click()

    def click_isTax(self):
        '''
        点击isTax
        '''
        self.fill_data_page.get_isTax_element().click()

    def click_isUsa(self):
        '''
        点击isUsa
        '''
        self.fill_data_page.get_isUsa_element().click()

    def click_isForUsa(self):
        '''
        点击isForUsa
        '''
        self.fill_data_page.get_isForUsa_element().click()

    def click_isEarnUsa(self):
        '''
        点击isEarnUsa
        '''
        self.fill_data_page.get_isEarnUsa_element().click()

    def send_position(self,position='服务员'):
        '''
        在填写个人信息页面输入职位
        '''
        self.fill_data_page.get_position_element().send_keys(position)

    def send_employerName(self,employerName='李老师'):
        '''
        在填写个人信息页面输入雇主名字
        '''
        self.fill_data_page.get_employerName_element().send_keys(employerName)

    def click_accept_data(self):
        '''
        点击accept_data
        '''
        self.fill_data_page.get_accept_data_element().click()

    def click_accept_person_data(self):
        '''
        点击accept_person_data
        '''
        self.fill_data_page.get_accept_person_data_element().click()

    def click_accept_term(self):
        '''
        点击accept_term
        '''
        self.fill_data_page.get_accept_term_element().click()

    def click_accept_open_form(self):
        '''
        点击accept_open_form
        '''
        self.fill_data_page.get_accept_open_form_element().click()

    def click_accept_Disclaimer(self):
        '''
        点击accept_Disclaimer
        '''
        self.fill_data_page.get_accept_Disclaimer_element().click()

    def click_accept_Disclosure_Statement(self):
        '''
        点击accept_Disclosure_Statement
        '''
        self.fill_data_page.get_accept_Disclosure_Statement_element().click()

    def click_accept_Policy(self):
        '''
        点击accept_Policy
        '''
        self.fill_data_page.get_accept_Policy_element().click()

    def click_accept_Financial_Services_Guide(self):
        '''
        点击accept_Financial_Services_Guide
        '''
        self.fill_data_page.get_accept_Financial_Services_Guide_element().click()

    def click_accept_Risk_Warning(self):
        '''
        点击accept_Risk_Warning
        '''
        self.fill_data_page.get_accept_Risk_Warning_element().click()

    def click_understand_trade(self):
        '''
        点击understand_trade
        '''
        self.fill_data_page.get_understand_trade_element().click()

    def click_understand_market(self):
        '''
        点击understand_market
        '''
        self.fill_data_page.get_understand_market_element().click()

    def click_understand_lever(self):
        '''
        点击understand_lever
        '''
        self.fill_data_page.get_understand_lever_element().click()

    def click_understand_risk(self):
        '''
        点击understand_risk
        '''
        self.fill_data_page.get_understand_risk_element().click()


    def click_upload_data(self):
        '''
        填写完个人信息后点击上传资料
        '''
        self.fill_data_page.get_upload_data_element().click()