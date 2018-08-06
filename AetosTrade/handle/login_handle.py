#!/usr/bin/env python
# -*- coding:utf-8 -*-
from page.login_page import LoginPage
class LoginHandle:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def send_username(self, user):
        '''
        在用户名登陆页面输入用户名
        '''
        self.login_page.get_username_element().send_keys(user)

    def send_password(self, password):
        '''
        在用户名登陆页面输入密码
        '''
        self.login_page.get_password_element().send_keys(password)

    def send_trade_account(self,account):
        '''
        在交易账号登陆页面输入交易账号
        '''
        self.login_page.get_trade_account_element().send_keys(account)

    def send_mt4_pwd(self,mt4_pwd):
        '''
        在交易账号登陆页面输入密码
        '''
        self.login_page.get_mt4_pwd_element().send_keys(mt4_pwd)

    def send_area_code(self,area_code):
        '''
        在其他地区登陆页面输入区号
        '''
        self.login_page.get_area_code_element().send_keys(area_code)

    def send_area_phone(self,phone):
        '''
        在其他地区登陆页面输入手机号
        '''
        self.login_page.get_area_phone_element().send_keys(phone)

    def send_area_pwd(self,area_pwd):
        '''
        在其他地区登陆页面输入密码
        '''
        self.login_page.get_area_pwd_element().send_keys(area_pwd)

    def click_server(self):
        '''
        选择服务器
        '''
        self.login_page.get_mt4_server_element().click()

    def click_back(self):
        '''
        点击返回按钮
        '''
        self.login_page.get_back_element().click()

    def click_login(self):
        '''
        点击登录按钮
        '''
        self.login_page.get_login_button_element().click()

    def click_forget_password(self):
        '''
        点击忘记密码
        '''
        self.login_page.get_forget_password_element().click()

    def click_remember_password(self):
        '''
        点击记住密码
        '''
        self.login_page.get_remember_password_element().click()

    def click_register(self):
        '''
        点击注册
        '''
        self.login_page.get_register_element().click()

    def click_show_password(self):
        '''
        点击显示密码
        '''
        self.login_page.get_show_pwd_element().click()

    def click_auto_login(self):
        '''
        点击自动登陆
        '''
        self.login_page.get_auto_login_element().click()

    def click_select_mt4_server(self,server):
        '''
        点击交易账号所在的服务器
        '''
        self.login_page.get_select_mt4_server_element(server).click()

    def click_mt4_btn(self):
        '''
        点击交易账号登陆页面的btn
        '''
        self.login_page.get_mt4_login_btn_element().click()

    def click_other_area_btn(self):
        '''
        点击其它地区登陆页面的btn
        '''
        self.login_page.get_other_area_btn_element().click()

    def get_fail_toast(self, message):
        '''
        获取toast，根据返回信息进行反数据
        '''
        self.login_page.get_toast_element(message)
