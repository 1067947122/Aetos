#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
from utils.read_ini import ReadIni
from utils.write_txt import WriteTxt
from base.base_driver import Driver
from page.register_demo_page import RegisterPage
from handle.register_demo_handle import RegisterHandle
from handle.login_handle import LoginHandle

class RegisterBusiness:
    def __init__(self,driver):
        self.register_handle = RegisterHandle(driver)
        self.driver = driver
        self.ini = ReadIni()
        self.txt = WriteTxt()
        self.register_page = RegisterPage(driver)
        self.login_handle = LoginHandle(driver)
        self.phone = self.ini.get_value('phone','register_input_value')
        self.verification_code = self.ini.get_value('Verification_Code','register_input_value')
        self.mail = self.ini.get_value('mail', 'register_input_value')
        self.call = self.ini.get_value('call', 'register_input_value')
        self.pwd = self.ini.get_value('pwd', 'register_input_value')
        self.confirm_pwd = self.ini.get_value('confirm_pwd', 'register_input_value')
        self.introducer = self.ini.get_value('introducer', 'register_input_value')
        self.driver.implicitly_wait(20)

    def register_demo_pass(self):
        '''
        成功注册demo用户
        '''
        self.login_handle.click_register()
        self.register_handle.click_register_au_btn()
        self.register_handle.switch_context()
        self.register_handle.send_phone(self.phone)
        self.register_handle.send_verification_code(self.verification_code)
        self.register_handle.click_next_step()
        self.register_handle.send_mail(self.mail)
        self.register_handle.send_call(self.call)
        self.register_handle.send_password(self.pwd)
        self.register_handle.send_confirm_password(self.confirm_pwd)
        self.register_handle.send_introducer(self.introducer)
        self.register_handle.click_accept_term()
        self.register_handle.click_accept_ad()
        self.register_handle.click_complete()
        time.sleep(20)
        # self.register_handle.screen_shot('reg_demo_success')

if __name__ == '__main__':
    driver = Driver().android_driver(0)
    bu = RegisterBusiness(driver)