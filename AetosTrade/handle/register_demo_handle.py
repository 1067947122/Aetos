#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time,os
from page.register_demo_page import RegisterPage
class RegisterHandle:
    def __init__(self, driver):
        self.register_page = RegisterPage(driver)
        self.driver = driver

    def send_phone(self,phone):
        '''
        在注册页面输入手机号
        '''
        self.register_page.get_phone_element().send_keys(phone)

    def send_verification_code(self,code):
        '''
        在注册页面输入验证码
        '''
        self.register_page.get_verification_code_element().send_keys(code)

    def send_mail(self,mail):
        '''
        在注册页面输入邮箱
        '''
        self.register_page.get_mail_element().send_keys(mail)

    def send_call(self,call):
        '''
        在注册页面输入称呼
        '''
        self.register_page.get_call_element().send_keys(call)

    def send_password(self,pwd):
        '''
        在注册页面输入注册密码
        '''
        self.register_page.get_pwd_element().send_keys(pwd)

    def send_confirm_password(self,pwd):
        '''
        在注册页面输入确认注册密码
        '''
        self.register_page.get_confirm_pwd_element().send_keys(pwd)

    def send_introducer(self,pwd):
        '''
        在注册页面输入介绍人
        '''
        self.register_page.get_introducer_element().send_keys(pwd)


    def click_send(self):
        '''
        点击发送
        '''
        self.register_page.get_send_btn_element().click()

    def click_next_step(self):
        '''
        点击下一步
        '''
        self.register_page.get_next_step_element().click()

    def click_back(self):
        '''
        点击返回
        '''
        self.register_page.get_back_element().click()

    def click_close(self):
        '''
        点击关闭
        '''
        self.register_page.get_close_element().click()

    def click_refresh(self):
        '''
        点击刷新
        '''
        self.register_page.get_refresh_element().click()

    def click_accept_term(self):
        '''
        点击接受条款
        '''
        self.register_page.get_accept_term_element().click()

    def click_accept_ad(self):
        '''
        点击接受广告信息
        '''
        self.register_page.get_accept_ad_element().click()

    def click_complete(self):
        '''
        点击完成按钮
        '''
        self.register_page.get_complete_element().click()

    def click_register_au_btn(self):
        '''
        点击注册AU账户按钮
        '''
        self.register_page.get_register_au_btn_element().click()

    def switch_context(self):
        '''
        切换到webview的context
        '''
        for cons in self.driver.contexts:
            if cons.lower().startswith("webview"):
                self.driver._switch_to.context(cons)
                break

    def click_fill_data_btn(self):
        '''
        点击完善资料并开立真实账户按钮
        '''
        self.register_page.get_fill_data_element().click()

    def click_entre_trade_btn(self):
        '''
        点击进入AETOSTrade按钮
        '''
        self.register_page.get_entre_trade_element().click()

    def screen_shot(self,shot_name):
        '''
        截图
        '''
        screen_path = os.path.join(os.path.dirname(os.getcwd()),'screenshots/{0}_screenshot_{1}.png'.format(shot_name,time.strftime("%Y-%m-%d %H-%M-%S")))
        self.driver.get_screenshot_as_file(screen_path)